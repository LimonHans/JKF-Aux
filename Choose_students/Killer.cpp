/*
HansLimon in 2021

Only for educational usages

CopyLEFT Mongrokey
*/
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <windows.h>
using namespace std;

int bef = -1, aft;
string names[]{};

int main(){
//	HWND console_checker = FindWindow("ConsoleWindowClass", NULL);
//	if (console_checker)
//		ShowWindow(console_checker, SW_HIDE);
	srand(time(NULL));
//	MessageBox(NULL, names[2].c_str(), "Test_2", MB_RETRYCANCEL + 64);
	while (aft = rand()%49, aft == bef || MessageBox(NULL, names[aft].c_str(), "达摩克利斯之剑", MB_RETRYCANCEL + 64) == 4){
		srand(rand()^time(NULL));
		bef = aft;
	}
	return 0;
}
