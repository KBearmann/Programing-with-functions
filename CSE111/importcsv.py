import csv
from datetime import datetime
import os

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                key = row[key_column_index]
                dictionary[key] = row
    except FileNotFoundError as e:
        print(f"Error: missing file\n{e}")
        exit()
    return dictionary

def main():
    # Paths to the files
    products_path = r'C:\Users\keill\OneDrive\Desktop\Spring2024\Programingwithfunctions\CSE111\products'
    request_path = r'C:\Users\keill\OneDrive\Desktop\Spring2024\Programingwithfunctions\CSE111\request'

    # Debugging: Print the paths to ensure they are correct
    print(f"Products path: {products_path}")
    print(f"Request path: {request_path}")

    # Debugging: Check if files exist
    print(f"Checking if {products_path} exists: {os.path.exists(products_path)}")
    print(f"Checking if {request_path} exists: {os.path.exists(request_path)}")

    if not os.path.exists(products_path):
        print(f"Error: The file {products_path} does not exist.")
        return
    if not os.path.exists(request_path):
        print(f"Error: The file {request_path} does not exist.")
        return

    # Read products file into a dictionary
    products_dict = read_dictionary(products_path, 0)

    print("Inkom Emporium\n")

    total_items = 0
    subtotal = 0.0
    sales_tax_rate = 0.06

    try:
        # Open the request file 
        with open(request_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                product_number = row[0]
                quantity = int(row[1])
                product = products_dict[product_number]
                product_name = product[1]
                product_price = float(product[2])
                total_items += quantity
                subtotal += product_price * quantity
                print(f"{product_name}: {quantity} @ {product_price:.2f}")

    except FileNotFoundError as e:
        print(f"Error: missing file\n{e}")
        return
    except KeyError as e:
        print(f"Error: unknown product ID in the request file\n{e}")
        return

    sales_tax = subtotal * sales_tax_rate
    total = subtotal + sales_tax

    print(f"\nNumber of Items: {total_items}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Sales Tax: {sales_tax:.2f}")
    print(f"Total: {total:.2f}")
    print("\nThank you for shopping at the Inkom Emporium.")

    current_date_and_time = datetime.now()
    print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y}")

if __name__ == "__main__":
    main()
