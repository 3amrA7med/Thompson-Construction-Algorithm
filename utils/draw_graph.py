from graphviz import Digraph
graph = Digraph(comment='NFA')


def draw_graph(json):
    """graph.node('A', 'King Arthur')
    graph.node('B', 'Sir Bedevere the Wise')
    graph.node('L', 'Sir Lancelot the Brave')

    graph.edges(['AB', 'AL'])
    graph.edge('B', 'L', constraint='false')"""
    graph.render('./graph', view=True, format='png', cleanup=True)
