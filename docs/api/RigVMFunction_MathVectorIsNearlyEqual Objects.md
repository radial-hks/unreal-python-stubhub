## RigVMFunction_MathVectorIsNearlyEqual Objects

```python
class RigVMFunction_MathVectorIsNearlyEqual(RigVMFunction_MathVectorBase)
```

Returns true if the value A is almost equal to B

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathVector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``a`` (Vector):  [Read-Write]
- ``b`` (Vector):  [Read-Write]
- ``result`` (bool):  [Read-Write]
- ``tolerance`` (float):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorIsNearlyEqual.__init__"></a>

#### __init__

```python
def __init__(a: Vector = [0.000000, 0.000000, 0.000000],
             b: Vector = [0.000000, 0.000000, 0.000000],
             tolerance: float = 0.000000,
             result: bool = False) -> None
```

<a id="unreal.RigVMFunction_MathVectorIsNearlyEqual.a"></a>

#### a

```python
@property
def a() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorIsNearlyEqual.a"></a>

#### a

```python
@a.setter
def a(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathVectorIsNearlyEqual.b"></a>

#### b

```python
@property
def b() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorIsNearlyEqual.b"></a>

#### b

```python
@b.setter
def b(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathVectorIsNearlyEqual.tolerance"></a>

#### tolerance

```python
@property
def tolerance() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorIsNearlyEqual.tolerance"></a>

#### tolerance

```python
@tolerance.setter
def tolerance(value: float) -> None
```

<a id="unreal.RigVMFunction_MathVectorIsNearlyEqual.result"></a>

#### result

```python
@property
def result() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigUnit_MathVectorIsNearlyEqual"></a>