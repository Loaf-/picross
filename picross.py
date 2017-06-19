#!/usr/intel/pkgs/python/2.7/bin/python
import sys
import copy


# graph has 0,0 in the top left corner.  [x][y] will be in the bottom right corner.

## GLOBALS
#tuples -- immutable lists
    #clues along Y axis from top to bottom/left to right
    #clues along X axis from left to right/top to bottom

ROW_CLUES_LIST = [];
COL_CLUES_LIST = [];
PUZZLE_NAME = [];
   # https://sites.google.com/site/wablatschki/solution02.jpg
PUZZLE_NAME.append("Jirachi");
ROW_CLUES_LIST.append( ((2, 1, 1), (6, 2, 1), (3, 1, 1, 3), (1, 1, 4, 1, 2), (1, 1, 2), (3, 2, 2, 1), (1, 3, 1, 2, 1, 3), (1, 1, 1, 1, 4, 1), (1, 1, 1, 1, 3, 1), (3, 1, 1, 2, 2), (2, 1, 2, 1, 1), (1, 3, 3, 2, 3), (4, 1, 2, 3), (4, 1, 1, 2, 3), (7, 2, 1, 6)) );
COL_CLUES_LIST.append( ((1, 1, 4), (1, 1, 3), (2, 3, 3), (3, 4, 4), (1, 1, 1, 1, 1), (1, 2, 1, 2), (3, 3, 2, 1, 1), (2, 3, 2, 1), (1, 1, 1, 1, 1), (3, 1, 2, 1), (2, 1, 2, 3), (2, 1, 1), (3, 1, 1), (4, 3), (1, 1, 1, 1, 1), (1, 3, 3), (1, 5, 2), (1, 3, 1, 2), (1, 1, 3, 1), (6, 1)) );

PUZZLE_NAME.append("Zygarde 10% forme");
ROW_CLUES_LIST.append( ((3, 5), (3, 4), (10, ), (3, 5), (4, 2), (3, 3), (10, ), (4, 4, 2), (3, 5, 3), (1, 6, 1, 3), (4, 2, 4, 2), (1, 2, 3), (1, 4), (1, 9), (1, 9)) );
COL_CLUES_LIST.append( ((2, ), (2, 1), (3, 1), (5, 1), (6, 1), (6, 1), (3, 1, 1, 1), (4, 1, 5), (1, 2, 6, 2), (8, ), (9, 1), (4, 3, 2, 2), (3, 2, 2), (3, 1, 3), (1, 2, 3), (1, 1, 3), (2, 4), (1, 1, 2), (2, 2, 2), (1, 1, 2)) );

PUZZLE_NAME.append("Zygarde 50% forme");
ROW_CLUES_LIST.append( ((1, 2, 1, 1, 2), (1, 4, 2, 3), (3, 1, 1, 2, 1), (1, 3, 1, 1, 1), (2, 2, 2, 1, 2), (1, 2, 2, 1, 3), (1, 6, 1, 2), (2, 4, 4, 2), (3, 1, 1, 1, 3, 1), (1, 2, 2, 1, 3), (2, 3, 2, 1, 4), (2, 1, 2, 2, 2), (2, 3, 2, 1, 2, 2), (1, 3, 2, 3, 2), (1, 5, 1, 2)) );
COL_CLUES_LIST.append( ((6, 1, 1), (1, 1, 1, 1, 2), (2, 1, 1, 1), (1, 6), (4, 2, 1, 3), (2, 4, 6), (4, 1), (1, 2, 1, 1, 1), (2, 3, 1, 3, 1), (7, 1, 1, 1), (1, 5, 1), (2, 1, 1), (3, 1), (1, 2, 5, 1), (4, 2, 1, 2), (1, 2, 1, 1), (1, 1, 1, 2), (1, 1, 1, 1, 1), (2, 2, 1, 1, 2), (1, 4, 2, 1, 1)) );

PUZZLE_NAME.append("Zygarde complete forme");
ROW_CLUES_LIST.append( ((1, 1, 2, 1, 2, 1, 1), (2, 3, 1, 1, 1, 1, 1), (3, 1, 2, 2, 1, 2), (3, 1, 3, 3, 1), (4, 4, 1, 1), (4, 4, 1, 1), (5, 2, 1, 1, 1), (3, 1, 2, 1, 1, 1, 1), (2, 1, 2, 4, 1, 1), (3, 1, 1, 2, 1, 1, 1), (2, 1, 1, 2, 1, 1), (4, 1, 3, 1, 1, 1, 1), (4, 7, 1, 1), (2, 3, 1, 6, 1), (2, 3, 4)) );
COL_CLUES_LIST.append( ((0, ), (7, 2), (10, 4), (11, ), (2, 3, 5), (3, 2, 3), (1, 2, 2, 2), (1, 5, 2, 1), (10, 3), (4, 1, 3), (1, 1, 1, 3), (2, 3, 3), (1, 1, 1, 2), (1, 1, 5), (1, 1, 4, 3), (6, 2, 2), (4, 1, 1), (6, 1, 1), (1, 1, 1), (2, 3, 1)) );

PUZZLE_NAME.append ("Kyogre");
ROW_CLUES_LIST.append( ((4, 1, 1, 1, 1), (2, 2, 6, 2), (2, 2, 2, 4), (1, 1, 2, 1), (3, 2, 1), (2, 1, 1), (1, 1, 2), (2, 2, 1), (1, 1, 2, 2), (2, 2, 1, 4, 4), (2, 5, 2, 2), (3, 4, 1, 1), (5, 1, 1, 1, 1), (2, 1, 2, 2), (2, 1, 1)) );
COL_CLUES_LIST.append( ((1, 1), (2, 1, 3), (1, 1, 4, 2), (1, 1, 2, 1, 2), (2, 1, 1, 1), (2, 1, 2), (1, 1, 1), (1, 1, 1), (2, 2, 1), (1, 1, 1, 2), (1, 3, 1), (1, 1, 1), (2, 1, 4), (1, 3), (1, 2, 2), (1, 2, 2, 3), (2, 3, 2), (1, 5), (3, 3, 2, 1), (4, 1, 1, 4)) );

PUZZLE_NAME.append ("Deoxys");
ROW_CLUES_LIST.append( ((2, 2), (2, 3), (3, 1, 3), (1, 1, 2, 1, 1), (1, 2, 1, 1, 1), (3, 2, 4), (2, 1, 1, 2), (4, 2, 2, 2), (2, 2, 6), (4, 2, 4, 1, 4), (4, 1, 2, 1, 2), (2, 1, 1 ,1, 1, 3), (1, 4, 2, 2, 1), (2, 2, 4, 3), (2, 1, 2, 1, 6)) );
COL_CLUES_LIST.append( ((1, 1, 1, 1), (1, 1, 1, 2), (1, 3, 1), (2, 1, 2, 1), (1, 1, 1, 1, 1), (1, 1, 6), (7, 1, 3), (2, 1, 3, 2), (1, 1, 2, 2), (1, 2, 3), (1, 2, 2, 2), (1, 3, 2), (1, 2, 1, 2), (4, 3), (1, 5, 2, 1), (2, 2, 1, 1, 3), (1, 1, 3, 2), (1, 1, 1, 1, 2), (2, 1, 1, 1), (1, 2, 1)) );

PUZZLE_NAME.append("Landorus Therian Forme");
ROW_CLUES_LIST.append(  ((3, 3), (2, 2, 3), (1, 2, 3, 2, 1), (2, 1, 1, 2, 1, 1), (5, 2, 1, 1), (2, 2, 2, 1), (1, 1, 1, 1, 1, 2, 4), (6, 1, 1, 1, 1, 3), (2, 1, 1, 2, 3), (1, 1, 3, 1), (1, 1, 1, 1, 2), (1, 4, 2, 1, 5), (3, 1, 1, 1, 2, 2), (1, 5, 1, 1), (3, 2)) );
COL_CLUES_LIST.append( ((1, 2), (1, 4), (1, 7, 2), (1, 3, 1, 1, 2), (1, 1, 1, 3, 3), (3, 1, 1, 1), (1, 1, 1, 1, 2, 2), (3, 1, 1, 1, 4), (1, 2, 1, 2), (3, 2, 1, 2), (1, 1, 2), (1, 1, 1, 1), (6, 1, 1), (2, 1), (1, 4), (1, 1, 3), (1, 4, 1, 3), (1, 2, 1), (1, 2, 2), (2, 2, 3)) );

