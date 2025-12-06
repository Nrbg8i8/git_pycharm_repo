from PyQt6.QtWidgets import (
    QMainWindow, QPushButton, QVBoxLayout, QWidget, QListWidget,
    QLineEdit, QLabel, QComboBox, QDateEdit
)
from PyQt6.QtCore import QDate
from booking_app.db_session import init_db, get_session
from models.models import User, Room, Booking

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Booking App - Extended")
        init_db()

        self.layout = QVBoxLayout()

        # --- Users ---
        self.layout.addWidget(QLabel("Потребители:"))
        self.user_list = QListWidget()
        self.layout.addWidget(self.user_list)

        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Въведи име на потребител")
        self.layout.addWidget(self.user_input)

        self.add_user_btn = QPushButton("Добави потребител")
        self.add_user_btn.clicked.connect(self.add_user)
        self.layout.addWidget(self.add_user_btn)

        # --- Rooms ---
        self.layout.addWidget(QLabel("Стаи:"))
        self.room_list = QListWidget()
        self.layout.addWidget(self.room_list)

        self.room_name_input = QLineEdit()
        self.room_name_input.setPlaceholderText("Име на стая")
        self.layout.addWidget(self.room_name_input)

        self.room_capacity_input = QLineEdit()
        self.room_capacity_input.setPlaceholderText("Капацитет")
        self.layout.addWidget(self.room_capacity_input)

        self.add_room_btn = QPushButton("Добави стая")
        self.add_room_btn.clicked.connect(self.add_room)
        self.layout.addWidget(self.add_room_btn)

        # --- Bookings ---
        self.layout.addWidget(QLabel("Резервации:"))
        self.booking_list = QListWidget()
        self.layout.addWidget(self.booking_list)

        self.user_combo = QComboBox()
        self.layout.addWidget(self.user_combo)

        self.room_combo = QComboBox()
        self.layout.addWidget(self.room_combo)

        self.date_edit = QDateEdit()
        self.date_edit.setDate(QDate.currentDate())
        self.layout.addWidget(self.date_edit)

        self.add_booking_btn = QPushButton("Добави резервация")
        self.add_booking_btn.clicked.connect(self.add_booking)
        self.layout.addWidget(self.add_booking_btn)

        # Основен widget
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

        # Зареждане на данни
        self.load_users()
        self.load_rooms()
        self.load_bookings()

    # --- Users ---
    def add_user(self):
        name = self.user_input.text().strip()
        if name:
            session = get_session()
            session.add(User(name=name))
            session.commit()
            session.close()
            self.user_input.clear()
            self.load_users()

    def load_users(self):
        self.user_list.clear()
        self.user_combo.clear()
        session = get_session()
        users = session.query(User).all()
        for u in users:
            self.user_list.addItem(f"{u.id}: {u.name}")
            self.user_combo.addItem(u.name, u.id)
        session.close()

    # --- Rooms ---
    def add_room(self):
        name = self.room_name_input.text().strip()
        capacity_text = self.room_capacity_input.text().strip()
        if name and capacity_text.isdigit():
            session = get_session()
            session.add(Room(name=name, capacity=int(capacity_text)))
            session.commit()
            session.close()
            self.room_name_input.clear()
            self.room_capacity_input.clear()
            self.load_rooms()

    def load_rooms(self):
        self.room_list.clear()
        self.room_combo.clear()
        session = get_session()
        rooms = session.query(Room).all()
        for r in rooms:
            self.room_list.addItem(f"{r.id}: {r.name} (Cap: {r.capacity})")
            self.room_combo.addItem(r.name, r.id)
        session.close()

    # --- Bookings ---
    def add_booking(self):
        user_id = self.user_combo.currentData()
        room_id = self.room_combo.currentData()
        date = self.date_edit.date().toPyDate()
        if user_id and room_id:
            session = get_session()
            booking = Booking(user_id=user_id, room_id=room_id, date=date)
            session.add(booking)
            session.commit()
            session.close()
            self.load_bookings()

    def load_bookings(self):
        self.booking_list.clear()
        session = get_session()
        bookings = session.query(Booking).all()
        for b in bookings:
            self.booking_list.addItem(f"{b.id}: {b.user.name} -> {b.room.name} on {b.date}")
        session.close()

