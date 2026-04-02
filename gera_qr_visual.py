import qrcode

URL_SITE = "https://site-production-6665.up.railway.app"

# Gera o QR code
img = qrcode.make(URL_SITE)

# Salva e mostra a imagem automaticamente
img.save("qrcode.png")
img.show()
