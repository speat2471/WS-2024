from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import json
from pymongo import MongoClient
from bson.json_util import dumps
import graphene
from graphene import ObjectType, String, List

app = Flask(__name__)
api = Api(app)

# MongoDB connections
client = MongoClient("mongodb://root:example@localhost:27017/")
db = client.Products  
collection = db.products 

API_KEY = "letmein"

# GraphQL object type for Product
class Product(ObjectType):
    id = String()
    name = String()

# GraphQL Query class
class Query(ObjectType):
    product_names = List(String)

    def resolve_product_names(self, info):
        # Fetch product names from MongoDB
        names = [product['name'] for product in collection.find({}, {'_id': 0, 'name': 1})]
        return names

# GraphQL schema
schema = graphene.Schema(query=Query)

class GetTitles(Resource):
    def get(self):
        try:
            # GraphQL query to fetch product names
            result = schema.execute('{ productNames }')

            # product names from the result
            product_names = result.data['productNames']

            # Return product names as JSON response
            return jsonify({"productNames": product_names})
        except Exception as e:
            # If there's an exception, return an error response
            error_message = {"error": str(e)}
            return jsonify(error_message), 500


# /getProducts - Gets all products in database
class GetProducts(Resource):
    def get(self):
        results = dumps(collection.find())
        return json.loads(results)

# /insertProduct - Inserts products into database through Postman
class InsertProducts(Resource):
    def post(self):
        # Check if API key is provided in the URL
        api_key = request.args.get('api_key')
        if api_key != API_KEY:
            return jsonify({"error": "Invalid API key"}), 401

        # Extract data from request
        data = request.json
        product_id = data.get('id')
        product_name = data.get('name')
        product_cost = data.get('cost')

        # Validate data
        if not (product_id and product_name and product_cost):
            return jsonify({"error": "Missing required data"}), 400

        # Insert product into MongoDB
        product = {
            "id": product_id,
            "name": product_name,
            "cost": product_cost
        }
        collection.insert_one(product)

        return jsonify({"message": "Product inserted successfully"}), 201

class Root(Resource):
    def get(self):
        # List of APIs and how to use them
        endpoints = {
            "/getTitles": "Returns a list of product titles from the MongoDB database via a GraphQL server.",
            ""
            "/getProducts": "Returns a complete JSON list of products from the MongoDB database.",
            ""
            "/insertProduct": "Allows insertion of a new product into the MongoDB database. Requires a product id, name, and cost to be sent in the request body. An API key must be provided as a query parameter for authentication.",
        }
        return jsonify(endpoints)

api.add_resource(Root, '/')
api.add_resource(GetTitles, '/getTitles')
api.add_resource(GetProducts, '/getProducts')
api.add_resource(InsertProducts, '/insertProducts')

if __name__ == '__main__':
    app.run(debug=True)

