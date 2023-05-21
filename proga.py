articles = []  # Assuming you have defined the articles list

def create_article():
    article = {"title": input("Title: "),
               "text": input("Text: "),
               "writer": input("Writer: ")}
    articles.append(article)
    print("Article created!")

# Call the function to create an article
create_article()
print(articles)
