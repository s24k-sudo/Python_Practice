class user:
    user_count = 0
    def __init__(self, user_name, email ):
        self.user_name = user_name
        self.email = email
        user.user_count +=1

    def display_user(self):
        print(f"The user name is :{self.user_name} and the email_id is :{self.email}")

user1 = user("batman", "user12@gmail.com")
user2 = user ("ironman", "user2@gmail.com")
user3 = user("superman","user3@gmail.com")

print(user.user_count)

user1.display_user()
user2.display_user()
user3.display_user()
        