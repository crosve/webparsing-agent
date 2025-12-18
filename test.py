import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
load_dotenv()

client = InferenceClient(
    model="Qwen/Qwen3-Next-80B-A3B-Thinking",
    api_key=os.environ["HF_TOKEN"],
    provider="novita"

)

completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ],
)

print(completion.choices[0].message)