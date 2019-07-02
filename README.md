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

## Looks like cython not like lambda functions, I have another pythong file with lambda which can not be compiled correctly even direct run is working
