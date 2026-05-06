
import statistics as stats
def display_main_menu():
    print("Enter some numbers seperated by commas (eg.5,67,32): ")
def get_user_input():
    inputted_numbers = input()
    string_list = inputted_numbers.split(",")
    float_list=[]
    for i in string_list:
        number = float(i)
        float_list.append(number)
       
    return float_list
def calc_average_temperature(float_list):
    average = sum(float_list)/len(float_list)
    print(f"The average of the numbers are {average:3f}")
def calc_min_max_temperature(float_list):
    minimum_number = min(float_list)
    maximum_number = max(float_list)
    print(f"The largest number is {maximum_number} and the minimum number is {minimum_number}")
def calc_median_temperature(float_list):
    median_value = stats.median(float_list)
    print(f"The median value is {median_value}")
def main():

    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

    display_main_menu()

    float_list=  get_user_input()
    calc_average_temperature(float_list)
    calc_min_max_temperature(float_list)
    calc_median_temperature(float_list)


if __name__ == "__main__":
    main()

