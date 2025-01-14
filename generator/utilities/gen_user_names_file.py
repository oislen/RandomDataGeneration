import json
import boto3
import sys
import pandas as pd
import time

sys.path.append("E:\\GitHub\\RandomTelecomPayments\\generator")

import cons
from utilities.Bedrock import Bedrock, prompt, system

def invoke_bedrock(model, n_user_names, country):
    """
    """
    # call bedrock model
    formatted_prompt = prompt.format(n_user_names=n_user_names, country=country)
    model_response = model.prompt(prompt=formatted_prompt, system=system, max_gen_len=2048)
    # split out answer
    text = model_response.split("<answer>")[1].split("</answer>")[0]
    # parse json
    record_set = json.loads(text)
    # generate pandas dataframe
    user_firstname_data = pd.Series(record_set["firstnames"], name="firstnames").to_frame().drop_duplicates()
    user_lastname_data = pd.Series(record_set["lastnames"], name="lastnames").to_frame().drop_duplicates()
    # add country
    user_firstname_data['country'] = country
    user_lastname_data['country'] = country
    # join on country codes
    tmp_firstname_country_data = user_firstname_data.merge(right=countrieseurope, left_on='country', right_on='name', how='inner').drop(columns=['name'])
    tmp_lastname_country_data = user_lastname_data.merge(right=countrieseurope, left_on='country', right_on='name', how='inner').drop(columns=['name'])
    # print shapes
    print(f"tmp_firstname_country_data.shape: {tmp_firstname_country_data.shape}")
    print(f"tmp_lastname_country_data.shape: {tmp_lastname_country_data.shape}")
    # save user names data to temp directory
    tmp_firstname_country_data.to_csv(f"E:\\GitHub\\RandomTelecomPayments\\data\\temp\\llama_firstnames_{country.lower()}.csv", index=False)
    tmp_lastname_country_data.to_csv(f"E:\\GitHub\\RandomTelecomPayments\\data\\temp\\llama_lastnames_{country.lower()}.csv", index=False)
    return (tmp_firstname_country_data, tmp_lastname_country_data)

if __name__ == "__main__":
    
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
    countrieseurope = pd.read_csv(cons.fpath_countrieseurope, usecols=['name', 'ISO alpha 2', 'ISO alpha 3'])
    orig_firstnames = pd.read_csv(cons.fpath_firstnames)
    orig_surnames = pd.read_csv(cons.fpath_lastnames)
    
    # determine file size
    orig_filesize = int((orig_firstnames.shape[0] + orig_surnames.shape[0])/2)
    n_countries = countrieseurope.shape[0]
    n_user_names = min(30, int(orig_filesize / n_countries))
    
    # generate user names
    firstname_country_data = []
    lastname_country_data = []
    for country in countrieseurope['name'].to_list():
        print(country)
        try:
            # call bedrock model and generate user names data
            tmp_firstname_country_data, tmp_lastname_country_data = invoke_bedrock(model=bedrock, n_user_names=n_user_names, country=country)
            # append to user country data
            firstname_country_data.append(tmp_firstname_country_data)
            lastname_country_data.append(tmp_lastname_country_data)
        except Exception as e:
            print(e)
        print("Waiting ...")
        # wait 30 seconds before retrying
        time.sleep(30)
    
    # concatenate user country data together
    firstname_country_df = pd.concat(firstname_country_data, axis=0, ignore_index=True)
    lastname_country_df = pd.concat(lastname_country_data, axis=0, ignore_index=True)
    
    # write data to disk
    if True:
        firstname_country_df.to_csv("E:\\GitHub\\RandomTelecomPayments\\generator\\ref\\llama_firstnames.csv", index=False)
        lastname_country_df.to_csv("E:\\GitHub\\RandomTelecomPayments\\generator\\ref\\llama_lastnames.csv", index=False)
    # read data from dsk
    if False:
        firstname_country_df = pd.read_csv("E:\\GitHub\\RandomTelecomPayments\\generator\\ref\\llama_firstnames.csv")
        lastname_country_df = pd.read_csv("E:\\GitHub\\RandomTelecomPayments\\generator\\ref\\llama_lastnames.csv")