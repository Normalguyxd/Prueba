import time
Libro = []
welcome = ("Bienvenido usuario de python ")
print (welcome)
time.sleep (0.3)
print (".")
time.sleep (0.3)
print (".")
time.sleep (0.3)
while True:
    diccionary = input ("Que gustaria agregar o aprender")
    if diccionary == "agregar" :
        time.sleep (0.3)
        print (".")
        time.sleep (0.3)
        print (".")
        time.sleep (0.3)
        add = input("Agrega Aqui = ")
        Libro.append(add)
    elif diccionary == "aprender":
        time.sleep (0.3)
        print (".")
        time.sleep (0.3)
        print (".")
        time.sleep (0.3)
        print (Libro)
    elif diccionary == "Easter Egg":
        time.sleep (0.3)
        print (".")
        time.sleep (0.3)
        print (".")
        time.sleep (0.3)
        print ("Easter Egg")
