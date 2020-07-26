import flask
from flask import request,jsonify,render_template
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def main():
    return render_template("calculator.html")
@app.route('/calculated', methods=['POST'])
def calculated():
    a=int(request.form['a'])
    b=int(request.form['b'])
    if(op=='+'):
        return jsonify({'result is': a+b})
    elif(op=='*'):
        return jsonify({'result is'    op=str(request.form['op'])
: a * b})
    else:
        return jsonify({'result is': "not a valid input"})


if __name__ == '__main__':
    app.run(debug=True)