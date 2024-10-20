import json
from pymongo import MongoClient

with open('ticket.json') as f:
    json_data = json.load(f)

city_to_country = {                 #  City-to-Country mapping
    "new_york": "usa",
    "dallas": "usa",
    "beijing": "china",
    "wuhan": "china",
    "colombo": "sri_lanka",
    "kandy": "sri_lanka",
    "hong_kong": "china",
    "chicago": "usa"
}

# country-to-visa rate mapping from the JSON
visa_rates = {}
for rate in json_data["visa_rates"]:
    visa_rates.update(rate)

# Step 4: Function to get visa rate
def visa_rate(city):
    city = city.lower()  # Convert input to lowercase for consistent matching
    if city in city_to_country:
        country = city_to_country[city]
        visa_rate = visa_rates.get(country)
        if visa_rate:
            return visa_rate
        else:

            return 0
    else:
        return 0






#mongo connecting code


client = MongoClient("mongodb://localhost:27017/")         #  MongoDB  connecting code
db = client["AirIndia"]
collection = db["tickets"]


tickets = collection.find()

for ticket in tickets:                                     # ticket information
    passenger_name = ticket.get("passenger_name")
    ticket_number = ticket.get("ticket_id")
    destination = ticket.get("destination")
    ticket_price = ticket.get("ticket_price")

    visa_stamped_locations = ticket.get("visa_stamped_locations", [])           # last visa stamped location
    if visa_stamped_locations:
        last_visa_location = visa_stamped_locations[-1]
        visa_price = visa_rate(last_visa_location)
    else:
        last_visa_location = None
        visa_price = 0

    total_cost = ticket_price + visa_price

    print(f"Passenger Name: {passenger_name}")
    print(f"Ticket ID: {ticket_number}")
    print(f"Final Destination: {destination}")
    print(f"Ticket Price: ${ticket_price:.2f}")
    print(f"last location: {last_visa_location}")
    print(f"Visa Price: ${visa_price:.2f}")
    print(f"Total Cost: ${total_cost:.2f}")
    print("-" * 30)

client.close()
#