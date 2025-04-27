## RigVMFunction_MathQuaternionToRotator Objects

```python
class RigVMFunction_MathQuaternionToRotator(RigVMFunction_MathQuaternionBase)
```

Retrieves the rotator

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathQuaternion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``result`` (Rotator):  [Read-Write]
- ``value`` (Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionToRotator.__init__"></a>

#### __init__

```python
def __init__(value: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             result: Rotator = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionToRotator.value"></a>

#### value

```python
@property
def value() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionToRotator.value"></a>

#### value

```python
@value.setter
def value(value: Quat) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionToRotator.result"></a>

#### result

```python
@property
def result() -> Rotator
```

(Rotator):  [Read-Only]

<a id="unreal.RigUnit_MathQuaternionToRotator"></a>