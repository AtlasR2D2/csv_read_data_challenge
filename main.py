

def csv_pkg_method():
    import csv

    with open("weather_data.csv") as data_file:
        data = csv.reader(data_file)
        # Identify column associated with Temperatures
        temperature_header = "temp"
        temperature_header_ord = 0
        i = 0
        for row in data:
            if i == 0:
                header_row = row
                break
        for col in header_row:
            if col == temperature_header:
                temperature_header_ord = i
                break
            i += 1
        # Construct temperatures list
        temperatures = []
        for row in data:
            temperatures.append(row[temperature_header_ord])

        # Print list to console
        print(temperatures)

def convert_c_to_f(temp_c):
    return temp_c * (9.0/5.0) + 32


def pandas_pkg_method():
    import pandas

    # data = pandas.read_csv("weather_data.csv")
    # temp_list = data["temp"].to_list()
    # print(temp_list)
    # max_temp = data["temp"].max()
    # max_temp_row = data[data["temp"] == max_temp]
    # print(max_temp_row)
    # monday = data[data.day == "Monday"]
    # print(convert_c_to_f(int(monday.temp)))

    # Create a dataframe from scratch
    data_dict = {
        "students": ["Amy", "James", "Angela"],
        "scores": [76, 56, 65]
    }
    data_dict_df = pandas.DataFrame(data_dict)
    print(data_dict_df)
    data_dict_df.to_csv("new_data.csv")

# pandas_pkg_method()

def squirrel_time():
    import pandas as pd
    squirrel_data = pd.read_csv("Squirrel_Data.csv")
    #print(squirrel_data)
    # Primary Fur Color
    squirrel_fur_color = squirrel_data.groupby("Primary Fur Color")["Primary Fur Color"].count()
    print(squirrel_fur_color)
    black_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
    cinnamon_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
    gray_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
    squirrel_counts = {
        "Fur Color": ["Black", "Cinnamon", "Gray"],
        "Count": [black_squirrels, cinnamon_squirrels, gray_squirrels]
    }
    # Export Counts
    pd.DataFrame(squirrel_counts).to_csv("squirrel_counts.csv")

    # fur_colors = pd.DataFrame(squirrel_fur_color)
    # fur_colors.to_csv("fur_colors.csv")



squirrel_time()
