from PIL import Image

img = Image.open("SadDogSong.jpg")

small = img.resize((img.width // 3, img.height // 3))
small.save("SmallSadDogSong.jpg")

gorizont = img.transpose(Image.FLIP_LEFT_RIGHT)
gorizont.save("HorizontSadDogSong.jpg")

vertical = img.transpose(Image.FLIP_TOP_BOTTOM)
vertical.save("VerticalSadDogSong.jpg")