/* --- PROLOG CODE --- */
/* 1. FACTS */
likes(john, mary).
likes(john, football).
likes(mary, sushi).
father(abir, basir).
father(basir, carl).
/* 2. RULES */
/* X is a friend of Y if both like the same thing Z */
friend(X, Y) :- 
 likes(X, Z), 
 likes(Y, Z).
/* X is grandfather of Z if X is father of Y AND Y is father of Z */
grandfather(X, Z) :- 
 father(X, Y), 
 father(Y, Z).
/* --- QUERIES TO RUN ---
?- likes(john, mary).
 Output: true.
?- grandfather(abir, Who).
 Output: Who = carl.
*/