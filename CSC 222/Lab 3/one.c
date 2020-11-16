// Parsa Jahanlou
// Question 1
// Lab 3

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
	
	// if there is only one argument
	if(argc < 2){
		printf("Usage: ./one val [val [ ... ] ]\n");
		printf("e.g., ./one 17 49 3 466\n");
		return 0;
	}
	
	int i, product =1;
	
	// calculating the results 
	for(i = 1; i < argc; i++){
		product *= atoi(argv[i]);
	}
	
	// outputting the results
	printf("The product of ");
	for(i = 1; i < argc; i++){
		printf("%d ", atoi(argv[i]));
	}
	
	printf("is %d\n",product);
	
	
	return 1;
}
