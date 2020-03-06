'''

A Python Program to create an Undirected Graph using Dictionary.
Author: Rohit Kumar Bindal
Data: January 30th, 2020
Time: 15:35:35

'''


import sys

class Undirected_Graph:
    def __init__(self, graph):
        self.graph = graph
        # graph = dict()

    def display_graph(self):
        print(self.graph)
        self.menu()

    def get_menu(self):
        msg = "Would you like to play around a little more?(y/n)"
        print(msg)
        if input()=='y':
            self.menu()
        else:
            sys.exit(0)
    
    def check_node(self, node):
        if node in self.graph:
            return True
        else:
            return False


    def node_exist_msg(self):
        print("Node already exists. Would you like to add a new node?(y/n):")
        inp = input()
        if inp == 'y':
            self.insert_multiple_nodes()
        else:
            self.menu()

    def node_does_not_exists(self):
        print("Node does not exist in graph. Would you like to create a new node?\nType yes or no:")
        inp = input()
        if inp == 'yes':
            self.insert_multiple_nodes()
        elif inp == 'no':
            self.menu()

    def insert_multiple_nodes(self):
        print("Enter all the nodes in the GRAPH:")
        list_of_nodes = []
        list_of_nodes = list(map(int, input().split()))
        for node in list_of_nodes:
            self.insert_node(node)
        self.display_graph()


    def insert_node(self,node):
        # check whether a node exists or not
        if self.check_node(node):
            self.node_exist_msg()
        else:
            # create an empty node with no edges
            self.graph[node] = []

    def check_edge(self, node_1, node_2):
        # returns true if edge exists
        if node_2 in self.graph[node_1]:
            return True
        else:
            return False

    def edge_exist_msg(self):
        print("Edge already exists. Would you like to add a new Edge?(y/n):")
        inp = input()
        if inp == 'y':
            self.insert_edge()
        else:
            self.menu()

    def edge_does_not_exists_msg(self):
        print("Edge does not exist in graph. Would you like to create a new Edge?\nType yes or no:")
        inp = input()
        if inp == 'yes':
            self.insert_edge()
        elif inp == 'no':
            self.menu()

    def insert_edge(self):
        print("Enter the Edge, Node A <--> Node B:\n")
        node_1, node_2 = input().split()
        node_1, node_2 = int(node_1), int(node_2)

        if self.check_edge(node_1, node_2):
            self.edge_exist_msg()
        else:
            if node_1 in self.graph and node_2 in self.graph:
                self.graph[node_1].append(node_2)
                self.graph[node_2].append(node_1)
                self.menu()
            else:
                self.node_does_not_exists()


# function to remove all the entries of node when it is deleted
    def del_edges_of_nodes(self, node):
        for index, value in iter(self.graph.items()):
            if node in value:
                del self.graph[index][value.index(node)]

# delete a node from the graph
    def del_node(self):
        print("Enter the Node to be deleted:\n")
        node = input()
        node = int(node)
        if self.check_node(node):
            del self.graph[node]
            self.del_edges_of_nodes(node)
            self.display_graph()
        else:
            self.node_does_not_exists()

# delete an edge from the graph
    def del_edge(self):
        print("Enter the Edge to be deleted, Node A <--> Node B:\n")
        node_1, node_2 = input().split()
        node_1, node_2 = int(node_1), int(node_2)
        if self.check_edge(node_1,node_2):
            value_node_1 = self.graph[node_1].index(node_2)
            del self.graph[node_1][value_node_1]
            value_node_2 = self.graph[node_2].index(node_1)
            del self.graph[node_2][value_node_2]
            self.display_graph()
        else:
            self.edge_does_not_exists_msg()


    def getdfs(self, node, visited_nodes):
        if node not in visited_nodes:
            print(node)
            visited_nodes.append(node)
            for adjacent_node in self.graph[node]:
                self.getdfs(adjacent_node, visited_nodes)

    def perform_depth_first_search(self):
        visited_nodes = []
        print("Enter the Starting Node:")
        node = input()
        node = int(node)
        self.getdfs(node, visited_nodes)
        self.get_menu()
        

    def breadth_first_search(self):
        queue_ = []
        visited_nodes = []
        bfs = []
        print("Enter the starting Node:")
        node = input()
        node = int(node)
        queue_.append(node)
        visited_nodes.append(node)
        while queue_:
            current_node = queue_.pop(0)
            bfs.append(current_node)
            for adjacent_node in self.graph[current_node]:
                if adjacent_node not in visited_nodes:
                    queue_.append(adjacent_node)
                    visited_nodes.append(adjacent_node)
        print(bfs)
        self.get_menu()

    def menu(self):
        print(
            "Select an option:\n",
            "1. Insert a New Node\n",
            "2. Insert an Edge\n",
            "3. Delete a Node\n",
            "4. Delete an Edge\n",
            "5. Perform Depth First Search\n",
            "6. Perform Breadth First Search\n",
            "7. Display the Graph\n",
            "8. Exit\n"
        )
        user_input = input()
        if user_input == '8':
            sys.exit()
        if user_input=='1':
            self.insert_multiple_nodes()
        if user_input=='2':
            self.insert_edge()
        if user_input=='3':
            self.del_node()
        if user_input=='4':
            self.del_edge()
        if user_input=='6':
            self.breadth_first_search()
        if user_input=='5':
            self.perform_depth_first_search()
        if user_input=='7':
            self.display_graph()

if __name__ == "__main__":
    graph = dict()
    obj = Undirected_Graph(graph)
    obj.menu()