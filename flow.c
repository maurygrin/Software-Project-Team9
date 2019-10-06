#include <stdio.h>
#include <string.h>
int main(){
    int result;
    string variable3 = "hi"
    printf("How much is 3+3?\n");
    scanf("%d", &result);
    if(result == 6) {
        printf("How much is 3*3?\n");
        scanf("%d", &result);
        if(result == 9) {
            printf("How much is 3*1?\n");
            scanf("%d", &result);
            if(result == 3) {
                printf("Ah Perro\n");
                return 0;
            }
            else {
                printf("No\n");
                return 0;
            }
        }
        else {
            printf("No\n");
            return 0;
        }
    }
    else {
        printf("No\n");
        return 0;
    }

}
