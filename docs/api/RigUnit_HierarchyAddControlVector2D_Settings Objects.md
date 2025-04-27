## RigUnit_HierarchyAddControlVector2D_Settings Objects

```python
class RigUnit_HierarchyAddControlVector2D_Settings(
        RigUnit_HierarchyAddControl_Settings)
```

Rig Unit Hierarchy Add Control Vector 2D Settings

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DynamicHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``display_name`` (Name):  [Read-Write]
- ``filtered_channels`` (Array[RigControlTransformChannel]):  [Read-Write]
- ``limits`` (RigUnit_HierarchyAddControlVector2D_LimitSettings):  [Read-Write]
- ``primary_axis`` (RigControlAxis):  [Read-Write]
- ``proxy`` (RigUnit_HierarchyAddControl_ProxySettings):  [Read-Write]
- ``shape`` (RigUnit_HierarchyAddControl_ShapeSettings):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlVector2D_Settings.__init__"></a>

#### __init__

```python
def __init__(
        display_name: Name = "None",
        primary_axis: RigControlAxis = RigControlAxis.X,
        limits: RigUnit_HierarchyAddControlVector2D_LimitSettings = [[
            True, True
        ], [True, True], [0.000000, 0.000000], [1.000000, 1.000000], True],
        shape: RigUnit_HierarchyAddControl_ShapeSettings = [
            True, "Default", [1.000000, 0.000000, 0.000000, 1.000000],
            [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
             [1.000000, 1.000000, 1.000000]]
        ],
        proxy: RigUnit_HierarchyAddControl_ProxySettings = [
            False, [], RigControlVisibility.BASED_ON_SELECTION
        ],
        filtered_channels: Array[RigControlTransformChannel] = []) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlVector2D_Settings.primary_axis"></a>

#### primary_axis

```python
@property
def primary_axis() -> RigControlAxis
```

(RigControlAxis):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlVector2D_Settings.primary_axis"></a>

#### primary_axis

```python
@primary_axis.setter
def primary_axis(value: RigControlAxis) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlVector2D_Settings.limits"></a>

#### limits

```python
@property
def limits() -> RigUnit_HierarchyAddControlVector2D_LimitSettings
```

(RigUnit_HierarchyAddControlVector2D_LimitSettings):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlVector2D_Settings.limits"></a>

#### limits

```python
@limits.setter
def limits(value: RigUnit_HierarchyAddControlVector2D_LimitSettings) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlVector2D_Settings.shape"></a>

#### shape

```python
@property
def shape() -> RigUnit_HierarchyAddControl_ShapeSettings
```

(RigUnit_HierarchyAddControl_ShapeSettings):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlVector2D_Settings.shape"></a>

#### shape

```python
@shape.setter
def shape(value: RigUnit_HierarchyAddControl_ShapeSettings) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlVector2D_Settings.proxy"></a>

#### proxy

```python
@property
def proxy() -> RigUnit_HierarchyAddControl_ProxySettings
```

(RigUnit_HierarchyAddControl_ProxySettings):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlVector2D_Settings.proxy"></a>

#### proxy

```python
@proxy.setter
def proxy(value: RigUnit_HierarchyAddControl_ProxySettings) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlVector2D_Settings.filtered_channels"></a>

#### filtered_channels

```python
@property
def filtered_channels() -> Array[RigControlTransformChannel]
```

(Array[RigControlTransformChannel]):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlVector2D_Settings.filtered_channels"></a>

#### filtered_channels

```python
@filtered_channels.setter
def filtered_channels(value: Array[RigControlTransformChannel]) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlVector2D"></a>