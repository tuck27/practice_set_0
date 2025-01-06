def main():
    food = input("What's your fav food? ").lower().strip()
    user(food)

def user(user_food):
    print(f"Your favorite food is: {user_food}")

main()