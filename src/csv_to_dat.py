
import pandas as pd
import typing
import traceback
import os


def read_csv_file(filename, delimeter=",", column_names=list()):
    '''
        This function reads the CSV file and converts it into pandas Dataframe
    '''
    csv_data = pd.read_csv(filepath_or_buffer=filename,
                            sep=delimeter,
                            usecols=column_names,
                            skip_blank_lines=True,
                            encoding="UTF-8",
                            engine="python")
    return csv_data


def read_and_convert(filename, delimeter=",", column_names=list()):
    print(column_names)
    csv_data = read_csv_file(filename, delimeter, column_names)

    return csv_data



if __name__ == "__main__":
    PROJECT_PATH = os.path.join(os.getcwd())
    filename = PROJECT_PATH + "\csv" + "\\"+ "2022_Forbes_list.csv"
    print(filename)
    col_names = ["Rank in India", "Name","Headquarters","Revenue(billions US$)","Profit(billions US$)","Assets(billions US$)","Value(billions US$)","Industry"]
    csv_data = read_and_convert(filename=filename, delimeter=",", column_names=col_names)

    print(type(csv_data))