PUZZLE_NAME.append("Garchomp");
ROW_CLUES_LIST.append( ((2, ), (1, 1), (7, 1), (1, 1, 4, 1), (2, 2, 2), (2, 1, 2), (2, 2, 1, 2, 4), (3, 2, 1, 1), (4, 4, 2), (2, 4, 1, 1), (2, 1, 1, 1), (1, 2, 2, 1, 1), (2, 2, 1, 1), (4, 1, 1), (1, 1)) );
COL_CLUES_LIST.append( ((5, ), (7, ), (1, 3), (1, 1, 1), (1, 1, 1, 1, 2), (1, 2, 3, 2), (2, 1, 4, 1), (1, 3, 1, 2), (2, 3, 1, 2), (1, 1, 1, 2), (1, 2), (3, 2, 2), (1, 5, 1, 1), (1, 1, 1, 3, 1), (1, 1, 2, 2)) );

PUZZLE_NAME.append("Giratina Origin Forme");
ROW_CLUES_LIST.append( ((4, 6, 1, 2), (2, 2, 2, 1, 2, 3), (1, 1, 1, 2, 1, 3), (2, 3, 1, 1, 4), (1, 1, 1, 2, 1, 4), (1, 1, 2, 4), (1, 1, 3, 3, 1), (2, 2, 2, 1, 2, 2), (2, 1, 2, 1, 1, 1, 2), (3, 4, 1, 1, 3), (4, 2, 2, 1, 2), (2, 1, 5, 1, 1), (1, 7, 1, 4), (2, 4, 2, 2, 2), (1, 1, 2, 1, 3, 2)) );
COL_CLUES_LIST.append( ((1, 1, 4), (2, 1, 7, 2), (5, 5), (1, 3, 1, 1), (3, 2, 1), (1, 2, 2, 1, 1), (1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 1, 1, 3), (2, 1, 1, 1, 3), (3, 2, 2, 1), (1, 2, 4), (5, 2, 1), (1, 1, 1, 1), (1, 3, 3, 1), (8, 2), (4, 1, 2), (5, 4,), (5, 4, 3), (3, 4, 3)) );

PUZZLE_NAME.append("Heatran");
ROW_CLUES_LIST.append( ((6, 3), (2, 4), (3, 3, 1), (2, 1, 1, 1, 3, 2), (1, 1, 1, 1, 1, 1, 1), (3, 2, 1, 1, 1), (1, 5, 2), (1, 1, 2, 2), (9, 1, 1, 1, 3), (2, 1, 3, 2, 1), (2, 3, 1, 1, 1, 1, 2), (1, 1, 2, 2, 1, 1), (3, 1, 1, 2, 1, 1), (1, 3, 1, 2, 3, 1), (1, 1, 4, 7, 2)) );
COL_CLUES_LIST.append( ((1, 1, 2), (2, 5), (1, 1, 2, 3), (1, 1, 2, 4), (5, 3, 2), (2, 2, 1, 1), (2, 2, 1, 4), (1, 1, 1, 1, 1, 1), (1, 1, 1, 1, 1), (1, 3, 1, 1, 4), (1, 3, 1, 2), (1, 3, 2, 1), (1, 1, 3, 4), (3, 2, 1, 3), (1, 1, 1, 2, 2), (2, 1, 1, 4, 1), (1, 1, 1), (1, 1, 1, 2, 3), (3, 1, 1, 1), (1, 1)) );

PUZZLE_NAME.append("Darkrai");
ROW_CLUES_LIST.append( ((3, 1, 1), (4, 1), (3, 1), (4, 1, 2, 1), (4, 1, 3, 2), (5, 1, 1, 1, 2, 2), (3, 1, 1, 2, 6), (3, 1, 4, 1, 5), (1, 7, 6), (2, 4, 1, 5), (3, 1, 1, 1, 6), (6, 1, 3, 3), (4, 1, 3, 3), (3, 1, 5, 2), (2, 6, 2)) );
COL_CLUES_LIST.append( ((4, ), (1, 4, 4), (8, 4), (13, ), (5, 1, 3), (1, 2, 1, 2), (1, 4, 1), (2, 1), (5, 1), (1, 3, 2), (2, 2, 2, 2), (4, 3), (3, 1, 1, 4), (1, 3, 1, 4), (1, 1, 4), (7, ), (6, ), (7, ), (11, ), (6, 4)) );

PUZZLE_NAME.append("Registeel");
ROW_CLUES_LIST.append( ((1, 3, 2), (2, 4, 2), (3, 5, 3), (1, 11, 2), (1, 1, 1, 1, 1, 2), (1, 1, 1, 1, 1 ), (1, 1, 5, 1), (1, 1, 1, 1, 1, 1, 1), (2, 1, 5, 2, 1, 2), (11, 3), (3, 4, 2, 1), (4, 4, 3, 1), (3, 1, 3, 1, 1), (4, 1, 3, 2, 2), (3, 1, 3, 2, 2)) );
COL_CLUES_LIST.append( ((4, 2), (1, 1, 3), (1, 7), (1, 4, 5), (3, 4), (1, 1, 1, 1, 1), (1, 2, 4, 2), (2, 2, 3), (4, 6, 1), (3, 2, 7), (5, 9), (4, 1, 3), (1, 1, 1), (1, 1), (1, 1, 3), (1, 4, 1, 2), (2, 2, 1, 2, 1), (3, 2), (1, 2, 2), (1, 8)) );

PUZZLE_NAME.append("Regirock");
ROW_CLUES_LIST.append( ((1, 3), (1, 1, 5, 1), (1, 1, 1, 1, 2, 1), (1, 2, 1, 1, 2), (1, 5, 1, 1, 2, 2), (1, 4, 1, 2, 3), (5, 1, 1, 1, 3), (3, 3, 1), (1, 3, 3), (3, 2, 6), (1, 1, 3, 5), (3, 2, 1, 1, 4), (2, 2, 1, 1, 3, 1), (2, 10, 1), (2, 1, 6, 1)) );
COL_CLUES_LIST.append( ((1, ), (2, ), (3, 2, 1, 1), (1, 2, 1, 3), (2, 10), (1, 5, 1), (6, 1, 1, 1), (1, 3, 1, 2), (1, 1, 1, 1, 1, 1), (2, 1, 1, 1), (1, 1, 1, 2, 2), (2, 1, 3), (1, 3, 1, 2), (2, 2, 1, 3), (3, 5, 2), (2, 4, 3), (9, ), (3, 4), (3, 1, 2, 1), (1, 1, 1, 3)) );

PUZZLE_NAME.append("Palkia");
ROW_CLUES_LIST.append( ((11, ), (1, 4, 1), (1, 5, 4, 2), (3, 1, 4, 3), (1, 1, 4, 1), (1, 2, 1, 2), (2, 1, 5, 5, 1, 1), (4, 1, 2, 3), (1, 4, 1, 2, 3), (2, 4, 2, 1, 1), (3, 3, 3), ( 1, 2, 3), (1, 1, 4 , 2, 1), (1, 2, 1, 2, 4, 1), (1, 1, 1, 2, 2, 1, 3)) );
COL_CLUES_LIST.append( ((1, 2, 1), (2, 2, 2, 1, 1), (1, 2, 3, 1), (1, 1, 3, 1, 1, 1), (1, 1, 1, 2, 1, 1), (1, 1, 2, 1, 1, 2), (1, 1, 1, 1), (1, 2, 2, 2, 1), (1, 1, 1, 2, 1, 3), (1, 1, 1, 3), (2, 1, 1, 3), (1, 1, 1, 5), (1, 1, 2, 2), (2, 1, 3, 3), (1, 1, 1, 2, 1), (1, 1, 1, 2, 3), (4, 1, 5), (1, 7, 1), (2, 2, 1), (2, 1, 1, 2, 2)) );

PUZZLE_NAME.append("Dialga");
ROW_CLUES_LIST.append( ((2, 5, 1), (2, 3, 5, 2), (1, 1, 1, 6, 2, 1), (1, 1, 1, 3, 2, 2), (1, 2, 2, 2, 2), (4, 1, 2), (1, 2, 2, 2, 2), (1, 1, 1, 1, 2), (2, 3, 1, 1, 2), (1, 1, 1, 4, 1), (4, 2, 2, 1), (3, 3, 2, 3), (1, 4, 2, 1, 1), (3, 2, 1), (4, 2, 3)) );
COL_CLUES_LIST.append( ((2, ), (1, 2, 1, 2), (1, 1, 2, 1), (1, 2, 3), (2, 3, 1, 2), (1, 3, 5), (2, 1, 1, 1), (1, 2, 2, 5), (1, 3, 6), (4, 2, 4), (2, 1, 2, 1), (3, 1, 6), (2, 2, 1, 1, 4), (2, 2, 2, 1, 1), (1, 2, 2, 1, 3), (1, 1, 2, 2, 1, 2), ( 1, 2, 2, 1), (1, 1, 1), (1, 1), (0, )) );

