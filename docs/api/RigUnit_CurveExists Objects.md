## RigUnit_CurveExists Objects

```python
class RigUnit_CurveExists(RigUnit)
```

CurveExists is used to check whether a curve exists or not.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_CurveExists.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``curve`` (Name):  [Read-Write] The name of the Curve to retrieve the transform for.
- ``exists`` (bool):  [Read-Write] Boolean indicating whether the named curve exists or not.
  Does not indicate whether the curve's value is valid or not.

<a id="unreal.RigUnit_CurveExists.__init__"></a>

#### __init__

```python
def __init__(curve: Name = "None", exists: bool = False) -> None
```

<a id="unreal.RigUnit_CurveExists.curve"></a>

#### curve

```python
@property
def curve() -> Name
```

(Name):  [Read-Write] The name of the Curve to retrieve the transform for.

<a id="unreal.RigUnit_CurveExists.curve"></a>

#### curve

```python
@curve.setter
def curve(value: Name) -> None
```

<a id="unreal.RigUnit_CurveExists.exists"></a>

#### exists

```python
@property
def exists() -> bool
```

(bool):  [Read-Only] Boolean indicating whether the named curve exists or not.
Does not indicate whether the curve's value is valid or not.

<a id="unreal.RigUnit_GetBoneTransform"></a>