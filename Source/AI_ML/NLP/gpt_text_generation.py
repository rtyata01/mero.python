# GPT-2 for text generation

from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

# Load tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Input prompt
prompt = "In the future, artificial intelligence will"
inputs = tokenizer.encode(prompt, return_tensors="pt")

# Generate text
outputs = model.generate(inputs, max_length=50, do_sample=True, top_k=50, top_p=0.95)
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(generated_text)
