# This program pickles CellPhone objects.
import pickle
import cellphone

# Constant for the filename.
FILENAME = 'cellphones.dat'

def main():
    # Initialize a variable to control the loop.
    again = 'y'

    # Open a file for binary writing.
    with open(FILENAME, 'wb') as output_file:

        # Get data from the user.
        while again.lower() == 'y':
            # Get cell phone data.
            manufacturer = input('Enter the manufacturer: ')
            model = input('Enter the model: ')
            price = float(input('Enter the price: '))

            # Create a CellPhone object.
            phone = cellphone.CellPhone(manufacturer, model, price)

            # Create a CellPhone object.
            pickle.dump(phone, output_file)

            # Pickle the object and write it to the file.
            again = input('Enter more phone data? (y/n): ')

        # Get more cell phone data?
        print(f'The data was written to {FILENAME}.')

# Call the main function.
if __name__ == '__main__':
    main()