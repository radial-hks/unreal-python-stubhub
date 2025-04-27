## RigUnit_MultiFABRIK_EndEffector Objects

```python
class RigUnit_MultiFABRIK_EndEffector(StructBase)
```

Rig Unit Multi FABRIK End Effector

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_MultiFABRIK.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone`` (Name):  [Read-Write] The last bone in the chain to solve - the effector
- ``location`` (Vector):  [Read-Write] The transform of the effector in global space

<a id="unreal.RigUnit_MultiFABRIK_EndEffector.__init__"></a>

#### __init__

```python
def __init__(bone: Name = "None",
             location: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigUnit_MultiFABRIK_EndEffector.bone"></a>

#### bone

```python
@property
def bone() -> Name
```

(Name):  [Read-Write] The last bone in the chain to solve - the effector

<a id="unreal.RigUnit_MultiFABRIK_EndEffector.bone"></a>

#### bone

```python
@bone.setter
def bone(value: Name) -> None
```

<a id="unreal.RigUnit_MultiFABRIK_EndEffector.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write] The transform of the effector in global space

<a id="unreal.RigUnit_MultiFABRIK_EndEffector.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.RigUnit_MultiFABRIK"></a>