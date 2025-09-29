# text = input("What is your name? ")
# color = input("What is your ")
# a = 'text'
# k = f"The is a {type(a)} {a}"
# print(k)
# span = float(input("Distance the cable must span in meters: "))
# dips = float(input("Distance the cable will sag in meters: "))

# length = span + (8 * dips)**2 / (3 * span)

# print(f"Length of cable in meters: {length:.2f}")

# number  = float(input("Please enter a number: "))
# r= round(number, 2)
# print(r)

# a = "joy"
# b = "james"
# c = "july"

# print(a,b,c, sep="|", end="\n", flush=True)

# import math

# number = float(input("Enter a number: "))
# ans = math.sqrt(number)
# print(ans)
# def fullname(w1,w2):
#   return w1 + ' ' + w2

# f=fullname(w2='faith',w1='charity')
# print(f)
# def func1():
#   a=1
# def func2():
#   a=2
#   func1()
#   return a
# a=0
# print(func2())


# number_items1 = input("Enter the number of items: ") 
# number_items2 = input("Enter the number of items per box: ") 
# print(f"For {number_items1} items, packing {number_items2} in the each box, you will need 2 boxes.")
# number_items3 = input("Enter the number of items: ") 
# number_items4 = input("Enter the number of items per box: ") 
# print(f"For {number_items3} items, packing {number_items4} in the each box, you will need 7 boxes.")



# names = ['osazee', 'kelvin', 'osamagbe', 'james', 'adams']
# for name in range(len(names)):
# # for name in names:
#     print(name)


# sum = 0

# for i in range(10):
#     number = float(input("Please enter a number: "))
#     if number == 0:
#            break
#     sum += number

# print(f'Total number: {sum}')

# Example 9
# def main():
#     # These are the indexes of each
#     # element in the inner lists.
#     YEAR_PLANTED_INDEX = 0
#     HEIGHT_INDEX = 1
#     GIRTH_INDEX = 2
#     FRUIT_AMOUNT_INDEX = 3
#     # Create a compound list that stores inner lists.
#     apple_tree_data = [
#         # [year_planted, height, girth, fruit_amount]
#         [2012, 2.7, 3.6, 70.5],
#         [2012, 2.4, 3.7, 81.3],
#         [2015, 2.3, 3.6, 62.7],
#         [2016, 2.1, 2.7, 42.1]
#     ]
#     total_fruit_amount = 0
#     # This loop will repeat once for each inner list
#     # in the apple_tree_data compound list.
#     for inner_list in apple_tree_data:
#         # Retrieve the fruit amount from
#         # the current inner list.
#         fruit_amount = inner_list[FRUIT_AMOUNT_INDEX]
#         # Print the fruit amount for the current tree.
#         print(fruit_amount)
#         # Add the current fruit amount to the total.
#         total_fruit_amount += fruit_amount
#     # Print the total fruit amount.
#     print(f"Total fruit amount: {total_fruit_amount:.1f}")
# # Call main to start this program.
# if __name__ == "__main__":
#     main()



# def main():
#     print("main()")
#     x = 5
#     lx = [7, -2]
#     print(f"Before calling modify_args(): x {x}  lx {lx}")
#     # Pass one integer and one list
#     # to the modify_args function.
#     modify_args(x, lx)
#     print(f"After calling modify_args():  x {x}  lx {lx}")
# def modify_args(n, alist):
#     """Demonstrate that the computer passes a value
#     for integers and passes a reference for lists.
#     Parameters
#         n: A number
#         alist: A list
#     Return: nothing
#     """
#     print("   modify_args(n, alist)")
#     print(f"   Before changing n and alist: n {n}  alist {alist}")
#     # Change the values of both parameters.
#     n += 1
#     alist.append(4)
#     print(f"   After changing n and alist:  n {n}  alist {alist}")
# # Call main to start this program.
# if __name__ == "__main__":
#     main()


# def main():
    # Create a dictionary with student IDs as the keys
    # and student data stored in a list as the values.
    # students_dict = {
    #     # student_ID: [given_name, surname, email_address, credits]
    #     "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
    #     "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
    #     "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
    #     "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
    #     "07-103-5621": ["Amelia", "Davis" "dav19008@byui.edu", 0]
    # }

def main():
    # Create a list that contains five student numbers.
    numbers_list = ["42-039-4736", "61-315-0160",
            "10-450-1203", "75-421-2310", "07-103-5621"]
    # Create a list that contains five student names.
    names_list = ["Clint Huish", "Amelia Davis",
            "Ana Soares", "Abdul Ali", "Amelia Davis"]
    # Convert the numbers and names lists into a dictionary.
    student_dict = dict(zip(numbers_list, names_list))
    # Print the entire student dictionary.
    print("Dictionary:1", student_dict)
    print()
    # Convert the student dictionary into
    # two lists named keys and values.
    keys = list(student_dict.keys())
    values = list(student_dict.values())
    # Print both lists.
    print("Keys:", keys)
    print()
    print("Values:", values)
# Call main to start this program.
if __name__ == "__main__":
    main()