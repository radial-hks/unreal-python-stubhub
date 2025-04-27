## RigVMFunction_MathQuaternionSlerp Objects

```python
class RigVMFunction_MathQuaternionSlerp(RigVMFunction_MathQuaternionBase)
```

Linearly interpolates between A and B using the ratio T

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathQuaternion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``a`` (Quat):  [Read-Write]
- ``b`` (Quat):  [Read-Write]
- ``result`` (Quat):  [Read-Write]
- ``t`` (float):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionSlerp.__init__"></a>

#### __init__

```python
def __init__(a: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             b: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             t: float = 0.000000,
             result: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionSlerp.a"></a>

#### a

```python
@property
def a() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionSlerp.a"></a>

#### a

```python
@a.setter
def a(value: Quat) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionSlerp.b"></a>

#### b

```python
@property
def b() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionSlerp.b"></a>

#### b

```python
@b.setter
def b(value: Quat) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionSlerp.t"></a>

#### t

```python
@property
def t() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionSlerp.t"></a>

#### t

```python
@t.setter
def t(value: float) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionSlerp.result"></a>

#### result

```python
@property
def result() -> Quat
```

(Quat):  [Read-Only]

<a id="unreal.RigUnit_MathQuaternionSlerp"></a>