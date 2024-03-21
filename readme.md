# Sailing Commands Interpreter
### MIASI Project based on Python and ANTLR4 languages.


## How to compile g4 file
Type command:

`antlr4 -v 4.13.0 -Dlanguage=Python3 -visitor -o gen grammar.SailingCommands.g4` 


## How to insert commands
Insert commands  by adding them to `input.txt` file

## List of commands
A list of words from naval commands in Polish:

**Speed**
- silnik - silnik (słowo kluczowe przed podaniem prędkości)
- awaryjna - na 100% mocy
- cała - na 80% mocy
- manewrowa - na 60% mocy
- pół - na 40% mocy
- wolna - na 20% mocy

**Direction**
- ster - ster (słowo kluczowe przed podaniem kierunku)
- lewo - w lewo na 50%
- lewo na burt - maksymanie w lewo (na 100%)
- prawo - w prawo na 50%
- prawo na burt - maksymalnie w prawo (na 100%)
- ostrzyć - sterować łodzią bardziej pod wiatr
- odpadać - sterować łodzią bardziej z wiatrem



**Sails commands**
- żagle - żagle (słowo kluczowe przed podaniem polecenia do żagli)
- do zwrotu przez rufę - przygotować się do zwrotu pod wiatr
- do zwrotu przez sztag - przygotować się do zwrotu z wiatrem
- kotwicę wybieraj - wyciągnij kotwicę
- staw - postaw w górę



**Others (unsupported)**

alarm - alarm

bardziej - bardziej

basta - położyć na ławkach

bosak - kij z metalowym kolcem i hakiem

burcie - burcie

burtą - burtą

burtę - burtę

burty - burty

chroń - ubezpieczej

cumę - linę do wiązania łodzi

cumy - liny do wiązania łodzi

człowiek - człowiek

człowieka - człowieka

człowiekowi - człowiekowi

desant na ląd - przywiązujący łódź przygotować do zejscia na pomost/ląd

desant na pokład - przywiązujący łódź przygotować się na pokładzie

do - do

do baksztagu - sterować łodzią ukośnie z wiatrem

do bejdewindu - sterować łodzią ukośnie pod wiatr

do fordewindu - sterować łodzią równolegle z wiatrem

do linii wiatru - sterować łodzią równolegle pod wiatr

do łodzi - wejść do łodzi

do półwiatru - sterować łodzią prostopadle do wiatru

dość - przestać

dziobowa - przy dziobie

dziób - dziób

fok - tylny żagiel

foka - tylny żagiel

foka szot - linę tylnego żagla

grot - przedni żagiel

grota - przedni żagiel

grota szot - linę przedniego żagla

hals - strona, z której wieje wiatr

hamuj - hamuj

i - i

klar na cumach - przywiązać liny do wiązania łodzi

Klar postojowy. - Jesteśmy przygotowani do postoju.

kop - przygazować

kotwicę - kotwicę i linę kotwiczną

Kula na sztag. - Ustawienie dziennego sygnału postojowego.

lekko - lekko

lewa - z lewej burty

lewej - lewej

lewo na wodę - ma mieć wodę z lewej strony

lewy - lewy/lewą

luz - poluzuj do końca

luzuj - poluzuj częściowo

maszt - maszt

mniej - mniej

na biegowo - nałożyć na narzęcia do przywiązyawania

na boję - nałożyć na boję

na keję - wciągnąć na pomost/ląd

na lewą burtę - założyć na lewą burtę

na pokład - wciągnąć na pokład

na prawą burtę - założyć na prawą burtę

na pych - do wypchnięcia łodzi z mielizny, opierając o dno

na wiatr - ustaw tak, aby łapał wiatr

naprzód - do przodu

niezbędnej - niezbędnej

obie - z obu stron

obłóż - przywiązać do narzęcia do przywiązyawania

obsada - obsadzający stanowiska

odbijaczach - odbijaczach

odbijacze - gumowe lub plastikowe zabezpieczenia burt

oddaj - oddaj

oddania - podania

odstaw - wyłączyć i zabezpieczyć



pod - pod

podać - podać

podaj - podaj

podjąć - wyciągnąć

podjęcia - wyciągnięcia

pokład - pokład

pomocy - pomocy

postawienia - postawienia

prawa - z prawej burty

prawo na wodę - ma mieć wodę z prawej strony

prawy - prawy/prawą

precz - zrzuć w dół

przy - przy

przygotować - przygotować

ratunkowe - ratunkowe

rufa - rufa

rufowa - przy rufie

rwij - mocno pociągnij

rzucenia - rzucenia

rzuć - rzuć

rzuć - opuśić za burtę

się - się

sklarować - przygotować do schowania

skróć - przesunąć na trzymakach do wnętrza łodzi i oprzeć rękojeścią o drugą burtę

spław - trzymać wewnętrzną ręką poza burtą, zwrócone rękojeścią ku dziobowi

stanowiska - stanowiska

stawienia - postawienia w górę

ster - ster

sternik - sternik

stop - zatrzymać

środki - środki

Światło kotwiczne włącz. - Ustawienie nocnego sygnału postojowego.

Tak stoimy. - Zakończyć działania zwiazane z postojem.

tak trzymać - utrzymać w tej pozycji

udzielić - udzielić

uruchom - uruchomić

uruchomienia - uruchomienia

wiosła - włożyć wiosła do trzymaków

wiosła (podczas wiosłowania) - przestać wiosłaować

wiosła chwyć - przygotować trzymaki do wioseł i ustawić wiosła prostopadle do burty

wiosła na wiatr - wiosła prostopadle do wody



wstecz - do tyłu

wybieraj - pociągnij częściowo

wybierz - pociągnij do końca

wyrzuć - wrzucić maksymalnie

wzwyż - postawić rekojeścią na dnie łodzi, trzymając zewnętrzną reką na wysokości barku i wewnętrzną na wysokości kolan

X, obserwator na człowieka - X, masz pilnować pozycji człowieka za burtą

z łodzi - wyjść z łodzi

za - za

załoga - załoga

zero - prostopadle do łodzi

złożenia - złożenia

zrzucenia - zrzucenia w dół


