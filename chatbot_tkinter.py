import tkinter as tk
from tkinter import scrolledtext
import requests
import json

# Remplacez 'https://your_username.pythonanywhere.com/chat' par l'URL de votre application Flask sur PythonAnywhere
server_url = 'https://slimane.pythonanywhere.com/chat'

messages = [{"role": "system", "content": "You are a helpful assistant."}]

def send_message():
    user_input = user_input_entry.get()
    if user_input.lower() == "quit":
        root.destroy()
        return

    messages.append({"role": "user", "content": user_input})
    print(messages)
    response = requests.post(server_url, json={"messages": messages})

    if response.status_code == 200:
        assistant_response = response.json().get("response", "")
        print(assistant_response)
        messages.append({"role": "assistant", "content": assistant_response})

        chat_display.config(state=tk.NORMAL)
        chat_display.insert(tk.END, "You: " + user_input + "\n")
        chat_display.insert(tk.END, "Assistant: " + assistant_response + "\n\n")
        chat_display.config(state=tk.DISABLED)

        user_input_entry.delete(0, tk.END)
    else:
        print("Failed to get response from server")

# Configuration de l'interface graphique Tkinter
root = tk.Tk()
root.title("ChatGPT Assistant")

chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
chat_display.pack(padx=10, pady=10)

user_input_entry = tk.Entry(root, width=50)
user_input_entry.pack(padx=10, pady=5)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=5)

root.mainloop()
