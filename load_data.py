def book_category_dictionary(file: str) -> dict:
    """
    Opens the csv file containing the books, and sorts them into a dictionary
    by category without duplicates.

 book_category_dictionary = {
    "Fiction": [ {"title": "Antiques Roadkill: A trash 'n' Treasures Mystery",
       "author": " Barbara Allan",
       "language": 3.3,
       "publisher": " Kensington Publishing Corp.",
       "pages": 288
       },
       {another element},
       ...
      ],
    """
    with open(file) as csv_file:
        current = []
        genres = []
        booklist = []
        genres = []
        for rows in csv_file:
            new = []
            books = rows.split(',')
            title = books[0]
            author = books[1]
            rating = books[2]
            publisher = books[3]
            pageCount = books[4]
            genre = books[5]
            language = books[6]
            newdict = {'title': title, 'authors': author, 'rating': rating,
                       'publisher': publisher, 'pageCount': pageCount,
                       'genre': genre, 'language': language}
            genres.append(genre)
            booklist.append(newdict)

        genres.pop(0)
        booklist.pop(0)
        sorted_genres = list(dict.fromkeys(genres))
        genres_dict = {}
        for genre in sorted_genres:
            new = []
            for i in range(0, len(booklist) - 1):
                d = True
                if genre == booklist[i]["genre"]:
                    if len(new) != 0:
                        for t in new:
                            if booklist[i]['title'] == t['title']:
                                d = False
                    if d == True:
                        new.append({"title": booklist[i]["title"],
                                    "authors": booklist[i]["authors"],
                                    "rating": booklist[i]["rating"],
                                    "publisher": booklist[i]["publisher"],
                                    "pageCount": booklist[i]["pageCount"],
                                    "language": booklist[i]["language"]})

            genres_dict[genre] = new

    return genres_dict


# Main Script

# print(book_category_dictionary("google_books_dataset.csv"))