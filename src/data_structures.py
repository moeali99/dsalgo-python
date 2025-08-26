from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Iterable, List, Optional, TypeVar


T = TypeVar("T")


class Stack(Generic[T]):
    """Simple LIFO stack.

    Push: O(1), Pop: O(1)
    """

    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, value: T) -> None:
        self._items.append(value)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> T:
        if not self._items:
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0


class Queue(Generic[T]):
    """Simple FIFO queue based on two stacks.

    Amortized O(1) for enqueue/dequeue.
    """

    def __init__(self) -> None:
        self._in: List[T] = []
        self._out: List[T] = []

    def enqueue(self, value: T) -> None:
        self._in.append(value)

    def dequeue(self) -> T:
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())
        if not self._out:
            raise IndexError("dequeue from empty queue")
        return self._out.pop()

    def is_empty(self) -> bool:
        return not self._in and not self._out


class MinHeap(Generic[T]):
    """Binary min heap.

    Insert: O(log n), Extract-min: O(log n)
    """

    def __init__(self, values: Optional[Iterable[T]] = None) -> None:
        import heapq

        self._heap: List[T] = []
        if values is not None:
            self._heap = list(values)
            heapq.heapify(self._heap)

    def push(self, value: T) -> None:
        import heapq

        heapq.heappush(self._heap, value)

    def pop(self) -> T:
        import heapq

        if not self._heap:
            raise IndexError("pop from empty heap")
        return heapq.heappop(self._heap)

    def peek(self) -> T:
        if not self._heap:
            raise IndexError("peek from empty heap")
        return self._heap[0]

    def __len__(self) -> int:  # pragma: no cover
        return len(self._heap)


