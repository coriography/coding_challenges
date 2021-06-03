# **** Linked Lists practice **** #

# class Node():
#     """creates a Node class."""

#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList():
#     """creates a Singly-Linked List class."""

#     def __init__(self):
#         self.head = None

#     def list_print(self):
#         """prints list of all nodes' data."""

#         current = self.head

#         while current:
#             print(current.data)
#             current = current.next

#     def insert_head(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node

#     def insert_tail(self, new_data):
#         new_node = Node(new_data)
#         current = self.head

#         while current.next:
#             current = current.next
        
#         current.next = new_node
#         new_node.next = None

#     def insert_after(self, p_data, new_data):
#         new_node = Node(new_data)
#         current = self.head

#         while current:
#             if current.data == p_data:
#                 new_node.next = current.next
#                 current.next = new_node
#                 return catlist.list_print()
#             else:
#                 current = current.next

#     def remove_node(self, remove_data):
#         prev = None
#         current = self.head

#         while current:
#             if current.data == remove_data:
#                 if prev:
#                     prev.next = current.next
#                 else:
#                     self.head = current.next
#                 return print("removed data")

#             prev = current
#             current = current.next

#         return print("data not in list")
            

# node1 = Node('Tuna')
# node2 = Node('Guppy')
# node3 = Node('Loja')
# catlist = LinkedList()
# catlist.head = node1
# catlist.head.next = node2
# node2.next = node3
# catlist.insert_head('Catsper')
# catlist.insert_tail('Sammy')
# catlist.insert_after('Tuna', 'Turner')