PUZZLE_NAME.append("Moltres");
ROW_CLUES_LIST.append( ((5,1,5,2), (1,2,2,4,1,2), (6,1,1,1), (2,3,2,1), (1,2,2,1,1), (3,4,2,6), (2,1,1,3,2), (1,4,3), (2,1,2,2), (2,1,3,1), (6,2), (1,1,1,1,1,5), (1,1,3,1,3), (1,6,3), (4,2,3)) );
COL_CLUES_LIST.append( ((2,2,), (2,1,1,1), (1,1,2,3,1), (4,5,2), (3,1,1,2,1), (1,2,1,1,2), (6,3,1), (5,1,1,1), (1,1,1,2), (1,3,1,1), (1,2,1,5), (1,1,2,1,1), (2,1,1,1,2), (1,2,2,1,1), (2,1,1,1,1), (1,1,2,1), (1,2,1,1), (2,1,1,1,2), (2,4,2), (3,1,3,2)) );

PUZZLE_NAME.append("Groudon");
ROW_CLUES_LIST.append ( ((1,1,2), (2,2,4), (2,2,1,1,2), (1,2,4,1,1,1), (1,1,1,1,5,1), (2,1,3,1,1,3), (1,1,2,1,2,1,1), (7,5,1), (2,5,6), (1,4,6,1), (4,1,1,8), (2,2,4,7), (1,6,1,4), (8,8), (6,1,4,1)) );
COL_CLUES_LIST.append ( ((3,), (2,2,), (4,1,3), (4,8), (2,2,5), (2,3,2,3), (2,9), (2,6,3), (2,1,1,3,1), (3,4,1), (1,2,2), (2,1,2,2,1), (2,1,5,2), (1,2,9), (1,11), (3,8), (1,1,8), (1,1,4,1), (2,1,1,1), (2,1)) );

PUZZLE_NAME.append("Entei");
ROW_CLUES_LIST.append( ((1,1,2,3), (4,1,1,3), (1,1,3,1), (1,1,2,4), (1,3,1), (6,2,2,1), (2,1,4,1,3,1), (2,1,1,1), (1,2,2,1,1), (2,1,3,1,3), (1,3,1,3,1,4), (2,3,3,2,4), (1,4,4,4), (3,1,3,1,1), (3,1,2,1)) );
COL_CLUES_LIST.append( ((1,3), (2,1,2,1), (2,1,1), (1,1,2), (1,2,1), (1,1,1), (2,2), (3,2,1,1,1), (2,10), (3,2,2), (2,5), (1,1,3,2), (4,1,2,3), (1,1,2,4), (1,1,7), (1,3,1), (1,3,3), (4,7), (2,1,1,4), (1,2,1,4)) );

PUZZLE_NAME.append("Terrakion");
ROW_CLUES_LIST.append( ((1,2,1,4,1), (1,1,1,1,3,1), (1,1,1,1,3), (1,1,4,1,4), (4,4,3,1), (2,3,1,3,1), (1,3,1), (2,1,4,1), (2,2,1,1,1), (2,1,1,1,2,1,1), (1,1,1,1,1,3), (1,1,1,1,2,2), (3,2,2,1,1,2), (2,3,2,1,1), (10,1)) );
COL_CLUES_LIST.append( ((2,2), (2,2), (2,5), (9,), (1,1,2,3), (1,2,1,2), (6,1,1), (2,4,1,1,2), (1,2,1,1,1), (5,2,1,1), (2,1,1), (2,3,2), (1,2,1,1,2,2), (1,1,1,1,2,1), (2,2,4,1), (1,1,2), (2,1,1), (1,2), (1,6), (1,5,1,1,1)) );

PUZZLE_NAME.append("Reshiram");
ROW_CLUES_LIST.append( ((2,2,1,2), (4,2,1), (3,2,3), (3,3,1,3), (2,1,1,2,4,1), (1,3,4,2), (1,2,2,2,1), (3,2,1,1,2,1), (3,3,2), (5,1,3,3), (3,1,2,1,1), (3,1,1,1,1), (2,5,1,1,1), (1,3,1,3,2,3), (3,2,2,5)) );
COL_CLUES_LIST.append( ((3,1,2), (1,2,1,1,1), (2,3,1,2), (2,1,2,1,2), (3,1,1,1,1,1), (3,2,1,1,2,1), (2,1,1,1,1,1), (1,2,1,2), (1,1,1,3), (1,1,2,1), (1,1,1,1,1), (1,1,6,1), (2,1,1,1,1), (1,2,4,1,1), (5,1,1,2), (6,2,3), (2,2,1), (2,2), (1,2,1,1), (2,2,1,1,2)) );

PUZZLE_NAME.append("unknown");
ROW_CLUES_LIST.append( ((3,2,1,1), (2,1,1,2,1), (1,1,1,1,2), (7,2), (1,1,1,2,1,1), (1,2,1), (1,3), (2,2,1,1), (3,1,3,1), (1,1,5,2), (2,3,2), (3,3,4,1), (2,2), (5,), (1,3)) );
COL_CLUES_LIST.append( ((2,1,1), (2,1,2), (1,3,1), (2,2,5), (2,1), (2,1), (1,1,2,1), (5,1,3,1), (1,4,2), (2,6), (9,1,1), (2,2,1,2), (2,1,1,1,2), (2,1,1,2,1), (3,1,1,2)) );

class graphCell :
    def __init__(self) :
        self.possibleColClues = [];       # list of indeces into COL_CLUES that are possible matches to cell
        self.possibleRowClues = [];       # list of indeces into ROW_CLUES that are possible matches to cell
        self.val = ' ';

    def fill_O (self) :
        if self.val == 'X' :
            raise Exception("Trying to place O in cell with X");
        else :
            self.val = 'O' ;

    def fill_X (self) :
        if self.val == 'O' :
            raise Exception("Trying to place X in cell with O");
        else :
            self.val = 'X' ;
            self.possibleColClues = [];
            self.possibleRowClues = [];

# initialize GRAPH given list of column clues and row clues
def initialize_graph ( column_clues, row_clues ) :
    global HEIGHT_OF_COL_CLUES, LENGTH_OF_ROW_CLUES;
    global ROW_CLUES, COL_CLUES;
    global PUZZLE_WIDTH, PUZZLE_HEIGHT;
    global GRAPH, PREV_GRAPH;

    PUZZLE_WIDTH = len(COL_CLUES);
    PUZZLE_HEIGHT = len(ROW_CLUES);
    HEIGHT_OF_COL_CLUES = 0;
    LENGTH_OF_ROW_CLUES = 0;
    GRAPH = [];
    PREV_GRAPH = [];
    # calculate dimensions and generate empty graph
    max_row_clues = 0;
    max_column_clues = 0;
    for j in row_clues :
        if(len(j) > max_row_clues) :
            max_row_clues = len(j);
    for j in column_clues :
        if (len(j) > max_column_clues) :
            max_column_clues = len(j);
    HEIGHT_OF_COL_CLUES = max_column_clues;
    LENGTH_OF_ROW_CLUES = max_row_clues;
    width = len(column_clues) + max_row_clues;
    height = len(row_clues) + max_column_clues;

    GRAPH = [ [ graphCell() for h in range(PUZZLE_HEIGHT)] for w in range(PUZZLE_WIDTH) ];   # horizontal list of vertical lists. top left is 0,0; bottom right is [w][h]

    # populate possible clues into cells
    # a clue can be in any cell up to the point where the sum of all clues after it (plus X fills) just fits
    # if cell index is less than this sum then that clue can apply to that cell
    # a clue can be in any cell up to the point where the sum of all clues before it (plus X fills) just fits
    # if cell index is greater than this sum then that clue can apply to that cell
    for h in range (0, PUZZLE_HEIGHT) :
        for w in range (0, PUZZLE_WIDTH) :
           # row clues
           sum_after = 0;
           sum_before = 0;
           if ROW_CLUES[h][0] == 0 :
               try :
                   GRAPH[w][h].fill_X();
               except :
                   print "Cell",x,",",y;
                   print_row_data(h);
                   print_col_data(w);
                   raise;

           else :
                # sum of clues
                for clue in ROW_CLUES[h] :
                    sum_after += clue;
                clue_index = 0;
                # check
                for clue in ROW_CLUES[h] :
                    sum_after -= clue;
                    if (w >= (sum_before + clue_index)) and (w < PUZZLE_WIDTH - (sum_after + (len(ROW_CLUES[h])-(clue_index+1)))) and not GRAPH[w][h].val == 'X' :
                        GRAPH[w][h].possibleRowClues.append(clue_index);
                    clue_index += 1;
                    sum_before += clue;
           # column clues
           sum_after = 0;
           sum_before = 0;
           if COL_CLUES[w][0] == 0 :
               try :
                GRAPH[w][h].fill_X();
               except :
                   print e;
                   print "Cell",x,",",y;
                   print_row_data(h);
                   print_col_data(w);
                   raise;
           else :
                # sum of clues
                for clue in COL_CLUES[w] :
                    sum_after += clue;
                clue_index = 0;
                # check
                for clue in COL_CLUES[w] :
                    sum_after -= clue;
                    if (h >= (sum_before + clue_index)) and (h < PUZZLE_HEIGHT - (sum_after + (len(COL_CLUES[w])-(clue_index+1)))) and not GRAPH[w][h].val == 'X' :
                        GRAPH[w][h].possibleColClues.append(clue_index);
                    clue_index += 1;
                    sum_before += clue;

