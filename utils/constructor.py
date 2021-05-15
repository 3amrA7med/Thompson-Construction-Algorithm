from structs.Node import Node
from PySimpleAutomata import automata_IO
import json

start = None
Input = [["A", "+", "1", "0"],
         ["B", "*", "A"]]


def get_idx(letter, nodes):
    for i in range(len(nodes)):
        if nodes[i].letter == letter:
            return i
    return -1


def OR(letter, first, second, nodes):
    # case if the two inputs are basic input 0 and/or 1
    if (first == "0" or first == "1") and (second == "0" or second == "1"):
        N0 = Node()
        N0.set_letter(letter + "ε")

        N1 = Node()
        N1.set_letter(letter + first)
        N1.add_out("ε", N0, True)

        N2 = Node()
        N2.set_letter(letter + second)
        N2.add_out("ε", N0, True)

        N3 = Node()
        N3.set_letter(letter)
        N3.add_out(first, N1, True)
        N3.add_out(second, N2, True)

        nodes.append(N3)
    # case if one of the inputs is basic and the other one is complex
    # complex means that there is more than expression in the state
    elif first == "0" or first == "1":
        idx = get_idx(second, nodes)

        N0 = Node()
        N0.set_letter(letter + "ε")

        N1 = Node()
        N1.set_letter(letter + first)
        N1.add_out("ε", N0, True)

        nodes[idx].add_out("ε", N0, False)

        N3 = Node()
        N3.set_letter(letter)
        N3.add_out(first, N1, True)
        N3.add_out("ε", nodes[idx], True)

        nodes.append(N3)
        nodes.pop(idx)
    # same previous case but with flipped inputs
    elif second == "0" or second == "1":
        idx = get_idx(first, nodes)

        N0 = Node()
        N0.set_letter(letter + "ε")

        N1 = Node()
        N1.set_letter(letter + second)
        N1.add_out("ε", N0, True)

        nodes[idx].add_out("ε", N0, False)

        N3 = Node()
        N3.set_letter(letter)
        N3.add_out("ε", nodes[idx], True)
        N3.add_out(second, N1, True)

        nodes.append(N3)
        nodes.pop(idx)
    # case two inputs are complex
    else:
        idx1 = get_idx(first, nodes)
        idx2 = get_idx(second, nodes)

        N0 = Node()
        N0.set_letter(letter + "ε")

        nodes[idx1].add_out("ε", N0, False)
        nodes[idx2].add_out("ε", N0, False)

        N3 = Node()
        N3.set_letter(letter)
        N3.add_out("ε", nodes[idx1], True)
        N3.add_out("ε", nodes[idx2], True)

        nodes.append(N3)
        nodes.pop(idx1)
        nodes.pop(idx2)


def asterisk(letter, first, nodes):
    if first == "0" or first == "1":
        N0 = Node()
        N0.set_letter(letter + "ε")

        N1 = Node()
        N1.set_letter(letter + first)
        N1.add_out("ε", N0, True)

        N2 = Node()
        N2.set_letter(letter + first + first)
        N2.add_out(first, N1, True)

        N3 = Node()
        N3.set_letter(letter)
        N3.add_out("ε", N2, True)
        N3.add_out("ε", N0, True)

        N1.add_out("ε", N3, True)

        nodes.append(N3)
    else:
        idx = get_idx(first, nodes)

        N0 = Node()
        N0.set_letter(letter + "ε")

        N1 = Node()
        N1.set_letter(letter)
        N1.add_out("ε", nodes[idx], True)
        N1.add_out("ε", N0, True)

        nodes[idx].add_out("ε", N0, False, N1)

        nodes.append(N1)
        nodes.pop(idx)


def concatenate(letter, first, second, nodes):
    if (first == "0" or first == "1") and (second == "0" or second == "1"):
        N0 = Node()
        N0.set_letter(letter + second)

        N1 = Node()
        N1.set_letter(letter + first)
        N1.add_out(second, N0, True)

        N2 = Node()
        N2.set_letter(letter)
        N2.add_out(first, N1, True)

        nodes.append(N2)

    elif first == "0" or first == "1":
        idx = get_idx(second, nodes)

        N0 = Node()
        N0.set_letter(letter)
        N0.add_out(first, nodes[idx], True)

        nodes.append(N0)
        nodes.pop(idx)

    elif second == "0" or second == "1":
        idx = get_idx(first, nodes)

        N0 = Node()
        N0.set_letter(letter + second)

        nodes[idx].add_out(second, N0, False)
        nodes[idx].set_letter(letter)

    else:
        idx1 = get_idx(first, nodes)
        idx2 = get_idx(second, nodes)

        nodes[idx1].add_out("ε", nodes[idx2], False)
        nodes[idx1].set_letter(letter)
        nodes.pop(idx2)


def construct_nfa(inputs):
    nodes = []
    for g in inputs:
        if g[1] == "+":
            OR(g[0], g[2], g[3], nodes)
        elif g[1] == "*":
            # pass
            asterisk(g[0], g[2], nodes)
        elif g[1] == "CONCAT":
            concatenate(g[0], g[2], g[3], nodes)

    json = '{\n'
    json += nodes[0].get_json()
    json = json[:-2]
    json += '\n}'
    print(json)
    # print(nodes[0])


if __name__ == "__main__":
    construct_nfa(Input)
