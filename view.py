from presenter import (create_article,
                      edit_article,
                      del_article,
                      read_article)
while True:
    choice = input("""
what you want to do:
1-create article
2-read article
3-edit article
4-delete article
5-stop working
""")

    if choice == "1":
        create_article()
    if choice == "2":
        read_article()
    if choice == "3":
        edit_article()
    if choice == "4":
        del_article()
    if choice == "5":
        print("press enter to end:")





