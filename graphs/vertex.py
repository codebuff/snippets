from snippets.graphs.utilities import Color


class Vertex:

    def __init__(self, vertex_id, nbrs=None):
        self.id = vertex_id
        if nbrs and isinstance(nbrs, dict):
            self.nbrs = nbrs
        else:
            self.nbrs = {}
        self.color = Color.WHITE
        self.distance = 0
        self.predecessor_id = None
        self.discovery_time = -1
        self.finish_time = -1

    def add_nbr(self, nbr_id, weight=None):
        self.nbrs[nbr_id] = weight

    def remove_nbr(self, nbr_id):
        if nbr_id in self.nbrs:
            del self.nbrs[nbr_id]

    def get_nbr_ids(self):
        return self.nbrs.keys()

    def get_nbr_ids_sorted_by_attribute(self, attribute, reverse=False):
        if attribute == "id":
            # in dicts, sort returns keys
            return sorted(self.nbrs, reverse=reverse)
        return sorted(self.nbrs, key=lambda x:x[attribute], reverse=reverse)

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        if nbr in self.nbrs:
            return self.nbrs[nbr]
        return None

    def set_weight(self, nbr_id, weight):
        self.nbrs[nbr_id, weight]

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_pred_id(self):
        return self.predecessor_id

    def set_pred_id(self, predecessor_id):
        self.predecessor_id = predecessor_id

    def get_distance(self):
        return self.distance

    def set_distance(self, distance):
        self.distance = distance

    def __str__(self):
        return str(self.id) + ' is connected to ' + str(list(self.nbrs.keys()))
