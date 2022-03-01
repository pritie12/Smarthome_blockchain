#include "blockchain.h"
#include <stdio.h>




int main (){
    printf("Hello \n");
    s_chain chain;
    printf("init chain\n");
    init_chain(&chain);
    printf("transaction 1\n");
    
    /*addTransaction(&chain,1,2,time(NULL),GET,0);
    printf( "transaction 2\n");
    addTransaction(&chain,2,1,time(NULL),SEND,0.5);

    s_bloc* b= chain.current;
    unsigned char strBlock[2000];
    blockDataToString(b,strBlock);
    printf("%s",strBlock);*/

    return 0;
}