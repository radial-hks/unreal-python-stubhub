## RigUnit_DebugArcItemSpace Objects

```python
class RigUnit_DebugArcItemSpace(RigUnit_DebugBaseMutable)
```

Draws an arc in the viewport, can take in different min and max degrees

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DebugPrimitives.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write]
- ``detail`` (int32):  [Read-Write]
- ``enabled`` (bool):  [Read-Write]
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``maximum_degrees`` (float):  [Read-Write]
- ``minimum_degrees`` (float):  [Read-Write]
- ``radius`` (float):  [Read-Write]
- ``space`` (RigElementKey):  [Read-Write]
- ``thickness`` (float):  [Read-Write]
- ``transform`` (Transform):  [Read-Write]
- ``world_offset`` (Transform):  [Read-Write]

<a id="unreal.RigUnit_DebugArcItemSpace.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             transform: Transform = [[0.000000, 0.000000, 0.000000],
                                     [-0.000000, 0.000000, 0.000000],
                                     [1.000000, 1.000000, 1.000000]],
             color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
             radius: float = 0.000000,
             minimum_degrees: float = 0.000000,
             maximum_degrees: float = 0.000000,
             thickness: float = 0.000000,
             detail: int = 0,
             space: RigElementKey = [RigElementType.NONE, "None"],
             world_offset: Transform = [[0.000000, 0.000000, 0.000000],
                                        [-0.000000, 0.000000, 0.000000],
                                        [1.000000, 1.000000, 1.000000]],
             enabled: bool = False) -> None
```

<a id="unreal.RigUnit_DebugArcItemSpace.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigUnit_DebugArcItemSpace.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.RigUnit_DebugArcItemSpace.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.RigUnit_DebugArcItemSpace.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.RigUnit_DebugArcItemSpace.radius"></a>

#### radius

```python
@property
def radius() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_DebugArcItemSpace.radius"></a>

#### radius

```python
@radius.setter
def radius(value: float) -> None
```

<a id="unreal.RigUnit_DebugArcItemSpace.minimum_degrees"></a>

#### minimum_degrees

```python
@property
def minimum_degrees() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_DebugArcItemSpace.minimum_degrees"></a>

#### minimum_degrees

```python
@minimum_degrees.setter
def minimum_degrees(value: float) -> None
```

<a id="unreal.RigUnit_DebugArcItemSpace.maximum_degrees"></a>

#### maximum_degrees

```python
@property
def maximum_degrees() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_DebugArcItemSpace.maximum_degrees"></a>

#### maximum_degrees

```python
@maximum_degrees.setter
def maximum_degrees(value: float) -> None
```

<a id="unreal.RigUnit_DebugArcItemSpace.thickness"></a>

#### thickness

```python
@property
def thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_DebugArcItemSpace.thickness"></a>

#### thickness

```python
@thickness.setter
def thickness(value: float) -> None
```

<a id="unreal.RigUnit_DebugArcItemSpace.detail"></a>

#### detail

```python
@property
def detail() -> int
```

(int32):  [Read-Write]

<a id="unreal.RigUnit_DebugArcItemSpace.detail"></a>

#### detail

```python
@detail.setter
def detail(value: int) -> None
```

<a id="unreal.RigUnit_DebugArcItemSpace.space"></a>

#### space

```python
@property
def space() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_DebugArcItemSpace.space"></a>

#### space

```python
@space.setter
def space(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_DebugArcItemSpace.world_offset"></a>

#### world_offset

```python
@property
def world_offset() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigUnit_DebugArcItemSpace.world_offset"></a>

#### world_offset

```python
@world_offset.setter
def world_offset(value: Transform) -> None
```

<a id="unreal.RigUnit_DebugArcItemSpace.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_DebugArcItemSpace.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.RigUnit_DebugTransform"></a>