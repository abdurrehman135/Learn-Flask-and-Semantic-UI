from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/install")
def about():
    return render_template('install.html', title='Installing Frameworks')

if __name__ == "__main__":
    app.run(debug=True)