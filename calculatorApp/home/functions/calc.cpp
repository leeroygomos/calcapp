#include <iostream>
#include <math.h>
#include "calc.h"
using namespace std;

long long int factorial(long long int n){
    if (n == 1){
        return 1;
    }
    else {
        return n * factorial(n-1);
    }
}

long long int fibonacci(long long int n){
    if (n == 0){
        return 0;
    }
    else if (n == 1 || n == 2){
        return 1;
    }
    else {
        return fibonacci(n-1) + fibonacci(n-2);
    }
}

long long int exponent(long long int n, long long int exp){
    if (exp == 0){
        return 1;
    }
    long long int val = 1;
    for (int i = 0; i < exp; i++){
        val = val * n;
    }
    return val;
}

double quadratic1(double a, double b, double c){
    double x1 = -b + sqrt(b*b-4*a*c) / 2 * a;
    return x1;
}

double quadratic2(double a, double b, double c){
    double x2 = -b - sqrt(b*b-4*a*c) / 2 * a;
    return x2;
}

double pythagorean(double a, double b){
    double c2 = a*a + b*b;
    double c = sqrt(c2);
    return c;
}