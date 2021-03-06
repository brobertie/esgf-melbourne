import urllib.request
import pandas as pd
from io import StringIO


def get_melbourne_data() -> pd.DataFrame:
    '''
    Returns a dataframe of the melbourne data set.
    :return: pd.DataFrame
    '''

    # URL of the raw csv data to download
    raw_url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-min-temperatures.csv"

    # Get the earthquake data from the API
    response = urllib.request.urlopen(raw_url)

    # Decode earthquake data
    response = response.read().decode('utf-8')

    # Return as a pandas dataframe
    data = pd.read_csv(StringIO(response))

    # Cast the date column to datetime
    data['Date'] = pd.to_datetime(data['Date'])

    return data


def split_train_test_data(melbourne_data: pd.DataFrame, split_year: str="1987") -> (pd.DataFrame, pd.DataFrame):
    '''
    Split the melbourne data into a training dataframe and a test dataframe.
    The training data is composed of all temperature points strictly anterior to the given split year.
    The test data is composed of all the points posterior or equal to the split year.
    :param melbourne_data: pd.DataFrame, with at least column ['Date']
    :param split_year: str, the year to split the data on
    :return: (pd.DataFrame, pd.DataFrame)
    '''

    # Format split year variable
    split_year = "{}".format(int(split_year) - 1)

    # Trainings data. Data anterior to the given split year
    train_data = melbourne_data.loc[:split_year]

    # Test data. Data posterior or equal to the given split year
    test_data = melbourne_data.loc[split_year:]

    return train_data, test_data
