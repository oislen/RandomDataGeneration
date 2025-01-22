import os
import json
import boto3
import sys
import time
import logging
import unidecode
import pandas as pd
import numpy as np

sys.path.append("E:\\GitHub\\RandomTelecomPayments\\generator")

import cons
from utilities.Bedrock import Bedrock, prompt, system

def invoke_bedrock(model, n_user_names, country):
    """
    """
    logging.info("Calling Bedrock ...")
    # call bedrock model
    formatted_prompt = prompt.format(n_user_names=n_user_names, country=country)
    logging.info(formatted_prompt)
    model_response = model.prompt(prompt=formatted_prompt, system=system, max_gen_len=2048)
    # split out answer
    text = model_response.split("<answer>")[1].split("</answer>")[0]
    # parse json
    record_set = json.loads(text)
    logging.info("Processing results ...")
    # generate pandas dataframe
    user_firstname_data = pd.Series(record_set["firstnames"], name="firstnames").to_frame().drop_duplicates(subset=["firstnames"])
    user_lastname_data = pd.Series(record_set["lastnames"], name="lastnames").to_frame().drop_duplicates(subset=["lastnames"])
    # add country
    user_firstname_data['country'] = country
    user_lastname_data['country'] = country
    # join on country codes
    llama_firstname_country_data = user_firstname_data.merge(right=countrieseurope, left_on='country', right_on='name', how='inner').drop(columns=['name'])
    llama_lastname_country_data = user_lastname_data.merge(right=countrieseurope, left_on='country', right_on='name', how='inner').drop(columns=['name'])
    # print shapes
    logging.info(f"llama_firstname_country_data.shape: {llama_firstname_country_data.shape}")
    logging.info(f"llama_lastname_country_data.shape: {llama_lastname_country_data.shape}")
    # format output file paths
    fpath_temp_llama_firstnames = cons.fpath_temp_llama_firstnames.format(country=country.lower())
    fpath_temp_llama_lastnames = cons.fpath_temp_llama_lastnames.format(country=country.lower())
    # check against previous iterations
    tmp_firstname_country_data = pd.DataFrame()
    tmp_lastname_country_data = pd.DataFrame()
    if os.path.exists(fpath_temp_llama_firstnames):
        tmp_firstname_country_data = pd.read_csv(fpath_temp_llama_firstnames, encoding="latin1")
    if os.path.exists(fpath_temp_llama_lastnames):
        tmp_lastname_country_data = pd.read_csv(fpath_temp_llama_lastnames, encoding="latin1")
    # concatenate results
    tmp_firstname_country_data = pd.concat(objs=[tmp_firstname_country_data, llama_firstname_country_data], axis=0, ignore_index=True)
    tmp_lastname_country_data = pd.concat(objs=[tmp_lastname_country_data, llama_lastname_country_data], axis=0, ignore_index=True)
    # standardise names formatting
    standardise_text_lambda = lambda x: unidecode.unidecode(" ".join(x.lower().strip().split())) if x not in [None, "", np.nan] else x
    tmp_firstname_country_data["firstnames"] = tmp_firstname_country_data["firstnames"].apply(lambda x: standardise_text_lambda(x))
    tmp_lastname_country_data["lastnames"] = tmp_lastname_country_data["lastnames"].apply(lambda x: standardise_text_lambda(x))
    # deduplicate data
    tmp_firstname_country_data = tmp_firstname_country_data.drop_duplicates(subset=["firstnames"])
    tmp_lastname_country_data = tmp_lastname_country_data.drop_duplicates(subset=["lastnames"])
    # print shapes
    logging.info(f"tmp_firstname_country_data.shape: {tmp_firstname_country_data.shape}")
    logging.info(f"tmp_lastname_country_data.shape: {tmp_lastname_country_data.shape}")
    # save firstnames names data to temp directory
    if tmp_firstname_country_data.shape[0] >= llama_firstname_country_data.shape[0]:
        tmp_firstname_country_data.to_csv(fpath_temp_llama_firstnames, index=False, encoding="latin1")
        logging.info(f"Wrote {fpath_temp_llama_firstnames} ...")
    # save lastnames data to temp directory
    if tmp_lastname_country_data.shape[0] >= llama_lastname_country_data.shape[0]:
        tmp_lastname_country_data.to_csv(fpath_temp_llama_lastnames, index=False, encoding="latin1")
        logging.info(f"Wrote {fpath_temp_llama_lastnames} ...")
    return (tmp_firstname_country_data, tmp_lastname_country_data)

