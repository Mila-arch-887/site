import qrcode
from PIL import Image

URL_SITE = "https://site-production-6665.up.railway.app"

# Gera o QR code
img = qrcode.make(URL_SITE)

# Mostra a imagem direto
img.show()
