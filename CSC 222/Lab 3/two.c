// Parsa Jahanlou
// Question 2
// Lab 3

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <time.h>

int main(int argc, char *argv[])
{  	
	// if there is only one argument
	if(argc < 2){
		printf("Usage: ./two <executable>\n");
		printf("e.g., ./two ./one\n");
		exit(1);
	}
	
	// forking 
	int cpid = fork();

	// printing out the child process ID
	if(cpid == 0){
		printf("In child %d: ",getpid());
		
		srand(time(0)); 
		
		int i, num; 
		int count = rand() % 10 + 1;
		
		char args[11][10];
		char *arg[11];
		strcpy(args[0], argv[1]);
		
		for(i = 1; i <= count; i++){
			num = (rand() % 10);
			sprintf(args[i], "%d", num); 
		}
		
		for(i = 0; i <= count; i++){
			arg[i] = args[i];
		}
		
		fflush(stdout);
		execvp(*arg, arg);
	} else{
		waitpid(cpid,NULL,0);
	}
	
    return 0;
}
