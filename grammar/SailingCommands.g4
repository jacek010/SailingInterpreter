grammar SailingCommands;

prog: stat* EOF;

stat: command;

//keywords :

// Reguły parsera
command : speed SPACE direction
        | direction SPACE speed
;

direction : STERE | LEFT_2 | RIGHT_2 | FORWARD | BACKWARD ;
speed : ENGINE | EMERGENCY | FULL | MANEUVERING | HALF | SLOW | STOP | BRAKE | SPEEDING ;
maneuvering_commands : READY | MAINSAIL | FORSAIL | OARS | ANCHOR_0 | HAWSER | HAWSERS_0 | HAWSERS_1 | BOW_0 | LEFT_0 | RIGHT_0 | STERN_0 | RUN_0 | SAILS;
others : ALARM | LIGHT | LIKE_THAT | SECURE | MAN_0 | LANDING_CREW | ENOUGH_ | BALL | HELMSMAN | PROVIDE | CREW ;
prepositions : TO | ON | BY | AND | INTO | FOR ;

// Tokeny
ALARM : 'alarm' ;
HALF : 'pół' ;
FULL : 'cała' ;
FORWARD : 'przód' ;
BACKWARD : 'wstecz' ;
READY : 'przygotować' ;
MAINSAIL : 'grot' ;
FORSAIL : 'fok' ;
TO : 'do' ;
CLAR : 'klar' ;
ANCHOR_0 : 'kotwicę' ;
ON : 'na' ;
LIGHT : 'świetło' ;
LIKE_THAT : 'tak' ;
OARS : 'wiosła' ;
OUT_OF_BOAT : 'z łodzi' ;
EMERGENCY : 'awarynjna' ;
MORE_ : 'bardziej' ;
ENOUGH : 'basta' ;
SIDE_0 : 'burta' ;
SIDE_1 : 'burcie' ;
SIDE_2 : 'burty' ;
SECURE : 'chroń' ;
HAWSER : 'cumę' ;
HAWSERS_0 : 'cumy' ;
HAWSERS_1 : 'cumach' ;
MAN_0 : 'człowiek' ;
MAN_1 : 'człowieka' ;
TO_MAN : 'człowiekowi' ;
LANDING_CREW : 'desant' ;
LAND : 'ląd' ;
BOARD : 'pokład' ;
BACKSTAY : 'baksztagu' ;
BAJDEWIND : 'bajdewindu' ;
LINE : 'lini' ;
WIND : 'wiaru' ;
BOAT : 'łodzi' ;
HALF_WIND : 'half wind' ;
ABOW : 'zwrotu' ;
BY : 'przez' ;
ENOUGH_ : 'dość' ;
BOW_1 : 'dziobowa' ;
BOW_0 : 'dziób' ;
STRING : 'szot' ;
TACK : 'hals' ;
BRAKE : 'hamuj' ;
AND : 'i' ;
PARKING : 'postojowy' ;
SPEEDING : 'kop' ;
BALL : 'kula' ;
FORSTAY : 'sztag' ;
LIGHTLY : 'lekko' ;
LEFT_1 : 'lewej' ;
LEFT_SIDE : 'lewa' ;
LEFT_2 : 'lewo' ;
SIDE_3 : 'burt' ;
WATER : 'wodę' ;
LEFT_0 : 'lewy' ;
LOOSEN : 'luz' ;
LOOSEN_PARTIALLY : 'luzuj' ;
MANEUVERING : 'manewrowa' ;
MAST : 'maszt' ;
LESS : 'mniej' ;
OVERLAPPING : 'biegowo' ;
BOUY : 'boję' ;
QUAY : 'keja' ;
LEFT_3 : 'lewą' ;
RIGHT_3 : 'prawą' ;
PUSHING : 'pych' ;
NECESSARY : 'niezbędnej' ;
BOTH : 'obie' ;
PUT_ON : 'obłóż' ;
TASK_STAFF : 'obsada' ;
FENDERS_1 : 'odbijaczaj' ;
FENDERS_0 : 'odbijacze' ;
GIVE_0 : 'oddaj' ;
GIVE_1 : 'oddania' ;
FALL_OFF : 'odpadać' ;
SET_ASIDE : 'odstawić' ;
EDGE : 'ostrzyć' ;
INTO : 'pod' ;
PASS_0 : 'podać' ;
PASS_1 : 'podaj' ;
PICK_UP_0 : 'podjąć' ;
PICK_UP_1 : 'podjęcia' ;
HELP : 'pomocy' ;
SET_2 : 'postawienia' ;
RIGHT_1 : 'prawa' ;
RIGHT_2 : 'prawo' ;
RIGHT_0 : 'prawy' ;
AWAY : 'precz' ;
RESCUE : 'ratunkowe' ;
STERN_0 : 'rufa' ;
STERN_1 : 'rufowa' ;
YANK : 'rwij' ;
THROW_1 : 'rzucenia' ;
THROW_0 : 'rzuć' ;
SELF : 'się' ;
ENGINE : 'silnik' ;
CLARIFY : 'sklarować' ;
SHORTEN : 'skróć' ;
RAFTING : 'spław' ;
STATIONS : 'stanowiska' ;
SET_0 : 'staw' ;
SET_1 : 'stawienia' ;
STERE : 'ster' ;
HELMSMAN : 'sternik' ;
STOP : 'stop' ;
EQUIPMENT : 'środki' ;
ANCHOR_1 : 'kotwiczne' ;
TURN_ON : 'włącz' ;
STAY : 'stoimy' ;
KEEP : 'trzymać' ;
PROVIDE : 'udzielić' ;
RUN_0 : 'uruchom' ;
RUN_1 : 'uruchomienia' ;
GRAB : 'chwyć' ;
SLOW : 'wolna' ;
PULL_UP_0 : 'wybieraj' ;
PULL_UP_1 : 'wybierz' ;
THROW_2 : 'wyrzuć' ;
UPWARDS : 'wzwyż' ;
FOR : 'za' ;
CREW : 'załoga' ;
ZERO : 'zero' ;
FOLD : 'złożenia' ;
THROW_3 : 'zrzucenia' ;
SAILS : 'żagle' ;




SPACE : ' ';

//NEWLINE : [\r\n]+ -> skip;
NEWLINE : [\r\n]+ -> channel(HIDDEN);

//WS : [ \t]+ -> skip ;
WS : [ \t]+ -> channel(HIDDEN) ;

INT     : [0-9]+ ;


ID : [a-zA-Z_][a-zA-Z0-9_]* ;

COMMENT : '/*' .*? '*/' -> channel(HIDDEN) ;
LINE_COMMENT : '//' ~'\n'* '\n' -> channel(HIDDEN) ;