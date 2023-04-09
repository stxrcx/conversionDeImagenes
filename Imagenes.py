#Presiona las siguientes teclas (windows + r) y escribe cmd
#Copia y pega lo siguiente en la consola: pip install Pillow
#Presiona enter y ya puedes usar el programa :)

from PIL import Image

path = input("Ingrese la ruta de la imagen y su extensión: ")

#Ejemplo: C:\Users\Emmanuel\Desktop\Imagenes\BMP.bmp

img = Image.open(path)

bits = input("Ingrese la cantidad de bits deseada (24, 8, 4): ")

if bits == '24':
    img = img.convert('RGB')
elif bits == '8':
    img = img.convert('P', palette=Image.ADAPTIVE, colors = 256)
elif bits == '4':
    img = img.convert('P', palette=Image.ADAPTIVE, colors = 16)
else:
    print("Error: El número de bits debe ser 24, 8 o 4.")
    exit()

format = input("Ingresa el formato de imagen deseado(bmp, jpeg, tiff, gif, png, otro): ")

nuevoNombre = input("Nombre de la imagen final: ")

img = img.convert('RGB')
img.save(nuevoNombre + "." + format.lower(), format=format)