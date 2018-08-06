import qrcode

img = qrcode.make("xxx，我喜欢你！")
img.get_image().show()
img.save('hello.png')