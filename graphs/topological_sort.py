def topological_sort(graph):
    # returns the order of steps
    # todo maybe check if there is only one connected component
    graph.dfs()
    return graph.get_all_vtx_ids_sorted_by_attribute(attribute="finish_time", reverse=True)

