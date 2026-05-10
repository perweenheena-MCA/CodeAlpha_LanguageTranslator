from googletrans import Translator

translator = Translator()

while True:
    text = input("\nEnter text: ")
    target = input("Target language (hi, fr, es, etc.): ")

    try:
        result = translator.translate(text, dest=target)
        print("Translated:", result.text)
    except:
        print("Error: Invalid language or network issue")

    choice = input("Translate again? (yes/no): ")
    if choice.lower() != 'yes':
        break