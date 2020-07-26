import flask
from flask import request,jsonify
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    a=int(request.args.get('a'))
    b=int(request.args.get('b'))
    op=str(request.args.get('op'))
    if(op==' '):
        return jsonify({'result is': a+b})
    elif(op=='*'):
        return jsonify({'result is': a * b})
    elif (op == '-'):
        return jsonify({'result is': a - b})
    else:
        return jsonify({'result is': "not a valid input"})


if __name__ == '__main__':
    app.run(debug=True)