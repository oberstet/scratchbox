# Lucas Sequences

[Lucas sequences](https://en.wikipedia.org/wiki/Lucas_sequence) <math>U_n(P,Q)</math> and <math>V_n(P, Q)</math> are certain [[constant-recursive sequence|constant-recursive]] [[integer sequence]]s that satisfy the [[recurrence relation]]

: <math>x*n = P \cdot x*{n - 1} - Q \cdot x\_{n - 2}</math>

where <math>P</math> and <math>Q</math> are fixed [[integer]]s. Any sequence satisfying this recurrence relation can be represented as a [[linear combination]] of the Lucas sequences <math>U_n(P, Q)</math> and <math>V_n(P, Q).</math>

> Famous examples of Lucas sequences include the Fibonacci numbers, Mersenne numbers,
> Pell numbers, Lucas numbers, Jacobsthal numbers, and a superset of Fermat numbers

The Lucas sequences for some values of P and Q have specific names:

- `Un(1, −1)`: Fibonacci numbers
- `Vn(1, −1)`: Lucas numbers
- `Un(2, −1)`: Pell numbers
- `Vn(2, −1)`: Pell–Lucas numbers (companion Pell numbers)
- `Un(1, −2)`: Jacobsthal numbers
- `Vn(1, −2)`: Jacobsthal–Lucas numbers
- `Un(3, 2)`: Mersenne numbers 2n − 1
- `Vn(3, 2)`: Numbers of the form 2n + 1, which include the Fermat numbers[2]
- `Un(6, 1)`: The square roots of the square triangular numbers.
- `Un(x, −1)`: Fibonacci polynomials
- `Vn(x, −1)`: Lucas polynomials
- `Un(2x, 1)`: Chebyshev polynomials of second kind
- `Vn(2x, 1)`: Chebyshev polynomials of first kind multiplied by 2
- `Un(x+1, x)`: Repunits in base x
- `Vn(x+1, x)`: xn + 1


## Usage

```
oberstet@amd-ryzen5:~/scm/oberstet/sempervivum/lucas$ just
Available recipes:
    default           # Liste aller Rezepte
    fibonacci_lucas n # P=1, Q=-1 erzeugt die klassischen Fibonacci-Zahlen (U_n) und Lucas-Zahlen (V_n)
    jacobsthal n      # P=1, Q=-2 erzeugt die Jacobsthal-Zahlen
    pell_lucas n      # P=2, Q=-1 erzeugt die Pell-Zahlen (U_n) und Pell-Lucas-Zahlen (V_n)
```

## Fibonacci-Zahlen

```
oberstet@amd-ryzen5:~/scm/oberstet/sempervivum/lucas$ just fibonacci_lucas 12
n       U_n (Fib)       V_n (Lucas)
------------------------------
0       0               2
1       1               1
2       1               3
3       2               4
4       3               7
5       5               11
6       8               18
7       13              29
8       21              47
9       34              76
10      55              123
11      89              199
```

## Pell-Lucas-Zahlen

```
oberstet@amd-ryzen5:~/scm/oberstet/sempervivum/lucas$ just pell_lucas 10
n       U_n (Pell)      V_n (Pell-Lucas)
-----------------------------------
0       0               2
1       1               2
2       2               6
3       5               14
4       12              34
5       29              82
6       70              198
7       169             478
8       408             1154
9       985             2786
```

## Jacobsthal-Zahlen

```
oberstet@amd-ryzen5:~/scm/oberstet/sempervivum/lucas$ just jacobsthal 10
n       U_n (Jacobsthal)
-------------------------
0       0
1       1
2       1
3       3
4       5
5       11
6       21
7       43
8       85
9       171
```
