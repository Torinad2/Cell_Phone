# This program tests the CellPhone class.

import cellphone

def main():
    # Get the phone data.
    manufacturer = input("Provide Manufacturer: ")
    model = input("Provide model: ")
    retail_price = float(input("Provide Retail Price: "))

    # Create an instance of the CellPhone class.
    test = cellphone.CellPhone(manufacturer, model, retail_price)

    # Display the data that was entered.
    print("\nHere is the data that you entered:")
    print("Manufacturer: " + test.get_manufact())
    print("Model: " + test.get_model())
    print(f"Price: ${test.get_retail_price():,.2f}")

# Call the main function.
if __name__ == "__main__":
    main()