from flask import Flask, render_template, url_for
app = Flask(__name__)

#PAGE 1: HOMEPAGE - SUMMARY
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

#PAGE 2: INSTALL FRAMEWORKS
@app.route("/install")
def about():
    return render_template('install.html', title='Installing Frameworks')

#PAGE 3 NEEDED!


#PAGE 4: DEMO PAGE - TORONTO
@app.route("/demo")
def demo():
    return render_template('demopage.html', title='Demo: Welcome to Toronto')

#PAGE 5: CONCLUSION
@app.route("/conclusion")
def conclusion():
    return render_template('conclusion.html', title='Conclusion')

#PAGE 6: CREDITS
@app.route("/credits")
def credits():
    return render_template('CreditsPage.html', title='Credits')

if __name__ == "__main__":
    app.run(debug=True)