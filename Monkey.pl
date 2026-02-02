/* --- PROLOG CODE --- */
/* Actions definitions: move(State1, Move, State2) */
/* 1. GRASP: If on box, at middle, and doesn't have banana */
move(state(middle, middle, on_box, has_not), 
 grasp, 
 state(middle, middle, on_box, has)).
/* 2. CLIMB: If at same position as box */
move(state(P, P, on_floor, H), 
 climb, 
 state(P, P, on_box, H)).
/* 3. PUSH: Monkey and box move from P1 to P2 */
move(state(P1, P1, on_floor, H), 
 push(P1, P2), 
 state(P2, P2, on_floor, H)).
/* 4. WALK: Monkey walks from P1 to P2 */
move(state(P1, B, on_floor, H), 
 walk(P1, P2), 
 state(P2, B, on_floor, H)).
/* Recursive Rule to check if goal is reachable */
canget(state(_, _, _, has)). /* Base case: Has banana */
canget(State1) :-
 move(State1, _, State2),
 canget(State2).
/* --- QUERY ---
?- canget(state(at_door, at_window, on_floor, has_not)).
 Output: true.
*/
