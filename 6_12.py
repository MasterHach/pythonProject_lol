import colorsys
from PIL import Image
import os
import PIL.Image

filename = 'anon.jpg'
target_hue = 0
image = Image.open(filename).convert('RGB')
image.load()
r, g, b = image.split()
result_r, result_g, result_b = [], [], []
# Обрабатывать каждый пиксель по очереди
for pixel_r, pixel_g, pixel_b in zip(r.getdata(), g.getdata(), b.getdata()):
        # Преобразовать в значение цвета HSV
    h, s, v = colorsys.rgb_to_hsv(pixel_r / 255., pixel_b / 255., pixel_g / 255.)
        # Переключиться обратно на цвет RGB
    rgb = colorsys.hsv_to_rgb(target_hue, s, v)
    pixel_r, pixel_g, pixel_b = [int(x * 255.) for x in rgb]
        # Сохранить результаты для каждого пикселя
    result_r.append(pixel_r)
    result_g.append(pixel_g)
    result_b.append(pixel_b)
r.putdata(result_r)
g.putdata(result_g)
b.putdata(result_b)
image = Image.merge('RGB', (r, g, b))
# Вывод картинки
image.save('output.png')
