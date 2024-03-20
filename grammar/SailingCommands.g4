grammar SailingCommands;

prog: stat* EOF;

stat: command;

// Reguły parsera
command : amount SPACE direction
        | direction SPACE amount
;
direction : FORWARD | BACKWARD ;
amount : PERCENT | FULL ;

// Tokeny
PERCENT : 'pół' ;
FULL : 'cała' ;
FORWARD : 'przód' ;
BACKWARD : 'wstecz' ;

SPACE: ' ';

//NEWLINE : [\r\n]+ -> skip;
NEWLINE : [\r\n]+ -> channel(HIDDEN);

//WS : [ \t]+ -> skip ;
WS : [ \t]+ -> channel(HIDDEN) ;

INT     : [0-9]+ ;


ID : [a-zA-Z_][a-zA-Z0-9_]* ;

COMMENT : '/*' .*? '*/' -> channel(HIDDEN) ;
LINE_COMMENT : '//' ~'\n'* '\n' -> channel(HIDDEN) ;
