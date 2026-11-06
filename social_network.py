class Person:
    def __init__(self, name):
        self.name = name
        self.friends = [] # List of Person objects

    def add_friend(self,friend):
        # Prevents duplicate friendships
        if friend not in self.friends:
            self.friends.append(friend)

class SocialNetwork:
    def __init__(self):
        self.people = {} # Dictionary of names and Person objects

    def add_person(self, name):
        # Adds a new person to the network
        if name not in self.people:
            self.people[name] = Person(name)

        else:
            print(f"{name} already exists in the network!")

    def add_friendship(self, person1_name, person2_name):
        # Adds a bidirectional friendship between two people
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} does not exist!")
            return

        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} does not exist!")
            return

        # Fetrieve Person objects from the dictionary
        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        # Add each person to the other's friends list
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        # Loops through each person in the network
        for person_name, person_obj in self.people.items():
            # Creates a list of each person's friends' names
            friend_names = [f.name for f in person_obj.friends]

            # Joins the names with a comma
            connected_friends = ", ".join(friend_names)

            print(f"{person_name} is friends with: {connected_friends}")


# Test your code here
network = SocialNetwork()

# Add people
network.add_person("Alex")
network.add_person("Jordan") 
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")
network.add_person("Alex")

# Create friendships
network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Jordan", "Johnny")
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

network.print_network()

# Design Memo

# Graphs work great for constructing social networks. An adjacency list, like we used in this assignment, allows 
# for each person (node) to have connections/friendships with multiple other people (edges). We were also able to 
# make the connections bidirectional, meaning when Alex becomes friends with Riley, Riley automatically becomes 
# friends with Alex. While adjacency lists work great for networks with relatively few connections per node, an a
# djacency matrix would be better suited for a network where most nodes connect with most other nodes. 

# Lists and trees would be poor options for a social network. Lists preserve order, which is functionally irrelevant 
# here, and a simple list doesn’t inherently represent relationships between different items. While a tree’s structure 
# shows relationships, they are hierarchical, like you would expect in a manager/subordinate relationship. This wouldn’t 
# make sense in a social network setting, and would also limit the diversity of connections that a graph does allow.

# When adding friendships, using a dictionary makes finding a person by name very efficient. However, the add_friend() 
# method checks the existing friends list before adding a new connection, which becomes slower as that list grows. Also, 
# because friendships are bidirectional, each new connection requires updating two separate lists. Printing the network 
# also becomes more time-consuming as it grows, since the program must loop through every person and their friends. For a 
# relatively small network like this, these trade-offs are insignificant, but they could become more noticeable in a much 
# larger social network.
