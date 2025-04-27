## RigUnit_GetControlVisibility Objects

```python
class RigUnit_GetControlVisibility(RigUnit)
```

GetControlVisibility is used to retrieve the visibility of a control

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetControlVisibility.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``item`` (RigElementKey):  [Read-Write] The name of the Control to set the visibility for.
- ``visible`` (bool):  [Read-Write] The visibility of the control

<a id="unreal.RigUnit_GetControlVisibility.__init__"></a>

#### __init__

```python
def __init__(item: RigElementKey = [RigElementType.NONE, "None"],
             visible: bool = False) -> None
```

<a id="unreal.RigUnit_GetControlVisibility.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write] The name of the Control to set the visibility for.

<a id="unreal.RigUnit_GetControlVisibility.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_GetControlVisibility.visible"></a>

#### visible

```python
@property
def visible() -> bool
```

(bool):  [Read-Only] The visibility of the control

<a id="unreal.RigUnit_SetControlVisibility"></a>