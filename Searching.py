def linear_search(numbers, target_value):
    for current_index in range(len(numbers)):
        if numbers[current_index] == target_value:
            return current_index
    return -1


def binary_search(sorted_numbers, target_value):
    left_boundary = 0
    right_boundary = len(sorted_numbers) - 1

    while left_boundary <= right_boundary:
        middle_position = (left_boundary + right_boundary) // 2

        if sorted_numbers[middle_position] == target_value:
            return middle_position

        elif sorted_numbers[middle_position] < target_value:
            left_boundary = middle_position + 1

        else:
            right_boundary = middle_position - 1

    return -1


if __name__ == "__main__":

    try:
        total_elements = int(input("Enter number of elements : "))
        numbers_list = []

        for element_count in range(total_elements):
            value = int(input(f"Enter element {element_count + 1} : "))
            numbers_list.append(value)

        search_value = int(input("\nEnter value to search : "))

        while True:
            print("----- SEARCH MENU -----")
            print("1. Linear Search")
            print("2. Binary Search")
            print("3. Exit")

            user_choice = int(input("Enter your choice : "))

            if user_choice == 1:
                result_index = linear_search(numbers_list, search_value)

                if result_index != -1:
                    print(f"Element found at index {result_index} (Linear Search)")
                else:
                    print("Element not found (Linear Search)")

            elif user_choice == 2:
                sorted_numbers = sorted(numbers_list)
                print("Sorted List for Binary Search : ", sorted_numbers)

                result_index = binary_search(sorted_numbers, search_value)

                if result_index != -1:
                    print(f"Element found at index {result_index} (Binary Search)")
                else:
                    print("Element not found (Binary Search)")

            elif user_choice == 3:
                print("Program exited")
                break

            else:
                print("Invalid choice")

    except ValueError:
        print("Please enter valid numeric input")