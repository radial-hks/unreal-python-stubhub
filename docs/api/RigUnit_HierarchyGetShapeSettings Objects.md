## RigUnit_HierarchyGetShapeSettings Objects

```python
class RigUnit_HierarchyGetShapeSettings(RigUnit_DynamicHierarchyBase)
```

Retrieves the shape settings of a control

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DynamicHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``item`` (RigElementKey):  [Read-Write] * The item to change
- ``settings`` (RigUnit_HierarchyAddControl_ShapeSettings):  [Read-Write] * The shape settings for the control

<a id="unreal.RigUnit_HierarchyGetShapeSettings.__init__"></a>

#### __init__

```python
def __init__(
    item: RigElementKey = [RigElementType.NONE, "None"],
    settings: RigUnit_HierarchyAddControl_ShapeSettings = [
        True, "Default", [1.000000, 0.000000, 0.000000, 1.000000],
        [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
         [1.000000, 1.000000, 1.000000]]
    ]
) -> None
```

<a id="unreal.RigUnit_HierarchyGetShapeSettings.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write] * The item to change

<a id="unreal.RigUnit_HierarchyGetShapeSettings.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_HierarchyGetShapeSettings.settings"></a>

#### settings

```python
@property
def settings() -> RigUnit_HierarchyAddControl_ShapeSettings
```

(RigUnit_HierarchyAddControl_ShapeSettings):  [Read-Only] * The shape settings for the control

<a id="unreal.RigUnit_HierarchySetShapeSettings"></a>