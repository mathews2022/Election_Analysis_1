counties_dict = [{"Arapahoe": 4228298, "Denver": 463353, "Jefferson": 43243}]

x_array = [1, 2, 3]

##y = counties_dict.keys
#(y)

for county, votes in counties_dict.items():
    print(f"{county} has votes {counties_dict[county]}")

for row in x_array:
    print(row)    