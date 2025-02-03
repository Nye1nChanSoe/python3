import os
import dotenv
from mistralai import Mistral
import logging

TEXT_MODEL = "mistral-large-latest"

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
dotenv.load_dotenv()

def get_api_key() -> str:
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        logging.error("API Key is missing! Make sure MISTRAL_API_KEY is set in .env")
        raise ValueError("Missing API Key")
    return api_key


def mistral_chat(prompt: str, model: str = TEXT_MODEL) -> str:
    try:
        client = Mistral(api_key=get_api_key())
        chat_response = client.chat.complete(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return chat_response.choices[0].message.content
    except Exception as e:
        logging.error(f"Failed to get response: {e}")
        return "Error: Could not retrieve response"


if __name__ == "__main__":
    while True:
        print("Welcome to Mistral Chat! Type 'exit' to quit.\n")
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye! 👋")
            break
        response = mistral_chat(user_input)
        print("\nMistral:", response, "\n")