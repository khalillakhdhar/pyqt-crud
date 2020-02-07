class User:
    def __init__(self,id,nom,login,mdp):
        self.id=id
        self.nom=nom
        self.login=login
        self.mdp=mdp
    def __init__(self,login,mdp):
        self.login=login
        self.mdp=mdp
"""u1=User("admin","pass")
print(u1.login)
u1.nom="ahmed"
print(u1.nom)"""