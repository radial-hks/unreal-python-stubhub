## RigUnit_ShapeExists Objects

```python
class RigUnit_ShapeExists(RigUnit)
```

Checks whether or not a shape is available in the rig's shape libraries

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_UserData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``result`` (bool):  [Read-Write] * True if the shape name exists in any of the shape libraries
- ``shape_name`` (Name):  [Read-Write] * The name of the shape to search for

<a id="unreal.RigUnit_ShapeExists.__init__"></a>

#### __init__

```python
def __init__(shape_name: Name = "None", result: bool = False) -> None
```

<a id="unreal.RigUnit_ShapeExists.shape_name"></a>

#### shape_name

```python
@property
def shape_name() -> Name
```

(Name):  [Read-Write] * The name of the shape to search for

<a id="unreal.RigUnit_ShapeExists.shape_name"></a>

#### shape_name

```python
@shape_name.setter
def shape_name(value: Name) -> None
```

<a id="unreal.RigUnit_ShapeExists.result"></a>

#### result

```python
@property
def result() -> bool
```

(bool):  [Read-Only] * True if the shape name exists in any of the shape libraries

<a id="unreal.RigUnit_DebugBezier"></a>