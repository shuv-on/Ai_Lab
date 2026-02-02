move(1, Source, Dest, _):-
    write('Move disk from '), write(Source), write(' to '), write(Dest), nl.
move(N, Source, Dest, Aux):-
    N > 1,
    M is N-1,
    move(M, Source, Aux, Dest),
    move(1, Source, Dest, Aux),
    move(M, Aux, Dest, Source).

/* --- QUERIES TO RUN ---
?- move(3, left, right, center).
 Output: 
Move disk from left to right
*/