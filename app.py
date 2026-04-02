from flask import Flask, send_file
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, timedelta
import os
import qrcode

app = Flask(__name__)

ARQUIVO_DATA = "ultimo.txt"
IMAGEM_ORIGINAL = "base.png"
IMAGEM_FINAL = "final.png"
QR_CODE = "qrcode.png"

URL_SITE = "http://127.0.0.1:5000"

def gerar_qr():
    if not os.path.exists(QR_CODE):
        img = qrcode.make(URL_SITE)
        img.save(QR_CODE)

@app.route("/")
def home():
    return f"""
    <html>
    <head>
        <title>araucaria.atende.net</title>
    </head>
    <body style="margin:0;">
        <img src="/imagem" style="width:100%;">
    </body>
    </html>
    """

@app.route("/imagem")
def gerar():
    if os.path.exists(ARQUIVO_DATA):
        with open(ARQUIVO_DATA, "r") as f:
            ultimo = f.read()
    else:
        ultimo = datetime.now().strftime("%d/%m/%Y às %H:%M")

    img = Image.open(IMAGEM_ORIGINAL)
    draw = ImageDraw.Draw(img)

    texto = f"Consulta em {ultimo}"
    fonte = ImageFont.truetype("DejaVuSans.ttf", 80)
    
    bbox = draw.textbbox((0, 0), texto, font=fonte)
    largura_texto = bbox[2] - bbox[0]
    altura_texto = bbox[3] - bbox[1]

    largura_img, altura_img = img.size
    x = largura_img - largura_texto - 40
    y = altura_img - altura_texto - 30

    draw.text((x, y), texto, fill=(80, 80, 80), font=fonte)

    img.save(IMAGEM_FINAL)

    agora = datetime.now().strftime("%d/%m/%Y às %H:%M")
    with open(ARQUIVO_DATA, "w") as f:
        f.write(agora)

    return send_file(IMAGEM_FINAL, mimetype='image/png')

if __name__ == "__main__":
    gerar_qr()
    app.run(host="0.0.0.0", port=5000)
