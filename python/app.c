#include <stdio.h>
#include <sys/resource.h>
#include <sys/time.h>
#include <unistd.h>

int main() {
    for (size_t i = 0; i < 100000; i++)
    {
        sleep(10);
        //printf("hola mundo \n");
    }
    
    
}