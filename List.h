//----------------------------------------------------
// List.h
// Header file for List ADT
// Implement you List ADT as a linked
// list of integers.
// ---------------------------------------------------

typedef struct ListObj* List;

// Constructors-Destructors --------------------------

List newList( void );		// returns reference to new empty list.
void freeList( List* pL );	// Frees memory associated with *pL, sets *pL to NULL.

// Access functions ----------------------------------
  
int  length( List L );		// returns number of elements in L.
				// throws an error if L does not exist.
int  max( List L );		// returns index of element with highest value,
				// throws an error if L is empty, or L does not exist.
				// return value varies from 0..length(L)-1
int  find( List L, int i );	// returns the index of first occurence of i in L.
				// returns -1 if i is not found in L.


// Manipulation functions ----------------------------

void delElement( List L, int i );	// deletes the ith element of L.
					// throws an error if L has less than i+1 elements.
void appendList( List L, int i );	// append i to the end of L.
					// throws an error if L does not exist.
