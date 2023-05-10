with open("dados.txt", "r") as arquivo:
    text = arquivo.read() 
    contador = text.count("Ola")
    print("Texto = ", repr(text))
    print("Total de Olás = ", contador)