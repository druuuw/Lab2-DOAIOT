import statistics


print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def calculate_bmi(height,weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height*height)
    print(bmi)
    if bmi < 18.5:
        print("Underweight")
    elif bmi > 25:
        print("Obese")
    else:
        print("Normal")

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5,57,32)")

def get_user_input():
    print("Enter Values: ")
    lists= input().split(",")
    list_of_floats = list(map(float,lists))
    return list_of_floats

def calc_average(list):
    average = statistics.mean(list)
    average_float = float(average)
    return average_float

def find_min_max(list):
    min_no = min(list)
    max_no = max(list)
    min_max = [min_no,max_no]
    return min_max

def sort_temp(list):
    sorted_list = sorted(list)
    return sorted_list

def calc_median(list):
    median = statistics.median(list)
    return median

def main():
    display_main_menu()
    list = get_user_input()
    print("You entered" + str(list))
    print("Average: " + str(calc_average(list)))
    print("[Min,Max] = " +  str(find_min_max(list)))
    print("Sorted: " + str(sort_temp(list)))
    print("Median: " + str(calc_median(list)))




if __name__ == "__main__":
    main()



#calculate_bmi(height=1.73,weight=57)
display_main_menu()
numbers = get_user_input()
calc_average(numbers)
