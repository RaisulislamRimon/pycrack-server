from flask import Flask, request, jsonify
from itertools import combinations_with_replacement
import math

app = Flask(__name__)

def get_possible_shapes(num_elements, dimensions):
    # Get all factors of num_elements
    factors = [i for i in range(1, num_elements + 1) if num_elements % i == 0]

    # Generate possible factor combinations for the specified dimensions
    valid_shapes = [
        shape for shape in combinations_with_replacement(factors, dimensions)
        if math.prod(shape) == num_elements
    ]
    return valid_shapes

@app.route('/calculate-shapes', methods=['POST'])
def calculate_shapes():
    data = request.get_json()
    num_elements = data.get("num_elements")
    dimensions = data.get("dimensions")

    # Validate input
    if not num_elements or not dimensions:
        return jsonify({"error": "Please provide valid num_elements and dimensions"}), 400

    shapes = get_possible_shapes(num_elements, dimensions)
    return jsonify({"shapes": shapes})

if __name__ == '__main__':
    app.run(debug=True)
