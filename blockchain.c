
#include "blockchain.h"

void addTransaction(s_transaction trans, s_bloc* block){
}

short cerifyChain(s_chain* chain){
    if (chain-> head==NULL){
        printf("Blockchin is empty! ");
        return 0;
    }

    s_bloc* curr = chain->head->nextBlock;
    s_bloc* prev = chain->head;
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

void init_chain(s_chaine* chain){
    chain= (s_chaine*) malloc(sizeof(s_chain));
    s_bloc* firstB= (s_bloc* )malloc(sizeof(s_bloc));
    firstB->prevHash="0000000000000000000000000";
    firstB->nextBlock= NULL;
    chain->head=firstB;
    chain->current= firstB;

}
void addTransaction();

s_bloc* initBlock(unsigned char prevHash[SHA_DEGEST_LENGHT] ){
    s_bloc* bloc= (s_bloc* )malloc(sizeof(s_bloc));
    bloc->prevHash = prevHash; // hashCopy()
    bloc->nextBlock= NULL;
    return bloc;

}

void addBlock(s_chain chain){
    s_bloc* newBlock = initBlock(chain->current->id_hash);
    chain->current->nextBlock= newBlock;
    chain->current=newBlock;
}

unsigned char* id_hash_gen(s_bloc b);
int proof_work_gen(unsigned char* id_hash);
short checkProof(unsigned char* id_hash, int proof);



