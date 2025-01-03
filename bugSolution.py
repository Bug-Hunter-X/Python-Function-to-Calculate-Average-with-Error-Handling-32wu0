def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 # Handle list with no numeric values
    return sum(numeric_numbers) / len(numeric_numbers)

# Example usage:
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_numbers2 = [10,20, 'a']
average2 = calculate_average(my_numbers2)
print(f"The average is: {average2}")
my_numbers3 = ['a', 'b', 'c']
average3 = calculate_average(my_numbers3)
print(f"The average is: {average3}") 