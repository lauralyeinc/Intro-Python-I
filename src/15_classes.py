# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def _init_(self, lat=0, lon=0):
        self.lat = lat
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def _init_(self, name, lat=0, lon=0):
        super()._init_(lat, lon)
        self.name = name



# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def _init_(self, name, difficulty, size, lat=0, lon=0):
        super()._init_(name, lat, lon)
        self.difficulty = difficulty
        self.size = size 
    def _str_(self):
        return f"<Geocache '{self.name}', {self.difficulty}, {self.size}, {self.lat},{self.lon} "

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
# YOUR CODE HERE
# w = Waypoint("Catacombs", 41.70505, -121.515221)

'''
line 37, in <module>
    w = Waypoint("Catacombs", 41.70505, -121.515221)
TypeError: Waypoint() takes no arguments
'''

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
# print(w)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
g = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(g)
