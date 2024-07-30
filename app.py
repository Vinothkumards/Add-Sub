from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/api/calculate',methods = ['POST'])

def calculate():
    data = request.get_json()
    operation = data['operation']
    num1 = data['num1']
    num2 = data['num2']

    if operation == 'add':
        result = num1 + num2
    elif operation == 'sub':
        result = num1 - num2
    elif operation == 'mul':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0 :
            result = num1 / num2
        else:
            result = 'Error: Division by Zero'
    else:
        result = 'Error: Invalid Operation'
    
    return jsonify({'result':result})
    
if __name__ == '__main__':
    app.run(debug=True)

