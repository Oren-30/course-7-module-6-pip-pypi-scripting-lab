from datetime import datetime

def generate_log(log_data):
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        for entry in log_data:
            file.write(entry + "\n")

    return filename


def main():
    log_data = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]

    filename = generate_log(log_data)
    print(f"Log written to {filename}")


if __name__ == "__main__":
    main()