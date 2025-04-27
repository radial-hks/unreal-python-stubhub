## RigVMFunction_DebugTransformArrayMutableNoSpace Objects

```python
class RigVMFunction_DebugTransformArrayMutableNoSpace(
        RigVMFunction_DebugBaseMutable)
```

Given a transform array, will draw a point, axis, or a box in the viewport

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_DebugTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write]
- ``enabled`` (bool):  [Read-Write]
- ``execute_context`` (RigVMExecuteContext):  [Read-Write] * This property is used to chain multiple mutable nodes together
- ``mode`` (RigUnitDebugTransformMode):  [Read-Write]
- ``parent_indices`` (Array[int32]):  [Read-Write]
- ``scale`` (float):  [Read-Write]
- ``thickness`` (float):  [Read-Write]
- ``transforms`` (Array[Transform]):  [Read-Write]
- ``world_offset`` (Transform):  [Read-Write]

<a id="unreal.RigVMFunction_DebugTransformArrayMutableNoSpace.__init__"></a>

#### __init__

```python
def __init__(execute_context: RigVMExecuteContext = [],
             transforms: Array[Transform] = [],
             parent_indices: Array[int] = [],
             mode: RigUnitDebugTransformMode = RigUnitDebugTransformMode.POINT,
             color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
             thickness: float = 0.000000,
             scale: float = 0.000000,
             world_offset: Transform = [[0.000000, 0.000000, 0.000000],
                                        [-0.000000, 0.000000, 0.000000],
                                        [1.000000, 1.000000, 1.000000]],
             enabled: bool = False) -> None
```

<a id="unreal.RigVMFunction_DebugTransformArrayMutableNoSpace.transforms"></a>

#### transforms

```python
@property
def transforms() -> Array[Transform]
```

(Array[Transform]):  [Read-Write]

<a id="unreal.RigVMFunction_DebugTransformArrayMutableNoSpace.transforms"></a>

#### transforms

```python
@transforms.setter
def transforms(value: Array[Transform]) -> None
```

<a id="unreal.RigVMFunction_DebugTransformArrayMutableNoSpace.parent_indices"></a>

#### parent_indices

```python
@property
def parent_indices() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.RigVMFunction_DebugTransformArrayMutableNoSpace.parent_indices"></a>

#### parent_indices

```python
@parent_indices.setter
def parent_indices(value: Array[int]) -> None
```

<a id="unreal.RigVMFunction_DebugTransformArrayMutableNoSpace.mode"></a>

#### mode

```python
@property
def mode() -> RigUnitDebugTransformMode
```

(RigUnitDebugTransformMode):  [Read-Write]

<a id="unreal.RigVMFunction_DebugTransformArrayMutableNoSpace.mode"></a>

#### mode

```python
@mode.setter
def mode(value: RigUnitDebugTransformMode) -> None
```

<a id="unreal.RigVMFunction_DebugTransformArrayMutableNoSpace.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.RigVMFunction_DebugTransformArrayMutableNoSpace.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.RigVMFunction_DebugTransformArrayMutableNoSpace.thickness"></a>

#### thickness

```python
@property
def thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_DebugTransformArrayMutableNoSpace.thickness"></a>

#### thickness

```python
@thickness.setter
def thickness(value: float) -> None
```

<a id="unreal.RigVMFunction_DebugTransformArrayMutableNoSpace.scale"></a>

#### scale

```python
@property
def scale() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_DebugTransformArrayMutableNoSpace.scale"></a>

#### scale

```python
@scale.setter
def scale(value: float) -> None
```

<a id="unreal.RigVMFunction_DebugTransformArrayMutableNoSpace.world_offset"></a>

#### world_offset

```python
@property
def world_offset() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_DebugTransformArrayMutableNoSpace.world_offset"></a>

#### world_offset

```python
@world_offset.setter
def world_offset(value: Transform) -> None
```

<a id="unreal.RigVMFunction_DebugTransformArrayMutableNoSpace.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigVMFunction_DebugTransformArrayMutableNoSpace.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.RigVMFunction_VisualDebugVector"></a>