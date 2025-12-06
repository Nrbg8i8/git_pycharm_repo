import csv
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



def export_bookings_csv(bookings, path):
    keys = ["id", "client_name", "service", "start", "end"]

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(keys)

        for b in bookings:
            writer.writerow([
                b.id,
                b.client.name if b.client else None,
                b.service,
                b.start.isoformat(),
                b.end.isoformat()
            ])
