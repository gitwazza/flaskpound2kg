# This Flask application demonstrates how
# we could use Flask to achieve a similar outcome to
# what we might achieve with a simple pounds to kgs program
# Created by Warren Sutton on 12 Feb 2024

from flask import Flask, request, render_template

app = Flask(__name__)

def convert(pound):
    if pound < 0:
        print("Cannot Convert Negatives")
    else:
        k = pound * 0.453592
        return str(k)

def convertv2(pound):
    if pound < 0:
        return "error"
    else:
        k = pound * 0.453592
        return str(k)

@app.route('/')
def index():
    return render_template("index.html")

# This first version ('/convert1' below)
# demonstrates flask with HTML files in the
# templates folder, but it has some issues with the way the
# results are displayed on the terminal rather than the page itself.
# It's also a bit ugly in the way the convert function returns a
# value if the conversion works, but reports the error itself if
# a negative value is entered.
@app.route('/convert1', methods=["POST","GET"])
def convert1():
    if request.method == 'POST':
        pounds = request.form["pounds"]
        kilograms = convert(int(pounds))
        print(f'{pounds} pounds is equal to {kilograms} kilograms')
        return render_template("result1.html")

    if request.method == 'GET':
        return render_template("convert1.html")

# In this second example we will return the result to a new page.
# The page returns the HTML directly embedded in the function.
# This allows the inclusion of variables into the string the
# program creates.
@app.route('/convert2', methods=["POST","GET"])
def convert2():
    if request.method == 'POST':
        pounds = request.form["pounds"]
        kilograms = convert(int(pounds))
        myline = f'{pounds} pounds is equal to {kilograms} kilograms'
        mypage = f"""
<body>
  <H1>The result in KGs</H1>
  <br>
  
  <p>{myline}</p>
</body>
        """
        return mypage

    if request.method == 'GET':
        return render_template("convert2.html")

# In this third example we will introduce Jinja. This will allow the use of
# passing variables between this python flask module and the flask rendering
# engine - this allows for non-standard HTML pages with variables within the
# HTML page itself using Jinja.
@app.route('/convert3', methods=["POST", "GET"])
def convert3():
    if request.method == 'POST':
        pounds = request.form["pounds"]
        kilograms = convert(int(pounds))
        myline = f'{pounds} pounds is equal to {kilograms} kilograms'
        return render_template("result3.html", myline=myline)

    if request.method == 'GET':
        return render_template("convert3.html")

# In this 4th example the convert4 function is very similar to the convert
@app.route('/convert4', methods=["POST", "GET"])
def convert4():
    if request.method == 'POST':
        pounds = request.form["pounds"]
        print(int(pounds))
        kilograms = convertv2(int(pounds))
        if kilograms == "error":
            myline = "The value entered was less than zero"
        else:
            myline = f'{pounds} pounds is equal to {kilograms} kilograms'
        return render_template("result3.html", myline=myline)

    if request.method == 'GET':
        return render_template("convert4.html")

if __name__ == '__main__':
    app.run()
