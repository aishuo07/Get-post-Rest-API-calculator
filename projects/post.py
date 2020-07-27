import flask
from flask import request,jsonify
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/calc', methods=['GET','POST'])
def home():
    if(flask.request.method=='GET'):
        a=int(request.args.get('value1'))
        b=int(request.args.get('value2'))
        op=str(request.args.get('operation'))
        if(op==' '):
            return jsonify({'result is': a+b})
        elif(op=='*'):
            return jsonify({'result is': a * b})
        elif (op == '-'):
            return jsonify({'result is': a - b})
        else:
            return jsonify({'result is': "not a valid input"})
    if(flask.request.method=='POST'):
        a=int(request.form['value1'])
        b=int(request.form['value2'])
        op=str(request.form['operation'])
        if(op=='+'):
            return jsonify({'result is': a+b})
        elif(op=='*'):
            return jsonify({'result is': a * b})
        elif(op=='-'):
            return jsonify({'result is': a - b})
        else:
            return jsonify({'result is': "not a valid input"})
    else:
        return "<h1>Bad Request</h1>"



if __name__ == '__main__':
    app.run(debug=True)
