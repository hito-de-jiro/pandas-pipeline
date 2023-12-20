# create data for project and save to CSV-file
import csv
from faker import Faker


def fake_data_generator(num: int) -> iter:
    """
    Create fake first and last name

    ...
    :param num: int
    :return: data: iter
    """
    fake = Faker()
    data = ((fake.first_name(), fake.last_name()) for _ in range(num))

    return data


def save_data(file_name: str, data: iter):
    """
    Save create data to CSV file

    ...
    :param data: iter
    :param file_name: str
    :return: None
    """
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(['first_name', 'last_name'])
        writer.writerows(data)


def main(num: int, file_name: str):
    """
    Assembly of the project

    :param num: int
    :param file_name: str
    :return: None
    """
    save_data(file_name, data=fake_data_generator(num=num))


if __name__ == '__main__':
    main(500000, file_name='input.csv')
    print('Done!')
