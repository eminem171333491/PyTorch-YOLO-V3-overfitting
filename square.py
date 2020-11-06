from PIL import Image
import os

img_path = r"./data/iamge"
i = 1
for img in os.listdir(img_path):
    image=Image.open(os.path.join(img_path,img))
    image = image.convert('RGB')
    w, h = image.size
    background = Image.new('RGB', size=(max(w, h), max(w, h)), color=(0,0,0))  # 创建背景图
    length = int(abs(w - h) // 2)  # 一侧需要填充的长度
    box = (length, 0) if w < h else (0, length)  # 粘贴的位置
    background.paste(image, box)
    im = background.resize((416,416))
    im.save(os.path.join("./data/va_img","{}.jpg".format(i)))
    i += 1

