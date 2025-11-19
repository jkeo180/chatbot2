from openai import OpenAI

client = OpenAI(api_key="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")

response = client.responses.create(
  model="gpt-5-nano",
 input="chat with me",
  store=True,
)

print(response.output_text)
