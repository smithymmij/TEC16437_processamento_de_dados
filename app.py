from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_triangle', methods=['POST'])
def check_triangle():
    a = int(request.form['lado_a'])
    b = int(request.form['lado_b'])
    c = int(request.form['lado_c'])

    if a == 0 or b == 0 or c == 0 or a + b <= c or a + c <= b or b + c <= a:
        resultado = "Não compõem triângulo"
    elif a == b == c:
        resultado = "Triângulo Equilátero"
    elif a == b or b == c or a == c:
        resultado = "Triângulo Isósceles"
    else:
        resultado = "Triângulo Escaleno"

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
