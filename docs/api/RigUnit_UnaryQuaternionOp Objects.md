## RigUnit_UnaryQuaternionOp Objects

```python
class RigUnit_UnaryQuaternionOp(RigUnit)
```

Two args and a result of Quaternion type

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Quaternion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``argument`` (Quat):  [Read-Write]
- ``result`` (Quat):  [Read-Write]

<a id="unreal.RigUnit_UnaryQuaternionOp.__init__"></a>

#### __init__

```python
def __init__(argument: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             result: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
```

<a id="unreal.RigUnit_UnaryQuaternionOp.argument"></a>

#### argument

```python
@property
def argument() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigUnit_UnaryQuaternionOp.argument"></a>

#### argument

```python
@argument.setter
def argument(value: Quat) -> None
```

<a id="unreal.RigUnit_UnaryQuaternionOp.result"></a>

#### result

```python
@property
def result() -> Quat
```

(Quat):  [Read-Only]

<a id="unreal.RigUnit_InverseQuaterion"></a>