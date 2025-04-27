## ProceduralDaySequenceBuilder Objects

```python
class ProceduralDaySequenceBuilder(Object)
```

A utility class for creating procedural Day Sequences.
Before adding any keys, SetActiveBoundObject should be called and provided a Day Sequence Actor or a component owned by a Day Sequence Actor.
All time values are currently normalized to the range [0, 1], inclusive on both ends. A time of 1 is handled as a special case and maps to the final frame.
This class assumes the target Day Sequence Actor will stay alive and that users will keep the generated sequence alive, it manages no lifetimes.

Consider using FProceduralDaySequence instead of using this class directly.

**C++ Source:**

- **Plugin**: DaySequence
- **Module**: DaySequence
- **File**: ProceduralDaySequenceBuilder.h

<a id="unreal.ProceduralDaySequenceBuilder.set_active_bound_object"></a>

#### set_active_bound_object

```python
def set_active_bound_object(object: Object) -> None
```

x.set_active_bound_object(object) -> None
Prepare the builder to begin adding keys animating properties on InObject.

Args:
    object (Object):

<a id="unreal.ProceduralDaySequenceBuilder.is_initialized"></a>

#### is_initialized

```python
def is_initialized() -> bool
```

x.is_initialized() -> bool
Returns true Initialize has been called with a valid actor.

Returns:
    bool:

<a id="unreal.ProceduralDaySequenceBuilder.initialize"></a>

#### initialize

```python
def initialize(actor: DaySequenceActor,
               initial_sequence: DaySequence = None,
               clear_initial_sequence: bool = True) -> DaySequence
```

x.initialize(actor, initial_sequence=None, clear_initial_sequence=True) -> DaySequence
Initialize the procedural sequence and set the TargetActor for this builder.

Args:
    actor (DaySequenceActor): The target DaySequenceActor that will be animated by the generated sequence.
    initial_sequence (DaySequence): Optional sequence that this builder can operate on instead of allocating a new sequence.
    clear_initial_sequence (bool): If true, calls ClearKeys().

Returns:
    DaySequence: The sequence which will be modified when calling SetActiveBoundObject and the Add*Key(s) functions.

<a id="unreal.ProceduralDaySequenceBuilder.clear_keys"></a>

#### clear_keys

```python
def clear_keys() -> None
```

x.clear_keys() -> None
Key Deletion:

<a id="unreal.ProceduralDaySequenceBuilder.add_visibility_override"></a>

#### add_visibility_override

```python
def add_visibility_override(value: bool) -> None
```

x.add_visibility_override(value) -> None
Add Visibility Override

Args:
    value (bool):

<a id="unreal.ProceduralDaySequenceBuilder.add_vector_override"></a>

#### add_vector_override

```python
def add_vector_override(property_name: Name, value: Vector) -> None
```

x.add_vector_override(property_name, value) -> None
Add Vector Override

Args:
    property_name (Name): 
    value (Vector):

<a id="unreal.ProceduralDaySequenceBuilder.add_vector_key"></a>

#### add_vector_key

```python
def add_vector_key(
        property_name: Name,
        key: float,
        value: Vector,
        interp_mode: RichCurveInterpMode = RichCurveInterpMode.RCIM_CUBIC
) -> None
```

x.add_vector_key(property_name, key, value, interp_mode=RichCurveInterpMode.RCIM_CUBIC) -> None
Add Vector Key

Args:
    property_name (Name): 
    key (float): 
    value (Vector): 
    interp_mode (RichCurveInterpMode):

<a id="unreal.ProceduralDaySequenceBuilder.add_translation_key"></a>

#### add_translation_key

```python
def add_translation_key(
        key: float,
        value: Vector,
        interp_mode: RichCurveInterpMode = RichCurveInterpMode.RCIM_CUBIC
) -> None
```

x.add_translation_key(key, value, interp_mode=RichCurveInterpMode.RCIM_CUBIC) -> None
Add Translation Key

Args:
    key (float): 
    value (Vector): 
    interp_mode (RichCurveInterpMode):

<a id="unreal.ProceduralDaySequenceBuilder.add_transform_override"></a>

#### add_transform_override

```python
def add_transform_override(value: Transform) -> None
```

x.add_transform_override(value) -> None
Add Transform Override

