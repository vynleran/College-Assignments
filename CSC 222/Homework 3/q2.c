// Parsa Jahanlou
// Homework 3
// CSC 222
// Due November 13th, 2020

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
	if(argc < 2){
		printf("Usage: ./q2 <dir>\n");
		exit(1);
	}
	
	char pwd[200];
	
	int cpid = fork();

	if(cpid == -1){
		// if fork failed
		fprintf(stderr, "Failed to create process\n");
	} else if(cpid == 0){
		// fork success
		getcwd(pwd, sizeof(pwd));
	
		printf("Current working directory: %s\n",pwd);
		printf("Executing ls %s --all -l --human-readable\n",argv[1]);
	
		if(chdir(argv[1]) != 0) {
			printf("Can't chdir to %s\n",argv[1]);
			exit(1);
		}
		
		// execute the external command using execlp
		execlp("ls", argv[1], "--all", "-l", "--human-readable", NULL);
	} else{
		// wait for child process
		waitpid(cpid,NULL,0);
	}
	
    return 0;
}
