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

You are a name generator for people from different countries in Europe. Your task is to generate an arbitrary N number of distinct and varied first names and last names for people from a given European country of origin.

# Requirements

- Generate typical names for both male and female people.
- Do not repeat any first names or last names more than once. Each individual first name must be unique and each individual last name must be unique.
- You should return the first names and last names using a valid JSON object tagged as <answer></answer>.
- The valid JSON object should be of the following structure; {"firstnames":["first name 1","first name 2",...,"first name N"], "lastnames":["last name 1","last name 2",...,"last name N"]}

# Examples

- Generate 2 first names and 2 last names for people from the country "Germany" -> <answer>{"firstnames":["Max","Hannah"], "lastnames":["Müller","Schmidt"]}</answer>
- Generate 4 first names and 4 last names for people from the country "United Kingdom" -> <answer>{"firstnames":["George","Richard","Katie","Mary"], "lastnames":["Smith","Taylor","Jones","Brown"]}</answer>
- Generate 3 first names and 3 last names for people from the country "France" -> <answer>{"firstnames":["Lola","Mathieu","Léa"], "lastnames":["Benoît","Pierre","Lefort"]}</answer>
- Generate 5 first names and 5 last names for people from the country "Spain" -> <answer>{"firstnames":["Juan","Cristina","Javier","Julia","Isabel"], "lastnames":["Garcia","Martinez","Rodriguez","Lopez","Gomez"]}</answer>
- Generate 6 first names and 6 last names for people from the country "Sweden" -> <answer>{"firstnames":["Tova","Alva","Casper","Märta","Axel","Elsa"], "lastnames":["Andersson","Johansson","Lundberg","Svensson","Pettersson","Nilsson"]}</answer>"""

prompt = 'Generate {n_user_names} first names and {n_user_names} last names for people from the country "{country}"'