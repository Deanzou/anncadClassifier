

class Hypercube:
    def __init__(self, coords):
        self.coords = coords
        self.examples = []
        self.hypercube_class = None

    def add_example(self, example):
        self.examples.append(example)
        self.list_of_classes = list(set([x.class_id for x in self.examples]))

    def set_hypercube_class(self):
        max_class = -1
        if not self.examples:
            self.hypercube_class = 'E'
        else:
            for class_id in self.list_of_classes:
                class_size = len(list(filter(lambda x: x.class_id == class_id, self.examples)))
                if class_size > max_class:
                    max_class = class_size
                    self.hypercube_class = class_id