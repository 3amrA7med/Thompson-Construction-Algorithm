class Node:
    def __init__(self, node = None):
        if(Node == None):
            self.Out = []
            self.Letter = None
            self.Start = True
            self.End = True
        else:
            self.Out = node.Out
            self.Letter = node.Letter
            self.Start = node.Start
            self.End = node.End

    def set_letter(self, letter):
        self.Letter = letter

    def set_start_true(self):
        self.Start = True

    def set_start_false(self):
        self.Start = False

    def set_end_true(self):
        self.End = True

    def set_end_false(self):
        self.End = False
    
    def add_out(self, input, node):
        self.Out.append({input: Node(node)})
        self.Out[-1][input].set_start_false()
        self.set_end_false()