import unittest
import os


class TestMyCode(unittest.TestCase):

    def test_os_system(self):
        command = "python3 weather_cli.py --input weather_data.csv --range '2023-01-01 2023-01-30' --type wind"
        os.system(command)
        with open('weather_logging.log', 'r') as file1:
            actual_result = file1.read()
        expected_result = """INFO:my_logger:wind is increasing
INFO:my_logger:Maximum wind : 27.475807
INFO:my_logger:Minimum wind : 5.3999996
INFO:my_logger:Average wind : 10.291861298809511
"""
        command = "python3 weather_cli.py --input weather_data.csv --range '2023-01-01 2023-01-30' --type temprature"
        os.system(command)
        with open('weather_logging.log', 'r') as file1:
            actual_result = file1.read()
        expected_result = """INFO:my_logger:temprature is increasing
INFO:my_logger:Maximum temprature : 14.500245
INFO:my_logger:Minimum temprature : -1.9797546
INFO:my_logger:Average temprature : 4.650170908305527
"""
        command = "python3 weather_cli.py --input weather_data.csv --range '2023-01-01 2023-01-30' --type humidity"
        os.system(command)
        with open('weather_logging.log', 'r') as file1:
            actual_result = file1.read()
        expected_result = """INFO:my_logger:humidity is increasing
INFO:my_logger:Maximum humidity : 99.947556
INFO:my_logger:Minimum humidity : 84.86319
INFO:my_logger:Average humidity : 83.53137272767864
"""
        assert actual_result == expected_result


if __name__ == '__main__':
    unittest.main()
