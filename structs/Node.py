import json
class Node:
    def __init__(self, node=None):
        self.visited = False    # for testing and printing
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

    def add_out(self, state_input, node, for_node, node2=None):
        if for_node:
            self.out.append({"input": state_input, "node": node})
            self.out[-1]["node"].set_start_false()
            self.set_end_false()
            return True
        else:
            if self.end:
                self.out.append({"input": state_input, "node": node})
                self.out[-1]["node"].set_start_false()
                self.set_end_false()
                # node2 for the case of asterisk to make one graph outs to same point in the same time
                if node2 is not None:
                    self.out.append({"input": state_input, "node": node2})
                return True
            else:
                for n in self.out:
                    return_val = n["node"].add_out(state_input, node, False, node2)
                    if return_val:
                        return True
                return False

            ##here we should add for the hole graph

    def __str__(self):
        if self.visited:
            return "visited before"
        for n in self.out:
            print(n["node"])
            print(n["input"])
        self.visited = True
        return self.letter + "\t" + str(self.start) + "\t" + str(self.end)

    def get_json(self):
        json = ''
        if not self.visited:
            self.visited = True

            if self.start:
                json += '\t"startingState":"' + self.letter + '"\n'
            json += '\t"' + self.letter + '":{\n\t\t"isTerminatingState":' + str(self.end) + ',\n'
            for n in self.out:
                json += '\t\t"' + n["input"] + '":' + n["node"].letter + ',\n'
            json = json[:-2]
            json += '\n\t},\n'

            if len(self.out) > 0:
                for n in self.out:
                    json += n["node"].get_json()


        return json

