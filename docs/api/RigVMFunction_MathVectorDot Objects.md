## RigVMFunction_MathVectorDot Objects

```python
class RigVMFunction_MathVectorDot(RigVMFunction_MathVectorBase)
```

Returns the dot product between two vectors

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathVector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``a`` (Vector):  [Read-Write]
- ``b`` (Vector):  [Read-Write]
- ``result`` (float):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorDot.__init__"></a>

#### __init__

```python
def __init__(a: Vector = [0.000000, 0.000000, 0.000000],
             b: Vector = [0.000000, 0.000000, 0.000000],
             result: float = 0.000000) -> None
```

<a id="unreal.RigVMFunction_MathVectorDot.a"></a>

#### a

```python
@property
def a() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorDot.a"></a>

#### a

```python
@a.setter
def a(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathVectorDot.b"></a>

#### b

```python
@property
def b() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorDot.b"></a>

#### b

```python
@b.setter
def b(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathVectorDot.result"></a>

#### result

```python
@property
def result() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_MathVectorDot"></a>