##################################################################################
def print_graph ( debug ) :
    global HEIGHT_OF_COL_CLUES, LENGTH_OF_ROW_CLUES;
    global PUZZLE_WIDTH, PUZZLE_HEIGHT;
    global GRAPH;

    width = PUZZLE_WIDTH + LENGTH_OF_ROW_CLUES;
    height = PUZZLE_HEIGHT + HEIGHT_OF_COL_CLUES;

    col_clues_count = HEIGHT_OF_COL_CLUES;
    for row in range(0, height) :
        row_clues_count = LENGTH_OF_ROW_CLUES;
        for col in range(0, width) :
            #top left corner is blank
            if row < HEIGHT_OF_COL_CLUES and col < LENGTH_OF_ROW_CLUES :
                print ' ',;
            #column clues
            elif row < HEIGHT_OF_COL_CLUES and col >= LENGTH_OF_ROW_CLUES :
                if len(COL_CLUES[col-LENGTH_OF_ROW_CLUES]) < col_clues_count :
                    print ' ',;
                else :
                        # if clue greater than 9, use alphabet to prevent misalignment
                    if COL_CLUES[col-LENGTH_OF_ROW_CLUES][len(COL_CLUES[col-LENGTH_OF_ROW_CLUES])-col_clues_count] > 9 :
                        print chr(ord("A")+(COL_CLUES[col-LENGTH_OF_ROW_CLUES][len(COL_CLUES[col-LENGTH_OF_ROW_CLUES])-col_clues_count]-10)),;
                    else :
                        print COL_CLUES[col-LENGTH_OF_ROW_CLUES][len(COL_CLUES[col-LENGTH_OF_ROW_CLUES])-col_clues_count],;
            #row clues
            elif row >= HEIGHT_OF_COL_CLUES and col < LENGTH_OF_ROW_CLUES :
                if len(ROW_CLUES[row-HEIGHT_OF_COL_CLUES]) < row_clues_count :
                    print ' ',;
                else :
                        # if clue greater than 9, use alphabet to prevent misalignment
                    if ROW_CLUES[row-HEIGHT_OF_COL_CLUES][len(ROW_CLUES[row-HEIGHT_OF_COL_CLUES])-row_clues_count] > 9 :
                        print chr(ord("A")+(ROW_CLUES[row-HEIGHT_OF_COL_CLUES][len(ROW_CLUES[row-HEIGHT_OF_COL_CLUES])-row_clues_count]-10)),;
                    else :
                        print ROW_CLUES[row-HEIGHT_OF_COL_CLUES][len(ROW_CLUES[row-HEIGHT_OF_COL_CLUES])-row_clues_count],;
                row_clues_count -= 1;
            #graph
            else :
                #print GRAPH[col-LENGTH_OF_ROW_CLUES][row-HEIGHT_OF_COL_CLUES].val,;
                if GRAPH[col-LENGTH_OF_ROW_CLUES][row-HEIGHT_OF_COL_CLUES].val == 'O' :
                    #print u"\xe2\x96\x88",;     # unicode for filled in block
                    print u"X",;     # unicode for filled in block
                elif GRAPH[col-LENGTH_OF_ROW_CLUES][row-HEIGHT_OF_COL_CLUES].val == 'X' :
                    #print GRAPH[col-LENGTH_OF_ROW_CLUES][row-HEIGHT_OF_COL_CLUES].val,;
                    print ".",;
                else :
                    print GRAPH[col-LENGTH_OF_ROW_CLUES][row-HEIGHT_OF_COL_CLUES].val,;

            #vertical lines
            if (col+1-LENGTH_OF_ROW_CLUES) % 5 == 0 and (col+1-LENGTH_OF_ROW_CLUES) >= 0 :
                print '|',;
        col_clues_count -= 1;
        print "";
        #horizontal lines
        if row == HEIGHT_OF_COL_CLUES-1 or (((row + 1 - HEIGHT_OF_COL_CLUES) % 5 == 0) and (row + 1 - HEIGHT_OF_COL_CLUES) >= 0 ):
            for col in range(0,LENGTH_OF_ROW_CLUES) :
                print '-',;
            print '+',;
            for col in range(1, width-LENGTH_OF_ROW_CLUES+1) :
                print '-',;
                if (col) % 5 == 0 and (col) >= 0 :
                    print '+',;
            print "";

    print "";
    if (debug == 1) :
        print_debug_info();

##################################################################################
# return list with column of GRAPH
def grab_column ( index ) :
    global GRAPH;
    list = [];
    list = GRAPH[index];
    return list;

##################################################################################
# return list with row of GRAPH
def grab_row ( index ) :
    global COL_CLUES;
    global GRAPH;
    list = [];
    for x, column in enumerate(COL_CLUES) :
        list.append(GRAPH[x][index]);
    return list;

##################################################################################
def print_row_data ( row_index ) :
    print "Row:", row_index;
    print "Clues: ", ROW_CLUES[row_index];
    row = grab_row( row_index );
    #index
    for i, entry in enumerate(row) :
        print i, "\t",;
    print "";
    for i, entry in enumerate(row) :
        print '|', "\t",;
    print "";
    for i, entry in enumerate(row) :
        print entry.val, "\t",;
    print "";
    for i, entry in enumerate(row) :
        print '|', "\t",;
    print "";
    for i, entry in enumerate(row) :
        print '-', "-----",;
    print "";

    max_clues = 1;
    for entry in row :
        if len(entry.possibleRowClues) > max_clues :
            max_clues = len(entry.possibleRowClues);

    for i in range (0,max_clues) :
        for entry in row :
            try :
                print entry.possibleRowClues[i], "\t",;
            except :
                print " \t",;
        print "";

##################################################################################
def print_col_data ( col_index ) :
    print "Column:", col_index;
    print "Clues: ", COL_CLUES[col_index];
    col = grab_column( col_index );
    for i, entry in enumerate(col) :
        print i, "----", entry.val, "----", entry.possibleColClues;

##################################################################################
def print_debug_info () :

    tmp = input("Enter row # for debug info, 99 to skip: ");
    if not tmp == 99 :
        print_row_data(tmp);
    while not (tmp == 99) :
        tmp = input("Enter row # for debug info, 99 to skip: ");
        if tmp == 99 :
            break;
        print_row_data(tmp);

    tmp = input("Enter col # for debug info, 99 to skip: ");
    if not tmp == 99 :
        print_col_data(tmp);
    while not (tmp == 99) :
        tmp = input("Enter col # for debug info, 99 to skip: ");
        if tmp == 99 :
            break;
        print_col_data(tmp);

