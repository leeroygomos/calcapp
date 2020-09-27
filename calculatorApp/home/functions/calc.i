%module calc

%{
#define SWIG_FILE_WITH_INIT
#include "calc.h"
%}

long long int factorial(long long int n);
long long int fibonacci(long long int n);
long long int exponent(long long int n, long long int exp);
double quadratic1(double a, double b, double c);
double quadratic2(double a, double b, double c);
double pythagorean(double a, double b);
