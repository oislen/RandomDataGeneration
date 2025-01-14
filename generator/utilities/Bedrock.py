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

system = """

# Task

You are a random name generator for users from different countries in Europe.
Your task is to generate an arbitrary number of typical / popular firstname and surname pairs for both male and female users from given a country of origin.
Do not repeat any firstnames or surnames, as each individual firstname must be unique and each individual surname must be unique.
You should return the random user names using a valid JSON record set tagged as <answer></answer>.
The valid JSON record set should be of the following structure

[{"firstname":"user_firstname_1", "lastname":"user_lastname_1"},{"firstname":"user_firstname_2", "lastname":"user_lastname_2"},...,{"firstname":"user_firstname_n", "lastname":"user_lastname_n"}]

# Example

Generate 4 user names for "United Kingdom"

<answer>[{"firstname":"George","lastname":"Smith"},{"firstname":"Richard","lastname":"Taylor"},{"firstname":"Katie","lastname":"Jones"},{"firstname":"Mary","lastname":"Brown"}]</answer>

"""

prompt = """

Now generate {n_user_names} typical or popular male and female names for "{country}"

"""