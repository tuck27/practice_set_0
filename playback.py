def main():
    sound = input("Name a song:").replace(" ", "...")
    song(sound)
def song(music):
    print(f"Slow Down! {music}")

main()