##################################################################################
# check graph for completion
def check_graph () :
    global GRAPH;
    for column in GRAPH :
        for entry in column :
            if entry.val == ' ' :
                #print "Graph incomplete";
                return 0;
            if entry.val == 'X' and (not (len(entry.possibleRowClues) == 0 and len(entry.possibleColClues) == 0)) :
                return 0;
            if entry.val == 'O' and ( (not len(entry.possibleRowClues) == 1) or (not len(entry.possibleColClues) == 1) ) :
                return 0;
    #print "GRAPH_COMPLETE!";
    return 1;

##################################################################################
# assume dimensions are equal
def graphs_equal(graph_1, graph_2) :
    return_val = 0;
    for w, column in enumerate(GRAPH) :
        for h, entry in enumerate(column) :
            if (cmp(graph_1[w][h].possibleColClues, graph_2[w][h].possibleColClues) == 0) and (cmp(graph_1[w][h].possibleRowClues, graph_2[w][h].possibleRowClues) == 0) and (graph_1[w][h].val == graph_2[w][h].val) :
                return_val = 1;
            else :
                return 0;
    return return_val;

##################################################################################
# count number of times a clue shows up
# compare number against value of clue
# if number < 2*clue then there is some overlap
def mark_overlaps_row ( row_number ) :
    global ROW_CLUES, COL_CLUES;
    global GRAPH;

    # clue_info
    # list of tuples, tuple is [first index where clue shows up, last index where clue shows up]
    clue_info = [ [-1, -1] for length in range(len(ROW_CLUES[row_number])) ];

    # collect clue data
    for x, column in enumerate(COL_CLUES) :
        for possible in GRAPH[x][row_number].possibleRowClues :
            # first index
            if clue_info[possible][0] == -1 :
                clue_info[possible][0] = x;
            # last index
            if clue_info[possible][1] < x :
                clue_info[possible][1] = x;

    # analyze clue data
    for index, clue_data in enumerate(clue_info) :
        possible_cells = clue_data[1] - clue_data[0] + 1;
        overlap = (2*ROW_CLUES[row_number][index]) - possible_cells;
        overlap_index = clue_data[1] - abs(ROW_CLUES[row_number][index] - possible_cells);
        #print "row is ", row_number, "index is ", index, " clue value is ", ROW_CLUES[row_number][index], " possible cell # ", clue_data[1], clue_data[0], possible_cells, " overlap is ", overlap, " overlap_index is ", overlap_index;
        # if overlap == clue size then place X's as well
        if overlap == ROW_CLUES[row_number][index] :
            try :
                if clue_data[0]-1 >= 0 :
                    try :
                        GRAPH[clue_data[0]-1][row_number].fill_X();
                        #GRAPH[clue_data[0]-1][row_number].possibleRowClues = [];
                    except :
                        print_row_data(row_number);
                        raise;
            except :
                0
            try :
                if clue_data[1]+1 < PUZZLE_WIDTH :
                    GRAPH[clue_data[1]+1][row_number].fill_X();
                    #GRAPH[clue_data[1]+1][row_number].possibleRowClues = [];
            except :
                print_row_data(row_number);
                raise;
        # mark overlaps
        while overlap > 0 :
            try :
                GRAPH[overlap_index][row_number].fill_O();
                GRAPH[overlap_index][row_number].possibleRowClues = [index];
            except :
                print overlap_index;
                print_row_data(row_number);
                raise;
            # erase lower indexes from all cells past marked cell
            for r in range (overlap_index+1, PUZZLE_WIDTH) :
                for lower_index in range (0, index) :
                    try :   
                        GRAPH[r][row_number].possibleRowClues.remove(lower_index);
                    except :
                        0;
            overlap_index -= 1;
            overlap -= 1;

    #print "before clean clues"
    #print_graph(debug);
    clean_clues_row(row_number);
    #print "after clean clues"
    #print_graph(debug);

def mark_overlaps_col ( col_number ) :
    global ROW_CLUES, COL_CLUES;
    global GRAPH;

    # clue_info
    # list of tuples, tuple is [first index where clue shows up, last index where clue shows up]
    clue_info = [ [-1, -1] for length in range(len(COL_CLUES[col_number])) ];

    # collect clue data
    for x, row in enumerate(ROW_CLUES) :
        for possible in GRAPH[col_number][x].possibleColClues :
            # first index
            if clue_info[possible][0] == -1 :
                clue_info[possible][0] = x;
            # last index
            if clue_info[possible][1] <= x :
                clue_info[possible][1] = x;

    # analyze clue data
    for index, clue_data in enumerate(clue_info) :
        possible_cells = clue_data[1] - clue_data[0] + 1;
        overlap = (2*COL_CLUES[col_number][index]) - possible_cells;
        overlap_index = clue_data[1] - abs(COL_CLUES[col_number][index] - possible_cells);
        # if overlap == clue size then place X's as well
        if overlap == COL_CLUES[col_number][index] :
            try :
                if clue_data[0]-1 >= 0 :
                    try :
                        GRAPH[col_number][clue_data[0]-1].fill_X();
                        #GRAPH[col_number][clue_data[0]-1].possibleColClues = [];
                    except :
                        print_col_data(col_number);
                        raise;
            except :
                0
            try :
                if clue_data[1]+1 < PUZZLE_HEIGHT :
                    GRAPH[col_number][clue_data[1]+1].fill_X();
                    #GRAPH[col_number][clue_data[1]+1].possibleColClues = [];
            except :
                print_col_data(col_number); 
                raise;
        # mark overlaps
        while overlap > 0 :
            try :
                GRAPH[col_number][overlap_index].fill_O();
                GRAPH[col_number][overlap_index].possibleColClues = [index];
                for r in range (overlap_index+1, PUZZLE_HEIGHT) :
                    for lower_index in range (0, index) :
                        try :   
                            GRAPH[col_number][r].possibleColClues.remove(lower_index);
                        except :
                            0;
                overlap_index -= 1;
                overlap -= 1;
            except :
                print "Cell",col_number,",",overlap_index;
                print_col_data(col_number);
                raise;

    clean_clues_col(col_number);

