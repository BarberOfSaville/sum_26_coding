#Brian Saville
#June 15, 2026
#Copy of the  admin and privilege classes
#for practicing importing modules.

from user import User

#Admin class
class Admin(User):
    """Represents an admin, which is a special kind of user."""
    def __init__(self, first_name, last_name, age, sex, fav_movie):
        super().__init__(first_name, last_name, age, sex, fav_movie)
        self.privileges = Privileges()


#Privilege class
class Privileges():
    """List of abilities given to an admin."""
    def __init__(self):
        self.privileges = []

    def give_privileges(self, new_privileges):
        """Grants an admin new privileges."""
        for new_privilege in new_privileges:
            self.privileges.append(new_privilege)

    def show_privileges(self):
        """Prints a list of privileges an admin has."""
        print("This admin has the following privileges:")
        for item in self.privileges:
            print(" -" + item)

    def reset_privileges(self):
        """Takes away an admin's privileges."""
        self.privileges = []
        print("Privileges have been reset.")