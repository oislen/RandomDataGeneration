import json
import boto3
from beartype import beartype

class Bedrock():
    """
    https://docs.aws.amazon.com/general/latest/gr/bedrock.html
    """
    @beartype
    def __init__(
        self, 
        session:boto3.Session,
        model_region="us-east-1",
        model_id:str="meta.llama3-8b-instruct-v1:0"
        ):
        self.client = session.client("bedrock-runtime", region_name=model_region)
        self.model_id = model_id
    
    @beartype
    def prompt(
        self,
        prompt:str,
        system:str="",
        top_p:float=0.5,
        temperature:float=0.5,
        max_gen_len:int=512
        ) -> str:
        # generate bedrock request    
        formatted_prompt = f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>{system}<|eot_id|><|start_header_id|>user<|end_header_id|>{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>"""
        native_request = {"prompt": formatted_prompt, "max_gen_len": max_gen_len, "temperature": temperature, "top_p":top_p}
        request = json.dumps(native_request)
        # call bedrock model
        try:
            # Invoke the model with the request.
            response = self.client.invoke_model(modelId=self.model_id, body=request)
        except Exception as e:
            print(f"ERROR: Can't invoke '{self.model_id}'. Reason: {e}")
            exit(1)
        # Decode and extract the response
        model_response = json.loads(response["body"].read())
        response_text = model_response["generation"]
        return(response_text)

system = """# Task

You are a name generator for users from different countries in Europe.
Your task is to generate an arbitrary N number of distinct and varied firstnames and lastnames, for both male and female users, from a given European country of origin.

# Requirements

Do not repeat any firstnames or lastnames more than once. Each individual firstname must be unique and each individual lastname must be unique.
You should return the random user names using a valid JSON record set tagged as <answer></answer>.
The valid JSON record set should be of the following structure

{"firstnames":["firstname 1","firstname 2",...,"firstname N"], "lastnames":["lastname 1","lastname 2",...,"lastname N"]}

# Examples

- Generate 2 firstnames and 2 lastnames, for both male and female users, for the country "Germany" -> <answer>{"firstnames":["Max","Hannah"], "lastnames":["Müller","Schmidt"]}</answer>
- Generate 4 firstnames and 4 lastnames, for both male and female users, for the country "United Kingdom" -> <answer>{"firstnames":["George","Richard","Katie","Mary"], "lastnames":["Smith","Taylor","Jones","Brown"]}</answer>
- Generate 3 firstnames and 3 lastnames, for both male and female users, for the country "France" -> <answer>{"firstnames":["Lola","Mathieu","Léa"], "lastnames":["Benoît","Pierre","Lefort"]}</answer>
- Generate 5 firstnames and 5 lastnames, for both male and female users, for the country "Spain" -> <answer>{"firstnames":["Juan","Cristina","Javier","Julia","Isabel"], "lastnames":["Garcia","Martinez","Rodriguez","Lopez","Gomez"]}</answer>"""

prompt = 'Generate {n_user_names} firstnames and {n_user_names} lastnames, for both male and female users, for the country "{country}"'