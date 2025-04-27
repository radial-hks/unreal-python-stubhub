## RigVMFunction_MathVectorParallel Objects

```python
class RigVMFunction_MathVectorParallel(RigVMFunction_MathVectorBase)
```

Returns true if the two vectors are parallel

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathVector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``a`` (Vector):  [Read-Write]
- ``b`` (Vector):  [Read-Write]
- ``result`` (bool):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorParallel.__init__"></a>

#### __init__

```python
def __init__(a: Vector = [0.000000, 0.000000, 0.000000],
             b: Vector = [0.000000, 0.000000, 0.000000],
             result: bool = False) -> None
```

<a id="unreal.RigVMFunction_MathVectorParallel.a"></a>

#### a

```python
@property
def a() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorParallel.a"></a>

#### a

```python
@a.setter
def a(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathVectorParallel.b"></a>

#### b

```python
@property
def b() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorParallel.b"></a>

#### b

```python
@b.setter
def b(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathVectorParallel.result"></a>

#### result

```python
@property
def result() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigUnit_MathVectorParallel"></a>