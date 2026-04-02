import qrcode

URL_SITE = "https://site-production-6665.up.railway.app"
QR_CODE = "qrcode.png"

img = qrcode.make(URL_SITE)
img.save(QR_CODE)
print(f"QR code gerado: {QR_CODE}")
