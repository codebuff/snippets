from graphs.priority_queue import PriorityQueue


def prim(graph, start_vtx_id):
    # minimum spanning tree
    # shortest path from one node to all others
    ans = []
    if not graph.is_weighted:
        for vtx in graph.get_all_vertices():
            for nbr_id in vtx.get_nbr_ids:
                vtx.set_weight(nbr_id, 1)

    import sys
    graph.re_initialize_all_vertex_attr("distance", sys.maxsize)
    graph.re_initialize_all_vertex_attr("predecessor_id", None)
    graph.get_vertex(start_vtx_id).set_distance(0)
    v_pq = PriorityQueue([[vtx.get_distance(), vtx.get_id()] for vtx in graph.get_all_vertices()])

    while not v_pq.is_empty():
        current_vertex_id = v_pq.del_min()
        ans.append(current_vertex_id)
        cur_vtx = graph.get_vertex(current_vertex_id)
        # todo maybe sorting is not required here
        #for nbr_id in cur_vtx.get_nbr_ids_sorted_by_attribute("weight"):
        for nbr_id in cur_vtx.get_nbr_ids():
            nbr = graph.get_vertex(nbr_id)
            new_dist = cur_vtx.get_weight(nbr_id)
            if nbr.get_distance() > new_dist and v_pq.has_vertex(nbr):
                nbr.set_distance(new_dist)
                nbr.set_pred(current_vertex_id)
                v_pq.decrease_key(nbr_id, new_dist)
    return ans
