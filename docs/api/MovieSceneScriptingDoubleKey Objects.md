## MovieSceneScriptingDoubleKey Objects

```python
class MovieSceneScriptingDoubleKey(MovieSceneScriptingKey)
```

Exposes a Sequencer double type key to Python/Blueprints.
Stores a reference to the data so changes to this class are forwarded onto the underlying data structures.

**C++ Source:**

- **Plugin**: SequencerScripting
- **Module**: SequencerScripting
- **File**: MovieSceneScriptingDouble.h

<a id="unreal.MovieSceneScriptingDoubleKey.set_value"></a>

#### set_value

```python
def set_value(new_value: float) -> None
```

x.set_value(new_value) -> None
Sets the value for this key, reflecting it in the owning channel.

Args:
    new_value (double): The new double value for this key.

<a id="unreal.MovieSceneScriptingDoubleKey.set_time"></a>

#### set_time

```python
def set_time(
        new_frame_number: FrameNumber,
        sub_frame: float = 0.000000,
        time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> None
```

x.set_time(new_frame_number, sub_frame=0.000000, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> None
Sets the time for this key in the owning channel. Will replace any key that already exists at that frame number in this channel.

Args:
    new_frame_number (FrameNumber): What frame should this key be moved to? This should be in the time unit specified by TimeUnit.
    sub_frame (float): If using Display Rate time, what is the sub-frame this should go to? Clamped [0-1), and ignored with when TimeUnit is set to Tick Resolution.
    time_unit (MovieSceneTimeUnit): Should the NewFrameNumber be interpreted as Display Rate frames or in Tick Resolution?

<a id="unreal.MovieSceneScriptingDoubleKey.set_tangent_weight_mode"></a>

#### set_tangent_weight_mode

```python
def set_tangent_weight_mode(new_value: RichCurveTangentWeightMode) -> None
```

x.set_tangent_weight_mode(new_value) -> None
If Interpolation Mode is RCIM_Cubic, the tangent weight mode at this key.

Args:
    new_value (RichCurveTangentWeightMode): Specifies which tangent weights should be respected when evaluating the key.

<a id="unreal.MovieSceneScriptingDoubleKey.set_tangent_mode"></a>

#### set_tangent_mode

```python
def set_tangent_mode(new_value: RichCurveTangentMode) -> None
```

x.set_tangent_mode(new_value) -> None
Sets the tangent mode for this key, reflecting it in the owning channel.

Args:
    new_value (RichCurveTangentMode): Tangent mode that this key should use to specify which tangent values are respected when evaluating. See ERichCurveTangentMode for more details.

<a id="unreal.MovieSceneScriptingDoubleKey.set_leave_tangent_weight"></a>

#### set_leave_tangent_weight

```python
def set_leave_tangent_weight(new_value: float) -> None
```

x.set_leave_tangent_weight(new_value) -> None
If Tangent Weight Mode is RCTWM_WeightedLeave or RCTWM_WeightedBoth, the weight of the leaving tangent on the right side.

Args:
    new_value (float): Specifies the new leaving tangent weight. Represents the length of the hypotenuse in the form of "sqrt(x*x+y*y)" using the same definitions for x and y as tangents.

<a id="unreal.MovieSceneScriptingDoubleKey.set_leave_tangent"></a>

#### set_leave_tangent

```python
def set_leave_tangent(new_value: float) -> None
```

x.set_leave_tangent(new_value) -> None
If Interpolation Mode is RCIM_Cubic, the leaving tangent at this key.

Args:
    new_value (float): Represents the geometric tangents in the form of "tan(y/x)" where y is the key's value and x is the seconds (both relative to key)

<a id="unreal.MovieSceneScriptingDoubleKey.set_interpolation_mode"></a>

#### set_interpolation_mode

```python
def set_interpolation_mode(new_value: RichCurveInterpMode) -> None
```

x.set_interpolation_mode(new_value) -> None
Sets the interpolation mode for this key, reflecting it in the owning channel.

Args:
    new_value (RichCurveInterpMode): Interpolation mode this key should use to interpolate between this key and the next.

<a id="unreal.MovieSceneScriptingDoubleKey.set_arrive_tangent_weight"></a>

#### set_arrive_tangent_weight

```python
def set_arrive_tangent_weight(new_value: float) -> None
```

x.set_arrive_tangent_weight(new_value) -> None
If Tangent Weight Mode is RCTWM_WeightedArrive or RCTWM_WeightedBoth, the weight of the arriving tangent on the left side.

Args:
    new_value (float): Specifies the new arriving tangent weight. Represents the length of the hypotenuse in the form of "sqrt(x*x+y*y)" using the same definitions for x and y as tangents.

<a id="unreal.MovieSceneScriptingDoubleKey.set_arrive_tangent"></a>

#### set_arrive_tangent

```python
def set_arrive_tangent(new_value: float) -> None
```

x.set_arrive_tangent(new_value) -> None
If Interpolation Mode is RCIM_Cubic, the arriving tangent at this key.

Args:
    new_value (float): Represents the geometric tangents in the form of "tan(y/x)" where y is the key's value and x is the seconds (both relative to key)

<a id="unreal.MovieSceneScriptingDoubleKey.get_value"></a>

#### get_value

```python
def get_value() -> float
```

x.get_value() -> double
Gets the value for this key from the owning channel.

Returns:
    double: The double value this key represents.

<a id="unreal.MovieSceneScriptingDoubleKey.get_time"></a>

#### get_time

```python
def get_time(
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> FrameTime
```

x.get_time(time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> FrameTime
Gets the time for this key from the owning channel.

Args:
    time_unit (MovieSceneTimeUnit): Should the time be returned in Display Rate frames (possibly with a sub-frame value) or in Tick Resolution with no sub-frame values?

Returns:
    FrameTime: The time of this key which combines both the frame number and the sub-frame it is on. Sub-frame will be zero if you request Tick Resolution.

<a id="unreal.MovieSceneScriptingDoubleKey.get_tangent_weight_mode"></a>

#### get_tangent_weight_mode

```python
def get_tangent_weight_mode() -> RichCurveTangentWeightMode
```

x.get_tangent_weight_mode() -> RichCurveTangentWeightMode
If Interpolation Mode is RCIM_Cubic, the tangent weight mode at this key

Returns:
    RichCurveTangentWeightMode: Tangent Weight Mode. See ERichCurveTangentWeightMode for more detail on what each mode does.

<a id="unreal.MovieSceneScriptingDoubleKey.get_tangent_mode"></a>

#### get_tangent_mode

```python
def get_tangent_mode() -> RichCurveTangentMode
```

x.get_tangent_mode() -> RichCurveTangentMode
Gets the tangent mode for this key from the owning channel.

Returns:
    RichCurveTangentMode: Tangent mode that this key is using specifying which tangent values are respected when evaluating.

<a id="unreal.MovieSceneScriptingDoubleKey.get_leave_tangent_weight"></a>

#### get_leave_tangent_weight

```python
def get_leave_tangent_weight() -> float
```

x.get_leave_tangent_weight() -> float
If Tangent Weight Mode is RCTWM_WeightedLeave or RCTWM_WeightedBoth, the weight of the leaving tangent on the right side.

Returns:
    float: Tangent Weight. Represents the length of the hypotenuse in the form of "sqrt(x*x+y*y)" using the same definitions for x and y as tangents.

<a id="unreal.MovieSceneScriptingDoubleKey.get_leave_tangent"></a>

#### get_leave_tangent

```python
def get_leave_tangent() -> float
```

x.get_leave_tangent() -> float
If Interpolation Mode is RCIM_Cubic, the leaving tangent at this key

Returns:
    float: Leaving Tangent value. Represents the geometric tangents in the form of "tan(y/x)" where y is the key's value and x is the seconds (both relative to key)

<a id="unreal.MovieSceneScriptingDoubleKey.get_interpolation_mode"></a>

#### get_interpolation_mode

```python
def get_interpolation_mode() -> RichCurveInterpMode
```

x.get_interpolation_mode() -> RichCurveInterpMode
Gets the interpolation mode for this key from the owning channel.

Returns:
    RichCurveInterpMode: Interpolation mode this key uses to interpolate between this key and the next.

<a id="unreal.MovieSceneScriptingDoubleKey.get_arrive_tangent_weight"></a>

#### get_arrive_tangent_weight

```python
def get_arrive_tangent_weight() -> float
```

x.get_arrive_tangent_weight() -> float
If Tangent Weight Mode is RCTWM_WeightedArrive or RCTWM_WeightedBoth, the weight of the arriving tangent on the left side.

Returns:
    float: Tangent Weight. Represents the length of the hypotenuse in the form of "sqrt(x*x+y*y)" using the same definitions for x and y as tangents.

<a id="unreal.MovieSceneScriptingDoubleKey.get_arrive_tangent"></a>

#### get_arrive_tangent

```python
def get_arrive_tangent() -> float
```

x.get_arrive_tangent() -> float
If Interpolation Mode is RCIM_Cubic, the arriving tangent at this key

Returns:
    float: Arrival Tangent value. Represents the geometric tangents in the form of "tan(y/x)" where y is the key's value and x is the seconds (both relative to key)

<a id="unreal.MovieSceneScriptingDoubleChannel"></a>