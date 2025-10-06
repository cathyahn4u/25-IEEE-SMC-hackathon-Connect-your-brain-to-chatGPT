# Call ChatGPT API
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API key 
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

# Create conversation
def create_conversation():
    convo = client.conversations.create()
    return convo.id

# Talk to ChatGPT
def send_message(conversation_id: str, user_message: str, model: str = "gpt-4o-mini") -> str:

    response = client.responses.create(
        model=model,
        conversation={"id": conversation_id},
        input=[{"role": "user", "content": user_message}],
    )

    try:
        return response.output[0].content[0].text
    except Exception as e:
        print(f"[Error extracting GPT response]: {e}")
        return "⚠️ Something went wrong with the model output."
