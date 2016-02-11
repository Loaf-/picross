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
# calculates clue sums for finding overlaps
def calc_clue_sums ( clues ) :
    clue_sums = [];
    for clue_set in clues :
        sum = 0;
        for clue in clue_set :
            sum = sum + clue;
        sum = sum + len(clue_set) - 1;
        clue_sums.append(sum);
    return clue_sums;

##################################################################################
def analyze_O_col ( col_number ) :
    for w in range (0, PUZZLE_HEIGHT) :
        # if O has multiple clues, see if any can be eliminated based on other Os
        if GRAPH[col_number][w].val == 'O' and len(GRAPH[col_number][w].possibleColClues) > 1 :
            clues_to_remove = [];
            lowest_clue_index = GRAPH[col_number][w].possibleColClues[0];
            highest_clue_index = GRAPH[col_number][w].possibleColClues[-1];
            # check cells before
            for tmp in range (0, w) :
                if GRAPH[col_number][tmp].val == 'O' :
                    tmp_lowest_clue_index = GRAPH[col_number][tmp].possibleColClues[0];
                    tmp_highest_clue_index = GRAPH[col_number][tmp].possibleColClues[-1];
                    # if lowest clues are the same but distance between cells is too big, add clue to remove list
                    if tmp_lowest_clue_index == lowest_clue_index and w-tmp+1 > COL_CLUES[col_number][lowest_clue_index] :
                        clues_to_remove.append(lowest_clue_index);
                        break;
                    elif tmp_lowest_clue_index > lowest_clue_index :
                        clues_to_remove.append(lowest_clue_index);
                        break;
            # check cells after
            for tmp in range(w+1, PUZZLE_HEIGHT) :
                if GRAPH[col_number][tmp].val == 'O' :
                    tmp_lowest_clue_index = GRAPH[col_number][tmp].possibleColClues[0];
                    tmp_highest_clue_index = GRAPH[col_number][tmp].possibleColClues[-1];
                    # if highest clues are the same but distance between cells is too big, add clue to remove list
                    if tmp_highest_clue_index == highest_clue_index and tmp-w+1 > COL_CLUES[col_number][highest_clue_index] :
                        clues_to_remove.append(highest_clue_index);
                        break;
                    elif tmp_highest_clue_index < highest_clue_index :
                        clues_to_remove.append(highest_clue_index);
                        break;
            for remove_clue in clues_to_remove :
                GRAPH[col_number][w].possibleColClues.remove(remove_clue);
            # check closest Os, if only X's in between and the closest O only has one possible clue update this cell's clue
                #down
            tmp_w = w-1;
            while tmp_w >= 0 :
                if GRAPH[col_number][tmp_w].val == 'X' :
                    tmp_w -= 1;
                else :
                    if GRAPH[col_number][tmp_w].val == 'O' and len(GRAPH[col_number][tmp_w].possibleColClues) == 1 and (w-tmp_w >= 2) :
                        GRAPH[col_number][w].possibleColClues = [GRAPH[col_number][tmp_w].possibleColClues[0]+1];
                    break;
                # corner case, all Xs before so clue must be 0
            if tmp_w < 0 :
                GRAPH[col_number][w].possibleColClues = [0];
                #up
            tmp_w = w+1;
            while tmp_w < PUZZLE_HEIGHT:
                if GRAPH[col_number][tmp_w].val == 'X' :
                    tmp_w += 1;
                else :
                    if GRAPH[col_number][tmp_w].val == 'O' and len(GRAPH[col_number][tmp_w].possibleColClues) == 1 and (tmp_w-w >= 2) :
                        GRAPH[col_number][w].possibleColClues = [GRAPH[col_number][tmp_w].possibleColClues[0]-1];
                    break;
                # corner case, all Xs after so clue must be largest index
            if tmp_w == PUZZLE_HEIGHT :
                GRAPH[col_number][w].possibleColClues = [len(COL_CLUES[col_number])-1];

        # if cell is O and only has one clue
        elif GRAPH[col_number][w].val == 'O' and len(GRAPH[col_number][w].possibleColClues) == 1 :
        # if O has only one possible clue, erase other cells with that clue that are outside of the clue value range
            if GRAPH[col_number][w].val == 'O' and len(GRAPH[col_number][w].possibleColClues) == 1 :
                clue_index = GRAPH[col_number][w].possibleColClues[0];
                clue_val = COL_CLUES[col_number][clue_index];
                # erase clue from cells outside of range before
                for r in range (0, w-clue_val+1) :
                    try :
                        GRAPH[col_number][r].possibleColClues.remove(clue_index);
                    except :
                        0;
                # erase clue from cells out of range after
                for r in range (w+clue_val, PUZZLE_HEIGHT) :
                    for lower_index in range (0, clue_index) :
                        try :   
                            GRAPH[col_number][r].possibleColClues.remove(lower_index);
                        except :
                            0;
                    try :
                        GRAPH[col_number][r].possibleColClues.remove(clue_index);
                    except :
                        0;

        # remove clues greater than this clue in all cells before it
            for tmp in range (0, w) :
                clues_to_remove = [];
                for clue in GRAPH[col_number][tmp].possibleColClues :
                    if clue > GRAPH[col_number][w].possibleColClues[0] :
                        clues_to_remove.append(clue);
                for remove_clue in clues_to_remove :
                    GRAPH[col_number][tmp].possibleColClues.remove(remove_clue);
        # remove clues less than this clue in all cells after it
            for tmp in range(w+1, PUZZLE_HEIGHT) :
                clues_to_remove = [];
                for clue in GRAPH[col_number][tmp].possibleColClues :
                    if clue < GRAPH[col_number][w].possibleColClues[0] :
                        clues_to_remove.append(clue);
                for remove_clue in clues_to_remove :
                    GRAPH[col_number][tmp].possibleColClues.remove(remove_clue);
        # clues directly before it need to be clue-1, there must be clueval number of cells with clue-1 as clue
            clue_index = GRAPH[col_number][w].possibleColClues[0];
            if (not clue_index == 0) and GRAPH[col_number][w-1].val == 'X' :
                prior_index = clue_index - 1;
                prior_clueval = COL_CLUES[col_number][prior_index];
                tmp_col_index = w - 2;
                while prior_clueval > 0 and tmp_col_index >= 0 :
                    if len(GRAPH[col_number][tmp_col_index].possibleColClues) > 0 :
                        try :
                            i = GRAPH[col_number][tmp_col_index].possibleColClues.index(prior_index);
                            if i > 0 :
                                tmp_list = GRAPH[col_number][tmp_col_index].possibleColClues[0:i+1];
                                GRAPH[col_number][tmp_col_index].possibleColClues = tmp_list;
                            else :
                                GRAPH[col_number][tmp_col_index].possibleColClues = [GRAPH[col_number][tmp_col_index].possibleColClues[0]];
                            prior_clueval -= 1;
                        except :
                            try :
                                GRAPH[col_number][tmp_col_index].fill_X();
                            except :
                                print "Cell",col_number,",",tmp_col_index;
                                print_row_data(tmp_col_index);
                                print_col_data(col_number);
                                raise;
                    tmp_col_index -= 1;
        # clues directly after it need to be clue+1, there must be clueval number of cells with clue+1 as clue
            clue_index = GRAPH[col_number][w].possibleColClues[0];
            if (not clue_index == len(COL_CLUES[col_number]) - 1) and GRAPH[col_number][w+1].val == 'X' :
                next_index = clue_index + 1;
                next_clueval = COL_CLUES[col_number][next_index];
                tmp_col_index = w + 2;
                while next_clueval > 0 and tmp_col_index < PUZZLE_HEIGHT :
                    if len(GRAPH[col_number][tmp_col_index].possibleColClues) > 0 :
                        try :
                            i = GRAPH[col_number][tmp_col_index].possibleColClues.index(next_index);
                            if i < len(GRAPH[col_number][tmp_col_index].possibleColClues) :
                                tmp_list = GRAPH[col_number][tmp_col_index].possibleColClues[i:];
                                GRAPH[col_number][tmp_col_index].possibleColClues = tmp_list;
                            else :
                                GRAPH[col_number][tmp_col_index].possibleColClues = [GRAPH[col_number][tmp_col_index].possibleColClues[-1]];
                            next_clueval -= 1;
                        except :
                            try :
                                GRAPH[col_number][tmp_col_index].fill_X();
                            except :
                                print "Cell",col_number,",",tmp_col_index;
                                print_row_data(tmp_col_index);
                                print_col_data(col_number);
                                raise;
                    tmp_col_index += 1;
    ## find contiguous Os, remove clues from those cells that are smaller than number of contiguous Os
    #front_index = 0;
    #end_index = -1;
    #while front_index < PUZZLE_HEIGHT :
    #    while front_index < PUZZLE_HEIGHT and not GRAPH[col_number][front_index].val == 'O' :
    #        front_index += 1;
    #    end_index = front_index;
    #    while end_index < PUZZLE_HEIGHT and GRAPH[col_number][end_index].val == 'O' :
    #        end_index += 1;
    #    o_length = end_index - front_index;
    #    # check clues in each cell in contiguous O
    #    for tmp in range(front_index, end_index) :
    #        try :
    #            for clue in GRAPH[col_number][tmp].possibleColClues :
    #                if COL_CLUES[col_number][clue] < o_length :
    #                    GRAPH[col_number][tmp].possibleColClues.remove(clue);
    #        except :
    #            0;
    #    front_index = end_index + 1;

    ## analyze cells between sections of Os without any Xs in between
    #first_O_length = 0;
    #first_O_last_index = -1;
    #second_O_length = 0;
    #second_O_first_index = -1;
    #index = 0;
    #while index < PUZZLE_HEIGHT :
    #    if GRAPH[col_number][index].val == 'O' :
    #        second_O_first_index = index;
    #        while index < PUZZLE_HEIGHT and GRAPH[col_number][index].val == 'O' :
    #            second_O_length += 1;
    #            index += 1;
    #        num_empty_between_Os = second_O_first_index - first_O_last_index - 1;
    #        #check cells between Os
    #        for between_index in range (first_O_last_index + 1, second_O_first_index) :
    #            possibleClues = GRAPH[col_number][between_index].possibleColClues;
    #            clues_to_remove = [];
    #            for clue in possibleClues :
    #                clue_space_req = COL_CLUES[col_number][clue];
    #                if first_O_last_index >= 0 and num_empty_between_Os <= 1 and clue_space_req <= 2 :
    #                    clues_to_remove.append(clue); 
    #            for remove_clue in clues_to_remove :
    #                GRAPH[col_number][between_index].possibleColClues.remove(remove_clue);
    #        first_O_last_index = second_O_first_index + second_O_length - 1;
    #        first_O_length = second_O_length;
    #        second_O_length = 0;
    #    else :
    #        index += 1;



