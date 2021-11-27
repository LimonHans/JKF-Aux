/*
HansLimon in 2021

Only for educational usages

CopyLEFT Mongrokey
*/
#include <ctime>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <iostream>
#include <windows.h>
using namespace std;

int aft, counter;
string names[]{};
vector<string> corder;

int main(){
	for (register int i = 0;i < 49;i ++)corder.push_back(names[i]);
//	HWND console_checker = FindWindow("ConsoleWindowClass", NULL);
//	if (console_checker)
//		ShowWindow(console_checker, SW_HIDE);
	srand(time(NULL));
	while (aft = rand()%corder.size(), MessageBox(NULL, corder[aft].c_str(), "达摩克利斯之剑——不重复", MB_RETRYCANCEL + 64) == 4){
		srand(rand()^time(NULL));
		//printf("removing num: %i, cal: %s\n", aft, corder[aft].c_str());
		corder.erase(corder.begin() + aft);
		//printf("now is: %s\n", corder[aft].c_str());
		if (++ counter == 49){
			MessageBox(NULL, "所有人已抽取完毕", "达摩克利斯之剑——不重复", MB_OK + 48);
			break;
		}
	}
	return 0;
}
