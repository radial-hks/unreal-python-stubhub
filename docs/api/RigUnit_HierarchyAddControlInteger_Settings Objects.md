## RigUnit_HierarchyAddControlInteger_Settings Objects

```python
class RigUnit_HierarchyAddControlInteger_Settings(
        RigUnit_HierarchyAddControl_Settings)
```

Rig Unit Hierarchy Add Control Integer Settings

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DynamicHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control_enum`` (Enum):  [Read-Write]
- ``display_name`` (Name):  [Read-Write]
- ``limits`` (RigUnit_HierarchyAddControlInteger_LimitSettings):  [Read-Write]
- ``primary_axis`` (RigControlAxis):  [Read-Write]
- ``proxy`` (RigUnit_HierarchyAddControl_ProxySettings):  [Read-Write]
- ``shape`` (RigUnit_HierarchyAddControl_ShapeSettings):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlInteger_Settings.__init__"></a>

#### __init__

```python
def __init__(
    display_name: Name = "None",
    primary_axis: RigControlAxis = RigControlAxis.X,
    control_enum: Enum = None,
    limits: RigUnit_HierarchyAddControlInteger_LimitSettings = [[True, True],
                                                                0, 100, True],
    shape: RigUnit_HierarchyAddControl_ShapeSettings = [
        True, "Default", [1.000000, 0.000000, 0.000000, 1.000000],
        [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
         [1.000000, 1.000000, 1.000000]]
    ],
    proxy: RigUnit_HierarchyAddControl_ProxySettings = [
        False, [], RigControlVisibility.BASED_ON_SELECTION
    ]
) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlInteger_Settings.primary_axis"></a>

#### primary_axis

```python
@property
def primary_axis() -> RigControlAxis
```

(RigControlAxis):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlInteger_Settings.primary_axis"></a>

#### primary_axis

```python
@primary_axis.setter
def primary_axis(value: RigControlAxis) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlInteger_Settings.control_enum"></a>

#### control_enum

```python
@property
def control_enum() -> Enum
```

(Enum):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlInteger_Settings.control_enum"></a>

#### control_enum

```python
@control_enum.setter
def control_enum(value: Enum) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlInteger_Settings.limits"></a>

#### limits

```python
@property
def limits() -> RigUnit_HierarchyAddControlInteger_LimitSettings
```

(RigUnit_HierarchyAddControlInteger_LimitSettings):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlInteger_Settings.limits"></a>

#### limits

```python
@limits.setter
def limits(value: RigUnit_HierarchyAddControlInteger_LimitSettings) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlInteger_Settings.shape"></a>

#### shape

```python
@property
def shape() -> RigUnit_HierarchyAddControl_ShapeSettings
```

(RigUnit_HierarchyAddControl_ShapeSettings):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlInteger_Settings.shape"></a>

#### shape

```python
@shape.setter
def shape(value: RigUnit_HierarchyAddControl_ShapeSettings) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlInteger_Settings.proxy"></a>

#### proxy

```python
@property
def proxy() -> RigUnit_HierarchyAddControl_ProxySettings
```

(RigUnit_HierarchyAddControl_ProxySettings):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlInteger_Settings.proxy"></a>

#### proxy

```python
@proxy.setter
def proxy(value: RigUnit_HierarchyAddControl_ProxySettings) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlInteger"></a>