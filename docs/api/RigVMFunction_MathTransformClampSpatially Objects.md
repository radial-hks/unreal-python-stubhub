## RigVMFunction_MathTransformClampSpatially Objects

```python
class RigVMFunction_MathTransformClampSpatially(RigVMFunction_MathTransformBase
                                                )
```

Clamps a position using a plane collision, cylindric collision or spherical collision.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``axis`` (AxisType):  [Read-Write]
- ``debug_color`` (LinearColor):  [Read-Write]
- ``debug_thickness`` (float):  [Read-Write]
- ``draw_debug`` (bool):  [Read-Write]
- ``maximum`` (float):  [Read-Write] This maximum allowed distance.
  A collision will occur towards the center at this wall.
  Note: For capsule this represents the length.
  Disable by setting to 0.0.
- ``minimum`` (float):  [Read-Write] The minimum allowed distance at which a collision occurs.
  Note: For capsule this represents the radius.
  Disable by setting to 0.0.
- ``result`` (Transform):  [Read-Write]
- ``space`` (Transform):  [Read-Write] The space this spatial clamp happens within.
  The input position will be projected into this space.
- ``type`` (RigVMClampSpatialMode):  [Read-Write]
- ``value`` (Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformClampSpatially.__init__"></a>

#### __init__

```python
def __init__(
    value: Transform = [[0.000000, 0.000000, 0.000000],
                        [-0.000000, 0.000000, 0.000000],
                        [1.000000, 1.000000, 1.000000]],
    axis: AxisType = AxisType.NONE,
    type: RigVMClampSpatialMode = RigVMClampSpatialMode.PLANE,
    minimum: float = 0.000000,
    maximum: float = 0.000000,
    space: Transform = [[0.000000, 0.000000, 0.000000],
                        [-0.000000, 0.000000, 0.000000],
                        [1.000000, 1.000000, 1.000000]],
    draw_debug: bool = False,
    debug_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
    debug_thickness: float = 0.000000,
    result: Transform = [[0.000000, 0.000000, 0.000000],
                         [-0.000000, 0.000000, 0.000000],
                         [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigVMFunction_MathTransformClampSpatially.value"></a>

#### value

```python
@property
def value() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformClampSpatially.value"></a>

#### value

```python
@value.setter
def value(value: Transform) -> None
```

<a id="unreal.RigVMFunction_MathTransformClampSpatially.axis"></a>

#### axis

```python
@property
def axis() -> AxisType
```

(AxisType):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformClampSpatially.axis"></a>

#### axis

```python
@axis.setter
def axis(value: AxisType) -> None
```

<a id="unreal.RigVMFunction_MathTransformClampSpatially.type"></a>

#### type

```python
@property
def type() -> RigVMClampSpatialMode
```

(RigVMClampSpatialMode):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformClampSpatially.type"></a>

#### type

```python
@type.setter
def type(value: RigVMClampSpatialMode) -> None
```

<a id="unreal.RigVMFunction_MathTransformClampSpatially.minimum"></a>

#### minimum

```python
@property
def minimum() -> float
```

(float):  [Read-Write] The minimum allowed distance at which a collision occurs.
Note: For capsule this represents the radius.
Disable by setting to 0.0.

<a id="unreal.RigVMFunction_MathTransformClampSpatially.minimum"></a>

#### minimum

```python
@minimum.setter
def minimum(value: float) -> None
```

<a id="unreal.RigVMFunction_MathTransformClampSpatially.maximum"></a>

#### maximum

```python
@property
def maximum() -> float
```

(float):  [Read-Write] This maximum allowed distance.
A collision will occur towards the center at this wall.
Note: For capsule this represents the length.
Disable by setting to 0.0.

<a id="unreal.RigVMFunction_MathTransformClampSpatially.maximum"></a>

#### maximum

```python
@maximum.setter
def maximum(value: float) -> None
```

<a id="unreal.RigVMFunction_MathTransformClampSpatially.space"></a>

#### space

```python
@property
def space() -> Transform
```

(Transform):  [Read-Write] The space this spatial clamp happens within.
The input position will be projected into this space.

<a id="unreal.RigVMFunction_MathTransformClampSpatially.space"></a>

#### space

```python
@space.setter
def space(value: Transform) -> None
```

<a id="unreal.RigVMFunction_MathTransformClampSpatially.draw_debug"></a>

#### draw_debug

```python
@property
def draw_debug() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformClampSpatially.draw_debug"></a>

#### draw_debug

```python
@draw_debug.setter
def draw_debug(value: bool) -> None
```

<a id="unreal.RigVMFunction_MathTransformClampSpatially.debug_color"></a>

#### debug_color

```python
@property
def debug_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformClampSpatially.debug_color"></a>

#### debug_color

```python
@debug_color.setter
def debug_color(value: LinearColor) -> None
```

<a id="unreal.RigVMFunction_MathTransformClampSpatially.debug_thickness"></a>

#### debug_thickness

```python
@property
def debug_thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformClampSpatially.debug_thickness"></a>

#### debug_thickness

```python
@debug_thickness.setter
def debug_thickness(value: float) -> None
```

<a id="unreal.RigVMFunction_MathTransformClampSpatially.result"></a>

#### result

```python
@property
def result() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigUnit_MathTransformClampSpatially"></a>