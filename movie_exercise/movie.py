class Movie:
    def __init__(self,name,genre,watched):
        self.name=name
        self.genre=genre
        self.watched=watched

    def __repr__(self):
        return "movie name {}".format(self.name)