"""
Final Project DS2001
Fall 2024
Fatal Encounters Data
"""
from statistics import mean, stdev
from math import sqrt
import matplotlib.pyplot as plt
import csv

from matplotlib.pyplot import xlabel
from numpy.ma.core import append

FILENAME = 'DS_Project_FATAL_ENCOUNTERS 1(in).csv'
def load_data(FILENAME):
    """
    Parameters: Read a comma-separated dataset in from a file, and, using csv.DictReader,
    return a list of dictionaries.
    filename (str): the path to the file
    Returns: A dataset, in list-of-dicts form.
    """

    with open(FILENAME, "r") as FILENAME:
        dr = csv.DictReader(FILENAME)
        l = [row for row in dr]
        FILENAME.close()
    return l

def get_column(data, name_of_key): #Kate
   '''
   parameter: check if data can be int or not
   return: return a list of values corresponding to the values from the dictionary
   does: this column retrieved all values from dictionaries (which is how the code
   is retrieved) and tests the type, if it is numerical the val is converted to a float.
   if not (using "except") then the value is added to the list as string. There is a
   special instruction for the date because only the last part of the information is needed
   so when calling that column it has its own function.
   '''

   # Code developed in office hours with Natika Jain

   column_lst = []
   for item in data:
        val = item[name_of_key]
        if val:
          try: # seeing if it can be converted to float
              num = float(val) # if yes then converts and appends
              column_lst.append(num)
          except ValueError: # so if not converted: next steps (have to dictate except all edge cases)
              if name_of_key == 'month/day/year':
                  year_only = val.split("/")[-1] # extracts only year (splitting string by slash)
                  column_lst.append(int(year_only))
              # elif name_of_key == 'Latitude':
              #      print (item['Name'])
              else:
                  column_lst.append(val) #for all other strings that are not numbers
   return column_lst

def col_count(col): #Kate
    '''
    Function: count events in each column
    param : dictionary list of column
    return: dictionary of counts
    does: uses the list of values returned from the get column and turns them into
    keys in a dict, then for the values it adds one everytime said key is encountered in the list
    creating a new dictionary if a new key is encountered
    '''

    col_counts = {}

    for item in col:
        count = item
        if count in col_counts:
            col_counts[count] += 1
        else:
            col_counts[count] = 1

    return col_counts


def int_list(lst):
    '''
    parameter: In takes list of strings and ints
    does: Separates stings and ints into separate lists, to 1) clean data and 2) count
        the amount of missing data from relevant columns
    return: returns list of ints or list of empty numbers to count
    '''
    num_lst = []
    string_lst = []
    for num in lst:

        if type(num) is float and num.is_integer():
            num_lst.append(int(num))
        elif type(num) is float:
            num_lst.append(num)

        else:
            string_lst.append(num)
    return num_lst


def seperate_list(str_list):
    '''
    param: list of strings
    return: list of strings
    '''
    other = []
    num = []
    for item in str_list:
        if item.isdigit() in str_list == False:
            other.append(item)
        else:
            num.append(item)
    return num


def group_age_bar_plot(lst):
    '''
    parameter: Taking the age list and grouping it 0-20, 21 - 40, and up to oldest. Then putting it into a bar graph
    return: returns a bar graph grouped by ages
    '''
    lst_to_20 = []
    lst_to_40 = []
    lst_to_60 = []
    lst_to_80 = []
    lst_to_100 = []
    lst_to_120 = []
    for num in lst:
        if num <= 20:
            lst_to_20.append(num)
        if 21 <= num <= 40:
            lst_to_40.append(num)
        if 41 <= num <= 60:
            lst_to_60.append(num)
        if 61 <= num <= 80:
            lst_to_80.append(num)
        if 81 <= num <= 100:
            lst_to_100.append(num)
        if 100 <= num <= 120:
            lst_to_120.append(num)
    X = [1, 2, 3, 4, 5, 6]
    Y = [lst_to_20, lst_to_40, lst_to_60, lst_to_80, lst_to_100, lst_to_120]

def plot_locations(longitude, latitude):
    """
    Make a scatter plot of all the end locations given by the lat and long
    columns in the data. Plot one point as a special point to differentiate
    it from the others
    :param longitude: list of floats
    :param latititude: list of floats
    :return: nothing
    does: graphs two lists of latitude and longitudes
    """

    plt.figure(figsize=(12,10))
    plt.scatter(longitude, latitude, s=.5, color="red", label="Location of Incident")
    plt.xlabel("longitude")
    plt.ylabel("latitude")
    plt.legend()
    plt.savefig("police_fatalities_locations.png")
    plt.show()

def plot_counts(count_dict):
    """
       Make a line graph of any function using a count,
       it from the others
       :param count_dict: the count dictionary that comes from using the col_count func.
       :param fig_name: string to name plots so function can be used for any col
       :param xlabel: string for xlabel
       :return: nothing
       does: sorts the values and keys into two separate lists then graphs them
       """
    vals_y = []
    keys_x = []
    order_year = dict(sorted(count_dict.items()))
    for key in order_year:
        keys_x.append(key)
        vals_y.append(count_dict[key])

    plt.figure(figsize=(12, 6))
    plt.bar(keys_x, vals_y, color="blue")
    plt.xticks(rotation = 45)
    plt.xlabel(xlabel)
    plt.ylabel("Amount of Fatalities") # does not change

    plt.show()
    plt.savefig("fig1")


def main():
    print("Final Project")

    fatal_data = load_data(FILENAME)

    # KATE'S CODE
    # PLOT locations
    # clean code for both lat and long
    find_lat = get_column(fatal_data,'Latitude')
    find_long = get_column(fatal_data,'Longitude')
    lat_final = int_list(find_lat) #int_list cleans empty vals
    long_final = int_list(find_long)
    # call plot function
    #plot_locations(long_final, lat_final)

    # PLOT number of fatalities by year
    find_year = get_column(fatal_data, 'month/day/year')
    year_count = col_count(find_year)
    plot_counts(year_count)

    find_age = get_column(fatal_data,'Age')
    final_age = int_list(find_age)







main()
