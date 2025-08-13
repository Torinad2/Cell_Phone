# This program creates five CellPhone objects and stores them in a list.
import cellphone

def main():
    # Get a list of CellPhone objects.
    phones = make_list()

    # Display the data in the list.
    display_list(phones)

# The make_list function gets data from the user
# for five phones. The function returns a list
# of CellPhone objects containing the data.
def make_list():
    # Create an empty list.
    phone_list = []

    # Add five CellPhone objects to the list.
    for count in range(1,3):
        print("Enter information about cellphone N " + str(count))

        # Get the phone data.
        manufacturer = input("Enter manufacturer: ")
        model = input("Model: ")
        retail_price = float(input("Price: "))

        # Create a new CellPhone object in memory and
        # assign it to the phone variable.
        phone = cellphone.CellPhone(manufacturer, model, retail_price)

        # Add the object to the list.
        phone_list.append(phone)

    # Return the list.
    return phone_list

# The display_list function accepts a list containing
# CellPhone objects as an argument and displays the
# data stored in each object.
def display_list(phone_list):
    for count, phone in enumerate(phone_list, start = 1):
        print()
        print("Information about phone N " + str(count) + ":")
        print("Manufacturer: " + phone.get_manufact())
        print("Model: " + phone.get_model())
        print(f"Price: ${phone.get_retail_price():,.2f}")

# Call the main function.
if __name__ == "__main__":
    main()