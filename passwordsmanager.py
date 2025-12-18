class credential :
    

    def __init__(self, title, usr, paswd):
        
        self.title = title
        self.username= usr
        self.password = paswd

    def getinfo(self) :
        output= f" (\n{self.title} \nusername:{self.username} \npassword : {self.password}"
        return output
    
cred = credential("whatsapp", "test_hack" , "hkg$%&")
cred2 = credential("github", "lermxy16","huoh$$_7>€")
cred3 = credential("facebook", "hadiza aliyu" , "%&$565667")
cred4 = credential("microsoft","Saabdullahi","drawer")
cred5 = credential("linux","leemxy","##ssool")
#vault that store cred

vault = []
vault.append(cred)
vault.append(cred2)
vault.append(cred3)
vault.append(cred4)
vault.append(cred5)
#search for a spevific cred
def search():
    query = input("enter your search term")
    for cred in vault :
        if query.lower() in cred.title.lower() :
            #partial search/ case sentuive
           print(cred.getinfo())


def displayAll():
    for cred in vault :
        print(cred.title)

def addCredential():
    myTitle = input("enter you title of credential")
    myUsername = input("enter the yser name")
    myPassword = input("enter your password")
    myCred = credential ( myTitle, myUsername, myPassword)
    vault.append(myCred)

while True :
    print("welcome to your password manager")
    print("what will you like to do?")
    print("  1. search")
    print("  2. add a credential ")
    print("  3. quit")

    try:

       response = int(input())

       if response == 1 :
          displayAll()
          print("--------\n")
          search()
          print("\n")
       elif response == 2 :
            addCredential()
            print("credential has been added\n")
            print("-------\n")

       elif response == 3 :
            break
       else :
            print("the only option available are 1,2 and 3")
    except ValueError :
        #display if user does not enter an unterger
        print ("Enter the digit that correspond to menu option")
        





























































