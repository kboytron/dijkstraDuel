
# Dijkstra Duel

A project comparing two implementations of Dijkstra's shortest-path algorithm. The project analyzes performance differences between a classic vanilla version and an optimized version that uses a priority queue.

## Features
- **Vanilla Dijkstra's Algorithm:** Uses a linear search to find the minimum distance vertex.
- **Optimized Dijkstra's Algorithm:** Uses a priority queue for efficient vertex selection.
- **Performance Comparison:** Runtime analysis between the two versions with theoretical justifications.

## Technology
- **Language:** Python 3
- **Key Concepts:** Graph Algorithms, Priority Queue, Performance Optimization
- **Tools:** Python Standard Library

## Project Structure
- `dijkstra_vanilla.py`: Implementation of the vanilla version of Dijkstra's algorithm.
- `dijkstra_optimized.py`: Implementation of the optimized version using a priority queue.
- `graph_testcase.txt`: Input graph file for testing.

## Setup & Run Instructions
1. Clone the repository.
2. Ensure Python 3 is installed.
3. Run the vanilla version:
   ```sh
   python dijkstra_vanilla.py
   ```
4. Run the optimized version:
   ```sh
   python dijkstra_optimized.py
   ```

## Usage Example
Modify the `graph_testcase.txt` to test with custom graphs. Results will display shortest-path distances from the source node to all other nodes.

## License
This project is for educational purposes. Modify and use it freely for learning.
