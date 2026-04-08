from PIL import Image

img = Image.open("sad.jpg")
img.show()

w, h = img.size
print("Ширина:", w)
print("Высота:", h)
print("Формат:", img.format)
print("Цветовая модель:", img.mode)