## MovieSceneComponentMaterialParameterSection Objects

```python
class MovieSceneComponentMaterialParameterSection(MovieSceneSection)
```

A movie scene section containing data for material parameters.

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieSceneComponentMaterialParameterSection.h

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

<a id="unreal.MovieSceneComponentMaterialParameterSection.remove_scalar_parameter"></a>

#### remove_scalar_parameter

```python
def remove_scalar_parameter(parameter_info: MaterialParameterInfo) -> bool
```

x.remove_scalar_parameter(parameter_info) -> bool
Removes a scalar parameter from this section.

Args:
    parameter_info (MaterialParameterInfo): The material parameter info of the scalar parameter to remove.

Returns:
    bool: True if a parameter with that name was found and removed, otherwise false.

<a id="unreal.MovieSceneComponentMaterialParameterSection.remove_color_parameter"></a>

#### remove_color_parameter

```python
def remove_color_parameter(parameter_info: MaterialParameterInfo) -> bool
```

x.remove_color_parameter(parameter_info) -> bool
Removes a color parameter from this section.

Args:
    parameter_info (MaterialParameterInfo): The material parameter info of the color parameter to remove.

Returns:
    bool: True if a parameter with that name was found and removed, otherwise false.

<a id="unreal.MovieSceneComponentMaterialParameterSection.add_scalar_parameter_key"></a>

#### add_scalar_parameter_key

```python
def add_scalar_parameter_key(parameter_info: MaterialParameterInfo,
                             time: FrameNumber, value: float, layer_name: str,
                             asset_name: str) -> None
```

x.add_scalar_parameter_key(parameter_info, time, value, layer_name, asset_name) -> None
Adds a a key for a specific scalar parameter at the specified time with the specified value.

Args:
    parameter_info (MaterialParameterInfo): 
    time (FrameNumber): 
    value (float): 
    layer_name (str): 
    asset_name (str):

<a id="unreal.MovieSceneComponentMaterialParameterSection.add_color_parameter_key"></a>

#### add_color_parameter_key

```python
def add_color_parameter_key(parameter_info: MaterialParameterInfo,
                            time: FrameNumber,
                            value: LinearColor,
                            layer_name: str,
                            asset_name: str,
                            channel_names: ParameterChannelNames = []) -> None
```

x.add_color_parameter_key(parameter_info, time, value, layer_name, asset_name, channel_names=[]) -> None
Adds a a key for a specific color parameter at the specified time with the specified value.

Args:
    parameter_info (MaterialParameterInfo): 
    time (FrameNumber): 
    value (LinearColor): 
    layer_name (str): 
    asset_name (str): 
    channel_names (ParameterChannelNames):

<a id="unreal.MovieSceneParameterSection"></a>