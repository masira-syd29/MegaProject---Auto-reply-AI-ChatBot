import pyautogui
import time
import pyperclip
import ollama

def lastMessage(chatHistory: str) -> bool:
    lines = [line.strip() for line in chatHistory.strip().split("/2025] ")[-1] if line.strip()]
    if not lines : return False

    lastLine = lines[-1]
    return "]Ozair" in lastLine

def ask_ollama(user_message):
    try:
        response = ollama.chat(
            model="llama3",
            messages=[
                {"role": "system", "content": "You are Maseera, from India, bilingual in English and Urdu, a coder. Analyze chat history and respond like Maseera. Output should be the next chat responseas Maseera"},
                {"role": "user", "content": user_message}
            ]
        )
        # Ollama returns 'message' inside 'message' key
        return response["message"]["content"]
    except Exception as e:
        return f"Error communicating with Ollama: {e}"
    
while True:
    time.sleep(2)
    try: 
        pyautogui.moveTo(666, 119, duration=0.5)
        pyautogui.mouseDown()

        pyautogui.moveTo(1900, 934, duration=1.5)
        pyautogui.mouseUp()

        # Copy to clipboard
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)

        # Get clipboard content
        chatHistory = pyperclip.paste()
        print("Chat History content: ")
        print(chatHistory)
        
        if lastMessage(chatHistory):

            print("\nLast message is from Ozair. Generating reply...")
            reply = ask_ollama(chatHistory)
            print("Ollama's Response: ")
            print (reply)

            pyautogui.moveTo(1155, 976, duration=0.5)
            pyautogui.click()
            pyperclip.copy(reply)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
        else:
            print("Last Message is not from the receiver")
    except Exception as e:
        print(f"An error occurred in the main loop: {e}")
# if __name__ == "__main__":
#     print("=== Ollama Test Client ===")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["exit", "quit", "q"]:
#             print("Goodbye!")
#             break
#         reply = ask_ollama(user_input)
#         print("Ollama:", reply)
# time.sleep(2)  # Time to switch to the target window
