## RigUnit_DebugTransformMutableItemSpace Objects

```python
class RigUnit_DebugTransformMutableItemSpace(RigUnit_DebugBaseMutable)
```

Given a transform, will draw a point, axis, or a box in the viewport

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DebugTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write]
- ``enabled`` (bool):  [Read-Write]
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``mode`` (RigUnitDebugTransformMode):  [Read-Write]
- ``scale`` (float):  [Read-Write]
- ``space`` (RigElementKey):  [Read-Write]
- ``thickness`` (float):  [Read-Write]
- ``transform`` (Transform):  [Read-Write]
- ``world_offset`` (Transform):  [Read-Write]

<a id="unreal.RigUnit_DebugTransformMutableItemSpace.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             transform: Transform = [[0.000000, 0.000000, 0.000000],
                                     [-0.000000, 0.000000, 0.000000],
                                     [1.000000, 1.000000, 1.000000]],
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

<a id="unreal.RigUnit_DebugTransformMutableItemSpace.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigUnit_DebugTransformMutableItemSpace.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.RigUnit_DebugTransformMutableItemSpace.mode"></a>

#### mode

```python
@property
def mode() -> RigUnitDebugTransformMode
```

(RigUnitDebugTransformMode):  [Read-Write]

<a id="unreal.RigUnit_DebugTransformMutableItemSpace.mode"></a>

#### mode

```python
@mode.setter
def mode(value: RigUnitDebugTransformMode) -> None
```

<a id="unreal.RigUnit_DebugTransformMutableItemSpace.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.RigUnit_DebugTransformMutableItemSpace.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.RigUnit_DebugTransformMutableItemSpace.thickness"></a>

#### thickness

```python
@property
def thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_DebugTransformMutableItemSpace.thickness"></a>

#### thickness

```python
@thickness.setter
def thickness(value: float) -> None
```

<a id="unreal.RigUnit_DebugTransformMutableItemSpace.scale"></a>

#### scale

```python
@property
def scale() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_DebugTransformMutableItemSpace.scale"></a>

#### scale

```python
@scale.setter
def scale(value: float) -> None
```

<a id="unreal.RigUnit_DebugTransformMutableItemSpace.space"></a>

#### space

```python
@property
def space() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_DebugTransformMutableItemSpace.space"></a>

#### space

```python
@space.setter
def space(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_DebugTransformMutableItemSpace.world_offset"></a>

#### world_offset

```python
@property
def world_offset() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigUnit_DebugTransformMutableItemSpace.world_offset"></a>

#### world_offset

```python
@world_offset.setter
def world_offset(value: Transform) -> None
```

<a id="unreal.RigUnit_DebugTransformMutableItemSpace.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_DebugTransformMutableItemSpace.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.RigUnit_DebugTransformArrayMutable"></a>