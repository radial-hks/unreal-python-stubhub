## RigUnit_ToRigSpace_Location Objects

```python
class RigUnit_ToRigSpace_Location(RigUnit)
```

Converts a position / location from world space to rig (global) space

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_WorldSpace.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``global_`` (Vector):  [Read-Write] The result position / location in global / rig space
- ``value`` (Vector):  [Read-Write] The input position / location in world

<a id="unreal.RigUnit_ToRigSpace_Location.__init__"></a>

#### __init__

```python
def __init__(value: Vector = [0.000000, 0.000000, 0.000000],
             global_: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigUnit_ToRigSpace_Location.value"></a>

#### value

```python
@property
def value() -> Vector
```

(Vector):  [Read-Write] The input position / location in world

<a id="unreal.RigUnit_ToRigSpace_Location.value"></a>

#### value

```python
@value.setter
def value(value: Vector) -> None
```

<a id="unreal.RigUnit_ToRigSpace_Location.location"></a>

#### location

```python
@property
def location() -> Vector
```

deprecated: 'location' was renamed to 'value'.

<a id="unreal.RigUnit_ToRigSpace_Location.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.RigUnit_ToRigSpace_Location.global_"></a>

#### global_

```python
@property
def global_() -> Vector
```

(Vector):  [Read-Only] The result position / location in global / rig space

<a id="unreal.RigUnit_ToWorldSpace_Rotation"></a>