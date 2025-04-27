## RigUnit_ControlRigSplineFromTransforms Objects

```python
class RigUnit_ControlRigSplineFromTransforms(RigUnit_ControlRigSplineBase)
```

* Creates a Spline curve from an array of positions

**C++ Source:**

- **Plugin**: ControlRigSpline
- **Module**: ControlRigSpline
- **File**: ControlRigSplineUnits.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``closed`` (bool):  [Read-Write]
- ``compression`` (float):  [Read-Write]
- ``samples_per_segment`` (int32):  [Read-Write]
- ``spline`` (ControlRigSpline):  [Read-Write]
- ``spline_mode`` (SplineType):  [Read-Write]
- ``stretch`` (float):  [Read-Write]
- ``transforms`` (Array[Transform]):  [Read-Write]

<a id="unreal.RigUnit_ControlRigSplineFromTransforms.__init__"></a>

#### __init__

```python
def __init__(transforms: Array[Transform] = [],
             spline_mode: SplineType = SplineType.B_SPLINE,
             closed: bool = False,
             samples_per_segment: int = 0,
             compression: float = 0.000000,
             stretch: float = 0.000000,
             spline: ControlRigSpline = []) -> None
```

<a id="unreal.RigUnit_ControlRigSplineFromTransforms.transforms"></a>

#### transforms

```python
@property
def transforms() -> Array[Transform]
```

(Array[Transform]):  [Read-Write]

<a id="unreal.RigUnit_ControlRigSplineFromTransforms.transforms"></a>

#### transforms

```python
@transforms.setter
def transforms(value: Array[Transform]) -> None
```

<a id="unreal.RigUnit_ControlRigSplineFromTransforms.spline_mode"></a>

#### spline_mode

```python
@property
def spline_mode() -> SplineType
```

(SplineType):  [Read-Write]

<a id="unreal.RigUnit_ControlRigSplineFromTransforms.spline_mode"></a>

#### spline_mode

```python
@spline_mode.setter
def spline_mode(value: SplineType) -> None
```

<a id="unreal.RigUnit_ControlRigSplineFromTransforms.closed"></a>

#### closed

```python
@property
def closed() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_ControlRigSplineFromTransforms.closed"></a>

#### closed

```python
@closed.setter
def closed(value: bool) -> None
```

<a id="unreal.RigUnit_ControlRigSplineFromTransforms.samples_per_segment"></a>

#### samples_per_segment

```python
@property
def samples_per_segment() -> int
```

(int32):  [Read-Write]

<a id="unreal.RigUnit_ControlRigSplineFromTransforms.samples_per_segment"></a>

#### samples_per_segment

```python
@samples_per_segment.setter
def samples_per_segment(value: int) -> None
```

<a id="unreal.RigUnit_ControlRigSplineFromTransforms.compression"></a>

#### compression

```python
@property
def compression() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_ControlRigSplineFromTransforms.compression"></a>

#### compression

```python
@compression.setter
def compression(value: float) -> None
```

<a id="unreal.RigUnit_ControlRigSplineFromTransforms.stretch"></a>

#### stretch

```python
@property
def stretch() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_ControlRigSplineFromTransforms.stretch"></a>

#### stretch

```python
@stretch.setter
def stretch(value: float) -> None
```

<a id="unreal.RigUnit_ControlRigSplineFromTransforms.spline"></a>

#### spline

```python
@property
def spline() -> ControlRigSpline
```

(ControlRigSpline):  [Read-Only]

<a id="unreal.RigUnit_SetSplinePoints"></a>