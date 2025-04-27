## RigUnit_HierarchyAddControl_ProxySettings Objects

```python
class RigUnit_HierarchyAddControl_ProxySettings(StructBase)
```

Rig Unit Hierarchy Add Control Proxy Settings

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DynamicHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``driven_controls`` (Array[RigElementKey]):  [Read-Write]
- ``is_proxy`` (bool):  [Read-Write]
- ``shape_visibility`` (RigControlVisibility):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControl_ProxySettings.__init__"></a>

#### __init__

```python
def __init__(
    is_proxy: bool = False,
    driven_controls: Array[RigElementKey] = [],
    shape_visibility: RigControlVisibility = RigControlVisibility.USER_DEFINED
) -> None
```

<a id="unreal.RigUnit_HierarchyAddControl_ProxySettings.is_proxy"></a>

#### is_proxy

```python
@property
def is_proxy() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControl_ProxySettings.is_proxy"></a>

#### is_proxy

```python
@is_proxy.setter
def is_proxy(value: bool) -> None
```

<a id="unreal.RigUnit_HierarchyAddControl_ProxySettings.driven_controls"></a>

#### driven_controls

```python
@property
def driven_controls() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControl_ProxySettings.driven_controls"></a>

#### driven_controls

```python
@driven_controls.setter
def driven_controls(value: Array[RigElementKey]) -> None
```

<a id="unreal.RigUnit_HierarchyAddControl_ProxySettings.shape_visibility"></a>

#### shape_visibility

```python
@property
def shape_visibility() -> RigControlVisibility
```

(RigControlVisibility):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControl_ProxySettings.shape_visibility"></a>

#### shape_visibility

```python
@shape_visibility.setter
def shape_visibility(value: RigControlVisibility) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlFloat_LimitSettings"></a>