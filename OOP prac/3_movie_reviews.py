class Movie:
    def __init__(self, movie):
        self.movie = movie
        self.ratings = []
    def add_rating(self, score):
        self.ratings.append(score)
    def average_rating(self):
        avg = sum(self.ratings) / len(self.ratings)
        return f"{avg:.2f}"
    def is_good(self):
        return sum(self.ratings) / len(self.ratings) > 7
        
        
def main():
    movie = Movie(input("Enter the name of the movie: "))
    
    get_ratings(movie)
    results(movie)
    
    
def get_ratings(movie):
    while True:
        score = input("\nEnter score from 1-10 (type 'done' when finished):\n")
        if score == "done":
            break
        try:
            score = int(score)
            if score in range(1,11):
                movie.add_rating(score)
            else:
                print("Score must be 1-10.")
        
        except ValueError:
            print("Must enter a number 1-10.")
            
            
def results(movie):
    print(f"\n'{movie.movie}'\n\nAverage rating: {movie.average_rating()}\n")
    if movie.is_good():
        print("This movie is good!")
    else:
        print("This movie is not so good.")
    
    
if __name__ == "__main__":
    main()
