#-------------------- Other functions used in the algorithms

# defining the node class
#-------------------------------------------------------------------
class Node:
    def __init__(self, name, val, parent, depth, cost):
        self.name = name
        self.parent = parent
        self.val = 	val 		# arbitrary value for goal condition 
        self.depth = depth
        self.cost = cost
#-------------------------------------------------------------------



# Expand the current node using the node tree defined
#-------------------------------------------------------------------
#-------------------------------------------------------------------
def expand(node_tree, parent_node):

	# Check if node has child nodes
	# -------------------------------------
	n_depth = parent_node.depth
	par_name = parent_node.name

	if par_name in node_tree: 
		expanded = node_tree[par_name]
		expNodes = []
		
		for i in range(len(expanded)):
			curNode = Node(expanded[i][0], expanded[i][1], parent_node, n_depth + 1, expanded[i][2])
			expNodes.append(curNode)

		return expNodes

	# else return an empty list
	# -------------------------------------
	else:
		return []
#-------------------------------------------------------------------


# Setting the priority of the frontier nodes based on an evaluation 
# function 
#-------------------------------------------------------------------
#-------------------------------------------------------------------
def setPrior(frontier):
	return sorted(frontier, key=lambda x: x.cost) # (priority queue)
#-------------------------------------------------------------------