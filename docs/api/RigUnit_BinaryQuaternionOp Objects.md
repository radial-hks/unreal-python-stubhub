## RigUnit_BinaryQuaternionOp Objects

```python
class RigUnit_BinaryQuaternionOp(RigUnit)
```

Two args and a result of Quaternion type

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Quaternion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``argument0`` (Quat):  [Read-Write]
- ``argument1`` (Quat):  [Read-Write]
- ``result`` (Quat):  [Read-Write]

<a id="unreal.RigUnit_BinaryQuaternionOp.__init__"></a>

#### __init__

```python
def __init__(argument0: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             argument1: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             result: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
```

<a id="unreal.RigUnit_BinaryQuaternionOp.argument0"></a>

#### argument0

```python
@property
def argument0() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigUnit_BinaryQuaternionOp.argument0"></a>

#### argument0

```python
@argument0.setter
def argument0(value: Quat) -> None
```

<a id="unreal.RigUnit_BinaryQuaternionOp.argument1"></a>

#### argument1

```python
@property
def argument1() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigUnit_BinaryQuaternionOp.argument1"></a>

#### argument1

```python
@argument1.setter
def argument1(value: Quat) -> None
```

<a id="unreal.RigUnit_BinaryQuaternionOp.result"></a>

#### result

```python
@property
def result() -> Quat
```

(Quat):  [Read-Only]

<a id="unreal.RigUnit_MultiplyQuaternion"></a>