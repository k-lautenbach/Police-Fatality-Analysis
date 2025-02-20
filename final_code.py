"""
Final Project DS2001
Emily Kelly, Kathleenn Lautenbach, and Stephanie Jacinto
Fall 2024
Fatal Encounters Data
"""
from statistics import mean
import matplotlib.pyplot as plt
import csv


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
                  column_lst.append(year_only)
              # elif name_of_key == 'Latitude':
              #      print (item['Name'])
              else:
                  column_lst.append(val) #for all other strings that are not numbers
   return column_lst



def col_count(col):
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


def group_age_bar_plot(lst):
    '''
    parameter: Taking the age list and grouping it 0-20, 21 - 40, and up to oldest. Then putting it into a bar graph
    return: returns a bar graph grouped by ages
    '''
    # Emily: I put this together using lists to iterate through and attach the ages accordingly
    lst_to_10 = []
    lst_to_20 = []
    lst_to_30 = []
    lst_to_40 = []
    lst_to_50 = []
    lst_to_60 = []
    lst_to_70 = []
    lst_to_80 = []
    lst_to_90 = []
    lst_to_110 = []

    for num in lst:
        if num <= 10:
            lst_to_10.append(num)
        if 11 <= num <= 20:
            lst_to_20.append(num)
        if 21 <= num <= 30:
            lst_to_30.append(num)
        if 31 <= num <= 40:
            lst_to_40.append(num)
        if 41 <= num <= 50:
            lst_to_50.append(num)
        if 51 <= num <=60:
            lst_to_60.append(num)
        if 61 <= num <= 70:
            lst_to_70.append(num)
        if 71 <= num <= 80:
            lst_to_80.append(num)
        if 81 <= num <= 90:
            lst_to_90.append(num)
        if 91 <= num <= 110:
            lst_to_110.append(num)

    # This is to set up the bar graph to use the len of the lists to find the amount of people were in that age group
    # to then put in the graph
    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Y = [len(lst_to_10), len(lst_to_20),len(lst_to_30), len(lst_to_40),len(lst_to_50), len(lst_to_60), len(lst_to_70),
         len(lst_to_80),len(lst_to_90), len(lst_to_110)]
    ig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(X, Y, color=["mediumseagreen", "darkseagreen", "yellowgreen", "forestgreen", "darkgreen"])

    ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ax.set_xticklabels([f"0 - 10", f"11 - 20", f"21 - 30", f"31 - 40", f"41 - 50", f"51 - 60", f"61 - 70", f"71 - 80",
                        f"81 - 90", f"91 - 110"])
    ax.set_ylabel("Number of Victims")
    ax.set_xlabel("Grouped by 10 year age groups intervals")
    ax.set_title("Number of victims by 10 year intervals")
    # This will print the amount of victims known per age group
    print("Ages 0 - 10:", len(lst_to_10), "  Ages 11 - 20:", len(lst_to_20), "  Ages 21 - 30:", len(lst_to_30),
          "  Ages 31 - 40:", len(lst_to_30), "  Ages 41 - 50:", len(lst_to_50))
    print("Ages 51 - 60:", len(lst_to_60), "  Ages 61 - 70:", len(lst_to_70), "  Ages 71 - 80:", len(lst_to_80),
          "  Ages 81 - 90:", len(lst_to_90), "  Ages 91 - 110:", len(lst_to_110))
    plt.savefig("Plot Age")
    plt.show()

def count_victims_race(data, race_column):
    '''
    :param data:
    :param race_column:
    :return: counts per race group
    '''
    race_counts = {}
    list_races = {"European-American/White", "African-American/Black", "Asian/Pacific Islander",
                   "Hispanic/Latino", "Native American/Alaskan", "Middle Eastern", "Unknown"}
    # created this list to help clean out the data and avoid any trouble when plotting
    # gathering the data in the race column and labeling it accordingly
    for row in data:
        if race_column in row:
            race = row[race_column].strip()
        else:
            race = "Unknown"

        if race not in list_races:
            race = "Race Unspecified"
        # calculating the counts in the data for each race group in order to find
        # total number of victims per race group
        if race in race_counts:
            race_counts[race] += 1
        else:
            race_counts[race] = 1
    return race_counts