##################################################################################
def clean_clues_row ( row_number ) :
    #print_row_data(row_number);
    for row_index in range (0,PUZZLE_WIDTH) :
        clues_to_remove = [];
        for clue in GRAPH[row_index][row_number].possibleRowClues :
            # check range of all clues to see if possible, if not remove clue
            # start with index as last possible cell for clue
            last_index = row_index;
            first_index = row_index - ROW_CLUES[row_number][clue] + 1;
            clue_fits = 0;
            # look for cases where clue CAN fit
            while first_index <= row_index and last_index < PUZZLE_WIDTH :
                if first_index < 0 :
                    first_index += 1;
                    last_index += 1;
                else :
                    # clue in each cell
                    clue_in_cells = 1;
                    for index in range (first_index, last_index + 1) :
                        try :
                            GRAPH[index][row_number].possibleRowClues.index(clue);
                        except :
                            clue_in_cells = 0;
                            break;
                    # if clue is in each cell, check cell on either side is X or empty, if not the clue can not fit
                    if ( clue_in_cells == 1 
                            and ( first_index == 0 or ( (not first_index == 0) and (GRAPH[first_index-1][row_number].val == ' ' or GRAPH[first_index-1][row_number].val == 'X') ) )
                            and ( last_index == PUZZLE_WIDTH-1 or ( (not last_index == PUZZLE_WIDTH-1) and (GRAPH[last_index+1][row_number].val == ' ' or GRAPH[last_index+1][row_number].val == 'X') ) )
                       ):
                                clue_fits = 1;
                                break;
                    first_index += 1;
                    last_index += 1;
            if clue_fits == 0 :
                clues_to_remove.append(clue);
        for clue_to_remove in clues_to_remove :
            GRAPH[row_index][row_number].possibleRowClues.remove(clue_to_remove);
   
    # going forward, each clue should appear at least it's clue value times without the next clue also being possible
    # in reverse, each clue should appear at least it's clue value times without the next clue also being possible
    #print_row_data(row_number);
    clue = 0;
    clue_val = ROW_CLUES[row_number][clue];
    for row_index in range (0, PUZZLE_WIDTH) :
        if clue_val >= 0 :
            if clue_val == 0 and not clue in GRAPH[row_index][row_number].possibleRowClues : #(GRAPH[row_index][row_number].val == 'X' or len(GRAPH[row_index][row_number].possibleRowClues) == 0) : # ok
                for cell_clue in GRAPH[row_index][row_number].possibleRowClues :
                    if cell_clue > clue :
                        GRAPH[row_index][row_number].possibleRowClues.remove(cell_clue);
                clue_val -= 1;
                if clue_val < 0 :
                    clue += 1;
                    if clue > len(ROW_CLUES[row_number])-1 :
                        break;
                    clue_val = ROW_CLUES[row_number][clue];
            elif GRAPH[row_index][row_number].val == 'X' :   # non contiguous, reset clue_val count; the passed through cells should be cleaned up
                # TODO: clean up passed through cells
                clue_val = ROW_CLUES[row_number][clue];
            elif clue in GRAPH[row_index][row_number].possibleRowClues :
                for cell_clue in GRAPH[row_index][row_number].possibleRowClues :
                    if cell_clue > clue :
                        GRAPH[row_index][row_number].possibleRowClues.remove(cell_clue);
                clue_val -= 1;
                if clue_val < 0 :
                    clue += 1;
                    if clue > len(ROW_CLUES[row_number])-1 :
                        break;
                    clue_val = ROW_CLUES[row_number][clue];
            elif not clue in GRAPH[row_index][row_number].possibleRowClues :
                for cell_clue in GRAPH[row_index][row_number].possibleRowClues :
                    if cell_clue > clue :
                        GRAPH[row_index][row_number].possibleRowClues.remove(cell_clue);

    clue = len(ROW_CLUES[row_number])-1;
    clue_val = ROW_CLUES[row_number][clue];
    for row_index in range (PUZZLE_WIDTH-1, -1, -1) :
        if clue_val >= 0 :
            if clue_val == 0 and not clue in GRAPH[row_index][row_number].possibleRowClues : #(GRAPH[row_index][row_number].val == 'X' or len(GRAPH[row_index][row_number].possibleRowClues) == 0) : # ok
                for cell_clue in GRAPH[row_index][row_number].possibleRowClues :
                    if cell_clue < clue :
                        GRAPH[row_index][row_number].possibleRowClues.remove(cell_clue);
                clue_val -= 1;
                if clue_val < 0 :
                    clue -= 1;
                    if clue < 0 :
                        break;
                    clue_val = ROW_CLUES[row_number][clue];
            elif clue in GRAPH[row_index][row_number].possibleRowClues :
                for cell_clue in GRAPH[row_index][row_number].possibleRowClues :
                    if cell_clue < clue :
                        GRAPH[row_index][row_number].possibleRowClues.remove(cell_clue);
                clue_val -= 1;
                if clue_val < 0 :
                    clue -= 1;
                    if clue < 0 :
                        break;
                    clue_val = ROW_CLUES[row_number][clue];
            elif GRAPH[row_index][row_number].val == 'X' :   # non contiguous, reset clue_val count; the passed through cells should be cleaned up
                # TODO: clean up passed through cells
                clue_val = ROW_CLUES[row_number][clue];
            elif not clue in GRAPH[row_index][row_number].possibleRowClues :
                for cell_clue in GRAPH[row_index][row_number].possibleRowClues :
                    if cell_clue < clue :
                        GRAPH[row_index][row_number].possibleRowClues.remove(cell_clue);
    
    # if a cell has O, the first clue can not be a possible clue in cells beyond the clue val from this cell
    #print_row_data(row_number);
    for row_index in range (0, PUZZLE_WIDTH) :
        if GRAPH[row_index][row_number].val == 'O' :
            clue = GRAPH[row_index][row_number].possibleRowClues[0];
            clue_val = ROW_CLUES[row_number][clue];
            boundary_index = row_index+clue_val; #includes following X
            for remove_index in range (boundary_index+1, PUZZLE_WIDTH) :
                if clue in GRAPH[remove_index][row_number].possibleRowClues :
                    GRAPH[remove_index][row_number].possibleRowClues.remove(clue);
    #going backwards, the last clue
    for row_index in range (PUZZLE_WIDTH-1, -1, -1) :
        if GRAPH[row_index][row_number].val == 'O' :
            clue = GRAPH[row_index][row_number].possibleRowClues[-1];
            clue_val = ROW_CLUES[row_number][clue];
            boundary_index = row_index-clue_val; #includes following X
            for remove_index in range (boundary_index, -1, -1) :
                if clue in GRAPH[remove_index][row_number].possibleRowClues :
                    GRAPH[remove_index][row_number].possibleRowClues.remove(clue);

##################################################################################
def clean_clues_col ( col_number ) :
    for col_index in range (0,PUZZLE_HEIGHT) :
        clues_to_remove = [];
        for clue in GRAPH[col_number][col_index].possibleColClues :
            # check range of all clues to see if possible, if not remove clue
            # start with index as last possible cell for clue
            last_index = col_index;
            first_index = col_index - COL_CLUES[col_number][clue] + 1;
            clue_fits = 0;
            # look for cases where clue CAN fit
            while first_index <= col_index and last_index < PUZZLE_HEIGHT :
                if first_index < 0 :
                    first_index += 1;
                    last_index += 1;
                else :
                    # clue in each cell
                    clue_in_cells = 1;
                    for index in range (first_index, last_index + 1) :
                        try :
                            GRAPH[col_number][index].possibleColClues.index(clue);
                        except :
                            clue_in_cells = 0;
                            break;
                    # if clue is in each cell, check cell on either side is X or empty, if not the clue can not fit
                    if ( clue_in_cells == 1 
                            and ( first_index == 0 or ( (not first_index == 0) and (GRAPH[col_number][first_index-1].val == ' ' or GRAPH[col_number][first_index-1].val == 'X') ) )
                            and ( last_index == PUZZLE_HEIGHT-1 or ((not last_index == PUZZLE_HEIGHT-1) and (GRAPH[col_number][last_index+1].val == ' ' or GRAPH[col_number][last_index+1].val == 'X') ) )
                       ):
                                clue_fits = 1;
                                break;
                    first_index += 1;
                    last_index += 1;
            if clue_fits == 0 :
                clues_to_remove.append(clue);
        for clue_to_remove in clues_to_remove :
            GRAPH[col_number][col_index].possibleColClues.remove(clue_to_remove);
   
    # going forward, each clue should appear at least it's clue value times without the next clue also being possible
    # in reverse, each clue should appear at least it's clue value times without the next clue also being possible
    clue = 0;
    clue_val = COL_CLUES[col_number][clue];
    for col_index in range (0, PUZZLE_HEIGHT) :
        if clue_val >= 0 :
            if clue_val == 0 and not clue in GRAPH[col_number][col_index].possibleColClues : #(GRAPH[col_number][col_index].val == 'X' or len(GRAPH[col_number][col_index].possibleColClues) == 0) : # ok
                for cell_clue in GRAPH[col_number][col_index].possibleColClues :
                    if cell_clue > clue :
                        GRAPH[col_number][col_index].possibleColClues.remove(cell_clue);
                clue_val -= 1;
                if clue_val < 0 :
                    clue += 1;
                    if clue > len(COL_CLUES[col_number])-1 :
                        break;
                    clue_val = COL_CLUES[col_number][clue];
            elif clue in GRAPH[col_number][col_index].possibleColClues :
                for cell_clue in GRAPH[col_number][col_index].possibleColClues :
                    if cell_clue > clue :
                        GRAPH[col_number][col_index].possibleColClues.remove(cell_clue);
                clue_val -= 1;
                if clue_val < 0 :
                    clue += 1;
                    if clue > len(COL_CLUES[col_number])-1 :
                        break;
                    clue_val = COL_CLUES[col_number][clue];
            elif GRAPH[col_number][col_index].val == 'X' :   # non contiguous, reset clue_val count; the passed through cells should be cleaned up
                # TODO: clean up passed through cells
                clue_val = COL_CLUES[col_number][clue];
            elif not clue in GRAPH[col_number][col_index].possibleColClues :
                for cell_clue in GRAPH[col_number][col_index].possibleColClues :
                    if cell_clue > clue :
                        GRAPH[col_number][col_index].possibleColClues.remove(cell_clue);
    clue = len(COL_CLUES[col_number])-1;
    clue_val = COL_CLUES[col_number][clue];
    for col_index in range (PUZZLE_HEIGHT-1, -1, -1) :
        if clue_val >= 0 :
            if clue_val == 0 and not clue in GRAPH[col_number][col_index].possibleColClues : #(GRAPH[col_number][col_index].val == 'X' or len(GRAPH[col_number][col_index].possibleColClues) == 0) : # ok
                for cell_clue in GRAPH[col_number][col_index].possibleColClues :
                    if cell_clue < clue :
                        GRAPH[col_number][col_index].possibleColClues.remove(cell_clue);
                clue_val -= 1;
                if clue_val < 0 :
                    clue -= 1;
                    if clue < 0 :
                        break;
                    clue_val = COL_CLUES[col_number][clue];
            elif clue in GRAPH[col_number][col_index].possibleColClues :
                for cell_clue in GRAPH[col_number][col_index].possibleColClues :
                    if cell_clue < clue :
                        GRAPH[col_number][col_index].possibleColClues.remove(cell_clue);
                clue_val -= 1;
                if clue_val < 0 :
                    clue -= 1;
                    if clue < 0 :
                        break;
                    clue_val = COL_CLUES[col_number][clue];
            elif GRAPH[col_number][col_index].val == 'X' :   # non contiguous, reset clue_val count; the passed through cells should be cleaned up
                # TODO: clean up passed through cells
                clue_val = COL_CLUES[col_number][clue];
            elif not clue in GRAPH[col_number][col_index].possibleColClues :
                for cell_clue in GRAPH[col_number][col_index].possibleColClues :
                    if cell_clue < clue :
                        GRAPH[col_number][col_index].possibleColClues.remove(cell_clue);
    
    # if a cell has O, the first clue can not be a possible clue in cells beyond the clue val from this cell
    for col_index in range (0, PUZZLE_HEIGHT) :
        if GRAPH[col_number][col_index].val == 'O' :
            clue = GRAPH[col_number][col_index].possibleColClues[0];
            clue_val = COL_CLUES[col_number][clue];
            boundary_index = col_index+clue_val; #includes following X
            for remove_index in range (boundary_index+1, PUZZLE_HEIGHT) :
                if clue in GRAPH[col_number][remove_index].possibleColClues :
                    GRAPH[col_number][remove_index].possibleColClues.remove(clue);
    #going backwards, the last clue
    for col_index in range (PUZZLE_HEIGHT-1, -1, -1) :
        if GRAPH[col_number][col_index].val == 'O' :
            clue = GRAPH[col_number][col_index].possibleColClues[-1];
            clue_val = COL_CLUES[col_number][clue];
            boundary_index = col_index-clue_val; #includes following X
            for remove_index in range (boundary_index, -1, -1) :
                if clue in GRAPH[col_number][remove_index].possibleColClues :
                    GRAPH[col_number][remove_index].possibleColClues.remove(clue);
                    
