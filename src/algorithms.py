from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from typing import Any, Deque, Dict, Iterable, List, Optional, Tuple


def insertion_sort(values: List[int]) -> List[int]:
    """Sort a list using insertion sort.

    Time: O(n^2), Space: O(1)
    """
    arr = values[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(values: List[int]) -> List[int]:
    """Sort a list using merge sort.

    Time: O(n log n), Space: O(n)
    """
    if len(values) <= 1:
        return values[:]

    mid = len(values) // 2
    left = merge_sort(values[:mid])
    right = merge_sort(values[mid:])

    result: List[int] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(values: List[int]) -> List[int]:
    """Sort a list using quick sort (Lomuto partition).

    Average: O(n log n), Worst: O(n^2)
    """
    arr = values[:]

    def partition(low: int, high: int) -> int:
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

    def sort(low: int, high: int) -> None:
        if low < high:
            p = partition(low, high)
            sort(low, p - 1)
            sort(p + 1, high)

    sort(0, len(arr) - 1)
    return arr


def binary_search(values: List[int], target: int) -> int:
    """Return index of target in sorted values or -1 if not found.

    Time: O(log n)
    """
    low, high = 0, len(values) - 1
    while low <= high:
        mid = (low + high) // 2
        if values[mid] == target:
            return mid
        if values[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


Graph = Dict[Any, List[Tuple[Any, int]]]


def bfs(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
    """Breadth-first search order from start.

    Time: O(V + E)
    """
    visited: List[Any] = []
    seen = set([start])
    q: Deque[Any] = deque([start])
    while q:
        node = q.popleft()
        visited.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in seen:
                seen.add(neighbor)
                q.append(neighbor)
    return visited


def dfs(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
    """Depth-first search order from start (iterative).

    Time: O(V + E)
    """
    visited: List[Any] = []
    seen = set()
    stack: List[Any] = [start]
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        visited.append(node)
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in seen:
                stack.append(neighbor)
    return visited


def dijkstra(graph: Graph, start: Any) -> Dict[Any, int]:
    """Shortest path distances from start using Dijkstra.

    Time: O((V + E) log V) with binary heap
    """
    import heapq

    distances: Dict[Any, int] = {start: 0}
    heap: List[Tuple[int, Any]] = [(0, start)]
    visited = set()

    while heap:
        dist, node = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)

        for neighbor, weight in graph.get(node, []):
            new_dist = dist + weight
            if neighbor not in distances or new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return distances


