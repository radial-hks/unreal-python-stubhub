## MovieSceneDataLayerSection Objects

```python
class MovieSceneDataLayerSection(MovieSceneSection)
```

Movie Scene Data Layer Section

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieSceneDataLayerSection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color_tint`` (Color):  [Read-Write] The color tint for this section
- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this section evaluates at runtime.
- ``data_layer_assets`` (Array[DataLayerAsset]):  [Read-Write] A list of data layers that should be loaded or unloaded by this section
- ``desired_state`` (DataLayerRuntimeState):  [Read-Write] The desired state for the data layers on this section when the section is actively evaluating.
- ``easing`` (MovieSceneEasingSettings):  [Read-Write]
- ``eval_options`` (MovieSceneSectionEvalOptions):  [Read-Write]
- ``flush_on_activated`` (bool):  [Read-Write] Determine if we need to flush level streaming when the data layers are activated. May result in a hitch.
- ``flush_on_unload`` (bool):  [Read-Write] Determine if we need to flush level streaming when the data layers unloads.
- ``is_active`` (bool):  [Read-Write] Toggle whether this section is active/inactive
- ``is_locked`` (bool):  [Read-Write] Toggle whether this section is locked/unlocked
- ``post_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to continue 'postrolling' this section for after evaluation has ended.
- ``pre_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to prepare this section for evaluation before it actually starts.
- ``preroll_state`` (DataLayerRuntimeState):  [Read-Write] The desired state for the data layers on this section when the section is pre or post-rolling.
- ``section_range`` (MovieSceneFrameRange):  [Read-Write] The range in which this section is active
- ``timecode_source`` (MovieSceneTimecodeSource):  [Read-Write] The timecode at which this movie scene section is based (ie. when it was recorded)

<a id="unreal.MovieSceneDataLayerSection.set_preroll_state"></a>

#### set_preroll_state

```python
def set_preroll_state(preroll_state: DataLayerRuntimeState) -> None
```

x.set_preroll_state(preroll_state) -> None
Set Preroll State

Args:
    preroll_state (DataLayerRuntimeState):

<a id="unreal.MovieSceneDataLayerSection.set_flush_on_unload"></a>

#### set_flush_on_unload

```python
def set_flush_on_unload(flush_on_unload: bool) -> None
```

x.set_flush_on_unload(flush_on_unload) -> None
Set Flush on Unload

Args:
    flush_on_unload (bool):

<a id="unreal.MovieSceneDataLayerSection.set_flush_on_activated"></a>

#### set_flush_on_activated

```python
def set_flush_on_activated(flush_on_activated: bool) -> None
```

x.set_flush_on_activated(flush_on_activated) -> None
Set Flush on Activated

Args:
    flush_on_activated (bool):

<a id="unreal.MovieSceneDataLayerSection.set_desired_state"></a>

#### set_desired_state

```python
def set_desired_state(desired_state: DataLayerRuntimeState) -> None
```

x.set_desired_state(desired_state) -> None
Set Desired State

Args:
    desired_state (DataLayerRuntimeState):

<a id="unreal.MovieSceneDataLayerSection.set_data_layer_assets"></a>

#### set_data_layer_assets

```python
def set_data_layer_assets(data_layer_assets: Array[DataLayerAsset]) -> None
```

x.set_data_layer_assets(data_layer_assets) -> None
Set Data Layer Assets

Args:
    data_layer_assets (Array[DataLayerAsset]):

<a id="unreal.MovieSceneDataLayerSection.get_preroll_state"></a>

#### get_preroll_state

```python
def get_preroll_state() -> DataLayerRuntimeState
```

x.get_preroll_state() -> DataLayerRuntimeState
Get Preroll State

Returns:
    DataLayerRuntimeState:

<a id="unreal.MovieSceneDataLayerSection.get_flush_on_unload"></a>

#### get_flush_on_unload

```python
def get_flush_on_unload() -> bool
```

x.get_flush_on_unload() -> bool
Get Flush on Unload

Returns:
    bool:

<a id="unreal.MovieSceneDataLayerSection.get_flush_on_activated"></a>

#### get_flush_on_activated

```python
def get_flush_on_activated() -> bool
```

x.get_flush_on_activated() -> bool
Get Flush on Activated

Returns:
    bool:

<a id="unreal.MovieSceneDataLayerSection.get_desired_state"></a>

#### get_desired_state

```python
def get_desired_state() -> DataLayerRuntimeState
```

x.get_desired_state() -> DataLayerRuntimeState
Get Desired State

Returns:
    DataLayerRuntimeState:

<a id="unreal.MovieSceneDataLayerSection.get_data_layer_assets"></a>

#### get_data_layer_assets

```python
def get_data_layer_assets() -> Array[DataLayerAsset]
```

x.get_data_layer_assets() -> Array[DataLayerAsset]
Get Data Layer Assets

Returns:
    Array[DataLayerAsset]:

<a id="unreal.MovieSceneDoubleSection"></a>