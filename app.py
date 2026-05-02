from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

def gerar_senha(tamanho, especiais, numeros, minusculas, maiusculas):
    caracteres = ""

    if especiais:
        caracteres += "!@#$%&*()-_=+[]{};:,.?/"

    if numeros:
        caracteres += string.digits

    if minusculas:
        caracteres += string.ascii_lowercase

    if maiusculas:
        caracteres += string.ascii_uppercase

    if not caracteres:
        return "Selecione ao menos uma opção."

    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    return senha

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gerar", methods=["POST"])
def gerar():
    data = request.get_json()

    tamanho = int(data.get("tamanho", 8))
    especiais = data.get("especiais", False)
    numeros = data.get("numeros", False)
    minusculas = data.get("minusculas", False)
    maiusculas = data.get("maiusculas", False)

    if tamanho < 4 or tamanho > 20:
        return jsonify({"senha": "A quantidade deve ser entre 4 e 20 dígitos."})

    senha = gerar_senha(
        tamanho,
        especiais,
        numeros,
        minusculas,
        maiusculas
    )

    return jsonify({"senha": senha})

if __name__ == "__main__":
    app.run(debug=True)
