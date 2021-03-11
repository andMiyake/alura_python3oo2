from abc import ABC     #abstract base classes

from collections.abc import MutableSequence
from numbers import Complex

class Numero(Complex):
    def __getitem__(self, item):
        super.__getitem__()


filmes = Numero()
