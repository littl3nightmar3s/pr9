from PIL import Image

img = Image.open("SadDogSong.jpg")
wm = Image.open("watermark.png")

img.paste(wm, (img.width - wm.width, img.height - wm.height), wm)
img.save("watermarkSadDogSong.jpg")




# faili = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
#
# wm = Image.open("watermark.png")
#
# for name in faili:
#     img = Image.open(name)
#     img.paste(wm, (img.width - wm.width, img.height - wm.height), wm)
#     img.save("WM" + name)