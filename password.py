class credential :
    

    def __init__(self, title, usr, paswd):
        self.title = title
        self.username= usr
        self.password = passphrase

    def getinfo(self) :
        output= f" (\n{self.title} \nusername:{self.username} \npassword : {self.password}"
        return output
    
cred = credential("facebook", "test_hack" , "hkg$%&")
cred2 = credential("github", "lermxy16","huoh$$_7>€")
#vault that store cred

vault = []
vault.append(cred)
vault.append(cred2)
#search for a spevific cred
query = input("enter your search term")

for cred in vault :
    if cred.title == query :
        print(cred.getinfo())
