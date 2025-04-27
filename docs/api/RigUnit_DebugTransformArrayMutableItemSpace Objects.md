## RigUnit_DebugTransformArrayMutableItemSpace Objects

```python
class RigUnit_DebugTransformArrayMutableItemSpace(RigUnit_DebugBaseMutable)
```

Given a transform array, will draw a point, axis, or a box in the viewport

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DebugTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write]
- ``enabled`` (bool):  [Read-Write]
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``mode`` (RigUnitDebugTransformMode):  [Read-Write]
- ``parent_indices`` (Array[int32]):  [Read-Write]
- ``scale`` (float):  [Read-Write]
- ``space`` (RigElementKey):  [Read-Write]
- ``thickness`` (float):  [Read-Write]
- ``transforms`` (Array[Transform]):  [Read-Write]
- ``world_offset`` (Transform):  [Read-Write]

<a id="unreal.RigUnit_DebugTransformArrayMutableItemSpace.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             transforms: Array[Transform] = [],
             parent_indices: Array[int] = [],
             mode: RigUnitDebugTransformMode = RigUnitDebugTransformMode.POINT,
             color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
             thickness: float = 0.000000,
             scale: float = 0.000000,
             space: RigElementKey = [RigElementType.NONE, "None"],
             world_offset: Transform = [[0.000000, 0.000000, 0.000000],
                                        [-0.000000, 0.000000, 0.000000],
                                        [1.000000, 1.000000, 1.000000]],
             enabled: bool = False) -> None
```

<a id="unreal.RigUnit_DebugTransformArrayMutableItemSpace.transforms"></a>

#### transforms

```python
@property
def transforms() -> Array[Transform]
```

(Array[Transform]):  [Read-Write]

<a id="unreal.RigUnit_DebugTransformArrayMutableItemSpace.transforms"></a>

#### transforms

```python
@transforms.setter
def transforms(value: Array[Transform]) -> None
```

<a id="unreal.RigUnit_DebugTransformArrayMutableItemSpace.parent_indices"></a>

#### parent_indices

```python
@property
def parent_indices() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.RigUnit_DebugTransformArrayMutableItemSpace.parent_indices"></a>

#### parent_indices

```python
@parent_indices.setter
def parent_indices(value: Array[int]) -> None
```

<a id="unreal.RigUnit_DebugTransformArrayMutableItemSpace.mode"></a>

#### mode

```python
@property
def mode() -> RigUnitDebugTransformMode
```

(RigUnitDebugTransformMode):  [Read-Write]

<a id="unreal.RigUnit_DebugTransformArrayMutableItemSpace.mode"></a>

#### mode

```python
@mode.setter
def mode(value: RigUnitDebugTransformMode) -> None
```

<a id="unreal.RigUnit_DebugTransformArrayMutableItemSpace.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.RigUnit_DebugTransformArrayMutableItemSpace.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.RigUnit_DebugTransformArrayMutableItemSpace.thickness"></a>

#### thickness

```python
@property
def thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_DebugTransformArrayMutableItemSpace.thickness"></a>

#### thickness

```python
@thickness.setter
def thickness(value: float) -> None
```

<a id="unreal.RigUnit_DebugTransformArrayMutableItemSpace.scale"></a>

#### scale

```python
@property
def scale() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_DebugTransformArrayMutableItemSpace.scale"></a>

#### scale

```python
@scale.setter
def scale(value: float) -> None
```

<a id="unreal.RigUnit_DebugTransformArrayMutableItemSpace.space"></a>

#### space

```python
@property
def space() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_DebugTransformArrayMutableItemSpace.space"></a>

#### space

```python
@space.setter
def space(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_DebugTransformArrayMutableItemSpace.world_offset"></a>

#### world_offset

```python
@property
def world_offset() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigUnit_DebugTransformArrayMutableItemSpace.world_offset"></a>

#### world_offset

```python
@world_offset.setter
def world_offset(value: Transform) -> None
```

<a id="unreal.RigUnit_DebugTransformArrayMutableItemSpace.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_DebugTransformArrayMutableItemSpace.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.RigUnit_StartProfilingTimer"></a>