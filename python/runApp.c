#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "runApp.h"

void runFile(char* filename){
    setPermissions(filename);
    char* command;
    command = malloc(sizeof(char)*200);
    strcat(command,"./files/");
    strcat(command,(char*)filename);
    system(command);
}

void setPermissions(char* filename){
    char* command;
    command = malloc(sizeof(char)*200);
    strcat(command,"chmod 770 ./files/");
    strcat(command,(char*)filename);
    system(command);

}