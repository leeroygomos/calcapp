from django.shortcuts import render
from django.http import HttpResponseRedirect
from home.functions import calc
from home.functions import conversions

# Create your views here.


def home(request):
    return render(request, 'home/home.html')

def factorial(request):
    if request.method =='POST':
        data = request.POST.get('data')
        if data == '':
            return render(request, 'home/factorial.html')
        fact = calc.factorial(int(data))
        return render(request, 'home/factorial.html', {'n': data, 'fact': fact})
    else:
        return render(request, 'home/factorial.html')

def conversion(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        if data == '':
            return render(request, 'home/conversion.html')
        start = request.POST.get('from')
        end = request.POST.get('to')
        if start == 'decimal':
            if end == 'hex':
                val = conversions.DecToHex(int(data))
            elif end == 'binary':
                val = conversions.DecToBin(int(data))
            elif end == 'decimal':
                val = data
            else:
                print('Something is wrong!')
                val = 'error'
            return render(request, 'home/conversion.html', {'data': data, 'val': val })
        elif start == 'hex':
            if end == 'hex':
                val = data
            elif end == 'binary':
                val = conversions.HexToBin(data)
            elif end == 'decimal':
                val = conversions.HexToDec(data)
            else:
                print('Something is wrong!')
                val = 'error'
            return render(request, 'home/conversion.html', {'data': data, 'val': val })
        elif start == 'binary':
            if end == 'hex':
                val = conversions.BinToHex(data)
            elif end == 'binary':
                val = data
            elif end == 'decimal':
                val = conversions.BinToDec(data)
            else:
                print('Something is wrong!')
                val = 'error'
            return render(request, 'home/conversion.html', {'data': data, 'val': val })
        else:
           return render(request, 'home/conversion.html') 
    else:
        return render(request, 'home/conversion.html')

def fibonacci(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        if data == '':
            return render(request, 'home/fibonacci.html')
        fib = calc.fibonacci(int(data))
        return render(request, 'home/fibonacci.html', {'data': data, 'fib': fib})
    else:
        return render(request, 'home/fibonacci.html')


def exponent(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        if data == '':
            return render(request, 'home/exponent.html')
        exp = request.POST.get('exp')
        val = calc.exponent(int(data),int(exp))
        return render(request, 'home/exponent.html', {'data': data, 'exp': exp, 'val': val})
    else:
        return render(request, 'home/exponent.html')

def quadratic(request):
    if request.method == 'POST':
        a = request.POST.get('a')
        b = request.POST.get('b')
        c = request.POST.get('c')
        if a == '' or b == '' or c == '':
            return render(request, 'home/quadratic.html')
        x1 = calc.quadratic1(float(a),float(b),float(c))
        x2 = calc.quadratic2(float(a),float(b),float(c))
        return render(request, 'home/quadratic.html', {'a': a, 'b': b, 'c': c, 'x1': x1, 'x2': x2})
    else:
        return render(request, 'home/quadratic.html')

def pythagorean(request):
    if request.method == 'POST':
        a = request.POST.get('a')
        b = request.POST.get('b')
        if a == '' or b == '':
            return render(request, 'home/pythagorean.html')
        c = calc.pythagorean(float(a),float(b))
        return render(request, 'home/pythagorean.html', {'a': a, 'b': b, 'c': c})
    else:
        return render(request, 'home/pythagorean.html')

