#ifndef BLOCKCHAIN_H
#define BLOCKCHAIN_H
#endif
#include <stdio.h>
#include "openssl/crypto.h"

#define NB_TRANS 100

typedef enum { USER, SENSOR, MOTOR} e_node_type;
typedef enum  {SEND, GET, SET} e_trans_type;

typedef struct Node{
    int id ;
    e_node_type type;
    double param; // ; Sensors -> seuil/param; Act -> on=1/off=0
    double val; //  Ui-> presence(1/0) 
} s_node;
 
typedef struct transaction{
    int sender_id;
    int dest_id;
    time_t time;
    e_trans_type type_tr;
    float val;
} s_transaction;

typedef struct Block{
    unsigned char* prevHash;
    s_transaction** data; // tableau ou liste de transactions
    int proof_work;
    unsigned char* id_hash;
    time_t time;
    struct Block* nextBlock;
} s_bloc;

typedef struct Chain{
    s_bloc* head;
    s_bloc* current;
    int num_node;
} s_chain;


void init_chain(s_chain* chain);
s_bloc* initBlock(unsigned char* prevHash, s_bloc* bloc );
void addTransaction( s_chain* chain, int src, int dest, time_t t,e_trans_type type, float val);
s_bloc* addBlock(s_chain* chain);
short cerifyChain(s_chain* chain);
short block_isValid(s_bloc* b);
unsigned char* id_hash_gen(s_chain chain, s_bloc b);
int proof_work_gen(unsigned char* id_hash);
short checkProof(unsigned char* id_hash, int proof,unsigned char* strBloc);
void blockDataToString(s_bloc*b,unsigned char* strBlock);
s_bloc* closeBlock(s_chain* chain);
int hashCompare(unsigned char* h1, unsigned char* h2);

