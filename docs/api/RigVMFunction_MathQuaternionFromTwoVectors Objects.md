## RigVMFunction_MathQuaternionFromTwoVectors Objects

```python
class RigVMFunction_MathQuaternionFromTwoVectors(
        RigVMFunction_MathQuaternionBase)
```

Makes a quaternion from two vectors, representing the shortest rotation between the two vectors.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathQuaternion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``a`` (Vector):  [Read-Write]
- ``b`` (Vector):  [Read-Write]
- ``result`` (Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionFromTwoVectors.__init__"></a>

#### __init__

```python
def __init__(a: Vector = [0.000000, 0.000000, 0.000000],
             b: Vector = [0.000000, 0.000000, 0.000000],
             result: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionFromTwoVectors.a"></a>

#### a

```python
@property
def a() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionFromTwoVectors.a"></a>

#### a

```python
@a.setter
def a(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionFromTwoVectors.b"></a>

#### b

```python
@property
def b() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionFromTwoVectors.b"></a>

#### b

```python
@b.setter
def b(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionFromTwoVectors.result"></a>

#### result

```python
@property
def result() -> Quat
```

(Quat):  [Read-Only]

<a id="unreal.RigUnit_MathQuaternionFromTwoVectors"></a>