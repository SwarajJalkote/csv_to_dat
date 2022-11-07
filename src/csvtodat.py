
import pandas as pd
import typing
import traceback


def read_csv_file(input_file, input_del=",", column_names=list()) -> pd.DataFrame:
    '''
        This function reads the CSV file and converts it into pandas Dataframe.\n
        Description:
            input_file: csv file which needs to be converted with complete path
            input_del: delimiter used in input file. Default: , (comma)
            column_names: list of names of columns which you want to extract from csv
    '''
    csv_data = pd.read_csv(filepath_or_buffer=input_file,
                            sep=input_del,
                            usecols=column_names,
                            skip_blank_lines=True,
                            encoding="UTF-8",
                            engine="python")
    return csv_data


def convert_to_dat(csv_data, output_path="output.dat", output_del="|") -> str:
    '''
        This function will convert the Dataframe to dat.\n
         Description:
            csv_data: pandas DataFrame returned by read_csv()
            output_path: dat file which will be created as output with expected path
            output_del: delimiter used in output file: Default: | (pipe)
    '''
    
    if output_path.endswith(".dat"):
        try:
            csv_data.to_csv(path_or_buf=output_path, sep=output_del, header=True, index=False, mode="w", encoding="UTF-8")
            return f"File created successfully in {output_path}" 
        except Exception as exception:
            print("Exception :", exception)
            traceback.print_exc()
    else:
        raise Exception("Please provide correct path with .dat file")
    
    return "Failed to provide correct output path"


def csv_to_dat(input_file, input_del=",", output_path="output.dat", output_del="|", column_names=list()) -> str:
    '''
        This function will convert the csv to dat.\n
        Description:
            input_file: csv file which needs to be converted with complete path
            input_del: delimiter used in input file. Default: , (comma)
            output_path: dat file which will be created as output with expected path
            output_del: delimiter used in output file: Default: | (pipe)
            column_names: list of names of columns which you want to extract from csv
    '''
    csv_data = read_csv_file(input_file, input_del, column_names)
    response = convert_to_dat(csv_data=csv_data, output_path=output_path, output_del=output_del)
    return response

# if __name__ == "__main__":
#     filename = "csv/2022_Forbes_list.csv"
#     col_names = ["Rank in India", "Name","Headquarters","Revenue(billions US$)","Profit(billions US$)","Assets(billions US$)","Value(billions US$)","Industry"]
#     response_message = read_and_convert(filename=filename, delimeter=",", column_names=col_names)
