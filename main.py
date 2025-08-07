from openai import OpenAI


client = OpenAI(base_url="http://192.168.178.25:1234/v1", api_key="lm-studio")



completion = client.chat.completions.create(
  #model = "qwen/qwen3-8b",
  model="gemma-1.1-2b-it",
  messages=[
    {"role": "system", "content": "Always answer in rhymes."},
    {"role": "user", "content": "Introduce yourself."}
  ],
  temperature=0.7,
)

print(completion.choices[0].message)