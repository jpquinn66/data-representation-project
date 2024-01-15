# Import necessary modules from Flask
from flask import Flask, render_template, request, jsonify

# Import the AntiB class from the AntiB module (Assuming it's a custom module in the same directory)
from AntiB import AntiB

# Create a Flask web application instance
app = Flask(__name__)

# Create an instance of the AntiB class
antiB_instance = AntiB()

# Define a route for the root URL ('/') that renders the 'index.html' template
@app.route('/')
def index():
    return render_template('index.html')

# Define a route for GET requests to '/api/data'
# This endpoint retrieves all data using the get_all_data method of the AntiB instance
@app.route('/api/data', methods=['GET'])
def get_all_data():
    data = antiB_instance.get_all_data()
    return jsonify(data)

# Define a route for POST requests to '/api/data'
# This endpoint adds new data by calling the create method of the AntiB instance
@app.route('/api/data', methods=['POST'])
def add_data():
    # Retrieve JSON data from the request
    data = request.json
    # Create new data using the create method of the AntiB instance
    new_data_id = antiB_instance.create(data)
    # Return a JSON response indicating success and the ID of the newly added data
    return jsonify({'message': 'Data added successfully!', 'new_data_id': new_data_id})

# Define a route for PUT requests to '/api/data/<int:data_id>'
# This endpoint updates existing data by calling the update method of the AntiB instance
@app.route('/api/data/<int:data_id>', methods=['PUT'])
def update_data(data_id):
    # Retrieve JSON data from the request
    data = request.json
    # Update data with the specified ID using the update method of the AntiB instance
    updated_data_id = antiB_instance.update(data_id, data)
    # Return a JSON response indicating success and the ID of the updated data
    return jsonify({'message': 'Data updated successfully!', 'updated_data_id': updated_data_id})

# Define a route for DELETE requests to '/api/data/<int:data_id>'
# This endpoint deletes existing data by calling the delete method of the AntiB instance
@app.route('/api/data/<int:data_id>', methods=['DELETE'])
def delete_data(data_id):
    # Delete data with the specified ID using the delete method of the AntiB instance
    deleted_data_id = antiB_instance.delete(data_id)
    # Return a JSON response indicating success and the ID of the deleted data
    return jsonify({'message': 'Data deleted successfully!', 'deleted_data_id': deleted_data_id})

# Run the Flask application if this script is the main module
if __name__ == "__main__":
    app.run(debug=True)
