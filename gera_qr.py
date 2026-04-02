import qrcode
import os

URL_SITE = "https://site-production-6665.up.railway.app"
QR_CODE = "qrcode.png"

print("Pasta atual:", os.getcwd())

img = qrcode.make(URL_SITE)
img.save(QR_CODE)
print(f"QR code gerado: {QR_CODE}")
