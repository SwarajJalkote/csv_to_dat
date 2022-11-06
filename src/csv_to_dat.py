
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


def convert_to_dat(csv_data, output_path="output.dat"):
    '''
        This function will convert the Dataframe to dat
    '''
    for i in range(3):
        if output_path.endswith(".dat"):
            try:
                csv_data.to_csv(path_or_buf=output_path, sep="|", header=True, index=False, mode="w", encoding="UTF-8")
                return f"File created successfully in {output_path}" 
            except TypeError:
                print("Please provide correct path with .dat file")
                traceback.print_exc()
        else:
            output_path = input("Please enter correct output path with .dat. Example: output.dat >")

    return "Failed to provide correct output path"


def read_and_convert(filename, delimeter=",", column_names=list()):
    '''
        This function will convert the csv to dat
    '''
    csv_data = read_csv_file(filename, delimeter, column_names)
    response = convert_to_dat(csv_data=csv_data, output_path="csv/output.dat")
    return response

if __name__ == "__main__":
    filename = "csv/2022_Forbes_list.csv"
    col_names = ["Rank in India", "Name","Headquarters","Revenue(billions US$)","Profit(billions US$)","Assets(billions US$)","Value(billions US$)","Industry"]
    response_message = read_and_convert(filename=filename, delimeter=",", column_names=col_names)
    
    print(response_message)
