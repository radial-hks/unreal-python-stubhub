## AnimationCurveIdentifier Objects

```python
class AnimationCurveIdentifier(StructBase)
```

Script-friendly structure for identifying an animation curve.
Wrapping the unique type and smart-name for use within the AnimDataController API.

**C++ Source:**

- **Module**: Engine
- **File**: CurveIdentifier.h

<a id="unreal.AnimationCurveIdentifier.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AnimationCurveIdentifier.set_curve_identifier"></a>

#### set_curve_identifier

```python
def set_curve_identifier(name: Name, curve_type: RawCurveTrackTypes) -> None
```

x.set_curve_identifier(name, curve_type) -> None
Constructs a valid FAnimationCurveIdentifier instance.

Args:
    name (Name): Name of the curve to find or add
    curve_type (RawCurveTrackTypes): Type of the curve to find or add

<a id="unreal.AnimationCurveIdentifier.is_valid"></a>

#### is_valid

```python
def is_valid() -> bool
```

x.is_valid() -> bool


Returns:
    bool: Whether or not the Curve Identifier is valid

<a id="unreal.AnimationCurveIdentifier.get_type"></a>

#### get_type

```python
def get_type() -> RawCurveTrackTypes
```

x.get_type() -> RawCurveTrackTypes


Returns:
    RawCurveTrackTypes: The animation curve type for the curve represented by the Curve Identifier

<a id="unreal.AnimationCurveIdentifier.get_transform_child_curve_identifier"></a>

#### get_transform_child_curve_identifier

```python
def get_transform_child_curve_identifier(channel: TransformCurveChannel,
                                         axis: VectorCurveChannel) -> bool
```

x.get_transform_child_curve_identifier(channel, axis) -> bool
Converts a valid FAnimationCurveIdentifier instance with RCT_Transform curve type to target a child curve.

Args:
    channel (TransformCurveChannel): Channel to target
    axis (VectorCurveChannel): Axis within channel to target

Returns:
    bool: Valid FAnimationCurveIdentifier if the operation was successful

<a id="unreal.AnimationCurveIdentifier.get_name"></a>

#### get_name

```python
def get_name() -> Name
```

x.get_name() -> Name


Returns:
    Name: The name used for displaying the Curve Identifier

<a id="unreal.CurveScaledPayload"></a>