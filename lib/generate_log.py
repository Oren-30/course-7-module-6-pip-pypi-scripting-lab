from datetime import datetime
import os

def generate_log(data, directory="."):
    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("Input data must be a list")

    # STEP 2: Ensure directory exists (important for test environments)
    os.makedirs(directory, exist_ok=True)

    # STEP 3: Generate filename (YYYYMMDD format)
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    filepath = os.path.join(directory, filename)

    # STEP 4: Write log file (handles empty list too)
    with open(filepath, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 5: Confirmation message
    print(f"Log successfully written to {filepath}")

    return filepath