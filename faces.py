
def main():
    emoji = input("Type a sentence with a smile or frown: ").replace(":)", "🙂").replace(":(", "🙁")
    convert(emoji)

def convert(emoji_face):
    print(f"Your sentence: {emoji_face}")

main()
