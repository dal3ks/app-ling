from book import Book

class BookRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all artists
    def all(self):
        rows = self._connection.execute('SELECT * from books')
        books = []
        for row in rows:
            item = Book(row["id"], row["title"], row["author"], row["rating"])
            books.append(item)
        return books
#Adding the benevolent secure create function
    def create(self,book):
        self._connection.execute('INSERT INTO books (title, author, rating) VALUES (%s, %s, %s)',[book.title, book.author, book.rating])
        return None

# # Adding ye ol' risky biscuit: 
#     def create(self, book):
#         self._connection.execute(
#             f"INSERT INTO books (title, author) VALUES ('{book.title}', '{book.author}')",
#             [])

        