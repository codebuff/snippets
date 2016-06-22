def traverse(graph,vertex):
    current_vertex = vertex

    while current_vertex.get_pred_id():
        print(current_vertex.get_id())
        current_vertex = graph.get_vertex(current_vertex.get_pred_id())
    print(current_vertex.get_id())


class Color:
    WHITE = "white"
    GREY = "grey"
    BLACK = "black"
