import math
archivo  = open('cos100.csv','w', encoding="utf-8")
for i in range (361):
    
    aux=i*math.pi/180
    Val=math.cos(aux)
    Val=(Val+1)*50
    print(i)
    print(Val)
    S="Grados: "+str(i)+"  Porcentaje: "+str(Val)
    str(Val)
    str(i)
    archivo.write(S+"\n")
archivo.close()
