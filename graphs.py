
###** NOTES **###

# BFS = queue - pop(0)
# DFS = stack - pop()

# inorder, preorder, postorder traversals - DFS algorithm
# BFS is algorithm, not traversal - uses vertical or level order traversal
# “Breadth-first search USES level-order traversal”


###** practice: create node and graph classes, search class**###

from queue import Queue

class PersonNode():
    """Node in a graph representing a person."""

    def __init__(self, name, adjacent=None):
        """Create a person node with friends adjacent"""

        if adjacent is None:
            adjacent = set()

        assert isinstance(adjacent, set), \
            "adjacent must be a set!"

        self.name = name
        self.adjacent = adjacent

    def __repr__(self):
        """Debugging-friendly representation"""

        return f"<PersonNode: {self.name}>"


class FriendGraph():
    """Graph holding people and their friendships."""

    def __init__(self):
        """Create an empty graph"""

        self.nodes = set()

    def __repr__(self):
        return f"<FriendGraph: { {n.name for n in self.nodes} }>"

    def add_person(self, person):
        """Add a person to our graph"""

        self.nodes.add(person)

    def set_friends(self, person1, person2):
        """Set two people as friends"""

        person1.adjacent.add(person2)
        person2.adjacent.add(person1)


cori = PersonNode('cori')
brittney = PersonNode('brittney')
scott = PersonNode('scott')
friends = FriendGraph()
friends.add_person(cori)
friends.add_person(brittney)
friends.add_person(scott)
friends.set_friends(cori, brittney)

class FriendSearch():
    def are_connected(self, person1, person2):
        """Are two people connected? Breadth-first search."""

        possible_nodes = Queue()
        seen = set()
        possible_nodes.put(person1) # add p1 to queue
        seen.add(person1) # add p1 to seen set

        while not possible_nodes.empty(): # while we still have a queue to check
            person = possible_nodes.get() # remove and return next up from queue
            print("checking", person)
            if person is person2: # if person from queue is who we're looking for
                return True
            else: # if person from queue is NOT who we're looking for
                for friend in person.adjacent - seen: # for each person who is friends with our person from queue - EXCEPT those we've already seen
                    possible_nodes.put(friend) # add them to queue
                    seen.add(friend) #add them to seen
                    print("added to queue:", friend)
        return False

bfs = FriendSearch()
# bfs.are_connected(brittney, cori)
# bfs.are_connected(brittney, scott)