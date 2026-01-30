class User():
    def __init__(self, name , _mail_id):
        self.name=name
        self. _mail_id =_mail_id
    @property
    def mail_id(self):
        print("Email accesed")
        return self._mail_id
    
    @mail_id.setter
    def mail_id(self, newmail):
        if "@" in newmail:
            self._mail_id = newmail
    

   
       

user1=User("Soham","soham@mail.com")

user1.mail_id ="Sk@gmail.com"

print(user1.mail_id)
