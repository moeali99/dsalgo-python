## Datenstrukturen und Algorithmen (Python)

Kleine Sammlung typischer Algorithmen und Datenstrukturen aus den ersten Semestern Informatik, inkl. Tests mit `pytest`.

### Inhalte
- Sortieralgorithmen: Insertion Sort, Merge Sort, Quick Sort
- Suchen: Binäre Suche
- Graph: BFS, DFS, Dijkstra (mit Prioritätswarteschlange)
- Datenstrukturen: Stack, Queue, MinHeap

### Projektstruktur
```
dsalgo-python/
  src/
    algorithms.py
    data_structures.py
  tests/
    test_algorithms.py
    test_data_structures.py
  requirements.txt
```

### Entwicklung
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

### Hinweise
- Der Fokus liegt auf klarer, gut testbarer Implementierung.
- Laufzeitkomplexitäten sind in Docstrings vermerkt.



