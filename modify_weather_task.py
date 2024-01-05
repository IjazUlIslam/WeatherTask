import click
import csv
from datetime import datetime as td


def import_data(file_path, range, type):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        all_data = []
        for row in csv_reader:
            all_data.append(row)

    # conversion of range from string to date time
    starting_date_str, ending_date_str = range.split()
    starting_date = td.strptime(starting_date_str, '%Y-%m-%d').date()
    ending_date = td.strptime(ending_date_str, '%Y-%m-%d').date()
    filter_data = []
    for rd in all_data[1:]:
        date_time_obj = td.strptime(rd[0], '%Y%m%dT%H%M').date()
        if date_time_obj >= starting_date and date_time_obj <= ending_date:
            if type == "temprature":
                filter_data.append([rd[1]])
            elif type == "humidity":
                filter_data.append([rd[2]])
            elif type == "wind":
                filter_data.append([rd[3]])

    with open('new_modify_weather_data.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(filter_data)


def analyze_data(output_file_path):
    with open('new_modify_weather_data.csv', 'r') as csv_file:
        csv_read = csv.reader(csv_file)
        all_data = []
        for row in csv_read:
            all_data.append(row[0])
        if not all_data:
            raise ValueError("first you need to import data in file")

    # iterate on nested list to acess elements
    maximum, minimum, sums = 0, 0, 0
    increasing = 0
    decreasing = 0
    last_item = 0
    for y in all_data:
        if float(y) > maximum:
            maximum = float(y)
        else:
            float(y) < minimum
            minimum = float(y)
        sums += float(y)

        if last_item > float(y):
            increasing += 1
        else:
            decreasing += 1
        last_item = float(y)
    average = sums / len(all_data)

    with open(output_file_path, 'w') as new_file:
        new_file.write(f"Maximum : {maximum}\n ")
        new_file.write(f"Minimum : {minimum}\n ")
        new_file.write(f"Average : {average}\n ")
        if increasing > decreasing:
            new_file.write("varriance increasing")
        else:
            new_file.write("varriance decreasing")


@click.command()
@click.option('--input', help="please input file")
@click.option('--range', help="please specify range of file")
@click.option('--output', help="please show output file")
@click.option('--operation', help="please specify operation")
@click.option('--type', help="please specify parameter type")
def main(operation, input, range, output, type):
    if operation == "import":
        import_data(input, range, type)
    elif operation == 'analyze':
        analyze_data(output)


if __name__ == '__main__':
    try:
        main()
    except ValueError as e:
        print(e)
