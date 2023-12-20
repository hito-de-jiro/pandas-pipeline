# Processing data
import pandas as pd


def create_data(input_file: str):
    """
    Create dataframe

    ...
    :param input_file: str
    :return: pandas.core.frame.DataFrame
    """
    df = pd.read_csv(input_file, delimiter=',')

    return df


def filtered_data(df):
    """
    Do filtered data

    ...
    :param df: pandas.core.frame.DataFrame
    :return: data: pandas.core.frame.DataFrame

    """
    # remove duplicates
    df = df.drop_duplicates()

    # sort all records by last name
    df = df.sort_values(by="last_name")

    # filter all records with last name started from letter 'S'
    data = df[df['last_name'].str.startswith('S')]
    
    return data


def save_data(df, output_file):
    """
    Save processed data

    ...
    :param df: pandas.core.frame.DataFrame
    :param output_file: str
    :return: None
    """
    df.to_csv(output_file)


def main(input_file, output_file):
    """
    Main function

    ...
    :param output_file: str
    :param input_file: str
    :return: None
    """
    save_data(filtered_data(create_data(input_file)), output_file)


if __name__ == '__main__':
    main(input_file='input.csv', output_file='output.csv')
