import tkinter as tk
from tkinter import messagebox
from deep_translator import GoogleTranslator
from gtts import gTTS
from playsound import playsound
import os

# Language dictionary
languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de"
}

def translate_text():
    text = text_input.get("1.0", tk.END).strip()
    lang_name = selected_lang.get()
    target = languages.get(lang_name)

    if not text:
        messagebox.showwarning("Input Error", "Please enter text")
        return

    try:
        translated = GoogleTranslator(source='auto', target=target).translate(text)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def copy_text():
    root.clipboard_clear()
    root.clipboard_append(output_text.get("1.0", tk.END))
    messagebox.showinfo("Copied", "Text copied!")

def clear_text():
    text_input.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

def speak_text():
    text = output_text.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Error", "No text to speak")
        return

    try:
        tts = gTTS(text=text, lang='en')
        tts.save("voice.mp3")
        playsound("voice.mp3")
        os.remove("voice.mp3")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI
root = tk.Tk()
root.title("Language Translator")
root.geometry("520x450")
root.configure(bg="#e6f2ff")

tk.Label(root, text="🌐 Language Translator",
         font=("Arial", 16, "bold"),
         bg="#e6f2ff").pack(pady=10)

tk.Label(root, text="Enter Text:", font=("Arial", 11), bg="#e6f2ff").pack()
text_input = tk.Text(root, height=5, width=55)
text_input.pack(pady=5)

tk.Label(root, text="Select Language:", font=("Arial", 11), bg="#e6f2ff").pack(pady=5)
selected_lang = tk.StringVar(value="Hindi")
tk.OptionMenu(root, selected_lang, *languages.keys()).pack()

tk.Button(root, text="Translate", command=translate_text,
          bg="#007acc", fg="white", font=("Arial", 10, "bold")).pack(pady=10)

btn_frame = tk.Frame(root, bg="#e6f2ff")
btn_frame.pack()

tk.Button(btn_frame, text="Copy", command=copy_text,
          bg="green", fg="white", width=10).grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="Clear", command=clear_text,
          bg="red", fg="white", width=10).grid(row=0, column=1, padx=5)

tk.Button(btn_frame, text="Speak", command=speak_text,
          bg="purple", fg="white", width=10).grid(row=0, column=2, padx=5)

tk.Label(root, text="Translated Text:", font=("Arial", 11), bg="#e6f2ff").pack(pady=5)
output_text = tk.Text(root, height=5, width=55)
output_text.pack(pady=5)

root.mainloop()