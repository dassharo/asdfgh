articles = []

def check_choice(func):
    def wrapper(choice2):
        while True:
            if choice2.isdigit() and 1 <= int(choice2) <= len(articles):
                return func(int(choice2))
            else:
                print("Invalid choice. Please try again.")
                choice2 = input("Choose an article to edit: ")
    return wrapper

