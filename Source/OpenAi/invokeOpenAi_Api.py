import os
from openai import OpenAI
from apikey import APIKEY

client = OpenAI(api_key=APIKEY)

print("----- standard request -----")
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "Generate lecture on python data types for students. Explain each data type with 3 examples",
        },
    ],
)

print("----- response -----")
print(completion.choices[0].message.content)
