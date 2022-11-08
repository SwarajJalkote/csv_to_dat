This is a Python Library to Read the CSV file and convert it into .dat file

# Description: 
**PyPi:** https://pypi.org/project/csvtodat/ <br />
![image](https://user-images.githubusercontent.com/29909977/200530068-5d78646d-cd5c-473f-98ed-7c6c140a0953.png)

# Installation:
``` pip install csvtodat ```

# Functions:
 ```python
 csv_to_dat(input_file, input_del=",", output_path="output.dat", output_del="|", column_names=list())
 ```
    - input_file: csv file which needs to be converted with complete path
    - input_del: delimiter used in input file. Default: , (comma)
    - output_path: dat file which will be created as output with expected path
    - output_del: delimiter used in output file: Default: | (pipe)
    - column_names: list of names of columns which you want to extract from csv

``` read_csv_file(input_file, input_del=",", column_names=list()) ```
    - input_file: csv file which needs to be converted with complete path
    - input_del: delimiter used in input file. Default: , (comma)
    - column_names: list of names of columns which you want to extract from csv

``` convert_to_dat(csv_data, output_path="output.dat", output_del="|") ```
    - csv_data: pandas DataFrame returned by read_csv()
    - output_path: dat file which will be created as output with expected path
    - output_del: delimiter used in output file: Default: | (pipe)