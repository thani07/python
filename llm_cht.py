from bytez import Bytez

# Initialize Bytez SDK with your API key
sdk = Bytez("01e652718e0e753c64c35d90498e03da")

# Choose the model
model = sdk.model("Qwen/Qwen3-4B-Instruct-2507")

# System role: set chatbot personality
SYSTEM_PROMPT = """You are an AI medical assistant chatbot.
Your role is to:
1. Analyze the user's health concerns.
2. Identify if their symptoms could indicate a fever.
3. List possible symptoms related to fever.
4. Suggest safe, general recovery methods (like hydration, rest, OTC meds).
5. Always remind them to consult a real doctor for confirmation.
Do not give dangerous or prescription-only advice."""

def ask_medical_chatbot(user_message):
    # Send conversation with system + user roles
    output, error = model.run([
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": user_message
        }
    ])

    if error:
        return f"Error: {error}"
    return output

# Example usage (change user input here)
user_input = "I have headache, sore throat, and body pain. Do I have fever?"
response = ask_medical_chatbot(user_input)

print("\nUser:", user_input)
print("Medical Chatbot:", response)
