import qrcode
from PIL import Image

# URL do seu site
URL_SITE = "https://site-production-6665.up.railway.app"

# Gera o QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(URL_SITE)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# Salva na área de trabalho (Windows) automaticamente
import os
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
caminho = os.path.join(desktop, "qrcode.png")
img.save(caminho)

# Mostra a imagem
img.show()

print(f"QR code gerado e salvo na área de trabalho: {caminho}")
