## RigVMFunction_Timeline Objects

```python
class RigVMFunction_Timeline(RigVMFunction_SimBase)
```

Simulates a time value - can act as a timeline playing back

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_Timeline.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``speed`` (float):  [Read-Write]
- ``time`` (float):  [Read-Write]

<a id="unreal.RigVMFunction_Timeline.__init__"></a>

#### __init__

```python
def __init__(speed: float = 0.000000, time: float = 0.000000) -> None
```

<a id="unreal.RigVMFunction_Timeline.speed"></a>

#### speed

```python
@property
def speed() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_Timeline.speed"></a>

#### speed

```python
@speed.setter
def speed(value: float) -> None
```

<a id="unreal.RigVMFunction_Timeline.time"></a>

#### time

```python
@property
def time() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_Timeline"></a>