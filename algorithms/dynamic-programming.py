"""Dynamic programming: divide into smaller sub problems, remember them, reuse them, examine previous results,
combine then to find the best solution.

Focuses on overall optimization as opposed to the greedy algorithm (local).

Memorizes divided sub problem output / solution, optimize for a bigger problem (different than divide and conquering)

e.g. Dijkstra Shortest Path

A - B = 2
B - D = 6
2 + 6 = 8 to go from A - D

A - D through path C is simply just 7

7 < 8 so use path C to go directly to D now. Update A-D path length to 7 instead of 8."""