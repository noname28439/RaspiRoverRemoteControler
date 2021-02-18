from flask import Flask, render_template, Markup, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/stickres/", methods=["POST"])
def stickreceaver():
    x = -float(request.form["x"])
    y = float(request.form["y"])

    k = 0.5

    if x != 0 and y != 0:
        right = -(y-k*x)
        left = -(y+k*x)

        if left>1:
            left=1
        if right>1:
            right=1

        print(str(left) + "|" + str(right))

    return ""




app.run(debug=True, host="0.0.0.0", threaded=True, port=8001)
