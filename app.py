
import json

from flask import (
    Flask, render_template, request,
    redirect, url_for, flash
)

from database import get_db_connection, init_db
from planner import generate_trip_plan, DESTINATIONS

app = Flask(__name__)
app.secret_key = "voyago-demo-secret-key"

init_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    conn = get_db_connection()

    total_trips = conn.execute(
        "SELECT COUNT(*) FROM trips"
    ).fetchone()[0]

    total_budget = conn.execute(
        "SELECT COALESCE(SUM(budget), 0) FROM trips"
    ).fetchone()[0]

    recent_trips = conn.execute(
        "SELECT * FROM trips ORDER BY id DESC LIMIT 5"
    ).fetchall()

    conn.close()

    return render_template(
        "dashboard.html",
        total_trips=total_trips,
        total_budget=total_budget,
        recent_trips=recent_trips
    )


@app.route("/plan-trip", methods=["GET", "POST"])
def plan_trip():

    if request.method == "POST":
        try:
            start = request.form.get("starting_location", "").strip()
            destination = request.form.get("destination", "").strip()
            days = int(request.form.get("days", 0))
            budget = float(request.form.get("budget", 0))
            travelers = int(request.form.get("travelers", 0))
            preference = request.form.get("preference", "Nature")

            if not start or destination not in DESTINATIONS:
                raise ValueError("Please select valid locations.")

            if not 1 <= days <= 30:
                raise ValueError("Trip duration must be between 1 and 30 days.")

            if budget <= 0 or not 1 <= travelers <= 50:
                raise ValueError("Please enter a valid budget and traveller count.")

            trip = generate_trip_plan(
                start, destination, days,
                budget, travelers, preference
            )

            conn = get_db_connection()

            cursor = conn.execute("""
                INSERT INTO trips (
                    starting_location, destination, days,
                    budget, travelers, preference, itinerary
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                start, destination, days, budget,
                travelers, preference, json.dumps(trip)
            ))

            trip_id = cursor.lastrowid
            conn.commit()
            conn.close()

            return redirect(url_for("itinerary", trip_id=trip_id))

        except (ValueError, TypeError):
            flash("Please enter valid trip details.", "error")

    return render_template("plan_trip.html")


@app.route("/itinerary/<int:trip_id>")
def itinerary(trip_id):
    conn = get_db_connection()

    trip = conn.execute(
        "SELECT * FROM trips WHERE id = ?", (trip_id,)
    ).fetchone()

    conn.close()

    if trip is None:
        flash("Trip not found.", "error")
        return redirect(url_for("home"))

    trip_data = json.loads(trip["itinerary"])

    return render_template(
        "itinerary.html",
        trip=trip_data,
        trip_id=trip_id
    )


@app.route("/destinations")
def destinations():
    return render_template(
        "destinations.html",
        destinations=DESTINATIONS
    )


@app.route("/my-trips")
def my_trips():
    conn = get_db_connection()

    trips = conn.execute(
        "SELECT * FROM trips ORDER BY id DESC"
    ).fetchall()

    conn.close()

    return render_template("my_trips.html", trips=trips)


if __name__ == "__main__":
    app.run(debug=True)
