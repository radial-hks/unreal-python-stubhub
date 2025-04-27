## RigUnit_HierarchyAddControlFloat_Settings Objects

```python
class RigUnit_HierarchyAddControlFloat_Settings(
        RigUnit_HierarchyAddControl_Settings)
```

Rig Unit Hierarchy Add Control Float Settings

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DynamicHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``display_name`` (Name):  [Read-Write]
- ``is_scale`` (bool):  [Read-Write]
- ``limits`` (RigUnit_HierarchyAddControlFloat_LimitSettings):  [Read-Write]
- ``primary_axis`` (RigControlAxis):  [Read-Write]
- ``proxy`` (RigUnit_HierarchyAddControl_ProxySettings):  [Read-Write]
- ``shape`` (RigUnit_HierarchyAddControl_ShapeSettings):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlFloat_Settings.__init__"></a>

#### __init__

```python
def __init__(
    display_name: Name = "None",
    primary_axis: RigControlAxis = RigControlAxis.X,
    is_scale: bool = False,
    limits: RigUnit_HierarchyAddControlFloat_LimitSettings = [[True,
                                                               True], 0.000000,
                                                              100.000000,
                                                              True],
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

<a id="unreal.RigUnit_HierarchyAddControlFloat_Settings.primary_axis"></a>

#### primary_axis

```python
@property
def primary_axis() -> RigControlAxis
```

(RigControlAxis):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlFloat_Settings.primary_axis"></a>

#### primary_axis

```python
@primary_axis.setter
def primary_axis(value: RigControlAxis) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlFloat_Settings.is_scale"></a>

#### is_scale

```python
@property
def is_scale() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlFloat_Settings.is_scale"></a>

#### is_scale

```python
@is_scale.setter
def is_scale(value: bool) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlFloat_Settings.limits"></a>

#### limits

```python
@property
def limits() -> RigUnit_HierarchyAddControlFloat_LimitSettings
```

(RigUnit_HierarchyAddControlFloat_LimitSettings):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlFloat_Settings.limits"></a>

#### limits

```python
@limits.setter
def limits(value: RigUnit_HierarchyAddControlFloat_LimitSettings) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlFloat_Settings.shape"></a>

#### shape

```python
@property
def shape() -> RigUnit_HierarchyAddControl_ShapeSettings
```

(RigUnit_HierarchyAddControl_ShapeSettings):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlFloat_Settings.shape"></a>

#### shape

```python
@shape.setter
def shape(value: RigUnit_HierarchyAddControl_ShapeSettings) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlFloat_Settings.proxy"></a>

#### proxy

```python
@property
def proxy() -> RigUnit_HierarchyAddControl_ProxySettings
```

(RigUnit_HierarchyAddControl_ProxySettings):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlFloat_Settings.proxy"></a>

#### proxy

```python
@proxy.setter
def proxy(value: RigUnit_HierarchyAddControl_ProxySettings) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlElement"></a>