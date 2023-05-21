from model import (articles)
#from view import (len_article, choice2)

def create_article():
    article = {"title": input("title: "),
                           "text": input("text: "),
                           "writer": input("writer: ")}
    articles.append(article)
    print("Article created!")

def read_article():
    choice2=int(input("оберіть статтю для роботи:"))
    print(articles[choice2-1])
    

def edit_article():
    choice2=int(input("оберіть статтю для роботи:"))
    edit_options = {"1": "title", "2": "text", "3": "writer"}
    edit_choice = input("What do you want to edit? 1-Title, 2-Text, 3-Writer: ")
    if edit_choice in edit_options:
        edit_key = edit_options[edit_choice]
        articles[choice2 - 1][edit_key] = input(f"New {edit_key}: ")
    else:
        print("Invalid choice. Please try again.")

def del_article():
    choice2=int(input("оберіть статтю для роботи:"))
    del articles[choice2 - 1]
