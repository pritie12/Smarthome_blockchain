
#include <stdio.h>
#include "openssl/crypto.h"

typedef enum { UI, SENSOR, MOTOR} e_node_type;
typedef enum  {SEND, GET, SET} e_trans_type;

typedef struct Node{
    int id ;
    enum node_type type;
    double param; // ; Sensors -> seuil/param; Act -> on=1/off=0
    double val; //  Ui-> presence(1/0) 
} s_node;

typedef struct Block{
    unsigned char prevHash[SHA_DEGEST_LENGHT];
    s_transaction data[100]; // tableau ou liste de transactions
    int proof_work;
     unsigned char id_hash[SHA_DEGEST_LENGHT];
    time_t timeStamp;
    s_bloc* nextBlock;
} s_bloc;

typedef struct Chain{
    s_bloc* head;
    s_bloc* current;
    int num_node;
} s_chain;
 
typedef struct transaction{
    int sender_id;
    int dest_id;
    time_t time;
    e_trans_type transaction;
    int val;
} s_transaction;


void init_chain(s_chain* chain);
void addTransaction();
void addBlock(s_bloc previous);

short cerifyChain(s_bloc* chain)
short block_isValid(s_bloc);
unsigned char* id_hash_gen(s_bloc b);
int proof_work_gen(unsigned char* id_hash);
short checkProof(unsigned char* id_hash, int proof);

