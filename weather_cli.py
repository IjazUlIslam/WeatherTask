import click
import logging
import csv
from datetime import datetime as td
logging.basicConfig(filename="weather_logging.log",
                    filemode="w", level=logging.INFO)
logger = logging.getLogger('my_logger')


def process_csv(file_path, range):
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
            if date_time_obj > starting_date and date_time_obj < ending_date:
                filter_data.append(rd)
        return filter_data


# analyze data
def analyze_data(data, type):
    maximum = 0
    minimum = 0
    sums = 0
    increasing = 0
    decreasing = 0
    # for specifying type
    index = 0
    if type == "temprature":
        index = 1
    elif type == "humidity":
        index = 2
    elif type == "wind":
        index = 3
    last_item = 0
    for row in data:
        # condition for maximum and minimum
        if float(row[index]) > maximum:
            maximum = float(row[index])
        else:
            float(row[index]) < minimum
            minimum = float(row[index])
        # sums for finding average
        sums += float(row[index])
        # condition for variance
        if last_item or float(row[index]) > float(last_item):
            increasing = increasing + float(row[index])
        else:
            decreasing = decreasing + float(row[index])
        last_item = row[index]
    # print out variance result
    if increasing > decreasing:
        logger.info(f"{type} is increasing")
    else:
        logger.info(f"{type} is decreasing")
    average = sums / len(data)
    # print out Maximum, Minimum, Average
    logger.info(f"Maximum {type} : {maximum}")
    logger.info(f"Minimum {type} : {minimum}")
    logger.info(f"Average {type} : {average}")


# using Click
@click.command()
@click.option('--input', help="giving csv file data as an input")
@click.option('--range', help="giving range for data")
@click.option("--type", help="specify the type")
def main(input, range, type):
    filtered_data = process_csv(input, range)
    if filtered_data:
        analyze_data(filtered_data, type)


if __name__ == '__main__':
    main()
