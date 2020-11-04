#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
//	freopen("2819.txt", "r", stdin);
	cin >> T;
	
    vector<vector<int>> move{
            {1, 4},     {0, 2, 5},      {1, 3, 6},      {2, 7},
            {0, 5, 8},  {1, 4, 6, 9},   {2, 5, 7, 10},  {3, 6, 11},
            {4, 9, 12}, {5, 8, 10, 13}, {6, 9, 11, 14}, {7, 10, 15},
            {8, 13},    {9, 12, 14},    {10, 13, 15},   {11, 14}
        };

	for(test_case = 1; test_case <= T; ++test_case)
	{
        vector<vector<vector<int>>> digit(7, vector<vector<int>>(16));
        for (int i=0;i<4;i++){
            int a, b, c, d;
            cin >> a >> b >> c >> d;
            digit[0][4*i].push_back(a);
            digit[0][4*i+1].push_back(b);
            digit[0][4*i+2].push_back(c);
            digit[0][4*i+3].push_back(d);
        }

        for (int i=1;i<7;i++){  // for each digit (2~7)
            for (int j=0;j<16;j++){     // for each cell
                for (int k=0;k<move[j].size();k++){     // for each adjacent cell
                    for (int l=0;l<digit[i-1][move[j][k]].size();l++){  // for each pre-costructed number
                        int temp = digit[0][j][0] * pow(10, i) + digit[i-1][move[j][k]][l];
                        vector<int>::iterator it = find(digit[i][j].begin(), digit[i][j].end(), temp);
                        if (it == digit[i][j].end()){
                            digit[i][j].push_back(temp);
                        }
                    }
                }
            }
        }

        vector<int> total;
        for (int j=0;j<16;j++){
            for (int m=0;m<digit[6][j].size();m++){
                vector<int>::iterator it = find(total.begin(), total.end(), digit[6][j][m]);
                if (it == total.end()){
                    total.push_back(digit[6][j][m]);
                }
            }
        }

        cout << "#" << test_case << " ";
        cout << total.size() << endl; 
	}
	return 0;
}
