// Parsa Jahanlou

// necessary libraries
#include <stdio.h>
#define PD '#'
#define MAX 500

// main function
int main(){
    int x;
    int num = 0;
    char character[MAX];
    bool noPD = (x = getchar()) != PD;

    printf("Enter some characters and end all of them with #:\n");

    while(noPD) {
        //condition for empty spaces
        if(x =='\n' || x =='') {
            continue;
        }
        // max condition
        if(num >= MAX){
            break;
            character[n++] = x;
        }
        // printing the output for the user
        for(int i=0;i<num;i++) {
            printf("%c:%3d", character[i], character[i]);
            if(i % 8 == 7) {
                printf("\n");
            }
        }
        printf("\n\n");
        return 0;
    }
}