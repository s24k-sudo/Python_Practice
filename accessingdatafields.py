from datetime import datetime
class User:
    def __init__(self, username,_mail_id,password):
        self.username=username
        self._mail_id=_mail_id
        self.password=password

    def access_mail(self):
        return self._mail_id
    
    def clean_email(self):
        return self._mail_id .lower().strip()
    
    def get_email(self): #getter method
        print(f"The mail accesed on :{datetime.now()}")
        return self._mail_id
    
    def set_email( self , newmail):
         if "@" in newmail :
              self._mail_id = newmail
              


user1=User("Spidy","Spidy@gmail.com","spyd@123")
user2=User("Batman","batman@gmail.com","batman@123")


#print (user1.clean_email())
#print(user1._mail_id)



user1.set_email("lnndjn@fnksdn.com")
print(user1.get_email())
