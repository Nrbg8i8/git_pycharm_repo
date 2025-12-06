from models.models import Client, Booking


class ClientService:
    def __init__(self, session):
        self.session = session

    def list_clients(self):
        return self.session.query(Client).order_by(Client.name).all()

    def create_client(self, name, phone, email):
        client = Client(name=name, phone=phone, email=email)
        self.session.add(client)
        self.session.commit()
        return client

    def delete_client(self, client_id):
        client = self.session.get(Client, client_id)
        if client:
            self.session.delete(client)
            self.session.commit()


class BookingService:
    def __init__(self, session):
        self.session = session

    def list_bookings(self):
        return self.session.query(Booking).order_by(Booking.start).all()

    def create_booking(self, client_id, service, start, end):
        overlaps = self.session.query(Booking).filter(
            Booking.client_id == client_id,
            Booking.end > start,
            Booking.start < end
        ).count()

        if overlaps:
            raise Exception("Client has overlapping booking!")

        booking = Booking(
            client_id=client_id,
            service=service,
            start=start,
            end=end
        )
        self.session.add(booking)
        self.session.commit()
        return booking

    def delete_booking(self, booking_id):
        booking = self.session.get(Booking, booking_id)
        if booking:
            self.session.delete(booking)
            self.session.commit()
