## RigUnit_HierarchyAddControlTransform_Settings Objects

```python
class RigUnit_HierarchyAddControlTransform_Settings(
        RigUnit_HierarchyAddControl_Settings)
```

Rig Unit Hierarchy Add Control Transform Settings

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DynamicHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``display_name`` (Name):  [Read-Write]
- ``filtered_channels`` (Array[RigControlTransformChannel]):  [Read-Write]
- ``initial_space`` (RigVMTransformSpace):  [Read-Write]
- ``limits`` (RigUnit_HierarchyAddControlTransform_LimitSettings):  [Read-Write]
- ``preferred_rotation_order`` (EulerRotationOrder):  [Read-Write]
- ``proxy`` (RigUnit_HierarchyAddControl_ProxySettings):  [Read-Write]
- ``shape`` (RigUnit_HierarchyAddControl_ShapeSettings):  [Read-Write]
- ``use_preferred_rotation_order`` (bool):  [Read-Write] Enables overriding the preferred rotation order

<a id="unreal.RigUnit_HierarchyAddControlTransform_Settings.__init__"></a>

#### __init__

```python
def __init__(
        display_name: Name = "None",
        initial_space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE,
        use_preferred_rotation_order: bool = False,
        preferred_rotation_order: EulerRotationOrder = EulerRotationOrder.XYZ,
        limits: RigUnit_HierarchyAddControlTransform_LimitSettings = [
            [False, False], [False, False], [False, False], [False, False],
            [False, False], [False, False], [False, False], [False, False],
            [False, False],
            [[-100.000000, -100.000000, -100.000000],
             [-180.000000, -180.000000, -180.000000],
             [0.000000, 0.000000, 0.000000]],
            [[100.000000, 100.000000, 100.000000],
             [180.000000, 180.000000, 180.000000],
             [10.000000, 10.000000, 10.000000]], True
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

<a id="unreal.RigUnit_HierarchyAddControlTransform_Settings.initial_space"></a>

#### initial_space

```python
@property
def initial_space() -> RigVMTransformSpace
```

(RigVMTransformSpace):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlTransform_Settings.initial_space"></a>

#### initial_space

```python
@initial_space.setter
def initial_space(value: RigVMTransformSpace) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlTransform_Settings.use_preferred_rotation_order"></a>

#### use_preferred_rotation_order

```python
@property
def use_preferred_rotation_order() -> bool
```

(bool):  [Read-Write] Enables overriding the preferred rotation order

<a id="unreal.RigUnit_HierarchyAddControlTransform_Settings.use_preferred_rotation_order"></a>

#### use_preferred_rotation_order

```python
@use_preferred_rotation_order.setter
def use_preferred_rotation_order(value: bool) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlTransform_Settings.preferred_rotation_order"></a>

#### preferred_rotation_order

```python
@property
def preferred_rotation_order() -> EulerRotationOrder
```

(EulerRotationOrder):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlTransform_Settings.preferred_rotation_order"></a>

#### preferred_rotation_order

```python
@preferred_rotation_order.setter
def preferred_rotation_order(value: EulerRotationOrder) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlTransform_Settings.limits"></a>

#### limits

```python
@property
def limits() -> RigUnit_HierarchyAddControlTransform_LimitSettings
```

(RigUnit_HierarchyAddControlTransform_LimitSettings):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlTransform_Settings.limits"></a>

#### limits

```python
@limits.setter
def limits(value: RigUnit_HierarchyAddControlTransform_LimitSettings) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlTransform_Settings.shape"></a>

#### shape

```python
@property
def shape() -> RigUnit_HierarchyAddControl_ShapeSettings
```

(RigUnit_HierarchyAddControl_ShapeSettings):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlTransform_Settings.shape"></a>

#### shape

```python
@shape.setter
def shape(value: RigUnit_HierarchyAddControl_ShapeSettings) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlTransform_Settings.proxy"></a>

#### proxy

```python
@property
def proxy() -> RigUnit_HierarchyAddControl_ProxySettings
```

(RigUnit_HierarchyAddControl_ProxySettings):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlTransform_Settings.proxy"></a>

#### proxy

```python
@proxy.setter
def proxy(value: RigUnit_HierarchyAddControl_ProxySettings) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlTransform_Settings.filtered_channels"></a>

#### filtered_channels

```python
@property
def filtered_channels() -> Array[RigControlTransformChannel]
```

(Array[RigControlTransformChannel]):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlTransform_Settings.filtered_channels"></a>

#### filtered_channels

```python
@filtered_channels.setter
def filtered_channels(value: Array[RigControlTransformChannel]) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlTransform"></a>