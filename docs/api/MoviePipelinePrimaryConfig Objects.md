## MoviePipelinePrimaryConfig Objects

```python
class MoviePipelinePrimaryConfig(MoviePipelineConfigBase)
```

This class describes the main configuration for a Movie Render Pipeline.
Only settings that apply to the entire output should be stored here,
anything that is changed on a per-shot basis should be stored inside of
UMovieRenderShotConfig instead.

THIS CLASS SHOULD BE IMMUTABLE ONCE PASSED TO THE PIPELINE FOR PROCESSING.
(Otherwise you will be modifying the instance that exists in the UI)

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MoviePipelinePrimaryConfig.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``settings`` (Array[MoviePipelineSetting]):  [Read-Only] Array of settings classes that affect various parts of the output pipeline.

<a id="unreal.MoviePipelinePrimaryConfig.initialize_transient_settings"></a>

#### initialize_transient_settings

```python
def initialize_transient_settings() -> None
```

x.initialize_transient_settings() -> None
Initializes a single instance of every setting so that even non-user-configured settings have a chance to apply their default values. Does nothing if they're already instanced for this configuration.

<a id="unreal.MoviePipelinePrimaryConfig.get_transient_settings"></a>

#### get_transient_settings

```python
def get_transient_settings() -> Array[MoviePipelineSetting]
```

x.get_transient_settings() -> Array[MoviePipelineSetting]
Get Transient Settings

Returns:
    Array[MoviePipelineSetting]:

<a id="unreal.MoviePipelinePrimaryConfig.get_effective_frame_rate"></a>

#### get_effective_frame_rate

```python
def get_effective_frame_rate(sequence: LevelSequence) -> FrameRate
```

x.get_effective_frame_rate(sequence) -> FrameRate
Returns the frame rate override from the Primary Configuration (if any) or the Sequence frame rate if no override is specified.
This should be treated as the actual output framerate of the overall Pipeline.

Args:
    sequence (LevelSequence): 

Returns:
    FrameRate:

<a id="unreal.MoviePipelinePrimaryConfig.get_all_settings"></a>

#### get_all_settings

```python
def get_all_settings(
        include_disabled_settings: bool = False,
        include_transient_settings: bool = False
) -> Array[MoviePipelineSetting]
```

x.get_all_settings(include_disabled_settings=False, include_transient_settings=False) -> Array[MoviePipelineSetting]
Get All Settings

Args:
    include_disabled_settings (bool): 
    include_transient_settings (bool): 

Returns:
    Array[MoviePipelineSetting]:

<a id="unreal.MoviePipelineMasterConfig"></a>