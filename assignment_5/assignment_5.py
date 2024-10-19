import pymysql
from pymongo import MongoClient

# MySQL Configuration
mysql_host = 'localhost'
mysql_user = 'root'
mysql_password = 'root'
mysql_db = 'ecomsite'

# MongoDB Configuration
mongo_host = 'localhost'
mongo_port = 27017
mongo_db = 'ecomsite'
mongo_collection = 'category'  # Only one collection will be used for categories

# Connect to MySQL
mysql_conn = pymysql.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    db=mysql_db
)
mysql_cursor = mysql_conn.cursor(pymysql.cursors.DictCursor)

# Connect to MongoDB
mongo_client = MongoClient(mongo_host, mongo_port)
mongo_db = mongo_client[mongo_db]
mongo_collection = mongo_db[mongo_collection]

def fetch_data_from_mysql(table_name):
    """Fetch data from a MySQL table."""
    mysql_cursor.execute(f"SELECT * FROM {table_name}")
    return mysql_cursor.fetchall()

def combine_products_into_categories(categories, products):
    """Combine products into their corresponding categories."""
    # Create a map from category ID to category document
    category_map = {category['cat_id']: category for category in categories}

    # Initialize 'products' field in each category document
    for category in category_map.values():
        category['products'] = []

    # Add products to their corresponding categories
    for product in products:
        cat_id = product['cat_id']
        if cat_id in category_map:
            category_map[cat_id]['products'].append({
                'product_id': product['product_id'],
                'product_name': product['product_name'],
                'price': product['price']
            })

    # Convert category_map values to a list
    combined_data = list(category_map.values())

    return combined_data

def insert_into_mongo(data):
    """Insert combined data into MongoDB."""
    if data:
        mongo_collection.insert_many(data)
        print(f"Inserted {len(data)} documents into MongoDB collection {mongo_collection.name}")
    else:
        print("No data to insert.")

# Fetch data from MySQL
categories = fetch_data_from_mysql('category')
products = fetch_data_from_mysql('product')

# Combine products into categories
combined_data = combine_products_into_categories(categories, products)

# Insert combined data into MongoDB
insert_into_mongo(combined_data)

# Close connections
mysql_cursor.close()
mysql_conn.close()
mongo_client.close()

print("Data migration and embedding complete.")