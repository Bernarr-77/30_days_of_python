class Cachorro:
    def __init__(self,nome,raca):
        self.nome = nome
        self.raca = raca
    def latir(self) -> str:
        return f"{self.nome} fez, au au"
    
dog = Cachorro(nome="rex",raca="Pug")
print(dog.latir())