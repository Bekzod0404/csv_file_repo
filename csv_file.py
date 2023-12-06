import csv
import os


class FileReader:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def read_file(self):
        data = []

        files = [f for f in os.listdir(self.folder_path) if os.path.isfile(os.path.join(self.folder_path, f))]

        for file_name in files:
            file_path = os.path.join(self.folder_path, file_name)

            with open(file_path, "r") as file:
                lines = file.readlines()

                name = lines[0].strip()
                price = lines[1].strip()
                description = lines[2].strip()

                data.append({
                    "name": name,
                    "price": price,
                    "description": description
                })
    
        return data

    def write_to_csv(self, csv_file_path, data):
        with open(csv_file_path, "w", newline='') as csvfile:
            fieldnames = ['name', 'price', 'description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for row in data:
                writer.writerow(row)


if __name__ == '__main__':
    folder_path = "descriptions"
    csv_file_path = "output.csv"

    file_reader = FileReader(folder_path)
    data = file_reader.read_file()
    file_reader.write_to_csv(csv_file_path, data)
