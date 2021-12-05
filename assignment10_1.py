"""
Dakota Tompkins
10.1: Your Own Class

The program allows the user to make either an action movie object or a biographical movie object 
and make a list of their titles and descriptions for easy movie night planning, instead of writing 
them down on boring paper- plus two bonus methods

Action - 
Takes in the title, the protagonist, the antagonist, the movies location, and its runtime
Printing the object gives a sentence descriptor using this information
The bonus method is called spoil_the_plot 

Biography -
Takes in the title, the person, the location, the time period, and the runtime
Printing the object gives a sentence descriptor using this information
The bonus method is called present_day

"""
movies = []

def print_list(movie_list):
    #Prints list title
    print("Movie List:\n")
    #Prints each movie in the list
    for f in movie_list:
            #Print the 
            print(f"{f}\n")

class Movie():
    movie_type = "N/A"
    #Takes in the title, location, and runtime that all child classes will use
    def __init__(self, identifier, location, runtime):
        self.__identifier = identifier
        self.__runtime = runtime
        self.__location = location
    
    #The methods to get and set the title
    def set_title(self, title):
        self.__identifier = title

    def get_title(self):
        return self.__identifier

    #The methods to get and set the runtime
    def set_runtime(self, time):
        self.__runtime = time

    def get_runtime(self):
        return (self.__runtime)

    #The methods to get and set the location
    def set_location(self, location):
        self.__location = location

    def get_location(self):
        return (self.__location)

    #Adds the movie to your watchlist
    def add_to_list(self):
        movies.append(self)

    #Removes the movie from your watchlist
    def remove_from_list(self):
        movies.remove(self)



class ActionMovie(Movie):
    movie_type = "Action"
    def __init__(self, identifier, protagonist, antagonist, location, runtime):
        super().__init__(identifier, location, runtime)
        self._protagonist = protagonist
        self._antagonist = antagonist

    #The methods to get and set the protagonist
    def set_prot(self, char):
        self._protagonist = char

    def get_prot(self):
        return self._protagonist

    #The methods to get and set the antagonist
    def set_ant(self, char):
        self._antagonist = char

    def get_ant(self):
        return self._antagonist

    #Prints a fun message spoiling the end of the movie
    def spoil_the_plot(self):
        print (f"{self.get_prot()} definitely dies at the end \nJust Kidding!\n\n\n ...or am I?")

    #When printing the object this will be used, printing the title, the objects (movies) type, and its information
    def __str__(self):
        return f"{self.movie_type} - {self.get_title()}: Pits {self.get_prot()} against {self.get_ant()} in {self.get_location()} for the runtime of {self.get_runtime()} minutes"

class BiographyMovie(Movie):
    movie_type = "Biography"
    def __init__(self, identifier, person, location, time_period, runtime):
        super().__init__(identifier, location, runtime)
        self._person = person
        self._time = time_period

    #The methods to get and set the person
    def set_person(self, newper):
        self._person = newper

    def get_person(self):
        return self._person

    #The methods to get and set the timeperiod
    def set_time(self, newtime):
        self._time = newtime

    def get_time(self):
        return self._time

    #Prints a message on the main character based on the timeperiod the movie is set in, either when the oldest woman alive was born (1903) or after
    def present_day(self):
        if int(self.get_time()) <= 1903:
            print(f"{self.get_person()} is most likely (unless they are the oldest human alive, are definitely) dead! Sorry!\n")
        else:
            print(f"We cannot comment on the current health of {self.get_person()}\n")

    #When printing the object this will be used, printing the title, the objects (movies) type, and its information
    def __str__(self):
        return f"{self.movie_type} - {self.get_title()}: Focuses on the life of {self.get_person()} set in {self.get_location()}, {self.get_time()}  for the runtime of {self.get_runtime()} minutes"


def main():
    #Makes an ActionMovie object labeled John_Wick and passes in the key plot elements
    John_Wick = ActionMovie("John Wick", "John Wick", "The Russian Mafia", "New York City", 101)
    #Adds the movie to my watchlist
    John_Wick.add_to_list()

    #Makes a BiographyMovie object labeled Lincoln and passes in the key plot elements
    Lincoln = BiographyMovie("Lincoln", "Abraham Linclon", "The United States", 1865, 150)
    #Adds the movie to my watchlist
    Lincoln.add_to_list()
    
    #Prints the movie descriptions
    print_list(movies)

    #Calls the ActionMovie method
    John_Wick.spoil_the_plot()
    #Calls the BiographyMovie method
    Lincoln.present_day()

if __name__== "__main__":
    main() 
    
