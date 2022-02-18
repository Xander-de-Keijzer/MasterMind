Filter out posible answers based on any answers given

G = Guess 
A = Answer (Black,White)

> Color filtering

G: AABB A: (0,1)
From this you can conclude that the answer should contain either A or B,
all answers that do NOT contain either A or B are no longer possible.

G: ABCD A: (0,1)
All ansers NOT containing either A|B|C|D can be filtered out

> Positional filtering

G: ABCD A: (1,0)

The answer MUST yield true for one and ONLY ONE of these conditions where X can be any color

AXXX
XBXX
XXCX
XXXD

> Conlusion:

From these examples we can create universal rules for any amount of black or white pegs

> Universal Positional Filter

G: ABCD A: (n,*)

The answer must yield true for n of these conditions
AXXX | XBXX | XXCX | XXXD

> Universal Color Filter

G: ABCD A: (*,n)

There a 4 conditions:
Contains A
Contains B
Contains C
Contains D

Any answer must yield true for n of these conditions