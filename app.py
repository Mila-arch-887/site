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

URL_SITE = "site-production-6665.up.railway.app"

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
    try:
        if os.path.exists(ARQUIVO_DATA):
            with open(ARQUIVO_DATA, "r") as f:
                ultimo = f.read()
        else:
            ultimo = (datetime.utcnow() - timedelta(hours=3)).strftime("%d/%m/%Y às %H:%M")

        img = Image.open(IMAGEM_ORIGINAL)
        draw = ImageDraw.Draw(img)

        texto = f"Consulta em {ultimo}"
        fonte = ImageFont.load_default()

        largura_img, altura_img = img.size
        x = largura_img - 300
        y = altura_img - 50

        draw.text((x, y), texto, fill=(0, 0, 0), font=fonte)

        img.save(IMAGEM_FINAL)

        agora = (datetime.utcnow() - timedelta(hours=3)).strftime("%d/%m/%Y às %H:%M")
        with open(ARQUIVO_DATA, "w") as f:
            f.write(agora)

        return send_file(IMAGEM_FINAL, mimetype='image/png')

    except Exception as e:
        return f"Erro: {e}"

if __name__ == "__main__":
    gerar_qr()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
