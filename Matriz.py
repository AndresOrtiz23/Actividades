class matriz:
    def __init__(self,lista):
        self.lista=lista
        if len(lista)==4:
            self.n=2
        elif len(lista)==9:
            self.n=3
    def __str__(self):
        if self.n==2:
            Palabra=""
            for i in range (4):
                Palabra=Palabra+str(self.lista[i])+","
                if i==1:
                    Palabra=Palabra+("\n")
            return f'{Palabra}'
        elif self.n==3:
            Palabra=""
            for i in range (9):
                Palabra=Palabra+str(self.lista[i])+","
                if (i+1)%3==0:
                    Palabra=Palabra+("\n")
            return f'{Palabra}'
    def __getitem__(self,indice):
        k=self.n*indice[0]+indice[1]
        return self.lista[k]
    
    def __setitem__(self,indice,valor):
        k=self.n*indice[0]+indice[1]
        self.lista[k]=valor         
a=[2,3,5,7]
#a=[2,3,5,7,8,2,7,8,3]
b=matriz(a)
print(b[0,1])
print(b)
b[0,1]=25
print(b)
