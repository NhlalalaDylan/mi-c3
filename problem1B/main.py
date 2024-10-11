from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

def time_difference(t1, t2):
    timestamp_format = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.strptime(t1, timestamp_format)
    dt2 = datetime.strptime(t2, timestamp_format)
    return abs(int((dt1 - dt2).total_seconds()))

@app.route('/calculate', methods=['POST'])
def calculate_time_difference():
    input_data = request.get_data(as_text=True).strip()
    input_lines = list(filter(None, input_data.splitlines()))
    T = int(input_lines[0])
    
    results = []
    for i in range(1, 2 * T, 2):
        t1 = input_lines[i].strip()
        t2 = input_lines[i + 1].strip()
        diff = time_difference(t1, t2)
        results.append(diff)

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
