## RigVMFunction_MathQuaternionDot Objects

```python
class RigVMFunction_MathQuaternionDot(RigVMFunction_MathQuaternionBase)
```

Returns the dot product between two quaternions

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathQuaternion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``a`` (Quat):  [Read-Write]
- ``b`` (Quat):  [Read-Write]
- ``result`` (float):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionDot.__init__"></a>

#### __init__

```python
def __init__(a: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             b: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             result: float = 0.000000) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionDot.a"></a>

#### a

```python
@property
def a() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionDot.a"></a>

#### a

```python
@a.setter
def a(value: Quat) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionDot.b"></a>

#### b

```python
@property
def b() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionDot.b"></a>

#### b

```python
@b.setter
def b(value: Quat) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionDot.result"></a>

#### result

```python
@property
def result() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_MathQuaternionDot"></a>