class dog:
    def __init__(self, name , breed, owner):# need to add the owner as parameter
        self.name= name
        self.breed= breed
        self.ownr=owner
    def Bark(self):
        print("Woof Woof")

class owner:# new class
    def __init__(self,name,address,contact_no):
        self.name=name
        self.address=address
        self.contact_no=contact_no

owner1=owner("Soham","Pune",1234567890)# new class object1
owner2=owner("Rohit","Mumbai",9876543210)# new class object2
    

dog1=dog("Tommy","Bulldog",owner1)#combining the objects
dog1.Bark()
print("Owner name: ",dog1.ownr.name) # printing the datafields of owner class
print("Owner address:",dog1.ownr.address)
print("Owner contact no:",dog1.ownr.contact_no)

print(dog1.name)
print(dog1.breed)


dog2=dog("Bruno","Labrador",owner2)
dog2.Bark()
print("Owner name: ",dog2.ownr.name)
print("Owner address:",dog2.ownr.address)
print("Owner contact no:",dog2.ownr.contact_no)

print(dog2.name)
print(dog2.breed)