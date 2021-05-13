from structs.Node import Node

start = None
Input = [["A", "+", "1", "0"]]
# Input =  [
# ["A", "+", "1", "0"],
# ["B", "*", "A"],
# ["C", "CONCAT", "1", "B"],
# ["D", "CONCAT", "C", "0"],
# ["E", "CONCAT", "D", "0"],
# ["F", "+","0", "E"],
# ["F"]
# ]

def get_idx(letter, nodes):
    for i in range(len(nodes)):
        if(nodes[i].Letter == letter):
            return i
    return -1

def OR(letter, first, second, nodes):
    #case if the two inputs are basic input 0 and/or 1
    if((first == "0" or first == "1") and (second == "0" or second == "1")):
        N0 = Node()
        N0.set_letter(letter+"ε")
        N1 = Node()
        N1.set_letter(letter+first)
        N1.add_out("ε", N0)
        N2 = Node()
        N2.set_letter(letter+second)
        N2.add_out("ε", N0)
        N3 = Node()
        N3.set_letter(letter)
        N3.add_out(first, N1)
        N3.add_out(second, N2)
        nodes.append(N3)
    #case if one of the inputs is basic and the other one is complex
    #complex means that there is more than expretion in the state
    elif(first == "0" or first == "1"):
        idx = get_idx(second, nodes)
        N0 = Node()
        N0.set_letter(letter+"ε")
        N1 = Node()
        N1.set_letter(letter+first)
        N1.add_out("ε", N0)
        nodes[idx].add_out("ε", N0)
        N3 = Node()
        N3.set_letter(letter)
        N3.add_out(first, N1)
        N3.add_out(second, nodes[idx])
        nodes.append(N3)
        nodes.pop(idx)
    #same previous case but with flipped inputs
    elif(second == "0" or second == "1"):
        idx = get_idx(first, nodes)
        N0 = Node()
        N0.set_letter(letter+"ε")
        N1 = Node()
        N1.set_letter(letter+second)
        N1.add_out("ε", N0)
        nodes[idx].add_out("ε", N0)
        N3 = Node()
        N3.set_letter(letter)
        N3.add_out(first, nodes[idx])
        N3.add_out(second, N1)
        nodes.append(N3)
        nodes.pop(idx)
    #case two inputs are complex
    else:
        idx1 = get_idx(first, nodes)
        idx2 = get_idx(second, nodes)
        N0 = Node()
        N0.set_letter(letter+"ε")
        nodes[idx1].add_out("ε", N0)
        nodes[idx2].add_out("ε", N0)
        N3 = Node()
        N3.set_letter(letter)
        N3.add_out(first, nodes[idx1])
        N3.add_out(second, nodes[idx2])
        nodes.append(N3)
        nodes.pop(idx1)
        nodes.pop(idx2)




        


def construct_NFA(input):
    nodes = []
    for g in input:
        if(g[1] == "+"):
            OR(g[0], g[2], g[3], nodes)
        elif(g[1] == "*"):
            ASTRIC(g[0], g[2], g[3])
        elif(g[1] == "CONCATE"):
            CONCATENATE(g[0], g[2], g[3])

    print(nodes[0])
    #return nodes[0]

construct_NFA(input)