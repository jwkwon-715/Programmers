#include <iostream>

using namespace std;
int solution(int n)
{
    int answer = 0;
    while(true){
        if(n>0){
            answer += n%10;
            n=n/10;
        }
        else break;
    }

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    cout << "Hello Cpp" << endl;

    return answer;
}