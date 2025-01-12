import json

class Bedrock():
    def __init__(self, session, model_id="meta.llama3-8b-instruct-v1:0"):
        self.client = session.client("bedrock-runtime", region_name="us-east-1")
        self.model_id = "meta.llama3-8b-instruct-v1:0"
    
    def prompt(self, prompt, system="", top_p=0.5, temperature=0.5, max_gen_len=512):
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

You are a random name generator for users from different European countries.
Your task is to generate an arbitrary number of typical or popular firstname and surname pairs for both male and female users from given a country of origin.
You should return the random user names using a valid JSON record set tagged as <answer></answer>.
The valid JSON record set should be of the following structure

[{"id":"1", "firstname":"user_firstname_1", "lastname":"user_lastname_1", "sex":"user_sex_1", "country":"user_country_1"},{"id":"2", "firstname":"user_firstname_2", "lastname":"user_lastname_2", "sex":"user_sex_2", "country":"user_country_2"},...,{"id":"n", "firstname":"user_firstname_n", "lastname":"user_lastname_n", "sex":"user_sex_n", "country":"user_country_n"}]

# Example

Generate 3 user names for "United Kingdom"

<answer>[{"id":"1", "firstname":"George", "lastname":"Adams", "sex":"Male", "country":"United Kingdom"},{"id":"2", "firstname":"Andy", "lastname":"Kirkpatrick", "sex":"Male", "country":"United Kingdom"},{"id":"3", "firstname":"Megan", "lastname":"Allard", "sex":"Female", "country":"United Kingdom"}]</answer>

"""

prompt = """

Now generate {n_user_names} typical or popular male and female names for "{country}"

"""