##################################################################################
# look at recently filled in row cell and update column
# only called if filled in cell only has a single possible column clue
def col_update(col_index, row_index) :
    if len(GRAPH[col_index][row_index].possibleColClues)==1 :
        #if filled O
        if GRAPH[col_index][row_index].val == 'O' :
            column_clue = GRAPH[col_index][row_index].possibleColClues[0];
            column_clue_val = COL_CLUES[col_index][column_clue];
            # check number of cells clue is in, if larger than clue value can clean a bit
            num_cells = 0;
            first_cell = PUZZLE_HEIGHT;
            last_cell = -1;
            first_cell_filled = PUZZLE_HEIGHT;
            last_cell_filled = -1;
            for r in range (0, PUZZLE_HEIGHT) :
                if column_clue in GRAPH[col_index][r].possibleColClues :
                    num_cells += 1;
                    if r < first_cell :
                        first_cell = r;
                    if r > last_cell :
                        last_cell = r;
                        if len(GRAPH[col_index][r].possibleColClues) == 1 and GRAPH[col_index][r].val == 'O' :
                            if r < first_cell_filled :
                                first_cell_filled = r;
                            if r > last_cell_filled :
                                last_cell_filled = r;
            # remove clues from cells that are out of range
            if column_clue_val < last_cell-first_cell+1 :
                for r in range(0, row_index-(column_clue_val-1)) :
                    if column_clue in GRAPH[col_index][r].possibleColClues :
                        for ColClue in GRAPH[col_index][r].possibleColClues :
                            if ColClue >= column_clue :
                                GRAPH[col_index][r].possibleColClues.remove(ColClue);
                                # TODO : if possibleColClues reduced to null list, fill X
                for r in range(row_index+column_clue_val, PUZZLE_HEIGHT) :
                    if column_clue in GRAPH[col_index][r].possibleColClues :
                        for ColClue in GRAPH[col_index][r].possibleColClues :
                            if ColClue <= column_clue :
                                GRAPH[col_index][r].possibleColClues.remove(ColClue);
                                # TODO : if possibleColClues reduced to null list, fill X
        #if filled X
        else :
            # TODO
            return
##################################################################################
# look at recently filled in col cell and update row 
# only called if filled in cell only has a single possible row clue
def row_update(col_index, row_index) :
    if len(GRAPH[col_index][row_index].possibleRowClues)==1 :
        #if filled O
        if GRAPH[col_index][row_index].val == 'O' :
            row_clue = GRAPH[col_index][row_index].possibleRowClues[0];
            row_clue_val = ROW_CLUES[row_index][row_clue];
            # check number of cells clue is in, if larger than clue value can clean a bit
            num_cells = 0;
            first_cell = PUZZLE_WIDTH;
            last_cell = -1;
            first_cell_filled = PUZZLE_WIDTH;
            last_cell_filled = -1;
            for c in range (0, PUZZLE_WIDTH) :
                if row_clue in GRAPH[c][row_index].possibleRowClues :
                    num_cells += 1;
                    if c < first_cell :
                        first_cell = c;
                    if c > last_cell :
                        last_cell = c;
                        if len(GRAPH[c][row_index].possibleRowClues) == 1 and GRAPH[c][row_index].val == 'O' :
                            if c < first_cell_filled :
                                first_cell_filled = c;
                            if c > last_cell_filled :
                                last_cell_filled = c;
            # remove clues from cells that are out of range
            if row_clue_val < last_cell-first_cell+1 :
                for c in range(0, col_index-(row_clue_val-1)) :
                    if row_clue in GRAPH[c][row_index].possibleRowClues :
                        for RowClue in GRAPH[c][row_index].possibleRowClues :
                            if RowClue >= row_clue :
                                GRAPH[c][row_index].possibleRowClues.remove(RowClue);
                                # TODO : if possibleRowClues reduced to null list, fill X
                for c in range(col_index+row_clue_val, PUZZLE_WIDTH) :
                    if row_clue in GRAPH[c][row_index].possibleRowClues :
                        for RowClue in GRAPH[c][row_index].possibleRowClues :
                            if RowClue <= row_clue :
                                GRAPH[c][row_index].possibleRowClues.remove(RowClue);
                                # TODO : if possibleRowClues reduced to null list, fill X
        #if filled X
        else :
            # TODO
            return
