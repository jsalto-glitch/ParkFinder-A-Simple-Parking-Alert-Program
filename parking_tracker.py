"""Functions for reading sample data and alerting about free spots."""
import csv
from parking_spot import ParkingSpot

def load_spots(file_path):
    """Load parking spots from a CSV file."""
    spots = {}
    with open(file_path, newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            spots[row["spot_id"]] = ParkingSpot(
                row["spot_id"], row["location"], int(row["occupied"])
            )
    return spots

def process_readings(spots, readings_file, alert_file):
    """Print and save an alert when a spot changes from occupied to free."""
    with open(readings_file, newline="", encoding="utf-8") as file:
        readings = list(csv.DictReader(file))

    with open(alert_file, "w", newline="", encoding="utf-8") as output:
        fields = ["timestamp", "spot_id", "location", "message"]
        writer = csv.DictWriter(output, fieldnames=fields)
        writer.writeheader()
        for reading in readings:
            spot_id = reading["spot_id"]
            if spot_id not in spots:
                print(f"Skipping unknown spot ID: {spot_id}")
                continue
            spot = spots[spot_id]
            was_occupied = spot.occupied
            spot.update_status(int(reading["occupied"]))
            if was_occupied and spot.is_free():
                message = f"Parking available at {spot.location} (spot {spot_id})"
                print("🔔 " + message)
                writer.writerow({
                    "timestamp": reading["timestamp"],
                    "spot_id": spot_id,
                    "location": spot.location,
                    "message": message
                })
    print(f"\nAlert log saved to: {alert_file}")
    print("Note: these are simulated readings, not live parking data.")
