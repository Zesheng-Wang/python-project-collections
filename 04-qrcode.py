import pyqrcode
import png
link = "https://github.com/Zesheng-Wang"
qr_code = pyqrcode.create(link)
qr_code.png("result.png", scale=5)
