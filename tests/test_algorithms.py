from src.algorithms import (
    insertion_sort,
    merge_sort,
    quick_sort,
    binary_search,
    bfs,
    dfs,
    dijkstra,
)


def test_sorting_algorithms_basic():
    data = [5, 3, 8, 1, 2]
    expected = [1, 2, 3, 5, 8]
    assert insertion_sort(data) == expected
    assert merge_sort(data) == expected
    assert quick_sort(data) == expected


def test_binary_search():
    arr = [1, 2, 3, 4, 5, 6]
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 4) == 3
    assert binary_search(arr, 6) == 5
    assert binary_search(arr, 7) == -1


def test_bfs_dfs():
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D"],
        "D": [],
    }
    assert bfs(graph, "A") == ["A", "B", "C", "D"]
    # DFS order can vary; with reversed push we expect this:
    assert dfs(graph, "A") == ["A", "B", "D", "C"]


def test_dijkstra():
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("C", 2), ("D", 5)],
        "C": [("D", 1)],
        "D": [],
    }
    dist = dijkstra(graph, "A")
    assert dist["A"] == 0
    assert dist["B"] == 1
    assert dist["C"] == 3
    assert dist["D"] == 4


