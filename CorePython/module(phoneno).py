import phonenumbers
from phonenumbers import geocoder
from phonenumbers import parse

number = input( "Enter the number = ")
parsed_number = parse(number, None)

national_code = parsed_number.country_code
national_number = parsed_number.national_number 

print(national_code)
print(national_number)

country_name = geocoder.description_for_number(national_number,"en")
latitude = country_name.latlng[0]  # Extracting latitude
longitude = country_name.latlng[1]  # Extracting longitude
print(country_name)
print(f"latitude = {latitude} and longitude = {longitude}")
