import csv

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
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row
    return dictionary

def main():
    # read the products.csv file into a dictionary
    products_dict = read_dictionary('products.csv', 0)
    print("All Products")
    print(products_dict)

    # open request.csv file
    with open('request.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  
        print("\nRequested Items")
        for row in reader:
            product_number = row[0]
            quantity = int(row[1])
            product = products_dict[product_number]
            product_name = product[1]
            product_price = float(product[2])
            print(f"{product_name}: {quantity} @ {product_price:.2f}")

if __name__ == "__main__":
    main()
