

Enum node_type : Ui; Sensor, Actuator
Enum trans_type: Send , Get , Set

Struct Node{
    Int id ;
    Node_type type;
    Double param; // ; Sensors -> seuil/param; Act -> on=1/off=0
    double val; //  Ui-> presence(1/0) 
}
Struct Block{
    Previous hash
    Data // tableau ou liste de transactions
    Int Proof_work
    Id_hash
    TimeStamp
}

Struct Chain{
    Block* first;
    Block* last;
    Int num_node
}
 
Struct transaction{
    Sender_id;
    Dest_id;
    Transaction_type;
    Int val
}
