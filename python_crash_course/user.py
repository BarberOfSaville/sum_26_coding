#Brian Saville
#June 15, 2026
#Copy of the user class
#for practicing importing modules.

#User class
class User():
    """A simple simulation of a user of a site."""
    
    def __init__(self, first_name, last_name, age, sex, fav_movie):
        """Initialize attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.fav_movie = fav_movie
        self.login_attempts = 0

    def describe_user(self):
        """Prints a summary of the user's information."""
        print("NAME: " + self.first_name.title() + " " + 
              self.last_name.title())
        print("AGE: " + str(self.age))
        print("SEX: " + self.sex)
        print("FAVORITE FILM: " + self.fav_movie.title())

    def greet_user(self):
        """Prints a greeting to an inputted user."""
        print("Top o' the mornin', " + self.first_name.title() + 
              " " + self.last_name.title() + "!!!")
        
    def increment_login_attempts(self):
        """Increases the number of login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets a user's login attempts to 0."""
        self.login_attempts = 0


