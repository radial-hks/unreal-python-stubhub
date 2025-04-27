## RigVMFunction_MathVectorLerp Objects

```python
class RigVMFunction_MathVectorLerp(RigVMFunction_MathVectorBase)
```

Linearly interpolates between A and B using the ratio T

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathVector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``a`` (Vector):  [Read-Write]
- ``b`` (Vector):  [Read-Write]
- ``result`` (Vector):  [Read-Write]
- ``t`` (float):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorLerp.__init__"></a>

#### __init__

```python
def __init__(a: Vector = [0.000000, 0.000000, 0.000000],
             b: Vector = [0.000000, 0.000000, 0.000000],
             t: float = 0.000000,
             result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathVectorLerp.a"></a>

#### a

```python
@property
def a() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorLerp.a"></a>

#### a

```python
@a.setter
def a(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathVectorLerp.b"></a>

#### b

```python
@property
def b() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorLerp.b"></a>

#### b

```python
@b.setter
def b(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathVectorLerp.t"></a>

#### t

```python
@property
def t() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorLerp.t"></a>

#### t

```python
@t.setter
def t(value: float) -> None
```

<a id="unreal.RigVMFunction_MathVectorLerp.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_MathVectorLerp"></a>