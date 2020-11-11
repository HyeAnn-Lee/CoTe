#include<iostream>
//#include <cstdio>
#include <set>

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

        set<int> score;
        score.insert(0);

        for (int i=0;i<problem;i++){
            set<int> temp(score);
            int point;
            cin >> point;
            set<int>::iterator iter = temp.begin();
            for (;iter != temp.end();iter++){
                score.insert(*iter + point);
            }
        }
        cout << "#" << test_case << " ";
        cout << score.size() << endl;
	}
	return 0;
}