if __name__ == "__main__":

    # set up logging
    lgr = logging.getLogger()
    lgr.setLevel(logging.INFO)

    # load aws config
    with open(cons.fpath_aws_session_token, "r") as j:
        aws_config = json.loads(j.read())
    
    # connect to aws boto3
    session = boto3.Session(
        aws_access_key_id=aws_config['Credentials']["AccessKeyId"],
        aws_secret_access_key=aws_config['Credentials']["SecretAccessKey"],
        aws_session_token=aws_config['Credentials']["SessionToken"],
        region_name="us-east-1"
    )
    
    # create bedrock instance
    bedrock = Bedrock(session=session, model_region="us-east-1", model_id="meta.llama3-70b-instruct-v1:0")
    
    # load countries, firstnames and surnames files
    countrieseurope = pd.read_csv(cons.fpath_countrieseurope, usecols=['name', 'ISO numeric'])
    orig_firstnames = pd.read_csv(cons.fpath_firstnames)
    orig_surnames = pd.read_csv(cons.fpath_lastnames)
    
    # determine file size
    orig_filesize = int((orig_firstnames.shape[0] + orig_surnames.shape[0])/2)
    n_countries = countrieseurope.shape[0]
    n_user_names = min(50, int(orig_filesize / n_countries))
    
    # generate user names
    firstname_country_data = []
    lastname_country_data = []
    error_countries = []
    run_bedrock = False

    # set countries list
    countries_list = countrieseurope['name'].to_list()
    #countries_list = ['Cyprus']

    for country in countries_list:
        logging.info(f"{country} ...")
        try:
            if run_bedrock:
                # call bedrock model and generate user names data
                tmp_firstname_country_data, tmp_lastname_country_data = invoke_bedrock(model=bedrock, n_user_names=n_user_names, country=country)
                logging.info("Waiting ...")
                # wait 30 seconds before retrying
                time.sleep(20)
            else:
                tmp_firstname_country_data = pd.read_csv(cons.fpath_temp_llama_firstnames.format(country=country.lower()), encoding="latin1")
                tmp_lastname_country_data = pd.read_csv(cons.fpath_temp_llama_lastnames.format(country=country.lower()), encoding="latin1")
            # append to user country data
            firstname_country_data.append(tmp_firstname_country_data)
            lastname_country_data.append(tmp_lastname_country_data)
        except Exception as e:
            logging.info(e)
            error_countries.append(country)
    
    # log if any countries failed to generate data
    if len(error_countries) > 0:
        logging.info(f"Failed to generated data for countries: {error_countries}")

    # load existing reference data
    firstname_country_df = pd.read_csv(cons.fpath_llama_firstnames, encoding="latin1")
    lastname_country_df = pd.read_csv(cons.fpath_llama_lastnames, encoding="latin1")
    # append to country data lists
    firstname_country_data.append(firstname_country_df)
    lastname_country_data.append(lastname_country_df)
    # concatenate user country data together and deduplicate across firstnames and countries
    output_firstname_country_df = pd.concat(firstname_country_data, axis=0, ignore_index=True)
    output_lastname_country_df = pd.concat(lastname_country_data, axis=0, ignore_index=True)
    # sort and deduplicate output data
    output_firstname_country_df = output_firstname_country_df.drop_duplicates(subset=["country","firstnames"]).sort_values(by=["country","firstnames"])
    output_lastname_country_df = output_lastname_country_df.drop_duplicates(subset=["country","lastnames"]).sort_values(by=["country","lastnames"])

    # write data to disk
    if output_firstname_country_df['country'].nunique() == n_countries:
        logging.info(f"output_firstname_country_df.shape: {output_firstname_country_df.shape}")
        output_firstname_country_df.to_csv(cons.fpath_llama_firstnames, index=False, encoding="latin1")
    else:
        logging.info("WARNING Insufficient first name data generated.")
    if output_lastname_country_df['country'].nunique() == n_countries:
        logging.info(f"output_lastname_country_df.shape: {output_lastname_country_df.shape}")
        output_lastname_country_df.to_csv(cons.fpath_llama_lastnames, index=False, encoding="latin1")
    else:
        logging.info("WARNING Insufficient last name data generated.")