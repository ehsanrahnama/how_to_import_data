import csv


file_path = "/home/ehsan/Desktop/ImportData/CSVFile/users-simple-five.csv"

# Import data using csv module, with csv reader
with open(file_path) as csv_file:
    csv_reader = csv.reader(csv_file, dialect='excel', quotechar='"')
    for row in csv_reader:
        print(row)


# load data as DictReader
fields_name = ["Id", "Reputation", "Location", "DisplayName"]
with open(file_path) as csv_file:
    csv_dict_reader = csv.DictReader(csv_file, fieldnames=fields_name)
    for row in csv_dict_reader:
        print(row['DisplayName']+' has a reputation of '+row['Reputation'])

# load unquoted numbers
with open(file_path) as csv_file:
    csv_reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    for row in csv_reader:
        print(row)


