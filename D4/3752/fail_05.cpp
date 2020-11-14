#include<iostream>
//#include <cstdio>
#include <set>
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

        int maxpoint = 0;
        vector<int> points(problem);
        for (int i=0;i<problem;i++){
            int point;
            cin >> point;
            points[i] = point;
            maxpoint += point;
        }
        sort(points.begin(), points.end());

        set<int> score {0};
        int size;
        bool half = false;

        for (int i=0;i<problem;i++){
            set<int> temp(score);
            set<int>::iterator iter = temp.begin();
            for (;iter != temp.end();iter++){
                int cal = *iter + points[i];
                if (2 * cal < maxpoint){
                    score.insert(cal);
                    continue;
                }
                if (2*cal == maxpoint)
                    half = true;
                if (i != problem-1){
                    break;
                }
                size = 2 * score.size();
                if (half) size++;
                break;
            }
        }

        cout << "#" << test_case << " ";
        cout << size << endl;
	}
	return 0;
}
