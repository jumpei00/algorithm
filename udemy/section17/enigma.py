import string
from typing import List
import random

ALPHABET = string.ascii_uppercase


class PlugBoard(object):
    def __init__(self, mapping_alphabet: str):
        self.alphabet = ALPHABET
        self.forward_map = dict(zip(self.alphabet, mapping_alphabet))
        self.backward_map = dict(zip(mapping_alphabet, self.alphabet))

    def forward(self, index: int) -> int:
        char = self.alphabet[index]
        alphabet = self.forward_map[char]
        return self.alphabet.index(alphabet)

    def backward(self, index: int) -> int:
        char = self.alphabet[index]
        alphabet = self.backward_map[char]
        return self.alphabet.index(alphabet)


class Router(PlugBoard):
    def __init__(self, mapping_alphabet: str, offset=1):
        super().__init__(mapping_alphabet)
        self.offset = offset
        self.rotation = 0

    def rotate(self):
        # 上回転
        self.alphabet = \
            self.alphabet[self.offset:] + self.alphabet[:self.offset]
        self.rotation += self.offset
        return self.rotation

    def reset(self):
        self.alphabet = ALPHABET
        self.rotation = 0


class Reflector(object):
    def __init__(self, mapping_alphabet: str):
        self.map = dict(zip(ALPHABET, mapping_alphabet))
        for k, v in self.map.items():
            if k != self.map[v]:
                raise ValueError(k, v)

    def reflect(self, index: int):
        alphabet = self.map[ALPHABET[index]]
        return ALPHABET.index(alphabet)


class EnigmaMachine(object):
    def __init__(self, plug_board: PlugBoard, routers: List[Router], reflector: Reflector):
        self.plug_board = plug_board
        self.routers = routers
        self.reflector = reflector

    def encript(self, text: str) -> str:
        return ''.join([self.go_through(char) for char in text])

    def decript(self, text: str) -> str:
        for router in self.routers:
            router.reset()

        return ''.join([self.go_through(char) for char in text])

    def go_through(self, char: str) -> str:
        char = char.upper()
        if char not in ALPHABET:
            return char

        index = ALPHABET.index(char)
        index = self.plug_board.forward(index)
        for router in self.routers:
            index = router.forward(index)

        index = self.reflector.reflect(index)

        for router in reversed(self.routers):
            index = router.backward(index)

        index = self.plug_board.backward(index)
        char = ALPHABET[index]

        for router in reversed(self.routers):
            if router.rotate() % len(ALPHABET) != 0:
                break

        return char


def get_random_alphabet():
    return ''.join(random.sample(ALPHABET, k=len(ALPHABET)))


if __name__ == "__main__":
    plug_board = PlugBoard(get_random_alphabet())
    router_1 = Router(get_random_alphabet())
    router_2 = Router(get_random_alphabet())
    router_3 = Router(get_random_alphabet())

    r = list(ALPHABET)
    indexes = [i for i in range(len(r))]
    for _ in range(len(indexes) // 2):
        x = indexes.pop(random.randint(0, len(indexes) - 1))
        y = indexes.pop(random.randint(0, len(indexes) - 1))
        r[x], r[y] = r[y], r[x]
    reflector = Reflector(''.join(r))

    enigma = EnigmaMachine(
        plug_board, [router_1, router_2, router_3], reflector)

    text = 'TODAY IS ON MONDAY'
    e = enigma.encript(text)
    print(e)
    d = enigma.decript(e)
    print(d)