Args:
    value (Transform):

<a id="unreal.ProceduralDaySequenceBuilder.add_scale_key"></a>

#### add_scale_key

```python
def add_scale_key(
        key: float,
        value: Vector,
        interp_mode: RichCurveInterpMode = RichCurveInterpMode.RCIM_CUBIC
) -> None
```

x.add_scale_key(key, value, interp_mode=RichCurveInterpMode.RCIM_CUBIC) -> None
Add Scale Key

Args:
    key (float): 
    value (Vector): 
    interp_mode (RichCurveInterpMode):

<a id="unreal.ProceduralDaySequenceBuilder.add_scalar_override"></a>

#### add_scalar_override

```python
def add_scalar_override(property_name: Name, value: float) -> None
```

x.add_scalar_override(property_name, value) -> None
Add Scalar Override

Args:
    property_name (Name): 
    value (double):

<a id="unreal.ProceduralDaySequenceBuilder.add_scalar_material_parameter_override"></a>

#### add_scalar_material_parameter_override

```python
def add_scalar_material_parameter_override(parameter_name: Name,
                                           material_index: int,
                                           value: float) -> None
```

x.add_scalar_material_parameter_override(parameter_name, material_index, value) -> None
Add Scalar Material Parameter Override

Args:
    parameter_name (Name): 
    material_index (int32): 
    value (float):

<a id="unreal.ProceduralDaySequenceBuilder.add_scalar_key"></a>

#### add_scalar_key

```python
def add_scalar_key(
        property_name: Name,
        key: float,
        value: float,
        interp_mode: RichCurveInterpMode = RichCurveInterpMode.RCIM_CUBIC
) -> None
```

x.add_scalar_key(property_name, key, value, interp_mode=RichCurveInterpMode.RCIM_CUBIC) -> None
Add Scalar Key

Args:
    property_name (Name): 
    key (float): 
    value (double): 
    interp_mode (RichCurveInterpMode):

<a id="unreal.ProceduralDaySequenceBuilder.add_rotation_key"></a>

#### add_rotation_key

```python
def add_rotation_key(
        key: float,
        value: Rotator,
        interp_mode: RichCurveInterpMode = RichCurveInterpMode.RCIM_CUBIC
) -> None
```

x.add_rotation_key(key, value, interp_mode=RichCurveInterpMode.RCIM_CUBIC) -> None
Add Rotation Key

Args:
    key (float): 
    value (Rotator): 
    interp_mode (RichCurveInterpMode):

<a id="unreal.ProceduralDaySequenceBuilder.add_material_override"></a>

#### add_material_override

```python
def add_material_override(material_index: int,
                          value: MaterialInterface) -> None
```

x.add_material_override(material_index, value) -> None
Add Material Override

Args:
    material_index (int32): 
    value (MaterialInterface):

<a id="unreal.ProceduralDaySequenceBuilder.add_color_override"></a>

#### add_color_override

```python
def add_color_override(property_name: Name, value: LinearColor) -> None
```

x.add_color_override(property_name, value) -> None
Add Color Override

Args:
    property_name (Name): 
    value (LinearColor):

<a id="unreal.ProceduralDaySequenceBuilder.add_color_material_parameter_override"></a>

#### add_color_material_parameter_override

```python
def add_color_material_parameter_override(parameter_name: Name,
                                          material_index: int,
                                          value: LinearColor) -> None
```

x.add_color_material_parameter_override(parameter_name, material_index, value) -> None
Add Color Material Parameter Override

Args:
    parameter_name (Name): 
    material_index (int32): 
    value (LinearColor):

<a id="unreal.ProceduralDaySequenceBuilder.add_bool_override"></a>

#### add_bool_override

```python
def add_bool_override(property_name: Name, value: bool) -> None
```

x.add_bool_override(property_name, value) -> None
Key Creation:

Args:
    property_name (Name): 
    value (bool):

<a id="unreal.ProceduralDaySequenceBuilder.add_bool_key"></a>

#### add_bool_key

```python
def add_bool_key(property_name: Name, key: float, value: bool) -> None
```

x.add_bool_key(property_name, key, value) -> None
Add Bool Key

Args:
    property_name (Name): 
    key (float): 
    value (bool):

<a id="unreal.SunMoonDaySequenceActor"></a>