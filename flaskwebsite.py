from flask import Flask, render_template, url_for, request
app = Flask(__name__)

#PAGE 1: HOMEPAGE - SUMMARY
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', active='home')

#PAGE 2: INSTALL FRAMEWORKS
@app.route("/install")#, methods=['GET', 'POST'])
def install():
	#if request.method == 'POST'
    return render_template('install.html', title='Installing Frameworks', active='install')

#PAGE 3 TUTORIAL
@app.route("/tutorial")
def tutorial():
    return render_template('tutorial.html', title='Tutorial', active='tutorial')

#PAGE 4: DEMO PAGE - TORONTO
@app.route("/demo")
def demo():
    return render_template('demopage.html', title='Demo: Welcome to Toronto', active='demo')

#PAGE 5: CONCLUSION
@app.route("/conclusion")
def conclusion():
    return render_template('conclusion.html', title='Conclusion', active='conclusion')

#PAGE 6: CREDITS
@app.route("/credits")
def credits():
    return render_template('creditspage.html', title='Credits', active='credits')

if __name__ == "__main__":
    app.run(debug=True)