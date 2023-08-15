import dotenv
import openai

# Configure OpenAI API key
openai.api_key = dotenv.get_key(".env", "OPENAI_API_KEY")

response = openai.Image.create(
    prompt='basketball with glasses cartoon',
    n=1,
    size="512x512"
)

print(response['data'][0]['url'])
