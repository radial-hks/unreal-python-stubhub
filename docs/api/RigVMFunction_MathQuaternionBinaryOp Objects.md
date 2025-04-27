## RigVMFunction_MathQuaternionBinaryOp Objects

```python
class RigVMFunction_MathQuaternionBinaryOp(RigVMFunction_MathQuaternionBase)
```

Rig VMFunction Math Quaternion Binary Op

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathQuaternion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``a`` (Quat):  [Read-Write]
- ``b`` (Quat):  [Read-Write]
- ``result`` (Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionBinaryOp.__init__"></a>

#### __init__

```python
def __init__(a: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             b: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             result: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionBinaryOp.a"></a>

#### a

```python
@property
def a() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionBinaryOp.a"></a>

#### a

```python
@a.setter
def a(value: Quat) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionBinaryOp.b"></a>

#### b

```python
@property
def b() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionBinaryOp.b"></a>

#### b

```python
@b.setter
def b(value: Quat) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionBinaryOp.result"></a>

#### result

```python
@property
def result() -> Quat
```

(Quat):  [Read-Only]

<a id="unreal.RigUnit_MathQuaternionBinaryOp"></a>