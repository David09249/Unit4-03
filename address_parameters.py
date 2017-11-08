# Created by: David Wang
# Created on: 2-Nov-2017
# Created for: ICS3U
# Daily Assignment - Unit4-03
# This program displays your address with an optional parameter

def print_address(street, city, province, postal_code, apt_number = ''):
    # print address
    if apt_number == '':
        print(street + ' , ' + city + ' , ' + province + ' , ' + postal_code)
    else:
        print(apt_number + ' , ' + street + ' , ' + city + ' , ' + province + ' , ' + postal_code)

your_street = raw_input("Enter your address: ")
your_city = raw_input("Enter your city: ")
your_province = raw_input("Enter your province: ")
your_postal_code = raw_input("Enter your postal code: ")
apt_number_choice = raw_input("Do you have an apartment number? (yes/no): ")
if apt_number_choice == 'yes':
    your_apt_number = raw_input("Enter your apartment number: ")
    print_address(your_street, your_city, your_province, your_postal_code, apt_number = your_apt_number)
else:
    print_address(your_street, your_city, your_province, your_postal_code)

