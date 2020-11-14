#include<iostream>
//#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
//	freopen("3752.txt", "r", stdin);
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
        int problem;
        cin >> problem;

        vector<int> points(problem);
        int maxpoint = 0;
        for (int i=0;i<problem;i++){
            int point;
            cin >> point;
            points[i] = point;
            maxpoint += point;
        }
        int vecsize = maxpoint/2 + 1;
        vector<bool> score(vecsize, false);
        score[0] = true;
        for (int i=0;i < problem;i++){
            for (int j = vecsize - 1; j>=0; j--){
                int point = points[i];
                if (score[j]){
                    if ((j + point) < vecsize)
                        score[j + point] = true;
                }
            }
        }

        int size = 2 * count(score.begin(), score.end(), true);
        if ((maxpoint % 2) == 0){
            if (score[vecsize-1])
                size--;
        }

        cout << "#" << test_case << " ";
        cout << size << endl;
	}
	return 0;
}
