## RigUnit_HierarchyAddControlRotator_Settings Objects

```python
class RigUnit_HierarchyAddControlRotator_Settings(
        RigUnit_HierarchyAddControl_Settings)
```

Rig Unit Hierarchy Add Control Rotator Settings

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DynamicHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``display_name`` (Name):  [Read-Write]
- ``filtered_channels`` (Array[RigControlTransformChannel]):  [Read-Write]
- ``initial_space`` (RigVMTransformSpace):  [Read-Write]
- ``limits`` (RigUnit_HierarchyAddControlRotator_LimitSettings):  [Read-Write]
- ``proxy`` (RigUnit_HierarchyAddControl_ProxySettings):  [Read-Write]
- ``shape`` (RigUnit_HierarchyAddControl_ShapeSettings):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlRotator_Settings.__init__"></a>

#### __init__

```python
def __init__(
        display_name: Name = "None",
        initial_space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE,
        limits: RigUnit_HierarchyAddControlRotator_LimitSettings = [
            [False, False], [False, False], [False, False],
            [-180.000000, -180.000000, -180.000000],
            [180.000000, 180.000000, 180.000000], True
        ],
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

<a id="unreal.RigUnit_HierarchyAddControlRotator_Settings.initial_space"></a>

#### initial_space

```python
@property
def initial_space() -> RigVMTransformSpace
```

(RigVMTransformSpace):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlRotator_Settings.initial_space"></a>

#### initial_space

```python
@initial_space.setter
def initial_space(value: RigVMTransformSpace) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlRotator_Settings.limits"></a>

#### limits

```python
@property
def limits() -> RigUnit_HierarchyAddControlRotator_LimitSettings
```

(RigUnit_HierarchyAddControlRotator_LimitSettings):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlRotator_Settings.limits"></a>

#### limits

```python
@limits.setter
def limits(value: RigUnit_HierarchyAddControlRotator_LimitSettings) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlRotator_Settings.shape"></a>

#### shape

```python
@property
def shape() -> RigUnit_HierarchyAddControl_ShapeSettings
```

(RigUnit_HierarchyAddControl_ShapeSettings):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlRotator_Settings.shape"></a>

#### shape

```python
@shape.setter
def shape(value: RigUnit_HierarchyAddControl_ShapeSettings) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlRotator_Settings.proxy"></a>

#### proxy

```python
@property
def proxy() -> RigUnit_HierarchyAddControl_ProxySettings
```

(RigUnit_HierarchyAddControl_ProxySettings):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlRotator_Settings.proxy"></a>

#### proxy

```python
@proxy.setter
def proxy(value: RigUnit_HierarchyAddControl_ProxySettings) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlRotator_Settings.filtered_channels"></a>

#### filtered_channels

```python
@property
def filtered_channels() -> Array[RigControlTransformChannel]
```

(Array[RigControlTransformChannel]):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlRotator_Settings.filtered_channels"></a>

#### filtered_channels

```python
@filtered_channels.setter
def filtered_channels(value: Array[RigControlTransformChannel]) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlRotator"></a>