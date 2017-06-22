import uuid


class generate_key():
    def __init__(self):
        self.num = 0
        self.list = []

    def generate(self, num):
        for i in range(num):
            self.list.append(uuid.uuid1())

    def return_list(self):
        return self.list


test = generate_key()
test.generate(200)
keys = test.return_list()
print(keys)
print(len(keys))
