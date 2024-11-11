# from flask import Flask, request, jsonify
# from itertools import combinations_with_replacement
# import math

# app = Flask(__name__)

# def get_possible_shapes(num_elements, dimensions):
#     # Get all factors of num_elements
#     factors = [i for i in range(1, num_elements + 1) if num_elements % i == 0]

#     # Generate possible factor combinations for the specified dimensions
#     valid_shapes = [
#         shape for shape in combinations_with_replacement(factors, dimensions)
#         if math.prod(shape) == num_elements
#     ]
#     return valid_shapes


# @app.route('/')
# def home():
#     return "Hello, Flask server is running!"


# @app.route('/calculate-shapes', methods=['POST'])
# def calculate_shapes():
#     data = request.get_json()
#     num_elements = data.get("num_elements")
#     dimensions = data.get("dimensions")

#     # Validate input
#     if not num_elements or not dimensions:
#         return jsonify({"error": "Please provide valid num_elements and dimensions"}), 400

#     shapes = get_possible_shapes(num_elements, dimensions)
#     return jsonify({"shapes": shapes})

# if __name__ == '__main__':
#     app.run(debug=True)



# api/index.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from itertools import combinations_with_replacement
import math

app = Flask(__name__)
CORS(app)



@app.route('/')
def home():
    return "Hello, Flask server is running!"


def get_possible_shapes(num_elements, dimensions=2):
    factors = [i for i in range(1, num_elements + 1) if num_elements % i == 0]
    valid_shapes = [
        shape for shape in combinations_with_replacement(factors, dimensions)
        if math.prod(shape) == num_elements
    ]
    return valid_shapes



# @app.route('/api/calculate-shapes', methods=['POST'])
@app.route('/calculate-shapes', methods=['POST'])
def calculate_shapes():
    data = request.get_json()
    num_elements = data.get("num_elements")
    dimensions = data.get("dimensions", 2)  # Default to 2D shapes if not provided

    if not num_elements or not isinstance(num_elements, int):
        return jsonify({"error": "Please provide a valid integer for num_elements"}), 400

    shapes = get_possible_shapes(num_elements, dimensions)
    return jsonify({"shapes": shapes})

# Run the Flask app if executing this script directly
if __name__ == '__main__':
    app.run(debug=True)
