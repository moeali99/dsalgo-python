from src.data_structures import Stack, Queue, MinHeap


def test_stack():
    s: Stack[int] = Stack()
    s.push(1)
    s.push(2)
    assert s.peek() == 2
    assert s.pop() == 2
    assert s.pop() == 1


def test_queue():
    q: Queue[int] = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3


def test_min_heap():
    h: MinHeap[int] = MinHeap([5, 3, 8, 1, 2])
    assert h.peek() == 1
    assert h.pop() == 1
    h.push(0)
    assert h.peek() == 0


