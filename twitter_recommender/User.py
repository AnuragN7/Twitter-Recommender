import networkx as nx
import matplotlib.pyplot as plt
import utils 

class User:

	def __init__(self, screen_name):
		""" Instantiates a User object 
		
		
		Args: 

		screen_name: The twitter handle that represents the twitter object 
		"""
		self.screen_name = screen_name
		self.similar_users = utils.get_similar_users(screen_name)

	def get_screen_name(self):
		return self.screen_name	
	
	def get_similar_users(self):
		return self.similar_users

	def display_related_users(self):
		person_lst = self.get_similar_users()
		print("Printing similar users: ")
		for person in person_lst:
			print("Name: " + person.name)
			print("Score: " + str(person.sim_score))	

	def build_graph(self):
		# Build the recommender graph for a specific user
		target_user = self.get_screen_name()
		similar_users = self.get_similar_users()
		graph = nx.Graph() # Create the graph
		graph.add_node(target_user)
		edge_list = [(target_user, person.name, person.sim_score) for person in similar_users]
		graph.add_weighted_edges_from(edge_list) # add the weighted edges
		plt.subplot(121)
		nx.draw(graph)

	
		
		
		
