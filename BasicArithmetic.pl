/* Sum of two numbers */
calc_sum(X, Y, Sum):-
    Sum is  X+Y.
/* Mul of two numbers*/
calc_mul(X, Y, Mul):-
    Mul is X*Y.
/* Subtraction of two numbers*/
calc_sub(X, Y, Sub):-
    Sub is X-Y.
/* Division of two numbers*/
calc_div(X, Y, Div):-
    Div is X/Y.
find_max(X, Y, Max):-
    X>=Y,
    Max is X.
/* --- QUERIES TO RUN ---
?- calc_sum(5, 3, Result).
 Output: Result = 8.
?- calc_mul(4, 2, Result).
 Output: Result = 8.
?- calc_sub(10, 6, Result).
 Output: Result = 4.
?- calc_div(20, 4, Result).
 Output: Result = 5.0.*/