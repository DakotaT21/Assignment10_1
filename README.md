# Assignment10_1
The program allows the user to make either an action movie object or a biographical movie object and make a list of their titles and descriptions for easy movie night planning, instead of writing them down on boring paper- plus two bonus methods. 

Action - 
Takes in the title, the protagonist, the antagonist, the movies location, and its runtime
Printing the object gives a sentence descriptor using this information
The bonus method is called spoil_the_plot 

Biography -
Takes in the title, the person, the location, the time period, and the runtime
Printing the object gives a sentence descriptor using this information
The bonus method is called present_day\

Variables
movies - A list to add movie objects, outside of classes

identifier - The title of the movie, in the parent class
location - The location of the movie, in the parent class
runtime - The runtime of the movie, in the parent class

movie_type - Saves what class the object is made from, set in Action and Biography each

protagonist - The protagonist of the movie, set in the Action child class
antagonist - The antagonist of the movie, set in the Action child class

person - The main character in the movie, set in the Biography child class
time_period - The time period the movie takes place in, set in the Biography child class

Movie Class Methods
Print_list - Takes in a list - Prints “Movie List” and a new line, then iterates through the list and prints each
Set_title - String movie title - Takes in a new title to replace the current title in a movie object
Get_title - No input - Returns the current title of the movie object called on
Set_runtime - Int value in minutes for movie length - Takes in a new runtime to replace the current runtime in a movie object
Get_runtime - No input - Returns the current runtime of the movie object called on
Set_location - String location of movie - Takes in a new location to replace the current location in a movie object 
Get_location - Not input - Returns the current location of the movie object called on
Add_to_list - No input - Adds the movie object called on to the “movies” list\
Remove_from_list - No input - Removes the movie object called on from the “movies” list

Action Class Methods
Set_prot - String name of protagonist character - Takes in a new protagonist to replace the current protagonist in the movie objet called on
Get_prot - Not input - Returns the current protagonist of the movie object called on
Set_ant - String name of antagonist character - Takes in a new antagonist to replace the current antagonist in the movie objet called on
Get_ant - Not input - Returns the current antagonist of the movie object called on
Spoil_the_plot - No input - Prints a funny message about the state of the protagonist
__str__ - Takes the movie type, uses the get methods for the title, the protagonist, the antagonist, the location, and the runtime and prints out a message with those variables

Biography Class Methods
Set_person - String name of person in biography - Takes in a new person to replace the current person in the movie object called on
Get_person - Not input - Returns the current person of the movie object called on
Set_ time - Int value for the movie time period - Takes in a new time period to replace the current time period in the movie object called on
Get_time - Not input - Returns the current time period of the movie object called on
Present_day - No input - Prints a message based on if the time period is set to before or equal to 1903, or after 1903
__str__ - Takes the movie type, uses the get methods for the title, the person, the location, the time period, and the runtime and prints out a message with those variables

Demo program:
My demo program 
Creates an ActionMovie object labeled John_Wick and passes in the key plot elements, then adds it to the watch list
Creates a BiographyMovie object labeled Lincoln and passes in the key plot elements, then adds it to the watchlist
Prints the watchlist
Calls John_Wick.spoil_the_plot()
Calls Lincoln.present_day()

A new user can create any number of their own action or biography movie objects, add them to their list, print the list, as well as removing the movie objects when they are finished watching it and wish to remove it from the list, or want to change the variables in the objects with the setter methods
