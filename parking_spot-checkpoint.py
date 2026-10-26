"""Class for a parking spot."""
class ParkingSpot:
    """Store a parking spot's ID, location, and occupancy status."""
    def __init__(self, spot_id, location, occupied):
        """Create a parking spot."""
        self.spot_id = str(spot_id)
        self.location = location
        self.occupied = bool(occupied)

    def update_status(self, occupied):
        """Update status: 1 means occupied, 0 means free."""
        if occupied not in (0, 1):
            raise ValueError("occupied must be 0 or 1")
        self.occupied = bool(occupied)

    def is_free(self):
        """Return True if the spot is free."""
        return not self.occupied

    def __str__(self):
        """Describe the spot."""
        status = "occupied" if self.occupied else "FREE"
        return f"Spot {self.spot_id} at {self.location}: {status}"
