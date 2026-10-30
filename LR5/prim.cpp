#include <iostream>
#include <cstring>
using namespace std;
#define INF 9999999
// number of vertices in grapj
#define V 8
// create a 2d array of size 6x6
//for adjacency matrix to represent graph
int G[V][V] = {
    {INF, 2, 7, 5, INF, INF, 10, INF},
    {2, INF, INF, INF, 5, INF, INF, INF},
    {7, INF, INF, INF, INF, 5, 9, INF},
    {5, INF, INF, INF, 6, 4, 4, INF},
    {INF, 5, INF, 6, INF, 3, INF, 3},
    {INF, INF, 5, 4, 3, INF, INF, 1},
    {10, INF, 9, 4, INF, INF, INF, 6},
    {INF, INF, INF, INF, 3, 1, 6, INF},
    };
int main () {
    int no_edge; // number of edge
    // create a array to track selected vertex
    // selected will become true otherwise false
    int selected[V];
    // set selected false initially
    memset (selected, false, sizeof (selected));
    // set number of edge to 0
    no_edge = 0;
    // the number of egde in minimum spanning tree will be
    // always less than (V -1), where V is number of vertices in
    //graph
    // choose 0th vertex and make it true
    selected[0] = true;
    int x; // row number
    int y; // col number
    // print for edge and weight
    cout << "Edge" << " : " << "Weight";
    cout << endl;
    while (no_edge < V - 1) {
        //For every vertex in the set S, find the all adjacent vertices
        // , calculate the distance from the vertex selected at step 1.
        // if the vertex is already in the set S, discard it otherwise
        //choose another vertex nearest to selected vertex at step 1.
        int min = INF;
        x = 0;
        y = 0;
        for (int i = 0; i < V; i++) {
            if (selected[i]) {
                for (int j = 0; j < V; j++) {
                    if (!selected[j] && G[i][j]) { // not in selected and there is an edge

                        if (min > G[i][j]) {
                            min = G[i][j];
                            x = i;
                            y = j;
                        }

                    }
                }

            }
        }

        cout << x+1 << " - " << y+1 << " : " << G[x][y];
        cout << endl;

        selected[y] = true;
        no_edge++;

    }

    return 0;
}