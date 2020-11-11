#include <iostream>
//#include <cstdio>
#include <vector>
#include <set>

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
        set<int> total;
        vector<vector<set<int>>> digit(7, vector<set<int>>(16));
        for (int i=0;i<4;i++){
            int a, b, c, d;
            cin >> a >> b >> c >> d;
            digit[0][4*i].insert(a);
            digit[0][4*i+1].insert(b);
            digit[0][4*i+2].insert(c);
            digit[0][4*i+3].insert(d);
        }

        for (int i=1;i<7;i++){  // for each digit (2~7)
            for (int j=0;j<16;j++){     // for each cell
                for (int k=0;k<move[j].size();k++){     // for each adjacent cell
                    set<int>::iterator iter = digit[i-1][move[j][k]].begin();
                    for (; iter != digit[i-1][move[j][k]].end(); iter++){   // for each pre-costructed numbe
                        int temp = *(digit[0][j].begin()) + (*iter)*10;
                        digit[i][j].insert(temp);
                        if (i == 6) total.insert(temp);
                    }
                }
            }
        }
        cout << "#" << test_case << " ";
        cout << total.size() << endl;
	}
	return 0;
}