def plot_victims_race(data, race_column):
    '''
    parameters: takes in the data and uses the race column
    does: creates bar plot for number of victims per race group
    '''
    race_counts = count_victims_race(data, race_column)
    races = []
    counts = []
    # Stephanie: creating a list to access necessary data regarding race groups and the number of
    # victims of police brutality from each group
    for race in race_counts.keys():
        races.append(race)
        counts.append(race_counts[race])
        # creating a bar plot to visualize the data gathered
    plt.bar(races, counts, color=["coral", "darkgoldenrod", "darkorange", "peru", "orangered"])

    plt.xlabel('Race')
    plt.ylabel('Number of Victims')
    plt.title('Number of Victims per Race Group')
    plt.xticks(rotation=45, ha="right")

    plt.show()

def count_victims_gender(data, gender_column):
    '''
    :param data:
    :param gender_column:
    :return: counts per gender group
    '''
    gender_counts = {}
    list_genders = {"Female", "Male", "Transgender"}
    # Stephanie: created this list to help clean out the data and avoid any trouble when plotting
    # cleaning the data and gathering the data in the gender column and labeling it accordingly
    for row in data:
        if gender_column in row:
            gender = row[gender_column].strip()
        else:
            gender = "Unknown"
        if gender not in list_genders:
            gender = "Gender Unspecified"

        if gender in gender_counts:
            gender_counts[gender] += 1
        else:
            gender_counts[gender] = 1
    return gender_counts

def plot_victims_gender(data, gender_column):
    '''
    Function: Creates bar plot of number of victims per gender group
    :param data:
    :param gender_column:
    '''
    # Stephanie:creating a list for our counts and gender groups to store our data to
    # later use to create our bar plot
    gender_counts = count_victims_gender(data, gender_column)
    genders = []
    counts = []

    for gender in gender_counts.keys():
        genders.append(gender)
        counts.append(gender_counts[gender])
    # creating a bar plot to visualize the number of victims per gender group
    plt.bar(genders, counts, color=["slateblue", "darkorchid", "plum", "indigo"])

    plt.xlabel('Gender')
    plt.ylabel('Number of Victims')
    plt.title('Number of Victims per Gender Group')
    plt.xticks(rotation=45, ha="right")

    plt.show()


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
    # Kate: Plotting the longitude and latitude
    plt.figure(figsize=(12,10))
    plt.scatter(longitude, latitude, s=.5, color="maroon", label="Location of Incident")
    plt.xlabel("longitude")
    plt.ylabel("latitude")
    plt.legend()
    plt.savefig("police_fatalities_locations.png")
    plt.title("Plot by Longitude and Latitude")
    plt.show()

def plot_years(count_dict):
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
    # sorts dictionary by year
    order_year = dict(sorted(count_dict.items()))
    for key in order_year:
        keys_x.append(key)
        vals_y.append(count_dict[key])

    plt.figure(figsize=(12, 6))
    plt.bar(keys_x, vals_y, color=["lightblue", "skyblue", "lightslategrey", "darkturquoise", "darkcyan", "cadetblue"])
    plt.xticks(rotation = 45)
    plt.xlabel('Years')
    plt.ylabel("Amount of Fatalities")
    plt.title("Deaths by Year")

    plt.show()
    plt.savefig("Years")

def main():
    # Emily: I took the files from Kate and Stephanie as well as mine and made it into one big file with all of our code
    print("Final Project")
    # This section is finding the average age, the min age, and max age
    # These findings are looking to understand the range of police caused fatalities and the average age of death
    # This is also will help with the bar graph for the ages
    fatal_data = load_data(FILENAME)

    find_age = get_column(fatal_data, 'Age')

    int_age = int_list(find_age)
    average_age = mean(int_age)
    min_age = min(int_age)
    max_age = max(int_age)
    print("This is the average age of police killed person was", round(average_age))
    print("This was the youngest age of a person killed by police", round(min_age))
    print("This was the oldest age of a person killed by police", round(max_age))
    print(count_victims_race(fatal_data, 'Race'))
    print(count_victims_gender(fatal_data, 'Gender'))
    print("The year with the highest fatalities is 2020 with 2085 deaths, the year "
          "with the least fatalities is 2000 with 865 deaths")
    group_age_bar_plot(int_age)
    # barplots showing the number of victims per race group and gender

    plot_victims_race(fatal_data, 'Race')
    plot_victims_gender(fatal_data, 'Gender')


    # KATE'S CODE
    # PLOT locations
    # clean code for both lat and long
    find_lat = get_column(fatal_data, 'Latitude')
    find_long = get_column(fatal_data, 'Longitude')
    # call plot function
    #print (find_lat)
    plot_locations(find_long, find_lat)

    # PLOT number of fatalities by year
    find_year = get_column(fatal_data, 'month/day/year')
    year_count = col_count(find_year)
    plot_years(year_count)



main()