#Définition image : Représentation mentale que l'on se fait de quelque chose ou de quelqu'un.
#Résolution image : La résolution représente une densité de points (ou pixels) sur une longueur donnée 
#Profondeur de couleur : La profondeur de couleurs, dont l'unité est le bits par pixel, est un terme utilisé en informatique décrivant le nombre de bits utilisés pour représenter la couleur d'un pixel dans une image.

from PIL import Image

img1 = Image.open("iguane.jpg")
img1.show()


def definition_image(image):
    largeur = image.width
    longueur = image.height
    return longueur * largeurecho "# MP4" >> README.md

print(definition_image(img1))

x = 5
y = 10
couleur = img1.getpixel((x, y))  # couleur est un tuple
R, V, B = couleur, couleur, couleur

print("Les composantes R,V,B du pixel (x={},y={}) sont R={},V={} et B={}".format(x, y, R, V, B))


def symetrie_horizontale(image):
    rotation = image.transpose(Image.FLIP_LEFT_RIGHT)
    rotation.show()
    return "Votre résultat s'affiche"


print(symetrie_horizontale(img1))


def symetrie_horizontale(image):
    rotation = image.transpose(Image.FLIP_TOP_BOTTOM)
    rotation.show()
    return "Votre résultat s'affiche"


print(symetrie_horizontale(img1))


def niveau_gris(image):
    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            pixelVal = image.getpixel((i, j))
            rouge = pixelVal[0]
            vert = pixelVal[1]
            bleu = pixelVal[2]
            pixel = rouge // 3 + vert // 3 + bleu // 3
            image.putpixel((i, j), (pixel, pixel, pixel))
    image.show()
    return "Votre résultat s'affiche"


print(niveau_gris(img1))


def negatif_image(image):
    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            pixelVal = image.getpixel((i, j))
            rouge = 255 - pixelVal[0]
            vert = 255 - pixelVal[1]
            bleu = 255 - pixelVal[2]
            image.putpixel((i, j), (rouge, vert, bleu))
    image.show()
    return "Votre résultat s'affiche"


print(negatif_image(img1))