from PIL import Image, ImageFilter

for i in range(1, 6):
    name = str(i) + ".jpg"
    img = Image.open(name)
    img2 = img.filter(ImageFilter.EMBOSS)
    img2.save("new_" + str(i) + ".jpg")