##################################################################################
# look at Xs and see if any information can be derived
def analyze_X_col ( col_number ) :
    global ROW_CLUES, COL_CLUES;
    global PUZZLE_HEIGHT, PUZZLE_WIDTH;
    global GRAPH;

    current_index = 0;
    previous_index = -1;
    next_index = 0;

    # check if spaces between Xs can accomodate possible clues
    # if not, mark X
    # if clue shows up number of times between Xs less than its value clean it up
    # if so -- if the spaces between Xs can accomodate some clues and the space after X can't accomdate more than the rest of the clues -- see if there are overlaps
    #               0 1 1 0 0 1 1 1 0 1 1 1 1 0 0
    #   ex: 2 3 4 | _ _ _ X _ _ _ _ X _ _ _ _ _ _
    #               2 2 2   2 2 3 3   3 4 4 4 4 4
    #                       3 3   4   4
    sum_of_clues = 0;
    for clue in COL_CLUES[col_number] :
        sum_of_clues ++ clue;

    ignore_sum_clue_list = [];
    while current_index < PUZZLE_HEIGHT :
        tmp_ignore_sum_clue_list = [];
        # find X
        while current_index < PUZZLE_HEIGHT and not GRAPH[col_number][current_index].val == 'X' :
            current_index += 1;
        # analyze cells between last X and this X
        #### build list of clues between Xs, if the clues aren't clues beyond Xs update the possible clue spots between Xs
        list_of_clues = [];
        list_of_clues_only_between_Xs = [];
        for tmp_index in range(previous_index+1, current_index) :
            for clue in GRAPH[col_number][tmp_index].possibleColClues :
                try :
                    list_of_clues.index(clue);
                except :
                    list_of_clues.append(clue); # get list of all clues between Xs

        list_of_clues_only_between_Xs = list_of_clues;
        # check if list of clues between Xs show up outside of Xs
        clues_only_between_Xs = 1;
        for tmp_index in range (0, previous_index+1) : # check before first X
            for clue in GRAPH[col_number][tmp_index].possibleColClues :
                try :
                    list_of_clues.index(clue);
                    list_of_clues_only_between_Xs.remove(clue);
                    clues_only_between_Xs = 0;
                except :
                    0;
        for tmp_index in range (current_index, PUZZLE_HEIGHT) : # check after X
            for clue in GRAPH[col_number][tmp_index].possibleColClues :
                try :
                    list_of_clues.index(clue);
                    list_of_clues_only_between_Xs.remove(clue);
                    clues_only_between_Xs = 0;
                except :
                    0;
        #### Check clues between Xs, if some clues are only between Xs see if
        #### adding any of the additional clues could still fit between Xs
        #sum_clues_only_between_Xs = 0;
        #count = 0;
        #for clue in list_of_clues_only_between_Xs :
        #    sum_clues_only_between_Xs += COL_CLUES[col_number][clue];
        #    count += 1;
        #sum_clues_only_between_Xs += count - 1;
        #if sum_clues_only_between_Xs <= (current_index - (previous_index+1)) :
        #    for tmp_index in range(previous_index+1, current_index) :
        #        tmp_possibleColClues = GRAPH[col_number][tmp_index].possibleColClues;
        #        for clue in tmp_possibleColClues :
        #            try :
        #                list_of_clues_only_between_Xs.index(clue);
        #            except :
        #                if sum_clues_only_between_Xs + COL_CLUES[col_number][clue] + 1 > current_index - (previous_index + 1) :
        #                    GRAPH[col_number][tmp_index].possibleColClues.remove(clue);

        # update clues if clues only between Xs
        if clues_only_between_Xs == 1 and len(list_of_clues) > 0 :
            for tmp_index in range(previous_index+1, current_index) :
                new_possibleColClues = [];
                # sum of clues
                sum_after = 0;
                sum_before = 0;
                for clue in list_of_clues :
                    sum_after += COL_CLUES[col_number][clue];
                clue_index = 0;
                # check
                for clue in list_of_clues :
                    sum_after -= COL_CLUES[col_number][clue];
                    if ((tmp_index-(previous_index+1)) >= (sum_before + clue_index)) and ((tmp_index-(previous_index+1))< (current_index -(previous_index+1)) - (sum_after + (len(list_of_clues)-(clue_index+1)))) :
                        new_possibleColClues.append(clue);
                    clue_index += 1;
                    sum_before += COL_CLUES[col_number][clue];
                if len(new_possibleColClues) <= len(GRAPH[col_number][tmp_index].possibleColClues) :
                    GRAPH[col_number][tmp_index].possibleColClues = new_possibleColClues;
                #GRAPH[col_number][tmp_index].possibleColClues = new_possibleColClues;
        ###

        for cell_index in range(previous_index+1, current_index) :
            can_X = 1;
            clues_to_remove = [];
            # for each possible clue in the cell see if the value could fit between the Xs
            # count number of times clue appears between Xs, if it's less than clue value then remove it
            for clue in GRAPH[col_number][cell_index].possibleColClues :
                if COL_CLUES[col_number][clue] <= current_index - (previous_index + 1) :
                    count_of_clue = 0;
                    for tmp_index in range (previous_index+1, current_index) :
                        try :
                            tmp = GRAPH[col_number][tmp_index].possibleColClues.index(clue);
                            count_of_clue += 1;
                        except :
                            0;
                    if count_of_clue < COL_CLUES[col_number][clue] :
                            clues_to_remove.append(clue);
                    else:
                        can_X = 0;      # if clue can fit in between Xs, can not X
                else :
                    # if it can't fit, the clue is not valid for the cell
                    clues_to_remove.append(clue);

            for clue in clues_to_remove :
                GRAPH[col_number][cell_index].possibleColClues.remove(clue);
            if can_X == 1 :             # can only X if none of the clues can fit in between Xs
                try :
                    GRAPH[col_number][cell_index].fill_X();
                except :
                    print_col_data(col_number);
                    raise;

            ####
            ## check if sum of clues in a cell can fit in between Xs, if not, pop.  
            ## Cells between Xs after this should only take into account popped clues but should not actually remove the other clues
            sum_clues = 0;
            count = 0;
            for clue in GRAPH[col_number][cell_index].possibleColClues :
                try : 
                    ignore_sum_clue_list.index(clue);
                except :
                   sum_clues += COL_CLUES[col_number][clue];
                   count += 1;
            sum_clues += count - 1;
            while sum_clues > current_index - (previous_index+1) :
                try :
                    popped = GRAPH[col_number][cell_index].possibleColClues.pop();
                except :
                    0;
                sum_clues = 0;
                count = 0;
                for clue in GRAPH[col_number][cell_index].possibleColClues :
                    try :
                        ignore_sum_clue_list.index(clue);
                    except :
                        sum_clues += COL_CLUES[col_number][clue];
                        count += 1;
                sum_clues += count - 1;
            for remaining_clue in GRAPH[col_number][cell_index].possibleColClues :
                try :
                    tmp_ignore_sum_clue_list.index(remaining_clue);
                except :
                    tmp_ignore_sum_clue_list.append(remaining_clue);
        for remaining_clue in tmp_ignore_sum_clue_list :
            try :
                ignore_sum_clue_list.index(remaining_clue) ;
            except :
                ignore_sum_clue_list.append(remaining_clue);

        previous_index = current_index;
        current_index += 1;

