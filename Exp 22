% Facts
male(john).
male(paul).
male(jim).
female(mary).
female(susan).
female(lisa).

parent(john, paul).
parent(mary, paul).
parent(john, susan).
parent(mary, susan).
parent(paul, jim).
parent(lisa, jim).

% Rules
father(F, C) :- male(F), parent(F, C).
mother(M, C) :- female(M), parent(M, C).
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
grandparent(GP, GC) :- parent(GP, P), parent(P, GC).
grandfather(GF, GC) :- male(GF), grandparent(GF, GC).
grandmother(GM, GC) :- female(GM), grandparent(GM, GC).
