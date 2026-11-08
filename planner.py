
import random


DESTINATIONS = {
    "Goa": {
        "category": "Beach & Adventure",
        "description": "Beautiful beaches, water activities and coastal experiences.",
        "places": [
            "Baga Beach",
            "Fort Aguada",
            "Calangute Beach",
            "Dudhsagar Falls",
            "Anjuna Beach",
            "Chapora Fort"
        ],
        "adventure": ["Water sports", "Beach activities", "Sunset cruise"],
        "nature": ["Dudhsagar Falls", "Beach sunset", "Nature walks"],
        "culture": ["Old Goa churches", "Local markets", "Fort Aguada"],
        "relaxation": ["Beach relaxation", "Spa experience", "Sunset viewing"]
    },
    "Ooty": {
        "category": "Nature & Hills",
        "description": "Peaceful hill stations, gardens and scenic mountain views.",
        "places": [
            "Ooty Lake",
            "Botanical Garden",
            "Doddabetta Peak",
            "Rose Garden",
            "Pykara Falls",
            "Tea Museum"
        ],
        "adventure": ["Mountain trekking", "Boating", "Nature trails"],
        "nature": ["Pykara Falls", "Botanical Garden", "Doddabetta Peak"],
        "culture": ["Tea Museum", "Local markets", "Heritage railway"],
        "relaxation": ["Ooty Lake", "Rose Garden", "Tea garden visit"]
    },
    "Manali": {
        "category": "Mountains & Adventure",
        "description": "Snowy mountains, beautiful valleys and adventure experiences.",
        "places": [
            "Solang Valley",
            "Hadimba Temple",
            "Old Manali",
            "Atal Tunnel",
            "Vashisht Temple",
            "Mall Road"
        ],
        "adventure": ["Paragliding", "Mountain trekking", "Adventure activities"],
        "nature": ["Solang Valley", "Mountain viewpoints", "Scenic valleys"],
        "culture": ["Hadimba Temple", "Vashisht Temple", "Local markets"],
        "relaxation": ["Old Manali", "Mall Road", "Mountain viewpoints"]
    },
    "Jaipur": {
        "category": "History & Culture",
        "description": "Royal palaces, historic forts and colourful markets.",
        "places": [
            "Hawa Mahal",
            "Amber Fort",
            "City Palace",
            "Jantar Mantar",
            "Nahargarh Fort",
            "Jal Mahal"
        ],
        "adventure": ["Fort exploration", "Cycling tours", "Local experiences"],
        "nature": ["Jal Mahal", "Nahargarh viewpoints", "Garden visits"],
        "culture": ["Hawa Mahal", "City Palace", "Amber Fort"],
        "relaxation": ["Local markets", "Traditional cafes", "Garden visits"]
    },
    "Kerala": {
        "category": "Nature & Backwaters",
        "description": "Green landscapes, backwaters and peaceful nature.",
        "places": [
            "Alleppey Backwaters",
            "Munnar Tea Gardens",
            "Fort Kochi",
            "Varkala Beach",
            "Thekkady",
            "Athirappilly Falls"
        ],
        "adventure": ["Trekking", "Boating", "Nature trails"],
        "nature": ["Munnar Tea Gardens", "Athirappilly Falls", "Thekkady"],
        "culture": ["Fort Kochi", "Local markets", "Cultural performances"],
        "relaxation": ["Alleppey Backwaters", "Varkala Beach", "Tea gardens"]
    },
    "Vizag": {
        "category": "Coastal & Nature",
        "description": "Beautiful coastline, beaches and scenic viewpoints.",
        "places": [
            "RK Beach",
            "Kailasagiri",
            "Rushikonda Beach",
            "Submarine Museum",
            "Yarada Beach",
            "Borra Caves"
        ],
        "adventure": ["Beach activities", "Trekking", "Cave exploration"],
        "nature": ["Yarada Beach", "Borra Caves", "Kailasagiri"],
        "culture": ["Submarine Museum", "Local markets", "Museums"],
        "relaxation": ["RK Beach", "Rushikonda Beach", "Beach sunset"]
    },
    "Araku": {
        "category": "Nature & Hills",
        "description": "Green valleys, coffee plantations and waterfalls.",
        "places": [
            "Borra Caves",
            "Araku Valley",
            "Coffee Museum",
            "Chaparai Waterfalls",
            "Tribal Museum",
            "Padmapuram Gardens"
        ],
        "adventure": ["Valley trekking", "Cave exploration", "Nature walks"],
        "nature": ["Araku Valley", "Chaparai Waterfalls", "Borra Caves"],
        "culture": ["Tribal Museum", "Coffee Museum", "Local markets"],
        "relaxation": ["Coffee plantations", "Padmapuram Gardens", "Valley views"]
    },
    "Hyderabad": {
        "category": "City & Heritage",
        "description": "Historic monuments, food experiences and modern attractions.",
        "places": [
            "Charminar",
            "Golconda Fort",
            "Hussain Sagar",
            "Salar Jung Museum",
            "Chowmahalla Palace",
            "Ramoji Film City"
        ],
        "adventure": ["Ramoji Film City", "Boating", "City exploration"],
        "nature": ["Hussain Sagar", "Public gardens", "Lake viewpoints"],
        "culture": ["Charminar", "Golconda Fort", "Salar Jung Museum"],
        "relaxation": ["Lake viewpoints", "Local cafes", "Shopping"]
    }
}


def generate_trip_plan(start, destination, days, budget, travelers, preference):

    if destination not in DESTINATIONS:
        destination = "Goa"

    details = DESTINATIONS[destination]

    preference_key = preference.lower()

    if preference_key not in ["adventure", "nature", "culture", "relaxation"]:
        preference_key = "nature"

    preferred_places = details[preference_key]

    activities = details["places"]

    itinerary = []

    for day in range(1, days + 1):

        place1 = activities[(day * 2 - 2) % len(activities)]
        place2 = activities[(day * 2 - 1) % len(activities)]
        activity = preferred_places[(day - 1) % len(preferred_places)]

        itinerary.append({
            "day": day,
            "title": f"Explore {destination}",
            "morning": place1,
            "afternoon": place2,
            "evening": activity,
            "description": f"Enjoy a memorable day exploring {destination}."
        })

    budget_breakdown = {
        "Accommodation": round(budget * 0.35, 2),
        "Food": round(budget * 0.20, 2),
        "Transport": round(budget * 0.25, 2),
        "Activities": round(budget * 0.15, 2),
        "Other Expenses": round(budget * 0.05, 2)
    }

    return {
        "destination": destination,
        "category": details["category"],
        "description": details["description"],
        "starting_location": start,
        "days": days,
        "travelers": travelers,
        "preference": preference,
        "total_budget": budget,
        "budget_per_person": round(budget / travelers, 2),
        "budget_breakdown": budget_breakdown,
        "itinerary": itinerary,
        "recommended_places": details["places"],
        "tips": [
            "Check weather conditions before travelling.",
            "Keep important travel documents with you.",
            "Confirm accommodation and transport arrangements.",
            "Maintain some extra money for unexpected expenses."
        ]
    }