##################################################################################
def analyze_O_row ( row_number ) :
    for w in range (0, PUZZLE_WIDTH) :
        # if O has multiple clues, see if any can be eliminated based on other Os
        if GRAPH[w][row_number].val == 'O' and len(GRAPH[w][row_number].possibleRowClues) > 1 :
            clues_to_remove = [];
            lowest_clue_index = GRAPH[w][row_number].possibleRowClues[0];
            highest_clue_index = GRAPH[w][row_number].possibleRowClues[-1];
            # check cells before
            for tmp in range (0, w) :
                if GRAPH[tmp][row_number].val == 'O' :
                    tmp_lowest_clue_index = GRAPH[tmp][row_number].possibleRowClues[0];
                    tmp_highest_clue_index = GRAPH[tmp][row_number].possibleRowClues[-1];
                    # if lowest clues are the same but distance between cells is too big, add clue to remove list
                    if tmp_lowest_clue_index == lowest_clue_index and w-tmp+1 > ROW_CLUES[row_number][lowest_clue_index] :
                        clues_to_remove.append(lowest_clue_index);
                        break;
                    elif tmp_lowest_clue_index > lowest_clue_index :
                        clues_to_remove.append(lowest_clue_index);
                        break;
            # check cells after
            for tmp in range(w+1, PUZZLE_WIDTH) :
                if GRAPH[tmp][row_number].val == 'O' :
                    tmp_lowest_clue_index = GRAPH[tmp][row_number].possibleRowClues[0];
                    tmp_highest_clue_index = GRAPH[tmp][row_number].possibleRowClues[-1];
                    # if highest clues are the same but distance between cells is too big, add clue to remove list
                    if tmp_highest_clue_index == highest_clue_index and tmp-w+1 > ROW_CLUES[row_number][highest_clue_index] :
                        clues_to_remove.append(highest_clue_index);
                        break;
                    elif tmp_highest_clue_index < highest_clue_index :
                        clues_to_remove.append(highest_clue_index);
                        break;
            for remove_clue in clues_to_remove :
                GRAPH[w][row_number].possibleRowClues.remove(remove_clue);
            # check closest Os, if only X's in between and the closest O only has one possible clue update this cell's clue
                #down
            tmp_w = w-1;
            while tmp_w >= 0 :
                if GRAPH[tmp_w][row_number].val == 'X' :
                    tmp_w -= 1;
                else :
                    if GRAPH[tmp_w][row_number].val == 'O' and len(GRAPH[tmp_w][row_number].possibleRowClues) == 1 and (w-tmp_w >= 2) :
                        GRAPH[w][row_number].possibleRowClues = [GRAPH[tmp_w][row_number].possibleRowClues[0]+1];
                    break;
                # corner case, all Xs before so clue must be 0
            if tmp_w < 0 :
                GRAPH[w][row_number].possibleRowClues = [0];
                #up
            tmp_w = w+1;
            while tmp_w < PUZZLE_WIDTH :
                if GRAPH[tmp_w][row_number].val == 'X' :
                    tmp_w += 1;
                else :
                    if GRAPH[tmp_w][row_number].val== 'O' and len(GRAPH[tmp_w][row_number].possibleRowClues) == 1 and (tmp_w-w >= 2) :
                        GRAPH[w][row_number].possibleRowClues = [GRAPH[tmp_w][row_number].possibleRowClues[0]-1];
                    break;
                # corner case, all Xs after so clue must be largest index
            if tmp_w == PUZZLE_WIDTH :
                GRAPH[w][row_number].possibleRowClues = [len(ROW_CLUES[row_number])-1];
        # if cell is O and only has one clue
        elif GRAPH[w][row_number].val == 'O' and len(GRAPH[w][row_number].possibleRowClues) == 1 :
        # if O has only one possible clue, erase other cells with that clue that are outside of the clue value range
            if GRAPH[w][row_number].val == 'O' and len(GRAPH[w][row_number].possibleRowClues) == 1 :
                clue_index = GRAPH[w][row_number].possibleRowClues[0];
                clue_val = ROW_CLUES[row_number][clue_index];
                # erase clue from cells outside of range before
                for r in range (0, w-clue_val+1) :
                    try :
                        GRAPH[r][row_number].possibleRowClues.remove(clue_index);
                    except :
                        0;
                # erase clue from cells out of range after, also erase clues with lower index
                for r in range (w+clue_val, PUZZLE_WIDTH) :
                    for lower_index in range (0, clue_index) :
                        try :   
                            GRAPH[r][row_number].possibleRowClues.remove(lower_index);
                        except :
                            0;
                    try :   
                        GRAPH[r][row_number].possibleRowClues.remove(clue_index);
                    except :
                        0;
        # remove clues greater than this clue in all cells before it
            for tmp in range (0, w) :
                clues_to_remove = [];
                for clue in GRAPH[tmp][row_number].possibleRowClues :
                    if clue > GRAPH[w][row_number].possibleRowClues[0] :
                        clues_to_remove.append(clue);
                for remove_clue in clues_to_remove :
                    GRAPH[tmp][row_number].possibleRowClues.remove(remove_clue);

        # remove clues less than this clue in all cells after it
            for tmp in range(w+1, PUZZLE_WIDTH) :
                clues_to_remove = [];
                for clue in GRAPH[tmp][row_number].possibleRowClues :
                    if clue < GRAPH[w][row_number].possibleRowClues[0] :
                        clues_to_remove.append(clue);
                for remove_clue in clues_to_remove :
                    GRAPH[tmp][row_number].possibleRowClues.remove(remove_clue);
        # clues directly before it need to be clue-1, there must be clueval number of cells with clue-1 as clue
            clue_index = GRAPH[w][row_number].possibleRowClues[0];
            if (not clue_index == 0) and GRAPH[w-1][row_number].val == 'X' :
                prior_index = clue_index - 1;
                prior_clueval = ROW_CLUES[row_number][prior_index];
                tmp_row_index = w - 2;
                while prior_clueval > 0 and tmp_row_index >= 0 :
                    if len(GRAPH[tmp_row_index][row_number].possibleRowClues) > 0 :
                        try :
                            i = GRAPH[tmp_row_index][row_number].possibleRowClues.index(prior_index);
                            if i > 0 :
                                tmp_list = GRAPH[tmp_row_index][row_number].possibleRowClues[0:i+1];
                                GRAPH[tmp_row_index][row_number].possibleRowClues = tmp_list;
                            else :
                                GRAPH[tmp_row_index][row_number].possibleRowClues = [GRAPH[tmp_row_index][row_number].possibleRowClues[0]];
                            prior_clueval -= 1;
                        except :
                            try :
                                GRAPH[tmp_row_index][row_number].fill_X();
                            except :
                                print "Cell",tmp_row_index,",",row_number;
                                print_col_data(tmp_row_index);
                                print_row_data(row_number);
                                raise;
                    tmp_row_index -= 1;
        # clues directly after it need to be clue+1, there must be clueval number of cells with clue+1 as clue
            clue_index = GRAPH[w][row_number].possibleRowClues[0];
            if (not clue_index == len(ROW_CLUES[row_number]) - 1) and GRAPH[w+1][row_number].val == 'X' :
                next_index = clue_index + 1;
                next_clueval = ROW_CLUES[row_number][next_index];
                tmp_row_index = w + 2;
                while next_clueval > 0 and tmp_row_index < PUZZLE_WIDTH :
                    if len(GRAPH[tmp_row_index][row_number].possibleRowClues) > 0 :
                        try :
                            i = GRAPH[tmp_row_index][row_number].possibleRowClues.index(next_index);
                            if i < len(GRAPH[tmp_row_index][row_number].possibleRowClues) :
                                tmp_list = GRAPH[tmp_row_index][row_number].possibleRowClues[i:];
                                GRAPH[tmp_row_index][row_number].possibleRowClues = tmp_list;
                            else :
                                GRAPH[tmp_row_index][row_number].possibleRowClues = [GRAPH[tmp_row_index][row_number].possibleRowClues[-1]];
                            next_clueval -= 1;
                        except :
                            try :
                                GRAPH[tmp_row_index][row_number].fill_X();
                            except :
                                print "Cell",tmp_row_index,",",row_number;
                                print_col_data(tmp_row_index);
                                print_row_data(row_number);
                                raise;
                    tmp_row_index += 1;
    ## find contiguous Os, remove clues from those cells that are smaller than number of contiguous Os
    #front_index = 0;
    #end_index = -1;
    #while front_index < PUZZLE_WIDTH :
    #    while front_index < PUZZLE_WIDTH and not GRAPH[front_index][row_number].val == 'O' :
    #        front_index += 1;
    #    end_index = front_index;
    #    while end_index < PUZZLE_WIDTH and GRAPH[end_index][row_number].val == 'O' :
    #        end_index += 1;
    #    o_length = end_index - front_index;
    #    # check clues in each cell in contiguous O
    #    for tmp in range(front_index, end_index) :
    #        try :
    #            for clue in GRAPH[tmp][row_number].possibleRowClues :
    #                if ROW_CLUES[row_number][clue] < o_length :
    #                    GRAPH[tmp][row_number].possibleRowClues.remove(clue);
    #        except :
    #            0;
    #    front_index = end_index + 1;

    ## analyze cells between sections of Os without any Xs in between
    #first_O_length = 0;
    #first_O_last_index = -1;
    #second_O_length = 0;
    #second_O_first_index = -1;
    #index = 0;
    #while index < PUZZLE_WIDTH :
    #    if GRAPH[index][row_number].val == 'O' :
    #        second_O_first_index = index;
    #        while index < PUZZLE_WIDTH and GRAPH[index][row_number].val == 'O' :
    #            second_O_length += 1;
    #            index += 1;
    #        num_empty_between_Os = second_O_first_index - first_O_last_index - 1;
    #        #check cells between Os
    #        for between_index in range (first_O_last_index + 1, second_O_first_index) :
    #            possibleClues = GRAPH[between_index][row_number].possibleRowClues;
    #            clues_to_remove = [];
    #            for clue in possibleClues :
    #                clue_space_req = ROW_CLUES[row_number][clue];
    #                if first_O_last_index >= 0 and num_empty_between_Os <= 1 and clue_space_req <= 2 :
    #                    clues_to_remove.append(clue); 
    #            for remove_clue in clues_to_remove :
    #                GRAPH[between_index][row_number].possibleRowClues.remove(remove_clue);
    #        first_O_last_index = second_O_first_index + second_O_length - 1;
    #        first_O_length = second_O_length;
    #        second_O_length = 0;
    #    else :
    #        index += 1;
        


