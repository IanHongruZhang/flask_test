from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

#Jinja 最为强大的地方在于他的模板继承功能，模板继承允许你创建一个基础的骨架模板
#这个模板包含您网站的通用元素，并且定义子模板可以重载的 blocks 。

@app.route("/",methods = ["GET","POST"])
def home():
	return render_template("hello.html",title_name = "welcome")

@app.route("/service",methods = ["GET","POST"])
def service():
	return "service"

@app.route("/about")
def about():
	return "about"

if __name__ == "__main__":
	app.run(debug = True)