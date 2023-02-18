import os
import openai 
from api_secrets import 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

openai.api_key = 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

prompt = "Say this is a test"

response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=6)

print(response)


print("Hello World")
greeting = input()
print(greeting)