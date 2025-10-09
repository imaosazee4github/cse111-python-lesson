import csv
from datetime import datetime, timedelta
# Program note
# The program displays a detailed list of items requested by the customer with quantity and price.
# The program computes and prints the number of items, subtotal, sales tax, and total.
# Prints also the number of items, subtotal, sales tax, and total.

# Enhancement Note:
# - Added "Buy One", Get one half off" discount items(1 cup of yogurt).
# - Added a Returned By Date 30dayes in the future.
# - Added formatted output for better readability.


def read_dictionary(filename, key_column_index):
    """Read the content of a CSV file into a dictionary."""
    products_dict = {}
    with open(filename, "rt") as csvfile:
        reader = csv.reader(csvfile)
        next(reader) # skip header line
        for row in reader:
            if len(row) == 0:
                continue
            key = row[key_column_index]
            products_dict[key] = row
    return products_dict


def main():
    PRODUCT_KEY_INDEX = 0
    PRODUCT_NAME_INDEX = 1
    PRODUCT_PRICE_INDEX = 2
    SALES_TAX_RATE = 0.06

    try:
        # Read product catalog
        products_dict = read_dictionary("products.csv", PRODUCT_KEY_INDEX)

        print("\n=== Osazee's Fresh Market === \n")

        total_items = 0
        subtotal = 0

        # Read customer request

        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)

            next(reader) 
            print("Requested Item")

            for row in reader:
                if len(row) == 0:
                    continue

                product_number = row[0]
                quantity = int(row[1])

                if product_number not in products_dict:
                    raise KeyError(product_number)
                
                product_info = products_dict[product_number]
                product_name = product_info[PRODUCT_NAME_INDEX]
                product_price = float(product_info[PRODUCT_PRICE_INDEX])

                # Apply Buy one, Get One Half Off for item DO83

                if product_number == "DO83":
                    full_price_count = quantity // 2 + quantity % 2
                    half_price_count = quantity // 2
                    item_total = (full_price_count * product_price) + (half_price_count * product_price * 0.5)
                    print(f"{product_name}: {quantity}  @ {product_price:.2f} (BOGO 50% applied)")
                else:
                    item_total = quantity * product_price
                    print(f"{product_name}: {quantity} @ ${product_price:.2f}")

                subtotal += item_total
                total_items += quantity


        sales_tax = subtotal * SALES_TAX_RATE
        total_due = subtotal + sales_tax

        # Display summary

        print("\n--------------")
        print(f"Number of Items: {total_items}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Sales Tax (6%): ${sales_tax:.2f}")
        print(f"Total Due: ${total_due:.2f}")
        print("---------------------------")

        # Print current date and time
        current_time = datetime.now()
        print(f"Date: {current_time:%A, %B %d, %Y %I:%M %p}\n")

        # Print return date (30 days in the future)
        return_date = current_time + timedelta(days=30)
        print(f"Return By: {return_date:%A, %B %d, %Y 9:00 PM}")


        print("\nThank you for shopping at Osazee's Fresh Market!")

    except FileNotFoundError as e:
        print(f"Error: Missing file — {e.filename}")
    except PermissionError as e:
        print(f"Error: Permission denied — {e.filename}")
    except KeyError as e:
        print(f"Error: Unknown product ID {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__=="__main__":
    main()