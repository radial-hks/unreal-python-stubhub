## RigVMFunction_MathQuaternionFromRotatorV2 Objects

```python
class RigVMFunction_MathQuaternionFromRotatorV2(
        RigVMFunction_MathQuaternionBase)
```

Makes a quaternion from a rotator

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathQuaternion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``result`` (Quat):  [Read-Write]
- ``value`` (Rotator):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionFromRotatorV2.__init__"></a>

#### __init__

```python
def __init__(value: Rotator = [0.000000, 0.000000, 0.000000],
             result: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionFromRotatorV2.value"></a>

#### value

```python
@property
def value() -> Rotator
```

(Rotator):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionFromRotatorV2.value"></a>

#### value

```python
@value.setter
def value(value: Rotator) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionFromRotatorV2.result"></a>

#### result

```python
@property
def result() -> Quat
```

(Quat):  [Read-Only]

<a id="unreal.RigUnit_MathQuaternionFromRotatorV2"></a>