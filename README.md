# cython-example
Simple sample to use cython convery python module into so file

## Install cython
```
pip install cython
```

## To create so files from last2file.py to lastfile.so
```
python compile.py build_ext --inplace
```

## To test result
```
python main.py
```

## Looks like cython not like lambda functions, I have another python file with lambda functions which can not be compiled correctly even direct run is working


```
Cython does not support nested tuple argument unpacking.

Your lambda uses nested tuple arguments:

lambda (x,y): x + y

Replace that with:

lambda x: x[0] + x[1]

or even just:

sum

and perhaps mix in some itertools.product() too here, as in:

from itertools import product

def test():
    return sorted(product(xrange(10), repeat=2), key=sum)

but then you mostly end up with code mostly served by C routines anyway..
```
