grammar simple;

a0: A1 a2;
A1: 'a';
a2: A1 A3 | A3 a2 A1;
A3: 'b';