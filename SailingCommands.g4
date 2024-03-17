grammar SailingCommands;

// Tokeny
PERCENT : 'pół' ;
FULL : 'cała' ;
FORWARD : 'przód' ;
BACKWARD : 'wstecz' ;
WS : [ \t\r\n]+ -> skip ;

// Reguły parsera
command : direction amount ;
direction : FORWARD | BACKWARD ;
amount : PERCENT | FULL ;
