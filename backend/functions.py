import click
from collections import Counter
from database import Person

@click.group(chain = True)
def main():
    pass

@main.command()
@click.option('--gender', help='Male or female gender ratio to show.')
def gender_ratio(gender):
  n_female = Person.select().where(Person.gender == "female").count()
  n_male = Person.select().where(Person.gender == "male").count()
  if gender == "male":
    ratio = round(n_male / n_female, 2)
    print("Male to female ratio: ", ratio)
  elif gender == "female":
    ratio = round(n_female / n_male, 2)
    print("Female to male ratio: ", ratio)
  else:
    print("Wrong option")


@main.command()
@click.option('--gender', help='Male, female or overall age to show.')
def get_average_age(gender):
  result = []
  for person in Person:
    result.append(person.dob_age)
  results_int = list(map(int, result))
  query_female = Person.select().where(Person.gender == 'female')
  result_female = []
  for person in query_female:
    result_female.append(person.dob_age)
  results_female_int = list(map(int, result_female))
  query_male = Person.select().where(Person.gender == 'male')
  result_male = []
  for person in query_male:
    result_male.append(person.dob_age)
  results_male_int = list(map(int, result_male))
  if gender == "male":
    print(round(sum(results_male_int) / len(results_male_int)),",",2)
  elif gender == "female":
    print(round(sum(results_female_int) / len(results_female_int)),",",2)
  elif gender == "overall":
    print(round(sum(results_int) / len(results_int)),",",2)
  else:
    print("Wrong option")

@main.command()
@click.option('--amount',help='amount of most popular cities you want to show ', type=int)
def most_popular_cities(amount):
  result = []
  for person in Person:
    result.append(person.location_city)
    most_common = Counter(result).most_common(amount)
  print(most_common)

@main.command()
@click.option('--amount',help='amount of most popular passwords you want to show ', type=int)
def most_popular_password(amount):
  result = []
  for person in Person:
    result.append(person.login_password)
    most_common = Counter(result).most_common(amount)
  print(most_common)

@main.command()
@click.option('--minimal_date',help='enter a minimal date to show the range of users dob')
@click.option('--maximal_date',help='enter a maximal date to show the range of users dob')
def users_dob_specific_range(minimal_date,maximal_date):
  result = []
  for person in Person:
    result.append(person.dob_date[:10] + " " + person.login_username)
  sorted_results = sorted(result)
  minimal_date = input('Enter a lower of dates in YYYY-MM-DD format: ')
  maximal_date = input('Enter a higher of dates in YYYY-MM-DD format: ')
  for date_of_birth in sorted_results:
    if date_of_birth >= minimal_date and date_of_birth <= maximal_date:
      print (date_of_birth)

@main.command()
def password_checker():

  users_paswords = []
  for password in Person:
    users_paswords.append(password.login_password)
  for single_password in users_paswords:
    password_points = 0

    if (len(single_password) >= 8):
      password_points += 5
    if any(char.isupper() for char in single_password):
      password_points += 2
    if any(char.islower() for char in single_password):
      password_points += 1
    if any(char.isdigit() for char in single_password):
      password_points += 1
    if any(not c.isalnum() for c in single_password):
      password_points += 3

    print(single_password, " ", password_points)







if __name__ == '__main__':
  main()