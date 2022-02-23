
#include "blockchain.h"
#include<string.h>


void init_chain(s_chain* chain){
    chain= (s_chain* ) malloc(sizeof(s_chain));
    
    unsigned char prevHash[100]="0000000000000000000000000";
    s_bloc* firstB;
    initBlock(prevHash, firstB);
   // firstB->nextBlock= NULL;
    chain->head=firstB;
    chain->current= firstB;
}

// oubli transaction_id
void addTransaction( s_chain* chain, int src,int dest, time_t t,e_trans_type type, float val){
    int i=0;
    s_bloc* bloc = chain->current;
    printf("%d\n",bloc->data[i]->sender_id);
    s_transaction* curr=bloc->data[i];
    
    while ( i<NB_TRANS && curr->sender_id != -1){
        i++;
    }
    if(i>=NB_TRANS){
         s_bloc* newBloc = closeBlock(chain);
         addTransaction(chain,src,dest,t,type,val);
    }
    else{
        curr->sender_id= src;
        curr->dest_id=dest;
        curr->time= t;
        curr->type_tr= type;
        curr->val= val;
    }
}

short cerifyChain(s_chain* chain){
    if (chain-> head==NULL){
        printf("Blockchin is empty! ");
        return 0;
    }

    s_bloc* curr = chain->head->nextBlock;
    s_bloc* prev = chain->head;
    int count=0;
    while (curr!=NULL){
        if(!hashCompare(curr->prevHash,prev->id_hash)){
            return 0;
        }
        prev=curr;
        curr=curr->nextBlock;
    }
    printf("chain verifed");
    return 1;
}





s_bloc* initBlock(unsigned char* prevHash, s_bloc* bloc ){
    bloc= (s_bloc* )malloc(sizeof(s_bloc));
    bloc->data=(s_transaction**) malloc(sizeof(s_transaction*)*NB_TRANS);
    bloc->prevHash = prevHash; // hashCopy()
    bloc->nextBlock= NULL;
    bloc-> time;

    for(int i=0;i<NB_TRANS; i++){
        bloc->data[i]=(s_transaction*) malloc(sizeof(s_transaction));
        bloc-> data[i]->sender_id=-1;
    }
    return bloc;
}

s_bloc* addBlock(s_chain* chain){
    s_bloc* newBloc;
    initBlock(chain->current->id_hash, newBloc);
    chain->current->nextBlock= newBloc;
    chain->current=newBloc;
    return newBloc;
}

unsigned char* id_hash_gen(s_chain chain,s_bloc b);
int mining(unsigned char* strBloc,  unsigned char* id_hash ){


};


void blockDataToString(s_bloc*b,unsigned char* strBlock){
    int i=0;
    s_transaction* curr= b->data[i];
     while ( i<NB_TRANS && curr->sender_id != -1){
        unsigned long seconds = difftime( curr->time, 0 );
        char c_tr[200];
        
        char val[6];
        gcvt(curr->val, 3, val);
        sprintf(c_tr, "%d,%d,%ld,%s,%s-", curr->sender_id,curr->dest_id,seconds,(char*)curr->type_tr,val); 
        strcat(strBlock,c_tr);
        i++;
        curr= b->data[i];
    }
}

s_bloc* closeBlock(s_chain* chain){
    s_bloc* b =chain->current;
    if(block_isValid(b)){
        unsigned char strBlock[2000]; // redef size
        blockDataToString(b,strBlock);
        unsigned char* id_hash;
        short proofIsValid = 0;
        int proof=0;
        while (proofIsValid!=1){
            int proof = mining(strBlock,id_hash);
            proofIsValid = checkProof(id_hash,proof,strBlock);
        }
        b->id_hash= id_hash;
        b->proof_work=proof;

         // send validation of the proof
        return (addBlock(chain));
    }
    return NULL;
}

short block_isValid(s_bloc* b){
    return 1;
}


int hashCompare(unsigned char* h1, unsigned char* h2){
    return 1;
};
short checkProof(unsigned char* id_hash, int proof,unsigned char* strBloc){
    return 1;
};



