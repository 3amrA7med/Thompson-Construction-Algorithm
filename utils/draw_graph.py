import json
from graphviz import Digraph
graph = Digraph(comment='NFA')


def draw_graph(json_obj):
    """
    This function draws graph given a json string
    :param json_obj: this is the json string
    :return: draw graph
    """
    data = json.loads(json_obj)
    nodes = []
    starting_state = None
    # Add nodes
    for d in data:
        if d != "startingState":
            if data[d]["isTerminatingState"] == "True":
                graph.node(str(d), shape="doublecircle")
            else:
                graph.node(str(d))
            nodes.append(str(d))
        else:
            starting_state = data["startingState"]
    graph.node("", shape="none")
    graph.edge("", starting_state)

    # Add edges
    for d in nodes:
        print(data[d])
        for attribute in data[d]:
            if attribute != "isTerminatingState":
                print(str(d), str(data[d][attribute]), attribute)
                graph.edge(d, data[d][attribute], attribute)

    graph.unflatten().render('./graph', view=True, format='png', cleanup=True)
