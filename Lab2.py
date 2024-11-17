def display_main_menu():
    print("Enter some number separated by commas (eg. 5,67,32)")
    
def get_user_input():
    temps = input()
    temp_list_str = temps.split(",")
    temp_list = []
    for temp in temp_list_str:
        temp_list.append(float(temp))
    return temp_list
def calc_average(temp_list):
    for temp in temp_list:
        total = total +temp
    average = total / len(temp_list)
    return average

def find_min_max(temp_list):
    list = []
    list.append(min(temp_list))
    list.append(max(temp_list))
    return list
def sort_temperature(temp_list):
    return

def calc_median_temperature(temp_list):
    return
