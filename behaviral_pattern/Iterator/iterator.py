from collections.abc import Iterator


class EggOrHen(Iterator):
    _collection = ["Egg", "Chick", "Hen"]
    _position: int = None
    _reverse: bool = False

    def __init__(self, reverse: bool = False):
        self._position = -1 if reverse else 0
        self._reverse = reverse

    def __next__(self) -> str:
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return value


if __name__ == "__main__":
    egg_or_hen = EggOrHen()
    for i in egg_or_hen:
        print(i)
