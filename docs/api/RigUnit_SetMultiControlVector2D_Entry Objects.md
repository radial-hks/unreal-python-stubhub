## RigUnit_SetMultiControlVector2D_Entry Objects

```python
class RigUnit_SetMultiControlVector2D_Entry(StructBase)
```

Rig Unit Set Multi Control Vector 2D Entry

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetControlTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control`` (Name):  [Read-Write] The name of the Control to set the transform for.
- ``vector`` (Vector2D):  [Read-Write] The transform value to set for the given Control.

<a id="unreal.RigUnit_SetMultiControlVector2D_Entry.__init__"></a>

#### __init__

```python
def __init__(control: Name = "None",
             vector: Vector2D = [0.000000, 0.000000]) -> None
```

<a id="unreal.RigUnit_SetMultiControlVector2D_Entry.control"></a>

#### control

```python
@property
def control() -> Name
```

(Name):  [Read-Write] The name of the Control to set the transform for.

<a id="unreal.RigUnit_SetMultiControlVector2D_Entry.control"></a>

#### control

```python
@control.setter
def control(value: Name) -> None
```

<a id="unreal.RigUnit_SetMultiControlVector2D_Entry.vector"></a>

#### vector

```python
@property
def vector() -> Vector2D
```

(Vector2D):  [Read-Write] The transform value to set for the given Control.

<a id="unreal.RigUnit_SetMultiControlVector2D_Entry.vector"></a>

#### vector

```python
@vector.setter
def vector(value: Vector2D) -> None
```

<a id="unreal.RigUnit_SetMultiControlVector2D"></a>