## RigUnit_SetControlVisibility Objects

```python
class RigUnit_SetControlVisibility(RigUnitMutable)
```

SetControlVisibility is used to change the visibility on a control at runtime

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetControlVisibility.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``item`` (RigElementKey):  [Read-Write] The name of the Control to set the visibility for.
- ``pattern`` (str):  [Read-Only] If the ControlName is set to None this can be used to look for a series of Controls
- ``visible`` (bool):  [Read-Write] The visibility to set for the control

<a id="unreal.RigUnit_SetControlVisibility.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             item: RigElementKey = [RigElementType.NONE, "None"],
             pattern: str = "",
             visible: bool = False) -> None
```

<a id="unreal.RigUnit_SetControlVisibility.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write] The name of the Control to set the visibility for.

<a id="unreal.RigUnit_SetControlVisibility.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_SetControlVisibility.pattern"></a>

#### pattern

```python
@property
def pattern() -> str
```

(str):  [Read-Only] If the ControlName is set to None this can be used to look for a series of Controls

<a id="unreal.RigUnit_SetControlVisibility.visible"></a>

#### visible

```python
@property
def visible() -> bool
```

(bool):  [Read-Write] The visibility to set for the control

<a id="unreal.RigUnit_SetControlVisibility.visible"></a>

#### visible

```python
@visible.setter
def visible(value: bool) -> None
```

<a id="unreal.RigUnit_SetCurveValue"></a>