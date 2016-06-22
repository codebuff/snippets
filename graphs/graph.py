from snippets.graphs.vertex import Vertex
from snippets.graphs.utilities import Color


class Graph:
    """
    by default the graphs are undirected and non-weighted
    """

    def __init__(self, undirected=False, weighted=False):
        self.is_undirected = undirected
        self.is_weighted = weighted
        self.vertices = {}
        self.no_of_vertices = 0
        self.time = 0

    def add_vertex(self, vertex_id=None, vertex=None):
        if vertex is not None:
            vid = vertex.get_id()
            if vid in self.vertices:
                # be careful of any existing nbrs of this vertex (incoming edges)
                self.vertices[vid] = vertex
                return
            else:
                self.vertices[vid] = vertex
                self.no_of_vertices += 1
                return

        if vertex_id not in self.vertices:
            if vertex_id not in self.vertices:
                self.vertices[vertex_id] = Vertex(vertex_id)
                self.no_of_vertices += 1
                return

    def remove_vertex(self, vertex_id):
        if vertex_id in self.vertices:
            del self.vertices[vertex_id]
            self.no_of_vertices -= 1
        for vertex in self.vertices.values():
            vertex.remove_nbr(vertex_id)

    def add_edge(self, from_vertex_id, to_vertex_id, weight=None):
        if from_vertex_id not in self.vertices:
            self.vertices[from_vertex_id] = Vertex(from_vertex_id)
            self.no_of_vertices += 1
        if to_vertex_id not in self.vertices:
            self.vertices[to_vertex_id] = Vertex(to_vertex_id)
            self.no_of_vertices += 1

        self.vertices[from_vertex_id].add_nbr(to_vertex_id, weight)

        if self.is_undirected:
            self.vertices[to_vertex_id].add_nbr(from_vertex_id, weight)

    def remove_edge(self, from_vertex_id, to_vertex_id):
        if from_vertex_id in self.vertices and to_vertex_id in self.vertices:
            self.vertices[from_vertex_id].remove_nbr(to_vertex_id)
            if self.is_undirected:
                self.vertices[to_vertex_id].remove_nbr(from_vertex_id)

    def get_all_vertices_ids(self):
        return self.vertices.keys()

    def get_all_vertices(self):
        return self.vertices.values()

    def get_vertex(self, vertex_id):
        return self.vertices[vertex_id]

    def set_vertex_attribute(self,vertex_id, attribute, value):
        setattr(vertex_id, attribute, value)

    def get_all_vtx_ids_sorted_by_attribute(self, attribute, reverse=False):
        vtx_ids = self.get_all_vertices_ids()

        def operation(vtx_id):
            return getattr(self.get_vertex(vtx_id), attribute)

        vtx_ids.sort(key=operation, reverse=reverse)
        return vtx_ids

    def dfs(self, start_vertex_id=None):
        self.time = -1
        if start_vertex_id is not None:
            if start_vertex_id not in self.vertices:
                return
            else:
                self.get_vertex(start_vertex_id).set_pred_id(None)
                if self.get_vertex(start_vertex_id).get_color() == Color.WHITE:
                    self.dfsvisit(start_vertex_id)
                return
        # no start vertex, go through each vertex
        self.re_initialize_all_vertex_attr("color", Color.WHITE)
        for vertex_id in self.vertices:
            vtx = self.get_vertex(vertex_id)
            if vtx.get_color() == Color.WHITE:
                vtx.set_pred_id(None)
                self.dfsvisit(vertex_id)

    def dfsvisit(self, start_vertex_id):
        self.time += 1
        start_vtx = self.get_vertex(start_vertex_id)
        start_vtx.discovery_time = self.time
        start_vtx.set_color(Color.GREY)
        for nbr_id in start_vtx.get_nbr_ids():
            vtx = self.get_vertex(nbr_id)
            if vtx.get_color() == Color.WHITE:
                vtx.set_pred_id(start_vertex_id)
                self.dfsvisit(nbr_id)
        self.time += 1
        start_vtx.finish_time = self.time
        start_vtx.set_color(Color.BLACK)

    def bfs(self, start_vertex_id):
        # self.re_initialize_all_vertex_attr("color", Color.WHITE)
        # for vertex_id in self.vertices:
        #     self.get_vertex(vertex_id).set_color(Color.WHITE)
        self.vertices[start_vertex_id].set_pred_id(None)
        self.vertices[start_vertex_id].set_distance(0)
        from collections import deque
        vq = deque()
        vq.append(start_vertex_id)
        while len(vq) > 0:
            current_vertex_id = vq.popleft()
            cur_vtx = self.get_vertex(current_vertex_id)
            cur_vtx.set_color(Color.GREY)
            for nbr_id in cur_vtx.get_nbr_ids():
                vtx = self.get_vertex(nbr_id)
                if vtx.get_color() == Color.WHITE:
                    # place to perform operation
                    # todo maybe decouple bfs and operations by passing a reference to operation_func to bfs
                    vtx.set_color(Color.GREY)
                    vtx.set_pred_id(current_vertex_id)
                    vtx.set_distance(cur_vtx.get_distance() + 1)
                    vq.append(nbr_id)
            cur_vtx.set_color(Color.BLACK)

    def get_no_of_connected_component(self):
        # if the graph is directed, returns no of weakly connected components
        if not self.vertices:
            return 0
        conn_comp = 0
        self.re_initialize_all_vertex_attr("color", Color.WHITE)
        for vertex_id in self.vertices:
            if self.get_vertex(vertex_id).get_color() == Color.WHITE:
                conn_comp += 1
                self.bfs(start_vertex_id=vertex_id)
        return conn_comp

    def bellman_ford(self):pass
    # shortest path with negative weight edges

    def floyd_warshall(self):pass
    # all pair shortest path

    def get_max_flow(self):pass
    # ford fulkerson with bfs = edmond karp

    def create_adjacency_matrix(self):pass

    def get_all_cycles(self):pass

    def bipartite_matching(self):pass
    # max cardinality matching

    def min_vertex_cover(self):pass
    # a bipartite matching
    # return min vertex cover

    def hungarian_algorithm(self):pass
    # maximum weighted matching [ min cost, max match ]
    # to convert to max cost max match , change cost of every edge to MAXCOST-cost of edge


    def print_graph(self):
        if self.is_undirected:
            print('Undirected graph')
        else:
            print('Directed graph')
        for vertex_id in self.vertices:
            print('-------------')
            print(self.vertices[vertex_id])
            for nbr_id in self.vertices[vertex_id].get_nbr_ids():
                print('from ' + str(vertex_id), 'to ' + str(nbr_id), 'weight ' + str(self.vertices[vertex_id].get_weight(nbr_id)))

    def __str__(self):
        self.print_graph()
        return ''

    def re_initialize_all_vertex_attr(self, name=None, value=None):
        if name is None:
            return
        for vertex in self.vertices.values():
            setattr(vertex, name, value)
