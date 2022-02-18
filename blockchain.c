
#include "blockchain.h"

void addTransaction(s_transaction trans, s_block* block){
}

short cerifyChain(s_block* chain){
    if (chain-> head==NULL){
        printf("Blockchin is empty! ");
        return 0;
    }

    s_block* curr = chain->head->nextBlock;
    s_block* prev = chain->head;
    int count=0;
    while (curr){
        if(!hashCompare(curr->prevHash,prev)){
            return 0
        }
        prev=curr;
        curr=curr->nextBlock;
    }
    printf("chain verifed");
    return 1;
}

int hashCompare();



