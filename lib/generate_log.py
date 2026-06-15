from datetime import datetime


def generate_log(log_data):
    # Validate input
    if not isinstance(log_data, list):
        raise ValueError("Input must be a list")

    # Create timestamped filename
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write file
    with open(filename, "w", encoding="utf-8") as file:
        for entry in log_data:
            file.write(entry + "\n")

    # Confirmation message (REQUIRED by test)
    print(f"Log written to {filename}")

    return filename