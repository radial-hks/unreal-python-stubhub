## InterpCurveTwoVectors Objects

```python
class InterpCurveTwoVectors(StructBase)
```

Describes an entire curve that is used to compute two 3D vector values from a float input.
note: This is a mirror of TInterpCurve<FTwoVectors>, defined in InterpCurve.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_looped`` (bool):  [Read-Write] Specify whether the curve is looped or not
- ``loop_key_offset`` (float):  [Read-Write] Specify the offset from the last point's input key corresponding to the loop point
- ``points`` (Array[InterpCurvePointTwoVectors]):  [Read-Write] Holds the collection of interpolation points.

<a id="unreal.InterpCurveTwoVectors.__init__"></a>

#### __init__

```python
def __init__(points: Array[InterpCurvePointTwoVectors] = [],
             is_looped: bool = False,
             loop_key_offset: float = 0.000000) -> None
```

<a id="unreal.InterpCurveTwoVectors.points"></a>

#### points

```python
@property
def points() -> Array[InterpCurvePointTwoVectors]
```

(Array[InterpCurvePointTwoVectors]):  [Read-Write] Holds the collection of interpolation points.

<a id="unreal.InterpCurveTwoVectors.points"></a>

#### points

```python
@points.setter
def points(value: Array[InterpCurvePointTwoVectors]) -> None
```

<a id="unreal.InterpCurveTwoVectors.is_looped"></a>

#### is_looped

```python
@property
def is_looped() -> bool
```

(bool):  [Read-Write] Specify whether the curve is looped or not

<a id="unreal.InterpCurveTwoVectors.is_looped"></a>

#### is_looped

```python
@is_looped.setter
def is_looped(value: bool) -> None
```

<a id="unreal.InterpCurveTwoVectors.loop_key_offset"></a>

#### loop_key_offset

```python
@property
def loop_key_offset() -> float
```

(float):  [Read-Write] Specify the offset from the last point's input key corresponding to the loop point

<a id="unreal.InterpCurveTwoVectors.loop_key_offset"></a>

#### loop_key_offset

```python
@loop_key_offset.setter
def loop_key_offset(value: float) -> None
```

<a id="unreal.InterpCurveVector"></a>