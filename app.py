
from flask import Flask, render_template, request, jsonify
import json
from main import main as convert_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        data = request.get_json()
        result = convert_data(data)
        return jsonify({'success': True, 'result': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/sample-data')
def sample_data():
    # Load sample data for testing
    with open("./data-1.json", "r") as f:
        data1 = json.load(f)
    with open("./data-2.json", "r") as f:
        data2 = json.load(f)
    
    return jsonify({
        'format1': data1,
        'format2': data2
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
