# Interview Questions

This repository is my interview tech questions I have archived. record of the problems I have worked through live for technical interviews, take-home challenges, and algorithm-heavy conversations.

It is a mix of polished solutions, active practice, notes, experiments, and hard-earned attempts. I keep it because it shows more than whether I can solve one isolated problem. It shows how I think, how I learn, how I keep going when a problem is uncomfortable, and how I build fluency through repetition.

This repo is a small bastion of trial by combat :).

## Repository Structure

```text
algorithms/
systems-and-backend/
machine-learning/
scratchpad/
```

- `algorithms/` contains algorithmbased interview q's I experienced : arrays, strings, trees, graphs, tries, heaps, search, math, and data structures.
- `systems-and-backend/` contains practical engineering problems: networking, billing, game state, unit conversion, and constraint validation.
- `machine-learning/` contains ML and LLM-oriented work.
- `scratchpad/` contains rougher attempts, notes, experiments, and files that I was askedyet to organize into correct foler. its todo

## What This Shows

- Breadth across arrays, strings, linked lists, trees, graphs, tries, heaps, dynamic programming, networking, billing logic, games, and machine learning.
- Comfort moving between practical business problems and classic computer science problems.
- A willingness to write things down, test ideas, revisit old solutions, and improve through practice.
- Persistence. Some files are clean. Some are rough. The roughness is separated into `scratchpad/` so the main folders stay easy to review while still preserving the journey.
- Human problem solving under pressure: reading a prompt, finding the shape of the problem, choosing a data structure, working through edge cases, and translating thought into code.

## Highlights

| Area | File | What it demonstrates |
| --- | --- | --- |
| Cache design | `algorithms/problem61.py` | LRU cache design using a hash map and linked-list style ordering for O(1) access patterns. |
| Billing logic | `systems-and-backend/problem28.py` | Practical subscription proration with dates, activation windows, historical billing, and cents-based results. |
| Game state | `systems-and-backend/problem23.py` | Connect 4 implementation with board state, move validation, turn switching, and win detection. |
| Machine learning | `machine-learning/problem35.py` | LLM response preference modeling using PyTorch, Transformers, datasets, training, and evaluation metrics. |
| Graphs | `algorithms/problem47.py` | Dijkstra's algorithm with a priority queue for shortest paths. |
| Graph reachability | `algorithms/problem19.py`, `algorithms/problem56.py` | Transitive closure using graph traversal and matrix-based reasoning. |
| Tries and bitwise reasoning | `algorithms/problem32.py` | Maximum XOR using trie-style bit traversal. |
| Text processing | `algorithms/problem57.py`, `algorithms/problem30.py` | Text justification and line-breaking problems with formatting constraints. |
| Trees | `algorithms/problem09.py`, `algorithms/problem10.py`, `algorithms/problem13.py`, `algorithms/problem17.py`, `algorithms/problem24.py`, `algorithms/problem31.py`, `algorithms/problem39.py` | Binary tree traversal, balanced BST construction, subtree checking, expression evaluation, and tree transformation. |
| Arrays and windows | `algorithms/problem06.py`, `algorithms/problem12.py`, `algorithms/problem25.py`, `algorithms/problem43.py`, `algorithms/problem49.py`, `algorithms/problem53.py`, `algorithms/problem58.py` | Sliding windows, partitioning, products, sorted windows, and intersection counting. |
| Systems and networking | `systems-and-backend/problem20.py` | TCP and UDP client/server practice. |
| Data structures | `algorithms/problem33.py`, `algorithms/problem37.py`, `algorithms/problem44.py`, `algorithms/problem50.py` | Sparse arrays, heap-backed stacks, autocomplete tries, and union-find. |
| Math and constraints | `algorithms/problem14.py`, `algorithms/problem42.py`, `algorithms/problem46.py`, `algorithms/problem52.py`, `algorithms/problem54.py` | Version comparison, restricted binary search, regular numbers, palindrome integers, and division without direct shortcuts. |

## Problem Map

### Algorithms

`algorithms/` is my  main interview lib. It includes:

- Foundations: Two Sum, median of sorted arrays, linked-list addition, number of islands, and sliding windows.
- Trees: traversal, same-tree checking, balanced BST construction, level sums, subtree checks, expression trees, and tree transformation.
- Graphs: transitive closure, Dijkstra's algorithm, reachability, and union-find.
- Strings and text: version comparison, word search, autocomplete, anagrams, text wrapping, and full justification.
- Data structures: Huffman coding, sparse arrays, heap-backed stacks, tries, and LRU cache design.
- Math and constraints: binary search restrictions, regular numbers, integer palindrome checks, division practice, partitioning, and large-array sorting.
- Other language practice: C++ and TypeScript versions of selected problems.

### Systems And Backend

`systems-and-backend/` contains problems that feel closer to real production engineering:

- `problem20.py` - TCP and UDP client/server classes
- `problem23.py` - Connect 4 game-state implementation
- `problem28.py` - Prorated subscription billing
- `problem40.py` - Unit conversion system
- `problem41.py` - Mastermind solver / validator

### Machine Learning

`machine-learning/` contains ML-oriented interview and competition practice:

- `problem35.py` - Kaggle-style LLM preference prediction with XLM-RoBERTa, PyTorch, and evaluation metrics

### Scratchpad

`scratchpad/` is the honest workshop corner. These files are part of the learning record, but they are not the polished front door of the repo.

- `problem11.txt` - Notes / prompt material
- `problem29.py` - Inorder successor attempt
- `problem38.py` - Word sense disambiguation attempt
- `problem55.py` - Division implementation practice
- `problem59.py` - Empty-string challenge attempt
- `problem60.py` - Event log parsing experiment

## How To Read This Repo

I recommend starting with the highlights table above. Those files show the range best: algorithmic thinking, real product logic, state modeling, systems practice, and machine learning curiosity.

The folder structure is intentional. The main folders show the strongest signal quickly. The `scratchpad/` folder preserves the process: unfinished ideas, mistakes, rough attempts, and the kind of repetition that actually builds skill.

## My Signal

I want this repo to communicate a few things clearly:

- I do not quit when the prompt is unfamiliar.
- I can move from theory to implementation.
- I care about constraints and edge cases.
- I practice across domains instead of staying in one comfort zone.
- I am still learning, and I keep receipts.

## Next Improvements

- Add small test cases for the strongest solutions.
- Add complexity notes to the best solutions.
- Continue promoting files from `scratchpad/` into the main folders as they are cleaned up.
- Add short per-folder README files so each section has its own guide.

## Closing

This repository is not only a list of interview questions I succeeded on and failed through. It is artifact evidence of preparation, curiosity, resilience, and the ability to wrestle with hard problems until they become understandable.
