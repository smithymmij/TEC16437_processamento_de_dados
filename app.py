from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_triangle', methods=['POST'])
def check_triangle():
    a = int(request.form['lado_a'])
    b = int(request.form['lado_b'])
    c = int(request.form['lado_c'])

    if a == 0 or b == 0 or c == 0:
        resultado = "Não compõem triângulo"
    else:
        if a == b == c:
            resultado = "Triângulo Equilátero"
        elif a == b or b == c or a == c:
            resultado = "Triângulo Isósceles"
        else:
            resultado = "Triângulo Escaleno"

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Pega a porta do ambiente ou usa 5000 por padrão
    app.run(host='0.0.0.0', port=port, debug=True)
