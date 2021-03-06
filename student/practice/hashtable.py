import hashlib


class HashTable(object):
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def hash(self, key: str):
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size

    def print(self):
        for i, table in enumerate(self.table):
            print(f'{i} ->', end=' ')
            for data in table:
                print(f'[key: {data[0]}, value: {data[1]}]', end=' ')
            print()

    def add(self, key, value):
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                data[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                return data[1]
        return None


if __name__ == "__main__":
    h = HashTable()
    h['pc'] = 'mac'
    h['car'] = 'tesla'
    h['language'] = 'English'
    h['sns'] = 'Twitter'
    h['sns'] = 'Facebook'
    print(h['sns'])
    print(h['web'])
    h.print()
