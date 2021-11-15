# Maximise-The-Bridges

## Maximise the bridges Problem Code: MAXBRIDGE Solved Submit (Practice)
Read problem statements in Bengali, Russian, Mandarin and Vietnamese as well.
Chef is given two integers N
 and M
. Please help Chef find any connected undirected graph G
 consisting of exactly N
 vertices and M
 edges, such that the number of bridges in G
 is maximized (among all graphs with N
 vertices and M
edges). G
 cannot have self-loops or multiple edges.

If there is more than one connected undirected graph with the maximum number of bridges, you may print any one of them.

Note: A bridge is an edge whose removal increases the number of connected components of the graph.

## Input Format
The first line of input contains a single integer T
, denoting the number of test cases. The description of T
 test cases follows.
Each testcase consists of a single line of input, containing two integers N,M
 - the number of vertices and edges of the graph you must construct.
## Output Format
For each test case, output M
 lines where the i
-th line contains two space-separated integers denoting the i
-th edge of the graph G
 you constructed. The edges may be printed in any order, and for each edge the endpoints may be printed in any order.

Note that G
 must not contain self-loops or multiple edges, and no other graph on N
 vertices and M
 edges can contain strictly more bridges than G
.

## Constraints
1≤T≤103
2≤N≤103
N−1≤M≤min(N⋅(N−1)/2,105)
Sum of N
 over all test cases do not exceed 103
Sum of M
 over all test cases do not exceed 105
Subtasks
Subtask 1 (100 points): Original constraints
## Sample Input 1 
 3
4 4
5 4
3 3
## Sample Output 1 
 1 2
2 3
3 4
1 3
1 2
2 3
3 4
4 5
1 2
2 3
3 1
