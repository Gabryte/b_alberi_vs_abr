class AbrNode:
    'classe nodo ABR'

    def __init__(self,key,satellite_data):
        self.key = key
        self.satellite_data = satellite_data
        self.p = None
        self.right = None
        self.left = None

    'getter'
    def get_key(self):
        return self.key

    def get_p(self):
        return self.p

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def get_satellite_data(self):
        return self.satellite_data

    'setter'
    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def set_parent(self, p):
        self.p = p

    def set_satellite_data(self, st):
        self.satellite_data = st