## RigUnit_HierarchySetShapeSettings Objects

```python
class RigUnit_HierarchySetShapeSettings(RigUnit_DynamicHierarchyBaseMutable)
```

Changes the shape settings of a control
Note: This node only runs as part of the construction event.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DynamicHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``item`` (RigElementKey):  [Read-Write] * The item to change
- ``settings`` (RigUnit_HierarchyAddControl_ShapeSettings):  [Read-Write] * The shape settings for the control

<a id="unreal.RigUnit_HierarchySetShapeSettings.__init__"></a>

#### __init__

```python
def __init__(
    execute_context: ControlRigExecuteContext = [],
    item: RigElementKey = [RigElementType.NONE, "None"],
    settings: RigUnit_HierarchyAddControl_ShapeSettings = [
        True, "Default", [1.000000, 0.000000, 0.000000, 1.000000],
        [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
         [1.000000, 1.000000, 1.000000]]
    ]
) -> None
```

<a id="unreal.RigUnit_HierarchySetShapeSettings.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write] * The item to change

<a id="unreal.RigUnit_HierarchySetShapeSettings.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_HierarchySetShapeSettings.settings"></a>

#### settings

```python
@property
def settings() -> RigUnit_HierarchyAddControl_ShapeSettings
```

(RigUnit_HierarchyAddControl_ShapeSettings):  [Read-Write] * The shape settings for the control

<a id="unreal.RigUnit_HierarchySetShapeSettings.settings"></a>

#### settings

```python
@settings.setter
def settings(value: RigUnit_HierarchyAddControl_ShapeSettings) -> None
```

<a id="unreal.RigUnit_HierarchyAddSocket"></a>