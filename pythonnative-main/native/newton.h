#ifndef NEWTON_H
#define NEWTON_H

extern "C" {
    void divided_diff(double *x, double *y, double *a, int n);
    double newton_interpolation(double *x, double *a, int n, double value);
}

#endif
