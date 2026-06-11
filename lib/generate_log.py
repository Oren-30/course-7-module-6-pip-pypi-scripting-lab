from datetime import datetime
import os

def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("Input data must be a list")

    # Create filename with today's date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write log entries to file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log successfully written to {filename}")
    return filename


if __name__ == "__main__":
    logs = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]

    generate_log(logs)
