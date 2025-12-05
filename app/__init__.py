from flask import Flask , render_template

app = Flask(__name__, template_folder="templates")

@app.get("/")
def home():
    return render_template("index.html")
@app.get("/index")
def home():
    return render_template("index.html")


if __name__== "__main__":
    app.run(debug=True , port=8000)