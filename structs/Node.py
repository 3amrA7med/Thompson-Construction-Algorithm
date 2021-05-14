class Node:
    def __init__(self, node=None):
        self.out = []
        self.letter = None
        self.start = True
        self.end = True
        if node is not None:
            for node_dic in node.out:
                self.out.append({"input": node_dic["input"], "node": node_dic["node"]})
            self.letter = node.letter
            self.start = node.start
            self.end = node.end

    def set_letter(self, letter):
        self.letter = letter

    def set_start_true(self):
        self.start = True

    def set_start_false(self):
        self.start = False

    def set_end_true(self):
        self.end = True

    def set_end_false(self):
        self.end = False

    def add_out(self, state_input, node, for_node):
        if for_node:
            self.out.append({"input": state_input, "node": node})
            self.out[-1]["node"].set_start_false()
            self.set_end_false()
            return True
        else:
            if self.end:
                self.out.append({"input": state_input, "node": Node(node)})
                self.out[-1]["node"].set_start_false()
                self.set_end_false()
                return True
            else:
                for n in self.out:
                    return_val = n["node"].add_out(state_input, node, False)
                    if return_val:
                        return True
                return False

            ##here we should add for the hole graph

    def __str__(self):
        for n in self.out:
            print(n["node"])
            print(n["input"])
        return self.letter + "\t" + str(self.start) + "\t" + str(self.end)
