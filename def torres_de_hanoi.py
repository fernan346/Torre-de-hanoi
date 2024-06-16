def torres_de_hanoi(n, origen,auxiliar,destino):
    if n==1:
        print(origen,destino)
        return
    torres_de_hanoi(n-1,origen,destino,auxiliar)
    print(n,origen,destino)
    torres_de_hanoi(n-1,auxiliar,origen,destino)
n=3
torres_de_hanoi(n,'A','B','C')