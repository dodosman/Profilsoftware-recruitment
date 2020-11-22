import json
from peewee import *

db = SqliteDatabase('people.db')

class Person(Model):
  gender = CharField()
  title = CharField()
  first_name = CharField()
  last_name = CharField()
  location_street = CharField()
  location_number = CharField()
  location_city = CharField()
  location_state = CharField()
  location_country = CharField()
  location_postcode = CharField()
  location_coordinates_latitude = CharField()
  location_coordinates_longitude = CharField()
  location_timezone_offset = CharField()
  location_timezone_description = CharField()
  email = CharField()
  login_uuid = CharField()
  login_username = CharField()
  login_password = CharField()
  login_salt = CharField()
  login_md5 = CharField()
  login_sha1 = CharField()
  login_sha256 = CharField()
  dob_date = CharField()
  dob_age = IntegerField()
  registered_date = CharField()
  registered_age = CharField()
  phone = CharField()
  cell = CharField()
  id_name = CharField()
  id_value = CharField(null=True)
  nat = CharField()
  time_till_birthday = CharField()

  class Meta:
    database = db  # This model uses the "people.db" database.


if __name__ == "__main__":
  db.connect()
  db.create_tables([Person])

with open('persons_clean_selected.json', encoding="utf8") as json_file:
  data = json.load(json_file)

for array in data:
  first_person = Person(
    gender=array["gender"],
    title=array["title"],
    first_name=array["first_name"],
    last_name=array["last_name"],
    location_street=array["location_street"],
    location_number=array["location_number"],
    location_city=array["location_city"],
    location_state=array["location_state"],
    location_country=array["location_country"],
    location_postcode=array["location_postcode"],
    location_coordinates_latitude=array["location_coordinates_latitude"],
    location_coordinates_longitude=array["location_coordinates_longitude"],
    location_timezone_offset=array["location_timezone_offset"],
    location_timezone_description=array["location_timezone_description"],
    email=array["email"],
    login_uuid=array["login_uuid"],
    login_username=array["login_username"],
    login_password=array["login_password"],
    login_salt=array["login_salt"],
    login_md5=array["login_md5"],
    login_sha1=array["login_sha1"],
    login_sha256=array["login_sha256"],
    dob_date=array["dob_date"],
    dob_age=array["dob_age"],
    registered_date=array["registered_date"],
    registered_age=array["registered_age"],
    phone=array["phone"],
    cell=array["cell"],
    id_name=array["id_name"],
    id_value=array["id_value"],
    nat=array["nat"],
    time_till_birthday=array["time_till_birthday"]
  )
  # first_person.save()
