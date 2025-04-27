## MovieSceneParameterSection Objects

```python
class MovieSceneParameterSection(MovieSceneSection)
```

A single movie scene section which can contain data for multiple named parameters.

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieSceneParameterSection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color_tint`` (Color):  [Read-Write] The color tint for this section
- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this section evaluates at runtime.
- ``easing`` (MovieSceneEasingSettings):  [Read-Write]
- ``eval_options`` (MovieSceneSectionEvalOptions):  [Read-Write]
- ``is_active`` (bool):  [Read-Write] Toggle whether this section is active/inactive
- ``is_locked`` (bool):  [Read-Write] Toggle whether this section is locked/unlocked
- ``post_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to continue 'postrolling' this section for after evaluation has ended.
- ``pre_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to prepare this section for evaluation before it actually starts.
- ``section_range`` (MovieSceneFrameRange):  [Read-Write] The range in which this section is active
- ``timecode_source`` (MovieSceneTimecodeSource):  [Read-Write] The timecode at which this movie scene section is based (ie. when it was recorded)

<a id="unreal.MovieSceneParameterSection.remove_vector_parameter"></a>

#### remove_vector_parameter

```python
def remove_vector_parameter(parameter_name: Name) -> bool
```

x.remove_vector_parameter(parameter_name) -> bool
Removes a vector parameter from this section.

Args:
    parameter_name (Name): The name of the vector parameter to remove.

Returns:
    bool: True if a parameter with that name was found and removed, otherwise false.

<a id="unreal.MovieSceneParameterSection.remove_vector2d_parameter"></a>

#### remove_vector2d_parameter

```python
def remove_vector2d_parameter(parameter_name: Name) -> bool
```

x.remove_vector2d_parameter(parameter_name) -> bool
Removes a vector2D parameter from this section.

Args:
    parameter_name (Name): The name of the vector2D parameter to remove.

Returns:
    bool: True if a parameter with that name was found and removed, otherwise false.

<a id="unreal.MovieSceneParameterSection.remove_transform_parameter"></a>

#### remove_transform_parameter

```python
def remove_transform_parameter(parameter_name: Name) -> bool
```

x.remove_transform_parameter(parameter_name) -> bool
Removes a transform parameter from this section.

Args:
    parameter_name (Name): The name of the transform parameter to remove.

Returns:
    bool: True if a parameter with that name was found and removed, otherwise false.

<a id="unreal.MovieSceneParameterSection.remove_scalar_parameter"></a>

#### remove_scalar_parameter

```python
def remove_scalar_parameter(parameter_name: Name) -> bool
```

x.remove_scalar_parameter(parameter_name) -> bool
Removes a scalar parameter from this section.

Args:
    parameter_name (Name): The name of the scalar parameter to remove.

Returns:
    bool: True if a parameter with that name was found and removed, otherwise false.

<a id="unreal.MovieSceneParameterSection.remove_color_parameter"></a>

#### remove_color_parameter

```python
def remove_color_parameter(parameter_name: Name) -> bool
```

x.remove_color_parameter(parameter_name) -> bool
Removes a color parameter from this section.

Args:
    parameter_name (Name): The name of the color parameter to remove.

Returns:
    bool: True if a parameter with that name was found and removed, otherwise false.

<a id="unreal.MovieSceneParameterSection.remove_bool_parameter"></a>

#### remove_bool_parameter

```python
def remove_bool_parameter(parameter_name: Name) -> bool
```

x.remove_bool_parameter(parameter_name) -> bool
Removes a bool parameter from this section.

Args:
    parameter_name (Name): The name of the bool parameter to remove.

Returns:
    bool: True if a parameter with that name was found and removed, otherwise false.

<a id="unreal.MovieSceneParameterSection.get_parameter_names"></a>

#### get_parameter_names

```python
def get_parameter_names() -> Set[Name]
```

x.get_parameter_names() -> Set[Name]
Gets the set of all parameter names used by this section.

Returns:
    Set[Name]: 

    parameter_names (Set[Name]):

<a id="unreal.MovieSceneParameterSection.add_vector_parameter_key"></a>

#### add_vector_parameter_key

```python
def add_vector_parameter_key(parameter_name: Name, time: FrameNumber,
                             value: Vector) -> None
```

x.add_vector_parameter_key(parameter_name, time, value) -> None
Adds a a key for a specific vector parameter at the specified time with the specified value.

Args:
    parameter_name (Name): 
    time (FrameNumber): 
    value (Vector):

<a id="unreal.MovieSceneParameterSection.add_vector2d_parameter_key"></a>

#### add_vector2d_parameter_key

```python
def add_vector2d_parameter_key(parameter_name: Name, time: FrameNumber,
                               value: Vector2D) -> None
```

x.add_vector2d_parameter_key(parameter_name, time, value) -> None
Adds a a key for a specific vector2D parameter at the specified time with the specified value.

Args:
    parameter_name (Name): 
    time (FrameNumber): 
    value (Vector2D):

<a id="unreal.MovieSceneParameterSection.add_transform_parameter_key"></a>

#### add_transform_parameter_key

```python
def add_transform_parameter_key(parameter_name: Name, time: FrameNumber,
                                value: Transform) -> None
```

x.add_transform_parameter_key(parameter_name, time, value) -> None
Adds a a key for a specific color parameter at the specified time with the specified value.

Args:
    parameter_name (Name): 
    time (FrameNumber): 
    value (Transform):

<a id="unreal.MovieSceneParameterSection.add_scalar_parameter_key"></a>

#### add_scalar_parameter_key

```python
def add_scalar_parameter_key(parameter_name: Name, time: FrameNumber,
                             value: float) -> None
```

x.add_scalar_parameter_key(parameter_name, time, value) -> None
Adds a a key for a specific scalar parameter at the specified time with the specified value.

Args:
    parameter_name (Name): 
    time (FrameNumber): 
    value (float):

<a id="unreal.MovieSceneParameterSection.add_color_parameter_key"></a>

#### add_color_parameter_key

```python
def add_color_parameter_key(parameter_name: Name, time: FrameNumber,
                            value: LinearColor) -> None
```

x.add_color_parameter_key(parameter_name, time, value) -> None
Adds a a key for a specific color parameter at the specified time with the specified value.

Args:
    parameter_name (Name): 
    time (FrameNumber): 
    value (LinearColor):

<a id="unreal.MovieSceneParameterSection.add_bool_parameter_key"></a>

#### add_bool_parameter_key

```python
def add_bool_parameter_key(parameter_name: Name, time: FrameNumber,
                           value: bool) -> None
```

x.add_bool_parameter_key(parameter_name, time, value) -> None
Adds a a key for a specific bool parameter at the specified time with the specified value.

Args:
    parameter_name (Name): 
    time (FrameNumber): 
    value (bool):

<a id="unreal.MovieSceneMaterialParameterSection"></a>