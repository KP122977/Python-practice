# Create a class to represent a Movie with attributes like title, director, and rating.

class Movie :
    def __init__(self,title,director,rating):
        self.title=title
        self.director=director
        self.rating=rating
        
    def show(self):
        return f"Movie  : {self.title} , director : {self.director}, ratings : {self.rating}"
    
try :
    title=input("enter title of the movie : ")
    director=input("enter name of the director : ")
    ratings=float(input('enter the rating movie got :  '))
    
    movie_details=Movie(title,director,ratings)
    print(movie_details.show())
    
    
except ValueError as e:
    print(e)