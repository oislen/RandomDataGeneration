import json
import os
import sys

# set huggingface hub directory
huggingface_hub_dir = 'E:\\huggingface\\hub'
os.environ['HF_HOME'] = huggingface_hub_dir
os.environ['HF_DATASETS_CACHE'] = huggingface_hub_dir
os.environ['TORCH_HOME'] = huggingface_hub_dir


import torch
torch.cuda.is_available()
# Output should be True

from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
from huggingface_hub import login


# load huggingface access token
with open('E:\\GitHub\\RandomTelecomPayments\\.creds\\huggingface.json') as f:
    token = json.load(f)
# log into huggingface
login(token = token)

access_token = "Enter your token here"
model = "meta-llama/Llama-2-7b-chat-hf"

tokenizer = AutoTokenizer.from_pretrained(model, token=access_token)

model = AutoModelForCausalLM.from_pretrained(
    model, 
    token=access_token
)

pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)

sequences = pipeline(
    'Hi! Tell me about yourself!',
    do_sample=True,
)
print(sequences[0].get("generated_text"))