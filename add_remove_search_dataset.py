from load_data import book_category_dictionary
from check_equal import check_equal


dictionary = book_category_dictionary("google_books_dataset.csv")


def add_book(dictionary: dict, book: tuple) -> dict:
    """
    adds a book to the list of books and appends it at the end. Proper book details are written in the order of title, author language, publisher, cateogyr, rating, and page number.
    """
    new_book = {'title': book[0], 'author': book[1], 'language': book[2], 'rating': book[5], 'publisher': book[3],
                'category': book[4], 'page_count': book[6]}
    if new_book['category'] in dictionary.keys():
        dictionary[new_book['category']].append(new_book)

    else:
        dictionary[new_book['category']] = []
        dictionary[new_book['category']].append(new_book)

    if new_book in dictionary[new_book['category']]:
        print('The book has been added correctly.')
    else:
        print('There was an error adding the book.')

    return dictionary



dictionary = book_category_dictionary("google_books_dataset.csv")


def remove_book(title: str, category: str, dictionary: dict) -> dict:
    """
    removes a book from the list when the proper title and category is given.
    """
    remove = False
    for book in dictionary[category]:
        if book['title'] == title:
            dictionary[category].remove(book)
            remove = True
    if remove == True:
        print('The book has been removed correctly.')
    else:
        print('There was an error removing the book. Book not found.')
    return dictionary



dictn = book_category_dictionary("google_books_dataset.csv")


def get_books_by_category(category: str):
    """
    Returns the number of books in the category
    """
    books = []
    author = []
    for i in dictn[category]:
        books.append(i["title"])
        author.append(i["authors"])

    print("The category", category, " has:", str(len(books)), "books")

    for i in range(len(books and author)):
        print(f"Book" + str(i + 1) + ":" + books[i] + "by" + author[i] + "\n")
    return len(books)


def get_books_by_rate(x: int):
    """
    Return the number of books for a rating
    """
    dictn = book_category_dictionary('google_books_dataset.csv')
    rate = []
    book = []
    author = []
    for category in dictn.keys():
        for rates in dictn[category]:
            if rates['rating'] != 'N/A':
                if x <= float(rates['rating']) < (x + 1):
                    rate.append(rates['rating'])
                    book.append(rates['title'])
                    author.append(rates['authors'])
    if x == 5:
        print(
            'There are ' + str(len(rate_lst)) + ' books with a rating of ' + str(x) + '. This is the list of books: \n')
    else:
        print('There are ' + str(len(rate)) + ' books whose rate is between ' + str(x) + ' and ' + str(
            x + 1) + '. This is the list of books: \n')
    for i in range(len(book and author)):
        print(f'Book ' + str(i + 1) + ': ' + book[i] + ' by ' + author[i] + '\n')
    return len(book)


bd = book_category_dictionary("google_books_dataset.csv")


def get_books_by_title(title: str, bd: dict) -> bool:
    """
    Returns True if the title exists in the dictionary, and False if the title
    is not found. It will also print "The book has been found" or "The book has
    NOT been found" respectively

    >>> find_books_by_title('Spider-Man: Anti-Venom',dictionary)
        The book has been found
        True
    >>> find_books_by_title('Venom-Man: Anti-Spider', dictionary)
        The book has NOT been found
        False
    """
    for stuff in bd.values():
        for book in stuff:
            if title == book['title']:
                print("The book has been found")
                return True
    print("The book has NOT been found")
    return False


bd = book_category_dictionary("google_books_dataset.csv")


def get_books_by_author(author_name: str, bd: dict) -> list:
    """
    Return the number of books written by the selected author(s) and prints all the titles by
the given author as follows:
The author zzz has published the following books:
Book 1: "Title", rate: "rating"
Book 2: "Title", rate: "rating"
"""
    print("The author", author_name, "has published the following books:")

    book_list = []

    for category in bd.keys():
        for book in bd[category]:
            if book["authors"] == author_name:
                title = book['title']
                if title not in book_list:
                    book_list.append(title)
                    print(f"Book {len(book_list)}: {title}, rate: {book['rating']}")
    return len(book_list)


bd = book_category_dictionary("google_books_dataset.csv")


def get_books_by_publisher(publisher: str, bd: dict) -> list:
    """
    Return the number of books published by the given publisher’s
(note that the same book in a different category counts as a single book). Additionally, the function
prints the books information for that publisher as follows:

        The Publisher zzz has published the following books:
        Book 1: "Title" by "Author"
        Book 2: "Title" by "Author"
    """
    book_list = []
    print('The Publisher', publisher, 'has published the following books:')

    for category in bd.keys():
        for book in bd[category]:
            if book["publisher"] == publisher:
                title = book['title']
                if title not in book_list:
                    book_list.append(title)
                    print(f"Book {len(book_list)}: {title}, by {book['authors']}")
    return len(book_list)


bd = book_category_dictionary("google_books_dataset.csv")


def get_all_categories_for_book_title(title: str, bd: dict) -> list:
    """
    The function returns the number of categories associated with the given title. Additionally, the function prints the following information:
The book title zzz belongs to the following categories:
Category 1: "Category"
Category 2: "Category"
    """
    category_list = []
    print('The book title', title, 'belongs to the following categories:')
    for category in bd.keys():
        for book in bd[category]:
            if book['title'] == title:
                category_list.append(category)
                print(f"Category {len(category_list)}: {category}")
    return len(category_list)


# The test functions you developed for automated testing

# Test 1:
def test_add_book() -> None:
    """
    """
    check_equal(
        "add_book(dictionary,('ECOR 1042 - Data Management','Hamza','English','Abu-Alkhair','Educational',3.2,129))",
        "The book has been added correctly", add_book(dictionary, (
        'ECOR 1042 - Data Management', 'Hamza', 'English', 'Abu-Alkhair', 'Educational', 3.2, 129)))


# test_add_book()


# Test 2:
def test_remove_book() -> None:
    """
    """
    check_equal("remove_book('ECOR 1042 - Data Management','Fiction', dictionary)",
                'The book has been removed correctly',
                remove_book('ECOR 1042 - Data Management', 'Fiction', dictionary))


# test_remove_book()


# Test 3

def test_get_books_by_category() -> None:
    check_equal("get_books_by_category('Fiction')", 39, get_books_by_category('Fiction'))


# test_get_books_by_category()


# Test 4

def test_get_books_by_rate() -> None:
    check_equal("get_books_by_rate(4.8)", 12, get_books_by_rate(4.8))


# test_get_books_by_rate()


# Test 5:
def test_get_books_by_title() -> None:
    """
    """
    check_equal("get_books_by_title('Spider-Man: Anti-Venom', bd)", True,
                get_books_by_title('Spider-Man: Anti-Venom', bd))


# test_get_books_by_title()


# Test 6
def test_get_books_by_author() -> None:
    """
    """
    check_equal("get_books_by_author('Brandon Sanderson', bd)", 2, get_books_by_author('Brandon Sanderson', bd))


# test_get_books_by_author()


# Function 7
def test_get_books_by_publisher() -> None:
    ""
    ""
    check_equal("get_books_by_publisher('DC', bd)", 2, get_books_by_publisher("DC", bd))


# test_get_books_by_publisher()


# Function 8
def test_get_all_categories_for_book_title() -> None:
    ""

    ""
    check_equal("get_all_categories_for_book_title('The Infinite Game', bd)", 1,
                get_all_categories_for_book_title('The Infinite Game', bd))


# test_get_all_categories_for_book_title()