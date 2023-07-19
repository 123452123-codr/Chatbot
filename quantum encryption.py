import tkinter as tk
from tkinter import scrolledtext, messagebox

def send_message():
    message = entry_message.get()
    if message.strip() != "":
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, "You: " + message + "\n")
        chat_area.config(state=tk.DISABLED)
        entry_message.delete(0, tk.END)
        # You can add code here to send the message to the other person or a server if needed.

def receive_message():
    message = "Received message from the other person."
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, "Other: " + message + "\n")
    chat_area.config(state=tk.DISABLED)

def on_close():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root = tk.Tk()
root.title("Chatting Interface")
root.geometry("400x400")

chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
chat_area.pack(expand=True, fill=tk.BOTH)

entry_message = tk.Entry(root, width=50)
entry_message.pack(side=tk.LEFT, padx=5, pady=5, expand=True, fill=tk.X)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT, padx=5, pady=5)

# In a real application, you might have a loop or event handling mechanism to receive messages.
# For this example, I'm simulating the reception of messages every few seconds using `after`.
def simulate_receive():
    receive_message()
    root.after(5000, simulate_receive)

root.protocol("WM_DELETE_WINDOW", on_close)

root.after(5000, simulate_receive)  # Simulate receiving messages every 5 seconds.

root.mainloop()