##################################################################################
# if all possible clue values match contiguous Os
# number of cells with clue as possibility matches clue value
def check_for_completed_clues () :
    global GRAPH;
    for w, column in enumerate(GRAPH) :
        for h, entry in enumerate(column) :
            if len(entry.possibleColClues) == 0 or len(entry.possibleRowClues) == 0 :
                try :
                    entry.fill_X();
                    #entry.possibleColClues = [];
                    #entry.possibleValClues = [];
                except :
                    print "Cell",w,",",h;
                    print_row_data(h);
                    print_col_data(w);
                    raise;
            if entry.val == 'O' :
                ###### COLUMN ######
                # check if all possible clues are same value
                is_same_clue_value = 1;
                prev_clue = COL_CLUES[w][entry.possibleColClues[0]];
                for clue_index in entry.possibleColClues :
                    clue = COL_CLUES[w][clue_index];
                    if not prev_clue == clue :
                        is_same_clue_value = 0;
                    prev_clue = clue;
                if is_same_clue_value == 1 :
                    # check for contiguous Os
                    copy_possibleColClues = entry.possibleColClues;
                    first_index = h - 1;
                    last_index = h + 1;
                    while first_index >= 0 :
                        if GRAPH[w][first_index].val == 'O' :
                            first_index -= 1;
                        else :
                            break;
                    while last_index < PUZZLE_HEIGHT :
                        if GRAPH[w][last_index].val == 'O' :
                            last_index += 1;
                        else :
                            break;
                    # contiguous Os match clue value, place Xs around it and remove clue from all other cells if only one clue is possible
                    if (last_index - first_index - 1) == prev_clue :
                        if first_index >= 0 :
                            try :
                                GRAPH[w][first_index].fill_X();
                                #GRAPH[w][first_index].possibleRowClues = [];
                                #GRAPH[w][first_index].possibleColClues = [];
                            except :
                                print_col_data(w);
                                raise;
                        if last_index < PUZZLE_HEIGHT :
                            try :
                                GRAPH[w][last_index].fill_X();
                                #GRAPH[w][last_index].possibleRowClues = [];
                                #GRAPH[w][last_index].possibleColClues = [];
                            except :
                                print_col_data(w);
                                raise;
                        if len(copy_possibleColClues) == 1 :
                            while first_index >= 0 :
                                for i, copy_clue in enumerate(copy_possibleColClues) :
                                    try :
                                        GRAPH[w][first_index].possibleColClues.remove(copy_clue);
                                    except :
                                        0
                                first_index -= 1;
                            while last_index < PUZZLE_HEIGHT :
                                for i, copy_clue in enumerate(copy_possibleColClues) :
                                    try :
                                        GRAPH[w][last_index].possibleColClues.remove(copy_clue);
                                    except :
                                        0
                                last_index += 1;
                        # if not only one clue is possible, but only one clue value is possible
                        # check if total cells filled with just those clues matches expected value (clue value * # of clues)
                        else :
                            num_clues = len(entry.possibleColClues);
                            total_fills = num_clues*prev_clue;
                            for x in column :
                                if x.val == 'O' and cmp(x.possibleColClues, entry.possibleColClues) == 0 :
                                    total_fills -= 1;
                            if total_fills == 0 :
                                for x in column :
                                    if (not x.val == 'O') :
                                        for y in entry.possibleColClues :
                                            try :
                                                x.possibleColClues.remove(y) ;
                                            except :
                                                0

                ###### ROW ######
                # check if all possible clues are same value
                is_same_clue_value = 1;
                prev_clue = ROW_CLUES[h][entry.possibleRowClues[0]];
                for clue_index in entry.possibleRowClues :
                    clue = ROW_CLUES[h][clue_index];
                    if not prev_clue == clue :
                        is_same_clue_value = 0;
                    prev_clue = clue;
                if is_same_clue_value == 1 :
                    # check for contiguous Os
                    copy_possibleRowClues = entry.possibleRowClues;
                    first_index = w - 1;
                    last_index = w + 1;
                    while first_index >= 0 :
                        if GRAPH[first_index][h].val == 'O' :
                            first_index -= 1;
                        else :
                            break;
                    while last_index < PUZZLE_WIDTH :
                        if GRAPH[last_index][h].val == 'O' :
                            last_index += 1;
                        else :
                            break;
                    # contiguous Os match clue value, place Xs around it and remove clue from all other cells if only one clue is possible
                    if (last_index - first_index - 1) == prev_clue :
                        if first_index >= 0 :
                            try :
                                GRAPH[first_index][h].fill_X();
                                #GRAPH[first_index][h].possibleRowClues = [];
                                #GRAPH[first_index][h].possibleColClues = [];
                            except :
                                print_row_data(h);
                                raise;
                        if last_index < PUZZLE_WIDTH :
                            try :
                                GRAPH[last_index][h].fill_X();
                                #GRAPH[last_index][h].possibleRowClues = [];
                                #GRAPH[last_index][h].possibleColClues = [];
                            except :
                                print_row_data(h);
                                raise;
                        if len(copy_possibleRowClues) == 1 :
                            while first_index >= 0 :
                                for i, copy_clue in enumerate(copy_possibleRowClues) :
                                    try :
                                        GRAPH[first_index][h].possibleRowClues.remove(copy_clue);
                                    except :
                                        0
                                first_index -= 1;
                            while last_index < PUZZLE_WIDTH :
                                for i, copy_clue in enumerate(copy_possibleRowClues) :
                                    try :
                                        GRAPH[last_index][h].possibleRowClues.remove(copy_clue);
                                    except :
                                        0
                                last_index += 1;
                        # if not only one clue is possible, but only one clue value is possible
                        # check if total cells filled with just those clues matches expected value (clue value * # of clues)
                        else :
                            num_clues = len(entry.possibleRowClues);
                            total_fills = num_clues*prev_clue;
                            for x, tmp_col in enumerate(GRAPH) :
                                if GRAPH[x][h].val == 'O' and cmp(GRAPH[x][h].possibleRowClues, entry.possibleRowClues) == 0 :
                                    total_fills -= 1;
                            if total_fills == 0 :
                                for x, tmp_col in enumerate(GRAPH) :
                                    if (not GRAPH[x][h].val == 'O') :
                                        for y in entry.possibleRowClues :
                                            try :
                                                GRAPH[x][h].possibleRowClues.remove(y) ;
                                            except :
                                                0

##################################################################################

        
########################################### MAIN ##############################################
print "Regression options:";
for i, puzzle_name in enumerate(PUZZLE_NAME) :
    print i, ":", puzzle_name;
print "all : run all puzzles";
regress_option = input("Enter regression choice: ");

if regress_option >= 0 and regress_option <= len(PUZZLE_NAME) - 1 :
    COL_CLUES = COL_CLUES_LIST[regress_option];
    ROW_CLUES = ROW_CLUES_LIST[regress_option];

    initialize_graph(COL_CLUES, ROW_CLUES);
    
    PREV_GRAPH = [ [ graphCell() for h in range(PUZZLE_HEIGHT)] for w in range(PUZZLE_WIDTH) ];   # horizontal list of vertical lists. top left is 0,0; bottom right is [w][h]
    
    debug = input("Option to print debug info 1 or 0? ");
    do_print = input("Option to print when any change occurs 1 or 0? ");
    print_graph(debug);
    print "\n";
    
    iteration = 1;
    
    while graphs_equal(PREV_GRAPH, GRAPH) == 0 :
        PREV_GRAPH = copy.deepcopy(GRAPH);
        # rows
        # iterates through rows and fills in overlaps
        TMP_GRAPH = copy.deepcopy(GRAPH);
        for i, clues in enumerate(ROW_CLUES) :
            mark_overlaps_row(i);
        if do_print == 1 and graphs_equal(TMP_GRAPH, GRAPH) == 0 :
            print iteration, " After overlaps row";
            print_graph(debug);
    
        # columns
        # iterates through columns and fills in overlaps
        TMP_GRAPH = copy.deepcopy(GRAPH);
        for i, clues in enumerate(COL_CLUES) :
            mark_overlaps_col(i);
        if do_print == 1 and graphs_equal(TMP_GRAPH, GRAPH) == 0 :
            print iteration, " After overlaps col";
            print_graph(debug);
        
        TMP_GRAPH = copy.deepcopy(GRAPH);
        for c in range (0, PUZZLE_WIDTH) :
            for r in range (0, PUZZLE_HEIGHT) :
                col_update(c, r);
                row_update(c, r);
        if do_print == 1 and graphs_equal(TMP_GRAPH, GRAPH) == 0 :
            print iteration, " After update";
            print_graph(debug);

        TMP_GRAPH = copy.deepcopy(GRAPH);
        check_for_completed_clues();
        if do_print == 1 and graphs_equal(TMP_GRAPH, GRAPH) == 0 :
            print iteration, " After checking for completed clues";
            print_graph(debug);
        iteration += 1;
    
    print_graph(0);
    print_debug_info();
    
    check_graph();
else :
    
    for puzzle_num, puzzle_name in enumerate(PUZZLE_NAME) :
        COL_CLUES = COL_CLUES_LIST[puzzle_num];
        ROW_CLUES = ROW_CLUES_LIST[puzzle_num];
    
        initialize_graph(COL_CLUES, ROW_CLUES);
        
        PREV_GRAPH = [ [ graphCell() for h in range(PUZZLE_HEIGHT)] for w in range(PUZZLE_WIDTH) ];   # horizontal list of vertical lists. top left is 0,0; bottom right is [w][h]
        
        while graphs_equal(PREV_GRAPH, GRAPH) == 0 :
            PREV_GRAPH = copy.deepcopy(GRAPH);
            for i, clues in enumerate(ROW_CLUES) :
                mark_overlaps_row(i);
            # columns
            # iterates through columns and fills in overlaps
            for i, clues in enumerate(COL_CLUES) :
                mark_overlaps_col(i);
        
            for c in range (0, PUZZLE_WIDTH) :
                for r in range (0, PUZZLE_HEIGHT) :
                    col_update(c, r);
                    row_update(c, r);

            check_for_completed_clues();
        
        if check_graph() == 0 :
            print "NOT COMPLETE", puzzle_num, puzzle_name;
        else :
            print "    COMPLETE", puzzle_num, puzzle_name;
