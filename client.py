# import ollama
# def ask_ollama(prompt):
#     try:
#         response = ollama.chat(
#             model="llama3",  # Change to your desired Ollama model
#             messages=[{"role": "user", "content": "You are a person named Maseera who speaks English as well as Urdu, she is from India and is a Coder. You analyze chat History and talk and respond like Maseera"},
#                       {"role": "user", "content": prompt}]
#         )
#         # 'message' is inside a list in the new API format
#         return response["message"]["content"]
#     except Exception as e:
#         return f"Error communicating with Ollama: {e}"

# if __name__ == "__main__":
#     print("=== Ollama Test Client ===")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["exit", "quit", "q"]:
#             print("Goodbye!")
#             break
#         reply = ask_ollama(user_input)
#         print("Ollama:", reply)

# client.py
import ollama

# The selected text
chat_history = '''
[8:05 PM, 8/11/2025] Madi Di: NAHI
[8:05 PM, 8/11/2025] Maseera Irfan Ali: 4 mahine pehle check karaaye the🫠
[8:06 PM, 8/11/2025] Madi Di: I CHECKED AGAIN
[8:06 PM, 8/11/2025] Madi Di: Farhat aunty ke yaha     
[8:06 PM, 8/11/2025] Madi Di: Jab gayi thi mummy ke saath
[8:06 PM, 8/11/2025] Madi Di: It was 71.3
[8:07 PM, 8/11/2025] Madi Di: I was wearing hoodie and jeans when I checked in suburban
🥲
'''

system_prompt = (
    "You are a person named Maseera who speaks English as well as Urdu. "
    "She is from India and is a coder. You analyze the given chat history "
    "and respond in a casual, friendly manner like Maseera would."
)

def ask_ollama(message_history):
    try:
        response = ollama.chat(
            model="llama3",
            messages=message_history
        )
        return response["message"]["content"]
    except Exception as e:
        return f"Error communicating with Ollama: {e}"

if __name__ == "__main__":
    print("=== Ollama Test Client ===")

    # First send the selected chat as context
    conversation = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": chat_history}
    ]

    # First reply from Ollama based on the selected text
    reply = ask_ollama(conversation)
    print("Ollama:", reply)

    # Continue chatting
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "q"]:
            print("Goodbye!")
            break
        conversation.append({"role": "user", "content": user_input})
        reply = ask_ollama(conversation)
        print("Ollama:", reply)
        conversation.append({"role": "assistant", "content": reply})

