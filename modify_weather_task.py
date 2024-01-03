import click
import csv
from datetime import datetime as td


def import_data(file_path, range, type):

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # conversion of range from string to date time
        starting_date_str, ending_date_str = range.split()
        starting_date = td.strptime(starting_date_str, '%Y-%m-%d').date()
        ending_date = td.strptime(ending_date_str, '%Y-%m-%d').date()
        # iterating csv data
        all_data = []
        for row in csv_reader:
            all_data.append(row)
        filter_data = []
        for rd in all_data[1:]:
            date_time_obj = td.strptime(rd[0], '%Y%m%dT%H%M').date()
            if date_time_obj >= starting_date and date_time_obj <= ending_date:
                # print(rd)
                # filter_data.append(rd)
                # print(filter_data)
                if type == "temprature":
                    filter_data.append([rd[1]])
                elif type == "humidity":
                    filter_data.append([rd[2]])
                elif type == "wind":
                    filter_data.append([rd[3]])
        # print(filter_data)
        # return filter_data
    with open('new_modify_weather_data.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(filter_data)


def analyze_data(output_file_path):
    with open('new_modify_weather_data.csv', 'r') as csv_file:
        csv_reader = csv_file.read(1)
    if not csv_reader:
        raise ValueError("first you need to import data in file")
    store_data = []
    for row in csv_reader:
        store_data.append(row)
    # iterate on nested list to acess elements
    maximum = 0
    minimum = 0
    sums = 0
    for x in store_data:
        for y in x:
            if float(y) > maximum:
                maximum = float(y)
            else:
                float(y) < minimum
                minimum = float(y)
            sums += float(y)
    average = sums / len(store_data)

    with open(output_file_path, 'w') as new_file:
        new_file.write(f"Maximum : {maximum} ")
        new_file.write('\n')
        new_file.write(f"Minimum : {minimum} ")
        new_file.write('\n')
        new_file.write(f"Average : {average} ")
        new_file.write('\n')


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
