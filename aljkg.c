#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    int num1, num2;
    printf("Enter two integers: ");
    scanf("%d %d", &num1, &num2);

    int fd1[2], fd2[2];

    if (pipe(fd1) == -1 || pipe(fd2) == -1) {
        perror("pipe");
        exit(EXIT_FAILURE);
    }

    pid_t pid1 = fork();
    if (pid1 < 0) {
        perror("fork");
        exit(EXIT_FAILURE);
    }

    if (pid1 == 0) {
        close(fd1[0]); 
        int sum = num1 + num2;
        write(fd1[1], &sum, sizeof(sum));
        close(fd1[1]); 
        exit(EXIT_SUCCESS);
    } else {
        pid_t pid2 = fork();
        if (pid2 < 0) {
            perror("fork");
            exit(EXIT_FAILURE);
        }

        if (pid2 == 0) {
            close(fd2[0]); 
            int product = num1 * num2;
            write(fd2[1], &product, sizeof(product));
            close(fd2[1]);
            exit(EXIT_SUCCESS);
        } else {
            close(fd1[1]); 
            close(fd2[1]); 

            int sum, product;
            read(fd1[0], &sum, sizeof(sum));
            read(fd2[0], &product, sizeof(product));

            close(fd1[0]);
            close(fd2[0]);
            wait(NULL);
            wait(NULL);

            int result = sum + product;
            printf("%d\n", result);
        }
    }

    return 0;
}
