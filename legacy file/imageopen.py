from PIL import Image

with Image.open("category/mga hayop sa pinas/agila.jpg") as im:
    im.rotate(45).show()
