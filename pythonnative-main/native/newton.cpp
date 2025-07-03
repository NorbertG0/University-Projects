#include "newton.h"

// obliczanie wspolczynnikow Newtona
void divided_diff(double *x, double *y, double *a, int n) {
    for (int i = 0; i < n; i++)
        a[i] = y[i];

    for (int j = 1; j < n; j++) {
        for (int i = n - 1; i >= j; i--) {
            a[i] = (a[i] - a[i - 1]) / (x[i] - x[i - j]);
        }
    }
}

// Obliczanie interpolowanego wielomianu
double newton_interpolation(double *x, double *a, int n, double value) {
    double result = a[n - 1];
    for (int i = n - 2; i >= 0; i--) {
        result = result * (value - x[i]) + a[i];
    }
    return result;
}
