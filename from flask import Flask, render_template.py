from flask import Flask, render_template_string

app = Flask(__name__)

html = open("teste_duplo_clique.html").read()  # arquivo HTML acima

@app.route("/")
def index():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
