## RigVMFunction_MathQuaternionFromRotator Objects

```python
class RigVMFunction_MathQuaternionFromRotator(RigVMFunction_MathQuaternionBase
                                              )
```

Makes a quaternion from a rotator

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathQuaternion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``result`` (Quat):  [Read-Write]
- ``rotator`` (Rotator):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionFromRotator.__init__"></a>

#### __init__

```python
def __init__(rotator: Rotator = [0.000000, 0.000000, 0.000000],
             result: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionFromRotator.rotator"></a>

#### rotator

```python
@property
def rotator() -> Rotator
```

(Rotator):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionFromRotator.rotator"></a>

#### rotator

```python
@rotator.setter
def rotator(value: Rotator) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionFromRotator.result"></a>

#### result

```python
@property
def result() -> Quat
```

(Quat):  [Read-Only]

<a id="unreal.RigUnit_MathQuaternionFromRotator"></a>