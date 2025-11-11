class Genealogy:
    """The genealogy and succession order for Envoy of the Kiktil."""

    def __init__(self, originator_name):
        # First we start with the Originator — the very first member of the family tree
        self.originator = originator_name
        self.children = {originator_name: []} # stores each person's children
        self.parent = {originator_name: None} # stores each person's parent

    def add_child(self, parent_name, child_name):
        # Add a new child under the given parent
        self.children[parent_name].append(child_name)
        self.children[child_name] = [] # Initialize child’s empty children list
        self.parent[child_name] = parent_name

    def get_primogeniture_order(self):
        # Returns list of names in primogeniture order (oldest child first, depth - first)
        order = []

        def family(name):
            order.append(name)
            for child in self.children[name]: # Go through children in birth order
                family(child)

        family(self.originator) #start from the first person of the fam tree
        return order

    def get_seniority_order(self):
        # Returns the family in generation - generation order
        order = []
        queue = [self.originator]

        while queue:
            current = queue.pop(0) # move on to the next person in line
            order.append(current) 
            queue.extend(self.children[current])  # add their children to queue

        return order

    def get_cousin_dist(self, ls_name, rs_name):
        # Calculates how closely two family members are related
        # ls and rs = left side and right side ancestors
        def get_ancestors(name):
            ancestors = {}
            dist = 0
            while name:
                ancestors[name] = dist
                name = self.parent[name]
                dist += 1
            return ancestors

        # Get all ancestors of both members (left and right side)
        ls_anc = get_ancestors(ls_name)
        rs_anc = get_ancestors(rs_name)

         # Find Most Recent Common Ancestor (MRCA)
        common = set(ls_anc) & set(rs_anc)
        mrca = min(common, key=lambda a: ls_anc[a])  # mrca= most recent common ancestor

        # Order is distance from MRCA to individual, excluding MRCA itself
        lhs_order = ls_anc[mrca] - 1
        rhs_order = rs_anc[mrca] - 1

        degree = min(lhs_order, rhs_order)  # degree gives us how many gens apart the current gen is
        removal = abs(lhs_order - rhs_order) # gives us the difference in generations

        return (degree, removal) #returns degree and removal of cousin relationship

