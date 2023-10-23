import statistics
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def calc_average(nums):
    calc_ave = sum(nums) / len(nums)
    return calc_ave

def get_user_input():
    user_input = input("Enter the temperatures separated by commas: ")
    nums = [float(num) for num in user_input.split(",")]
    return nums

def find_min_max(nums):
    min_temp = int(min(nums))
    max_temp = int(max(nums))
    return min_temp, max_temp

def sort_temperature(nums):
    sorted_list = sorted(nums)  # Corrected the sorting method
    return sorted_list

def calc_median_temperature(nums):
    median_temp=statistics.median(nums)
    return median_temp

def main():
    display_main_menu()
    list_input = get_user_input()
    average = calc_average(list_input)
    min_temp, max_temp = find_min_max(list_input)
    sorted_temp = sort_temperature(list_input)
    median_temp = calc_median_temperature(list_input)

    print("Average is " + str(average))
    print("Min Temp is " + str(min_temp))
    print("Max Temp is " + str(max_temp))
    print("Median Temp is " + str(median_temp))
    print("Sorted List of Temps: " + ', '.join(map(str, sorted_temp)))

if __name__ == "__main__":
    main()
