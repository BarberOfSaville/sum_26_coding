#Brian Saville
#May 26, 2026
#Working through Ch6: Dictionaries in Python Crash Course

#A simple dictionary
#keys and their associated values
alien_0 = {"color" : "green", "points" : 5}
print(alien_0["color"])
print(alien_0["points"])

#ex: look up how many points a player should get
new_points = alien_0["points"]
print("You just eanred " + str(new_points) + " points!")

#adding new key-value pairs to a dictionary
print(alien_0)
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

#You can also start with an empty dictionary and populate it
alien_0 = {}
alien_0["color"] = "green"
alien_0["points"] = 5
print(alien_0)

#modifying values in a dictionary
alien_0["color"] = "yellow"
print("The alien is now " + alien_0["color"] + ".")

#removing key-value pairs
del alien_0["points"]

#Dictionary of Similar Objects
favorite_languages = {
    "brian": "python",
    "annika" : "c", 
    "angelica" : "matlab",
    "obi" : "python",
}

print("Obi's favorite language is " + 
      favorite_languages["obi"].title()+ 
      ".")
favorite_languages["angelica"]

#TRY IT YOURSELF
#6-1: Person
annika = {"first_name" : "Annika", "last_name" : "Rudolph",
           "age" : 23, "city" : "Manhattan"}
print("Her first name is " + annika["first_name"] + ".")
print("Her last name is " + annika["last_name"] + ".")
print("She is " + str(annika["age"]) + " years of age.")
print("She lives in " + annika["city"] + ".")

#6-2: Favorite Numbers
fav_numbers = {"brian" : 39, "annika" : 12, "peeks" : 67, 
               "sam" : 30, "mom" : 61}
#print everybody's favorite numbers
print("Brian's favorite number is " + str(fav_numbers["brian"]) + ".")
print("Annika's favorite number is " + str(fav_numbers["annika"]) + ".")
print("Peeks's favorite number is " + str(fav_numbers["peeks"]) + ".")
print("Sam's favorite number is " + str(fav_numbers["sam"]) + ".")
print("Mom's favorite number is " + str(fav_numbers["mom"]) + ".")

#6-3: Glossary
glossary = {"append" : "add to the end of a list",
            "dictionary" : "like a list to store multiple associated values",
            "commit" : "new iteration of a repository",
            "elif" : "portmentaeu of else and if, which describes it well",
            "git" : "version history of your repository"}
#print the definitions
print("Append: " + glossary["append"])
print("Dictionary: " + glossary["dictionary"])
print("Commit: " + glossary["commit"])
print("elif: " + glossary["elif"])
print("Git: " + glossary["git"])


#Looping through a dictionary
user_0 = {
    "username" : "btsavi",
    "first" : "brian",
    "middle" : "thomas",
    "last" : "saville",
}

#looping through keys and values in a dictionary:
for key, value in user_0.items():
    print("Key: " + key)
    print("Value: " + value)

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")
    
#loop through all keys (note that it's .keys, not .items)
for name in favorite_languages.keys(): 
    print(name.title())

#this is the default method when looping through a dictionary
#keys() just makes your code easier to read
for name in favorite_languages:
    print(name)

#looping through dictionary looking for certain keys
friends = ["angelica", "obi"]
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("Hi " + name.title() + 
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!!")
        
if "erin" not in favorite_languages.keys():
    print("Erin, please take our poll!")

#looping through a dictionary's keys in order
#can use the sorted() function toward this end
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", we appreciate you taking the poll.")

#looping through all the values in a dictionary
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

#want to avoid repeats? Use a SET
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())