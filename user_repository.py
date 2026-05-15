from user import User

class UserRepository:
    # first initialise the database connection
    def __init__(self, connection):
        self._connection = connection

    # function to create new users
    def create(self, user):
        self._connection.execute('INSERT INTO users (username, password) VALUES (%s, %s)', [user.username, user.password])
        return None
    
    # function to retrieve users:
    def all(self):
        rows= self._connection.execute('SELECT * FROM users')
        users =[]
        for user in rows: 
            item = User(user["username"], user["password"], user["id"])
            users.append(item)
        return users
    
    #function to find the user:
    def find_by_username(self, username):
        user_details = self._connection.execute('SELECT* FROM users WHERE username = %s', [username])[0]
        return User(
            user_details["username"],
            user_details["password"],
            user_details["id"]
        )