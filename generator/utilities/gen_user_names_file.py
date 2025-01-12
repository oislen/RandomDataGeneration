import json
import boto3
import sys
import pandas as pd

sys.path.append("E:\\GitHub\\RandomTelecomPayments\\generator")

import cons
from utilities.Bedrock import Bedrock, prompt, system

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
bedrock = Bedrock(session=session, model_id="meta.llama3-8b-instruct-v1:0")

# load countries file
countrieseurope = pd.read_csv(cons.fpath_countrieseurope, usecols=['name', 'ISO alpha 2', 'ISO alpha 3'])

user_country_data = []
n_user_names = 10
for country in countrieseurope['name'].to_list():
    print(country)
    # call bedrock model
    formatted_prompt = prompt.format(n_user_names=n_user_names, country=country)
    model_response = bedrock.prompt(prompt=formatted_prompt, system=system)
    # split out answer
    text = model_response.split("<answer>")[1].split("</answer>")[0]
    # parse json
    record_set = json.loads(text)
    # generate pandas dataframe
    user_data = pd.DataFrame.from_records(record_set).set_index('id')
    # join on country codes
    tmp_user_country_data = user_data.merge(right=countrieseurope, left_on='country', right_on='name', how='inner')
    # append to user country data
    user_country_data.append(tmp_user_country_data)

# concatenate user country data together
user_country_df = pd.concat(user_country_data, axis=0, ignore_index=True).drop(columns=['name'])

# write data to disk
if False:
    user_country_df.to_csv("E:\\GitHub\\RandomTelecomPayments\\generator\\ref\\llama_user_names.csv", index=False)
# read data from dsk
if True:
    user_country_df = pd.read_csv("E:\\GitHub\\RandomTelecomPayments\\generator\\ref\\llama_user_names.csv")