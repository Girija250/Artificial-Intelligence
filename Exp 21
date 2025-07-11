% Facts: These are known facts in the knowledge base.
person(john).
person(mary).
person(jane).
person(paul).

% Facts about relationships: these describe who is a parent of whom.
parent(john, mary).
parent(john, jane).
parent(mary, paul).

% Rules: Rules that help deduce new facts.
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

% Forward chaining rule: if we know that X is a parent of Y, we can infer X is a grandparent of Y.
forward_chaining(Goal) :-
    person(X),
    Goal = grandparent(X, Y),
    call(Goal),
    write(X), write(' is the grandparent of '), write(Y), nl.
