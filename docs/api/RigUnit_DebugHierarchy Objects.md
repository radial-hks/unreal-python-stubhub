## RigUnit_DebugHierarchy Objects

```python
class RigUnit_DebugHierarchy(RigVMFunction_DebugBase)
```

Draws vectors on each bone in the viewport across the entire hierarchy

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DebugHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write]
- ``enabled`` (bool):  [Read-Write]
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write]
- ``items`` (Array[RigElementKey]):  [Read-Write] the items to draw the pose for.
  if this is empty we'll draw the whole hierarchy
- ``scale`` (float):  [Read-Write]
- ``thickness`` (float):  [Read-Write]
- ``world_offset`` (Transform):  [Read-Write]

<a id="unreal.RigUnit_DebugHierarchy.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             items: Array[RigElementKey] = [],
             scale: float = 0.000000,
             color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
             thickness: float = 0.000000,
             world_offset: Transform = [[0.000000, 0.000000, 0.000000],
                                        [-0.000000, 0.000000, 0.000000],
                                        [1.000000, 1.000000, 1.000000]],
             enabled: bool = False) -> None
```

<a id="unreal.RigUnit_DebugHierarchy.execute_context"></a>

#### execute_context

```python
@property
def execute_context() -> ControlRigExecuteContext
```

(ControlRigExecuteContext):  [Read-Write]

<a id="unreal.RigUnit_DebugHierarchy.execute_context"></a>

#### execute_context

```python
@execute_context.setter
def execute_context(value: ControlRigExecuteContext) -> None
```

<a id="unreal.RigUnit_DebugHierarchy.items"></a>

#### items

```python
@property
def items() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Write] the items to draw the pose for.
if this is empty we'll draw the whole hierarchy

<a id="unreal.RigUnit_DebugHierarchy.items"></a>

#### items

```python
@items.setter
def items(value: Array[RigElementKey]) -> None
```

<a id="unreal.RigUnit_DebugHierarchy.scale"></a>

#### scale

```python
@property
def scale() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_DebugHierarchy.scale"></a>

#### scale

```python
@scale.setter
def scale(value: float) -> None
```

<a id="unreal.RigUnit_DebugHierarchy.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.RigUnit_DebugHierarchy.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.RigUnit_DebugHierarchy.thickness"></a>

#### thickness

```python
@property
def thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_DebugHierarchy.thickness"></a>

#### thickness

```python
@thickness.setter
def thickness(value: float) -> None
```

<a id="unreal.RigUnit_DebugHierarchy.world_offset"></a>

#### world_offset

```python
@property
def world_offset() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigUnit_DebugHierarchy.world_offset"></a>

#### world_offset

```python
@world_offset.setter
def world_offset(value: Transform) -> None
```

<a id="unreal.RigUnit_DebugHierarchy.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_DebugHierarchy.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.RigUnit_DebugPose"></a>