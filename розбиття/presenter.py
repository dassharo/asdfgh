from model import (articles, check_choice)

def create_article():
    article = {"title": input("title: "),
                           "text": input("text: "),
                           "writer": input("writer: ")}
    articles.append(article)
    print("Article created!")

@check_choice
def read_article(choice2):
    print(articles[choice2-1])
    
@check_choice
def edit_article(choice2):
    edit_options = {
        "1": "title",
        "2": "text",
        "3": "writer"
    }
    edit_choice = input("Що бажаєте змінити? 1 - Заголовок, 2 - Текст, 3 - Автор: ")
    if edit_choice in edit_options:
        edit_key = edit_options[edit_choice]
        articles[choice2 - 1][edit_key] = input(f"Нове значення для {edit_key}: ")
        print("Статтю відредаговано!")
    else:
        print("Невірний вибір. Будь ласка, спробуйте знову.")

@check_choice
def del_article(choice2):
    del articles[choice2 - 1]