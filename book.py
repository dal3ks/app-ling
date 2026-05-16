class Book:

    def __init__(self, id, title, author, rating):
        self.id = id
        self.title = title
        self.author = author
        self.rating = rating


    def __eq__(self, other):
        return self.__dict__ == other.__dict__


    def __repr__(self):
        return f"Book({self.id}, {self.title}, {self.author}, {self.rating})"
    

    # books don't have an id until they are saved to the database 
    # so we need a default value for id
    # and parameters with a default must come last 
    # this change means the BookRepository will no longer work as expected