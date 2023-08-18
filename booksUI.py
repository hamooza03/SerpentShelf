from load_data import book_category_dictionary
from add_remove_search_dataset import add_book, remove_book, get_books_by_title, get_books_by_author, \
    get_books_by_rate, get_books_by_publisher, get_books_by_category, get_all_categories_for_book_title
from sorting_fun import sort_books_title, sort_books_ascending_rate, sort_books_publisher, sort_books_author


# Team Code
def menu() -> None:
    """
    This is the Main menu: prints the initial user interface that is shown in the shell:
The Available Commands Are:
  1 - L)oad data
  2 - A)dd book
  3 - R)emove book
  4 - G)et books
        T)itle   R)ate   A)uthor  P)ublisher  C)ategory
  5 - GCT) Get all Categories for book Title
  6 - S)ort books
        T)itle   R)ate   P)ublisher  A)uthor
  7 - Q)uit

Please type your command:
    """

    operator = input(
        "Welcome to SerpentShelf! \n The Available Commands Are: \n  1 - L)oad data \n  2 - A)dd book    3 - R)emove book \n  4 - G)et books \n        T)itle   R)ate   A)uthor  P)ublisher  C)ategory \n  5 - GCT) Get all Categories for book Title     6 - S)ort books \n        T)itle   R)ate   P)ublisher  A)uthor \n  7 - Q)uit \n \nPlease type your command: ").upper()
    return operator


def run_commands() -> dict:
    """
    Commands are run here. First, a file/data must be loaded and then can be dealt with with the following functions in the menu function.
    For load data:
    filename = "google_books_dataset.csv"

    """
    work = True
    file_loaded = False
    commands = ["L", "G", "T", "R", "A", "P", "C", "GCT", "S", "Q"]

    while work:
        operator = menu()
        if operator not in commands:
            print("No such command")
        elif operator == "L":
            chosen_file = str(input("Please enter your chosen file: "))
            file = book_category_dictionary(filename)
            file_loaded = True
            print("Loaded file:", chosen_file)
        elif file_loaded == False:
            print("No file loaded")

        elif operator == "A":
            book_title = input("Please enter a title: ")
            book_author = input("Please enter a author: ")
            book_language = input("Please enter a language: ")
            book_publisher = input("Please enter a publisher: ")
            book_category = input("Please enter a category: ")
            book_rate = float(input("Please enter a rating: "))
            book_pages = int(input("Please enter the number of pages: "))
            book_details = (
            book_title, book_author, book_language, book_publisher, book_category, book_rate, book_pages)
            print(add_book(file, book_details))

        elif operator == "R":
            title = str(input("Enter the desired book's title here: "))
            category = str(input("Enter the desired book's category here: "))
            print(remove_book(title, category, file))

        elif operator == "G":
            get_operators = str(
                input("How do you want to get books?\n\tT)itle R)ate A)uthor P)ublisher C)ategory: ")).upper()
            if get_operators == "T":
                title = str(input("Enter the desired book's title here: "))
                get_books_by_title(title, file)

            if get_operators == "R":
                x = float(input("Enter the desired rating here: "))
                get_books_by_rate(x)

            if get_operators == "A":
                author_name = str(input("Enter the desired author's name here: "))
                get_books_by_author(author_name, file)

            if get_operators == "P":
                publisher = str(input("Enter the desired book's publisher here: "))
                get_books_by_publisher(publisher, file)

            if get_operators == "C":
                category = str(input("Enter the desired category here: "))
                get_books_by_category(category)
        elif operator == "GCT":
            title = str(input("Enter the desired book's title here: "))
            get_all_categories_for_book_title(title, file)

        elif operator == "S":
            sort_operator = str(input("How do you want to sort?\n\tT)itle R)ate P)ublisher A)uthor: ")).upper()
            if sort_operator == "T":
                print(sort_books_title(file))

            if sort_operator == "R":
                print(sort_books_ascending_rate(file))

            if sort_operator == "P":
                print(sort_books_publisher(file))

            if sort_operator == "A":
                print(sort_books_author(file))

        elif operator == "Q":
            break


# Main Script
filename = "google_books_dataset.csv"
run_commands()