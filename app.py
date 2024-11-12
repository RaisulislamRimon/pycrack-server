from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import math

app = Flask(__name__)
CORS(app)

def find_2d_shape(total_elements):
    for i in range(1, int(math.sqrt(total_elements)) + 1):
        if total_elements % i == 0:
            return (i, total_elements // i)
    return None

def find_3d_shape(total_elements):
    for i in range(1, int(total_elements ** (1/3)) + 1):
        if total_elements % i == 0:
            sub_total = total_elements // i
            for j in range(1, int(math.sqrt(sub_total)) + 1):
                if sub_total % j == 0:
                    return (i, j, sub_total // j)
    return None



@app.route('/')
def home():
    return "Hello, Flask server is running!"


@app.route('/reshape', methods=['POST'])
def reshape_array():
    data = request.get_json()
    total_elements = data['total_elements']

    # Find 2D and 3D shapes
    shape_2d = find_2d_shape(total_elements)
    shape_3d = find_3d_shape(total_elements)

    if not shape_2d or not shape_3d:
        return jsonify({"error": "Cannot find suitable 2D or 3D shape for the given total elements"}), 400

    num = np.arange(total_elements)
    reshaped_2d = num.reshape(shape_2d).tolist()
    reshaped_3d = num.reshape(shape_3d).tolist()

    return jsonify({
        "reshaped_2d": reshaped_2d,
        "reshaped_3d": reshaped_3d,
        "shape_2d": shape_2d,
        "shape_3d": shape_3d
    })

if __name__ == '__main__':
    app.run(debug=True)