##################################################################################
def analyze_X_row ( row_number ) :
    global ROW_CLUES, COL_CLUES;
    global PUZZLE_HEIGHT, PUZZLE_WIDTH;
    global GRAPH;

    current_index = 0;
    previous_index = -1;

    # check if spaces between Xs can accomodate possible clues
    ignore_sum_clue_list = [];
    while current_index < PUZZLE_WIDTH :
        tmp_ignore_sum_clue_list = [];
        while current_index < PUZZLE_WIDTH and not GRAPH[current_index][row_number].val == 'X' :
            current_index += 1;
    # analyze cells between last X and this X
        #### build list of clues between Xs, if the clues aren't clues beyond Xs, update the possible clue spots between Xs
        list_of_clues = [];
        for tmp_index in range(previous_index+1, current_index) :
            for clue in GRAPH[tmp_index][row_number].possibleRowClues :
                try :
                    list_of_clues.index(clue);
                except :
                    list_of_clues.append(clue); # get list of all clues between Xs

        list_of_clues_only_between_Xs = list_of_clues;
        # check if list of clues between Xs show up outside of Xs
        clues_only_between_Xs = 1;
        for tmp_index in range (0, previous_index+1) : # check before first X
            for clue in GRAPH[tmp_index][row_number].possibleRowClues :
                try :
                    list_of_clues.index(clue) ;
                    clues_only_between_Xs = 0;
                except :
                    0;
        for tmp_index in range (current_index, PUZZLE_WIDTH) : # check after X
            for clue in GRAPH[tmp_index][row_number].possibleRowClues :
                try :
                    list_of_clues.index(clue) ;
                    clues_only_between_Xs = 0;
                except :
                    0;
        #### Check clues between Xs, if some clues are only between Xs see if
        #### adding any of the additional clues could still fit between Xs
        #sum_clues_only_between_Xs = 0;
        #count = 0;
        #for clue in list_of_clues_only_between_Xs :
        #    sum_clues_only_between_Xs += ROW_CLUES[row_number][clue];
        #    count += 1;
        #sum_clues_only_between_Xs += count - 1;
        #if sum_clues_only_between_Xs <= (current_index - (previous_index+1)) :
        #    for tmp_index in range(previous_index+1, current_index) :
        #        tmp_possibleRowClues = GRAPH[tmp_index][row_number].possibleRowClues;
        #        for clue in tmp_possibleRowClues :
        #            try :
        #                list_of_clues_only_between_Xs.index(clue);
        #            except :
        #                if sum_clues_only_between_Xs + ROW_CLUES[row_number][clue] + 1 > current_index - (previous_index + 1) :
        #                    GRAPH[tmp_index][row_number].possibleRowClues.remove(clue);

        # update clues if clues only between Xs
        if clues_only_between_Xs == 1 and len(list_of_clues) > 0 :
            for tmp_index in range(previous_index+1, current_index) :
                new_possibleRowClues = [];
                # sum of clues
                sum_after = 0;
                sum_before = 0;
                for clue in list_of_clues :
                    sum_after += ROW_CLUES[row_number][clue];
                clue_index = 0;
                # check
                for clue in list_of_clues :
                    sum_after -= ROW_CLUES[row_number][clue];
                    if ((tmp_index-(previous_index+1)) >= (sum_before + clue_index)) and ((tmp_index-(previous_index+1))< (current_index -(previous_index+1)) - (sum_after + (len(list_of_clues)-(clue_index+1)))) :
                        new_possibleRowClues.append(clue);
                    clue_index += 1;
                    sum_before += ROW_CLUES[row_number][clue];
                if len(new_possibleRowClues) <= len(GRAPH[tmp_index][row_number].possibleRowClues) :
                    GRAPH[tmp_index][row_number].possibleRowClues = new_possibleRowClues;
                #GRAPH[tmp_index][row_number].possibleRowClues = new_possibleRowClues;
        ###

        for cell_index in range(previous_index+1, current_index) :
            can_X = 1;
            clues_to_remove = [];

            for clue in GRAPH[cell_index][row_number].possibleRowClues :
                if ROW_CLUES[row_number][clue] <= current_index - (previous_index + 1) :
                    # count number of times clue appears between Xs, if it's less than clue value then remove it
                    count_of_clue = 0;
                    for tmp_index in range (previous_index+1, current_index) :
                        try :
                            tmp = GRAPH[tmp_index][row_number].possibleRowClues.index(clue);
                            count_of_clue += 1;
                        except :
                            0;
                    if count_of_clue < ROW_CLUES[row_number][clue] :
                            clues_to_remove.append(clue);
                    else :
                        can_X = 0;  # if clue can fit in between Xs, can not X
                else :
                    # if it can't fit, the clue is not valid for the cell
                    clues_to_remove.append(clue);
            for clue in clues_to_remove :
                    GRAPH[cell_index][row_number].possibleRowClues.remove(clue);
            if can_X == 1 :         # can only X if none of the clues can fit in between Xs
                try :
                    GRAPH[cell_index][row_number].fill_X();
                except :
                    print_row_data(row_number);
                    raise;

            ####
            ## check if sum of clues in a cell can fit in between Xs, if not, pop.  
            ## Cells between Xs after this should only take into account popped clues but should not actually remove the other clues
            sum_clues = 0;
            count = 0;
            for clue in GRAPH[cell_index][row_number].possibleRowClues :
                try : 
                    ignore_sum_clue_list.index(clue);
                except :
                   sum_clues += ROW_CLUES[row_number][clue];
                   count += 1;
            sum_clues += count - 1;
            while sum_clues > current_index - (previous_index+1) :
                try :
                    popped = GRAPH[cell_index][row_number].possibleRowClues.pop();
                except :
                    0;
                sum_clues = 0;
                count = 0;
                for clue in GRAPH[cell_index][row_number].possibleRowClues :
                    try :
                        ignore_sum_clue_list.index(clue);
                    except :
                        sum_clues += ROW_CLUES[row_number][clue];
                        count += 1;
                sum_clues += count - 1;
            for remaining_clue in GRAPH[cell_index][row_number].possibleRowClues :
                try :
                    tmp_ignore_sum_clue_list.index(remaining_clue);
                except :
                    tmp_ignore_sum_clue_list.append(remaining_clue);
        for remaining_clue in tmp_ignore_sum_clue_list :
            try :
                ignore_sum_clue_list.index(remaining_clue) ;
            except :
                ignore_sum_clue_list.append(remaining_clue);

        previous_index = current_index;
        current_index += 1;

