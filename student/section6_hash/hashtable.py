import hashlib


class HashTable(object):
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def hash(self, key: str) -> int:
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size

    def add(self, key, value):
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                data[1] = value
        else:
            self.table[index].append([key, value])

    def get(self, key):
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                return data[1]

    @property
    def print(self):
        for index in range(self.size):
            print(f'{index} ->', end=' ')
            for data in self.table[index]:
                print(f'{data}', end=' ')
            print()


if __name__ == "__main__":
    hash_table = HashTable()
    hash_table['car'] = 'Tesla'
    hash_table['sns'] = 'Twitter'
    hash_table['pc'] = 'Mac'
    hash_table['tablet'] = 'iPad'
    hash_table['watch'] = 'apple watch'
    hash_table.print
    print(hash_table['sns'])
