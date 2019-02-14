from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route("/")
@app.route("/home")			#PAGE 1: HOMEPAGE - SUMMARY
def home():
    return render_template('home.html', active='home')


@app.route("/install")		#PAGE 2: INSTALL FRAMEWORKS
def install():
    return render_template('install.html', title='Installing Frameworks', active='install')


@app.route("/tutorial")		#PAGE 3 TUTORIAL
def tutorial():
    return render_template('tutorial.html', title='Tutorial', active='tutorial')


@app.route("/demo")			#PAGE 4: DEMO PAGE - TORONTO
def demo():
    return render_template('demopage.html', title='Demo: Welcome to Toronto', active='demo')


@app.route("/conclusion")	#PAGE 5: CONCLUSION
def conclusion():
    return render_template('conclusion.html', title='Conclusion', active='conclusion')


@app.route("/credits")		#PAGE 6: CREDITS
def credits():
    return render_template('creditspage.html', title='Credits', active='credits')

if __name__ == "__main__":
    app.run(debug=True)		#debug=True for debug mode
