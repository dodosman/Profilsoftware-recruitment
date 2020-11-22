# Dwie dane:
# 1) urodziny
# 2) today
#
# 1. Czy koles urodził się 29.02?
# 	1.1 Nie:
# 		1.1.1 Czy urodziny w danym roku już miał (is today > urodziny)
# 		    1.1.1.1 Tak: (urodziny + 1 rok) - today (tak, miał już urodziny)
# 			1.1.1.2 Nie: urodziny - today
#
# 	1.2 Tak:
# 		1.2.1 Czy urodziny w danym roku już miał (is today > urodziny)
# 			1.2.1.1 Nie:
# 				1) is_leap_year(today) == True: urodziny - today
# 				2) is_leap_year(today) == False: (urodziny (- 1 day)) - today
# 			1.2.1.2 Tak:
# 				1) is_leap_year(today + 1 rok) == True: urodziny - today
# 				2) is_leap_year(today + 1 rok) == False: (urodziny (- 1 day)) - today
#
# Pytania:  1.jeśli urodził się w lutym ale nie 29?
#           2. jesli urodził się 29 a nie w lutym
#           3.czasami na poprawnych darach mi pokazuje ze koleś ma mieć urodziny za np.448 dni

import json

from calendar import isleap
from datetime import datetime

with open('persons.json', encoding="utf8") as json_file:
  data = json.load(json_file)

arrays = data["results"]
today = datetime.today()


def days_till_birthday(today, dob_date):
  # jeśli nie urodził się 29.02
  if (dob_date.month != 2 or dob_date.day != 29):

    # jeśli już miał urodziny
    if (dob_date.month < today.month) or (dob_date.month == today.month and dob_date.day < today.day):
      birthday = datetime(today.year + 1, dob_date.month, dob_date.day)
      time_till_birthday = birthday - today
      return time_till_birthday.days

      # jeżeli jeszcze nie miał  urodzin
    elif (dob_date.month > today.month) or (dob_date.month == today.month and dob_date.day >= today.day):
      birthday = datetime(today.year, dob_date.month, dob_date.day)
      time_till_birthday = birthday - today
      return time_till_birthday.days

    else:
      return "Not working"

  # jeśli urodził się 29.02
  elif (dob_date.month == 2 and dob_date.day == 29):

    # jeśli jeszcze nie miał urodzin
    if (dob_date.month > today.month) or (dob_date.month == today.month and dob_date.day >= today.day):

      if isleap(today.year) == True:
        birthday = datetime(today.year, dob_date.month, dob_date.day)
        time_till_birthday = birthday - today
        return time_till_birthday.days

      elif isleap(today.year) == False:
        birthday = datetime(today.year, dob_date.month, dob_date.day - 1)
        time_till_birthday = birthday - today
        return time_till_birthday.days

      else:
        return "Not working"

    # jeśli juz miał urodziny
    elif (dob_date.month < today.month) or (dob_date.month == today.month and dob_date.day < today.day):

      if isleap(today.year + 1) == True:
        birthday = datetime(today.year + 1, dob_date.month, dob_date.day)
        time_till_birthday = birthday - today
        return time_till_birthday.days

      elif isleap(today.year + 1) == False:
        birthday = datetime(today.year + 1, dob_date.month, dob_date.day - 1)
        time_till_birthday = birthday - today
        return time_till_birthday.days

      else:
        return "Not working"

  else:
    return "Not working"


for array in arrays:
  # Calculate time till birthday
  dob_string = array["dob"]["date"][:10]
  dob_date = datetime.strptime(dob_string, "%Y-%m-%d")

  array["time_till_birthday"] = days_till_birthday(today, dob_date)

  # Clean up phone fields
  array["phone"] = ''.join(e for e in array["phone"] if e.isnumeric())
  array["cell"] = ''.join(e for e in array["cell"] if e.isnumeric())

  # Remove picture
  array.pop("picture", None)

with open("persons_clean.json", "w") as json_file:
  json.dump(arrays, json_file)

with open('persons_clean.json', encoding="utf8") as json_file:
  data = json.load(json_file)

new_data = []
for array in data:
  new_array = {}
  new_array["gender"] = array["gender"]
  new_array["title"] = array["name"]["title"]
  new_array["first_name"] = array["name"]["first"]
  new_array["last_name"] = array["name"]["last"]
  new_array["location_street"] = array['location']['street']['name']
  new_array["location_number"] = array['location']['street']['number']
  new_array["location_city"] = array["location"]["city"]
  new_array["location_state"] = array["location"]["state"]
  new_array["location_country"] = array["location"]["country"]
  new_array["location_postcode"] = array["location"]["postcode"]
  new_array["location_coordinates_latitude"] = array['location']['coordinates']['latitude']
  new_array["location_coordinates_longitude"] = array['location']['coordinates']['longitude']
  new_array["location_timezone_offset"] = array["location"]["timezone"]["offset"]
  new_array["location_timezone_description"] = array["location"]["timezone"]["description"]
  new_array["email"] = array["email"]
  new_array["login_uuid"] = array["login"]["uuid"]
  new_array["login_username"] = array["login"]["username"]
  new_array["login_password"] = array["login"]["password"]
  new_array["login_salt"] = array["login"]["salt"]
  new_array["login_md5"] = array["login"]["md5"]
  new_array["login_sha1"] = array["login"]["sha1"]
  new_array["login_sha256"] = array["login"]["sha256"]
  new_array["dob_date"] = array["dob"]["date"]
  new_array["dob_age"] = array["dob"]["age"]
  new_array["registered_date"] = array["registered"]["date"]
  new_array["registered_age"] = array["registered"]["age"]
  new_array["phone"] = array["phone"]
  new_array["cell"] = array["cell"]
  new_array["id_name"] = array["id"]["name"]
  new_array["id_value"] = array["id"]["value"]
  new_array["nat"] = array["nat"]
  new_array["time_till_birthday"] = array["time_till_birthday"]

  new_data.append(new_array)

with open("persons_clean_selected.json", "w") as json_file:
  json.dump(new_data, json_file)