##################################################################################
# count number of times a clue shows up
# compare number against value of clue
# if number < 2*clue then there is some overlap
def mark_overlaps_row ( row_number ) :
    global ROW_CLUES, COL_CLUES;
    global GRAPH;

    # first index, last index
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

def mark_overlaps_col ( col_number ) :
    global ROW_CLUES, COL_CLUES;
    global GRAPH;

    # first index, last index
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
# if all possible clue values match contiguous Os
# number of cells with clue as possibility matches clue value
def check_for_completed_clues () :
    global GRAPH;
    for w, column in enumerate(GRAPH) :
        for h, entry in enumerate(column) :
            if len(entry.possibleColClues) == 0 or len(entry.possibleRowClues) == 0 :
                try :
                    entry.fill_X();
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
                            except :
                                print_col_data(w);
                                raise;
                        if last_index < PUZZLE_HEIGHT :
                            try :
                                GRAPH[w][last_index].fill_X();
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
                            except :
                                print_row_data(h);
                                raise;
                        if last_index < PUZZLE_WIDTH :
                            try :
                                GRAPH[last_index][h].fill_X();
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
def clean_clues_row ( row_number ) :
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
    
        TMP_GRAPH = copy.deepcopy(GRAPH);
        for i, clues in enumerate(ROW_CLUES) :
            analyze_X_row(i);
        if do_print == 1 and graphs_equal(TMP_GRAPH, GRAPH) == 0 :
            print iteration, " After analyze row X";
            print_graph(debug);
    
        TMP_GRAPH = copy.deepcopy(GRAPH);
        for i, clues in enumerate(ROW_CLUES) :
            analyze_O_row(i);
        if do_print == 1 and graphs_equal(TMP_GRAPH, GRAPH) == 0 :
            print iteration, " After analyze row O";
            print_graph(debug);
    
        TMP_GRAPH = copy.deepcopy(GRAPH);
        for i, clues in enumerate(ROW_CLUES) :
            clean_clues_row(i);
        if do_print == 1 and graphs_equal(TMP_GRAPH, GRAPH) == 0 :
            print iteration, " After clean clues row";
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
        for i, clues in enumerate(COL_CLUES) :
            analyze_X_col(i);
        if do_print == 1 and graphs_equal(TMP_GRAPH, GRAPH) == 0 :
            print iteration, " After analyze col X";
            print_graph(debug);
    
        TMP_GRAPH = copy.deepcopy(GRAPH);
        for i, clues in enumerate(COL_CLUES) :
            analyze_O_col(i);
        if do_print == 1 and graphs_equal(TMP_GRAPH, GRAPH) == 0 :
            print iteration, " After analyze col O";
            print_graph(debug);
    
        TMP_GRAPH = copy.deepcopy(GRAPH);
        for i, clues in enumerate(COL_CLUES) :
            clean_clues_col(i);
        if do_print == 1 and graphs_equal(TMP_GRAPH, GRAPH) == 0 :
            print iteration, " After clean clues col";
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
            for i, clues in enumerate(ROW_CLUES) :
                analyze_X_row(i);
            for i, clues in enumerate(ROW_CLUES) :
                analyze_O_row(i);
            for i, clues in enumerate(ROW_CLUES) :
                clean_clues_row(i);
            # columns
            # iterates through columns and fills in overlaps
            for i, clues in enumerate(COL_CLUES) :
                mark_overlaps_col(i);
            for i, clues in enumerate(COL_CLUES) :
                analyze_X_col(i);
            for i, clues in enumerate(COL_CLUES) :
                analyze_O_col(i);
            for i, clues in enumerate(COL_CLUES) :
                clean_clues_col(i);
        
            check_for_completed_clues();
        
        if check_graph() == 0 :
            print "NOT COMPLETE", puzzle_num, puzzle_name;
        else :
            print "    COMPLETE", puzzle_num, puzzle_name;
