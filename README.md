# VectorLib: A library to create and manage vectors in Python.
## Installation
```sh
python -m pip install vectorlib-py
# or
python -m pip install git+https://github.com/AaravMalani/vectorlib
```

## Usage
```python
import vectorlib
u = vectorlib.Vector(0, 10) 
v = vectorlib.Vector(-10, 0, 3)
t = 4
a_avg = (v-u)/t
print(a_avg) # Vector(-2.5, -2.5, 0.75)
print(a_avg.magnitude) # 3.61420807370024 
print(a_avg.dim) # (3,)
print(a_avg.direction) # Vector(-0.6917144638660746, -0.6917144638660746, 0.2075143391598224)
m = 4 
f = m * a
print(f) # Vector(-10.0, -10.0, 3.0)
print(f.dot(a_avg)) # 52.25
print(f.cross(a_avg)) # Vector(0.0, 0.0, 0.0)
```