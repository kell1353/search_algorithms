import other_funcs as f
from other_funcs import Node 

import numpy as np 
import math as m
import sys 

# UNINFROMED SEARCH METHODS (some)

# Best-first Search (Time complexity: O(nlogn))
# ===============================================================================
	# root
	# expand initial root
	# order the expansion via lowest cost from parent node and exapand in order
		# check if expansions are the end
			# if they haven't been reached add them to list
	# repeat until the state is found
	# retrace steps to find path and cost
# ===============================================================================
# ===============================================================================
def best_fs(node_tree, start, end):

	# define two empty lists
	#------------------------------------
	openList, closedList = [], []
	#------------------------------------

	# append the root node to both lists
	#------------------------------------
	# root = pathNode(start, None, 0)
	root = Node(start, None, None, 0, None)

	openList.append(root) # frontier (states to be expanded)
	closedList.append(start) # reached states 
	#------------------------------------

	while(len(openList) > 0):
		openList_tmp = []

		for i in range(len(openList)): 

			# Expand the current frontier node
			#------------------------------------
			cur = openList[i]
			# exp = expand(node_tree, cur.node)
			exp = f.expand(node_tree, cur)
			#------------------------------------

			for child in exp: 

				# if child node is our end than retrace
				# from the current node to each 
				# successive parent node backward
				#------------------------------------
				if (child.name == end): 
					# print('f')
					path = []

					while (cur != None):
						path.append(cur.name)
						cur = cur.parent

					path.reverse() 		# reverse path
					path.append(end) 	# append the end node

					print('')
					print('Best-first Search Example')
					print('--------------------------')
					print(path)
					return path
				#------------------------------------

				# if not check if the child node has been 
				# reached alreaady. if not add it to frontier list
				#------------------------------------
				elif (child.name not in closedList): 
					closedList.append(child.name)
					# openList_tmp.append(pathNode(child.name, cur, child.cost))
					openList_tmp.append(child)
				#------------------------------------

		# order the new frontier nodes based on evaluation function (priority queue)
		#------------------------------------
		openList = f.setPrior(openList_tmp)
		#------------------------------------

	# Return an empty list if no path exists
	return []
#-------------------------------------------------------------------
# ===============================================================================
# ===============================================================================





# Breadth-first Search (Time and Memory complexity: 1 + b + b^2 + ... + b^d = O(b^d))
	# if each successive node generates the same number of nodes, b. d = depth of tree
# ===============================================================================
	# Useful when all actions have the same cost
	# Used to search for a node in a decision tree that satisfies a condition
	# In this example I am trying to find a node that has a value below a threshold

	# root
	# expand initial root
	# exapand in order of first in first out
		# check if the node has the properties we want
			# if they haven't been reached add them to list
	# repeat until the state is found

# ===============================================================================
# ===============================================================================
def breadth_fs(node_tree, start, goal):

	# define two empty lists
	#------------------------------------
	openList, closedList = [], []
	#------------------------------------

	# append the root node to both lists
	#------------------------------------
	root = Node(start, None, None, 0, None)

	openList.append(root) # frontier (states to be expanded)
	closedList.append(start) # reached states
	#------------------------------------

	while(len(openList) > 0):
		openList_tmp = []

		for i in range(len(openList)): 

			# Expand the current frontier node
			#------------------------------------
			cur = openList[i]
			exp = f.expand(node_tree, cur)
			#------------------------------------

			if len(exp) == 0: 
				continue
			else: 
				for child in exp: 

					# if child node satisfies the goal
					# return the current node.
					# here the goal condition is if the node 
					# value is less then the goal
					#------------------------------------
					if (child.val < goal):

						print('')
						print('Breadth-first Search Example')
						print('--------------------------')
						print('Satisfactory Node : ', child.name)
						print('Value             : ', child.val)
						return [child.name, child.val]
					#------------------------------------

					# if not check if the child node has been 
					# reached alreaady. if not add it to frontier list 
					# this creates a first in first out queue (FIFO)
					#------------------------------------
					elif (child.name not in closedList): 
						closedList.append(child.name)
						openList_tmp.append(child)
					#------------------------------------

		openList = openList_tmp


	# Return an empty list if no node exists
	print('No node satisfies the goal...')

# ===============================================================================
# ===============================================================================





# Depth first Limited Search (Time complexity: )  
# ===============================================================================
	# We exapand the deepest node of each successive child state 
	# - checking if we reached the goal each step
	# - once it hits the end of the space, it begins the same process for each 
	# - unexpanded successor. Eventually travelling the whole space
	# - returns first solution irregardless of cost

	# Useful and efficient for finite acyclic state spaces. Saves on memory,
	# since we aren't keeping track of reached nodes.
		# In infinite spaces it is not complete and can get stuck down an infinite 
		# or in an infinite loop. Can run visit the same state multiple times.

	# Here is a common variation of the depth first search where we implement an
	# depth limit, l, which can be chosen based on the knowledge of the problem.
		# We can also introduce iterative deeping where we try multiple 
		# depth limits until a solution is found or it fails
# ===============================================================================
# ===============================================================================

# ---------------------------------------------------------
# ---------------------------------------------------------
def iter_deepening(node_tree, start, goal, l): # max nodal depth

	print('')
	print('Depth-first Search Example')
	print('--------------------------')

	for depth in range(0, l): 
		print('Trial Node Depth: ', depth)
		result = depth_ls(node_tree, start, goal, depth)

		if result != depth: 
			print('')
			print('Satisfactory Node : ', result)
			return result

	if result == l-1: 
		print('')
		print('No node satisfies by setting the maximum nodal depth of ' + str(l-1) + '...')
		return result

	# Return an empty list if no node exists
	return []
	print('No node satisfies the goal...')
# ---------------------------------------------------------


def depth_ls(node_tree, start, goal, l):

	# define two empty lists
	#------------------------------------
	openList = []
	#------------------------------------

	notCycle = True # function to determine if the expansion is caught in a cycle
	depth = 0

	# append the root node to both lists
	#------------------------------------
	root = Node(start, 0, None, 0, None)

	openList.append(root) # frontier (states to be expanded)
	#------------------------------------

	while(len(openList) > 0):

		# Set the current node using a LIFO (last in first out) queue
		#------------------------------------
		cur = openList[-1]

		# Removing the current node from frontier
		openList.pop(-1)
		#------------------------------------

		# if node satisfies the goal return the current node.
		#------------------------------------
		if (cur.val == goal): return cur.name
		#------------------------------------

		# if the node is too deep don't expand
		#------------------------------------
		elif (cur.depth >= l): result = l
		#------------------------------------

		# else expand the node 
		else: 
			exp = f.expand(node_tree, cur)
		#------------------------------------

			if len(exp) == 0: 
				continue

			else: 
				for child in exp: 

					# check if we are in a cycle if not add it to frontier list 
					#------------------------------------
					if (notCycle): openList.append(child)
					#------------------------------------

		# print('')
		# print('=======================')
		# for i in openList: print(i.name)

	return result

# ===============================================================================
# ===============================================================================






