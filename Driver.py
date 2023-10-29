class Driver:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.status = "free"  # status could be "free" or "busy"
        self.reservation_detail = None
        self.reservation_start_time = None
        self.reservation_end_time = None
        self.time_spent_on_reservation = None

    def assign_reservation(self, reservation_detail):
        self.status = "busy"
        self.reservation_detail = reservation_detail

    def conclude_reservation(self):
        self.status = "free"
        self.reservation_detail = None

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "reservation_detail": self.reservation_detail,
            "reservation_start_time": self.reservation_start_time,
            "reservation_end_time": self.reservation_end_time,
            "time_spent_on_reservation": self.time_spent_on_reservation
            

        }