# Start

oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", "Natalie Portman",
                 "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo", "Chris Hemsworth",
                   "Jeremy Renner"}
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}

# a
oscar_winners.add("Emma Watson")

# b
oscar_winners_copy = oscar_winners.copy()
oscar_winners_copy.discard("Meryl Streep")
oscar_winners_copy.clear()

# c
common_titanic_darkknight = titanic_actors.intersection(dark_knight_actors)
if titanic_actors.isdisjoint(dark_knight_actors):
    print("No actors played in Dark Knight and in Titanic.")
else:
    print(f"The actors that played in Dark Knight and in Titanic are:", titanic_actors.intersection(dark_knight_actors))

# d
if iron_man_actors.isdisjoint(avengers_actors):
    print("No actors played in Iron Man and in The Avengers.")
else:
    print(f"The actors that played in Iron Man and in The Avengers are:", iron_man_actors.intersection(avengers_actors))

# e
if actor_list.issubset(oscar_winners):
    print("All the actors in actor_list won an oscar.")
else:
    print(f"Only {actor_list & oscar_winners} won an oscar.")

# f
if actor_list.issubset(avengers_actors):
    print("All the actors in The Avengers are in actor_list")
else:
    print("Not all the actors in The Avengers are in actor_lis")

# g
movie_cast.pop()

# h
movie_cast.remove("Matt Damon")
print(movie_cast)

# i
print(f"The actors that played in the Titanic and haven't won an oscar are:", titanic_actors - oscar_winners)

# j
print(f"The actors that played either on The Dark Knight or The Titanic are: {dark_knight_actors ^ titanic_actors}")

# k
oscar_winners.update(["Cate Blanchett", "Daniel Day-Lewis"])
print(oscar_winners)

# l
print(dark_knight_actors|titanic_actors)

# Stop