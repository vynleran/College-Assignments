// Parsa Jahanlou

// importing the necessary libraries
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 100

// function for the tokens
void print_count_token(char input[]){
    int counter = 0;
    int len = strlen(input);
    char *token = (char*)malloc((len+1) * sizeof(char));
    int tok_size = 0;
    printf("Token(s) :\n");
    // going through what the user has put in
    for(int i = 0; i <= len; i++){
        if(input[i] == ' ' || input[i] == '\0'){
            token[tok_size] = '\0';
            counter++;
            printf("%s\n",token);
            tok_size = 0;
        }
        else{
            token[tok_size++] = input[i];
        }
    }
    printf("%d token(s) read\n\n",counter);
}

// the main function to execute everything
int main(void)
{
    char input[MAX];
    while(1){
        printf("$ ");
        fgets(input, MAX, stdin);
        if(strcmp(input, "exit\n") == 0 || strcmp(input, "exit\r") == 0 || strcmp(input, "exit") == 0){
            break;
        }
        printf("Line read: %s\n", input);
        print_count_token(input);
    }
    return 0;
}