#Brian Saville
#June 15, 2026
#Working on the Ch. 9 exercises on importing classes.

#9-10: Imported Restaurant
from restaurant import Restaurant

dutch_baby = Restaurant("Dutch Baby", "diner")

dutch_baby.describe_restaurant()

dutch_baby.open_restaurant()

dutch_baby.set_number_served(28)
print(dutch_baby.number_served)

dutch_baby.increment_number_served(39)
print(dutch_baby.number_served)


#9-11: Imported Admin
from user import User, Admin, Privileges

peeks = Admin("MAtthew", "peeks", "25", "male", "Sherlock gnomes")
peeks.privileges.give_privileges(["ban users", "can delete posts", "can legally kill users"])
peeks.privileges.show_privileges()


#9-12: multiple modules
from user import User
from admin import Admin, Privileges

peeks = Admin("MAtthew", "peeks", "25", "male", "Sherlock gnomes")
peeks.privileges.give_privileges(["ban users", "can delete posts", "can legally kill users"])
peeks.privileges.show_privileges()
