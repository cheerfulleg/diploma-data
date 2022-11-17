import csv


def write_to_csv(data: list[dict], columns: list[str], filename: str):
    try:
        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=columns)
            writer.writeheader()
            for data in data:
                writer.writerow(data)
    except IOError:
        print("I/O error")
