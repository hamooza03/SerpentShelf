from load_data import book_category_dictionary


dictionary = book_category_dictionary("google_books_dataset.csv")


def list_conversion(dictionary: dict) -> list:
    """
    Converts dictionary to list
    """
    books = []

    for category in dictionary.keys():
        genre = dictionary.get(category)
        for book in genre:
            book['genres'] = [category]
            if len(books) == 0:
                books.append(book)
            else:
                bookss = True
                for i in range(len(books)):
                    if books[i]['title'] == book['title']:
                        books[i]['genres'] += book['genres']
                        bookss = False
                if bookss == True:
                    books.append(book)
    return books


def bubblesort(book_list: list, header: str, ord: str) -> None:
    """
    Sorts list alphabetically
    """
    for i in range(len(book_list)):
        for j in range(0, len(book_list) - i - 1):
            if ord == "ascending":
                if (book_list[j][header] > book_list[j + 1][header]):
                    book_list[j], book_list[j + 1] = book_list[j + 1], book_list[j]
            else:
                if book_list[j][header] < book_list[j + 1][header]:
                    book_list[j], book_list[j + 1] = book_list[j + 1], book_list[j]
    return book_list


# Function 1
def sort_books_title(dictionary: dict) -> list:
    """
    Returns dictionary with book elements and titles assorted in alphabetical order using bubble
    >>> sort_books_title(book_category_dictionary("google_books_dataset.csv"))

    """
    book_list = list_conversion(dictionary)
    book_list = bubblesort(book_list, 'title', 'ascending')
    return book_list


# Function 2
def sort_books_publisher(dictionary: dict) -> list:
    """
    Returns dictionary with book elements and publishers assorted in alphabetical order using bubble
    >>> sort_books_publisher(book_category_dictionary("google_books_dataset.csv"))
    """
    book_list = list_conversion(dictionary)
    book_list = bubblesort(book_list, 'title', 'ascending')
    book_list = bubblesort(book_list, 'publisher', 'ascending')
    return book_list


# Function 3
def sort_books_author(dictionary: dict) -> list:
    """
    Returns dictionary with book elements and authors assorted in alphabetical order using bubble
    >>> sort_books_author(book_category_dictionary("google_books_dataset.csv"))

    """
    book_list = list_conversion(dictionary)
    book_list = bubblesort(book_list, 'authors', 'ascending')
    return book_list


# Function 4
def sort_books_ascending_rate(dictionary: dict) -> list:
    """
    Returns dictionary with book elements and ratings assorted in ascending order
print(sort_books_ascending_rate(book_category_dictionary("google_books_dataset.csv")))

    """
    header = 'rating'

    book_list = list_conversion(dictionary)
    for i in range(len(book_list)):
        for j in range(0, len(book_list) - i - 1):
            if (book_list[j][header] == 'N/A' and book_list[j + 1][header] == 'N/A'):
                if book_list[j]['title'] > book_list[j + 1]['title']:
                    book_list[j], book_list[j + 1] = book_list[j + 1], book_list[j]
            elif (book_list[j][header] == 'N/A' and book_list[j + 1][header] != 'N/A'):
                pass
            elif (book_list[j][header] != 'N/A' and book_list[j + 1][header] == 'N/A'):
                book_list[j], book_list[j + 1] = book_list[j + 1], book_list[j]
            elif book_list[j][header] == book_list[j + 1][header]:
                if book_list[j]['title'] > book_list[j + 1]['title']:
                    book_list[j], book_list[j + 1] = book_list[j + 1], book_list[j]
            elif book_list[j][header] > book_list[j + 1][header]:
                book_list[j], book_list[j + 1] = book_list[j + 1], book_list[j]
    return book_list


# Main Script
# print(sort_books_title(dictionary))
# print(sort_books_publisher(dictionary))
# print(sort_books_author(dictionary))
# print(sort_books_ascending_rate(dictionary))