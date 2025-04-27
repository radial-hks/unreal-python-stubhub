## MoviePipelineGameOverrideSetting Objects

```python
class MoviePipelineGameOverrideSetting(MoviePipelineSetting)
```

Movie Pipeline Game Override Setting

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MoviePipelineGameOverrideSetting.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cinematic_quality_settings`` (bool):  [Read-Write] If true, automatically set the engine to the Cinematic Scalability quality settings during render. See the Scalability Reference documentation for information on how to edit cvars to add/change default quality values.
- ``disable_hlo_ds`` (bool):  [Read-Write] Should we disable Hierarchical LODs and instead use their real meshes regardless of distance?
- ``flush_grass_streaming`` (bool):  [Read-Write] Flushing grass streaming (combined with override view distance scale) prevents visible pop-in/culling of grace instances.
- ``flush_streaming_managers`` (bool):  [Read-Write] Experimental. If true flush the streaming managers (Texture Streaming) each frame. Allows Texture Streaming to not have visible pop-in in final frames.
- ``game_mode_override`` (type(Class)):  [Read-Write]
  deprecated: Please use the SoftGameModeOverride property instead.
- ``override_view_distance_scale`` (bool):  [Read-Write] Should we override the View Distance Scale? Can be used in situations where MaxDrawDistance has been set before for in-game performance.
- ``override_virtual_texture_feedback_factor`` (bool):  [Read-Write] If true then override the virtual texture feedback resolution factor. Otherwise the value from the project renderer settings will be used.
- ``shadow_distance_scale`` (int32):  [Read-Write] Scalability option to trade shadow distance versus performance for directional lights
- ``shadow_radius_threshold`` (float):  [Read-Write] Cull shadow casters if they are too small, value is the minimal screen space bounding sphere radius
- ``soft_game_mode_override`` (Class):  [Read-Write] Optional Game Mode to override the map's default game mode with. This can be useful if the game's normal mode displays UI elements or loading screens that you don't want captured.
- ``texture_streaming`` (MoviePipelineTextureStreamingMethod):  [Read-Write] Defines which If true, when using texture streaming fully load the required textures each frame instead of loading them in over time. This solves objects being blurry after camera cuts.
- ``use_high_quality_shadows`` (bool):  [Read-Write] Should we override shadow-related CVars with some high quality preset settings?
- ``use_lod_zero`` (bool):  [Read-Write] Should we try to use the highest quality LOD for meshes and particle systems regardless of distance?
- ``view_distance_scale`` (int32):  [Read-Write] Controls the view distance scale. A primitive's MaxDrawDistance is scaled by this value.
- ``virtual_texture_feedback_factor`` (int32):  [Read-Write] The virtual texture feedback resolution factor. A lower factor will increase virtual texture feedback resolution.

<a id="unreal.MoviePipelineGameOverrideSetting.game_mode_override"></a>

#### game_mode_override

```python
@property
def game_mode_override() -> Class
```

(type(Class)):  [Read-Write]
deprecated: Please use the SoftGameModeOverride property instead.

<a id="unreal.MoviePipelineGameOverrideSetting.game_mode_override"></a>

#### game_mode_override

```python
@game_mode_override.setter
def game_mode_override(value: Class) -> None
```

<a id="unreal.MoviePipelineGameOverrideSetting.soft_game_mode_override"></a>

#### soft_game_mode_override

```python
@property
def soft_game_mode_override() -> Class
```

(Class):  [Read-Write] Optional Game Mode to override the map's default game mode with. This can be useful if the game's normal mode displays UI elements or loading screens that you don't want captured.

<a id="unreal.MoviePipelineGameOverrideSetting.soft_game_mode_override"></a>

#### soft_game_mode_override

```python
@soft_game_mode_override.setter
def soft_game_mode_override(value: Class) -> None
```

<a id="unreal.MoviePipelineGameOverrideSetting.cinematic_quality_settings"></a>

#### cinematic_quality_settings

```python
@property
def cinematic_quality_settings() -> bool
```

(bool):  [Read-Write] If true, automatically set the engine to the Cinematic Scalability quality settings during render. See the Scalability Reference documentation for information on how to edit cvars to add/change default quality values.

<a id="unreal.MoviePipelineGameOverrideSetting.cinematic_quality_settings"></a>

#### cinematic_quality_settings

```python
@cinematic_quality_settings.setter
def cinematic_quality_settings(value: bool) -> None
```

<a id="unreal.MoviePipelineGameOverrideSetting.texture_streaming"></a>

#### texture_streaming

```python
@property
def texture_streaming() -> MoviePipelineTextureStreamingMethod
```

(MoviePipelineTextureStreamingMethod):  [Read-Write] Defines which If true, when using texture streaming fully load the required textures each frame instead of loading them in over time. This solves objects being blurry after camera cuts.

<a id="unreal.MoviePipelineGameOverrideSetting.texture_streaming"></a>

#### texture_streaming

```python
@texture_streaming.setter
def texture_streaming(value: MoviePipelineTextureStreamingMethod) -> None
```

<a id="unreal.MoviePipelineGameOverrideSetting.use_lod_zero"></a>

#### use_lod_zero

```python
@property
def use_lod_zero() -> bool
```

(bool):  [Read-Write] Should we try to use the highest quality LOD for meshes and particle systems regardless of distance?

<a id="unreal.MoviePipelineGameOverrideSetting.use_lod_zero"></a>

#### use_lod_zero

```python
@use_lod_zero.setter
def use_lod_zero(value: bool) -> None
```

<a id="unreal.MoviePipelineGameOverrideSetting.disable_hlo_ds"></a>

#### disable_hlo_ds

```python
@property
def disable_hlo_ds() -> bool
```

(bool):  [Read-Write] Should we disable Hierarchical LODs and instead use their real meshes regardless of distance?

<a id="unreal.MoviePipelineGameOverrideSetting.disable_hlo_ds"></a>

#### disable_hlo_ds

```python
@disable_hlo_ds.setter
def disable_hlo_ds(value: bool) -> None
```

<a id="unreal.MoviePipelineGameOverrideSetting.use_high_quality_shadows"></a>

#### use_high_quality_shadows

```python
@property
def use_high_quality_shadows() -> bool
```

(bool):  [Read-Write] Should we override shadow-related CVars with some high quality preset settings?

<a id="unreal.MoviePipelineGameOverrideSetting.use_high_quality_shadows"></a>

#### use_high_quality_shadows

```python
@use_high_quality_shadows.setter
def use_high_quality_shadows(value: bool) -> None
```

<a id="unreal.MoviePipelineGameOverrideSetting.shadow_distance_scale"></a>

#### shadow_distance_scale

```python
@property
def shadow_distance_scale() -> int
```

(int32):  [Read-Write] Scalability option to trade shadow distance versus performance for directional lights

<a id="unreal.MoviePipelineGameOverrideSetting.shadow_distance_scale"></a>

#### shadow_distance_scale

```python
@shadow_distance_scale.setter
def shadow_distance_scale(value: int) -> None
```

<a id="unreal.MoviePipelineGameOverrideSetting.shadow_radius_threshold"></a>

#### shadow_radius_threshold

```python
@property
def shadow_radius_threshold() -> float
```

(float):  [Read-Write] Cull shadow casters if they are too small, value is the minimal screen space bounding sphere radius

<a id="unreal.MoviePipelineGameOverrideSetting.shadow_radius_threshold"></a>

#### shadow_radius_threshold

```python
@shadow_radius_threshold.setter
def shadow_radius_threshold(value: float) -> None
```

<a id="unreal.MoviePipelineGameOverrideSetting.override_view_distance_scale"></a>

#### override_view_distance_scale

```python
@property
def override_view_distance_scale() -> bool
```

(bool):  [Read-Write] Should we override the View Distance Scale? Can be used in situations where MaxDrawDistance has been set before for in-game performance.

<a id="unreal.MoviePipelineGameOverrideSetting.override_view_distance_scale"></a>

#### override_view_distance_scale

```python
@override_view_distance_scale.setter
def override_view_distance_scale(value: bool) -> None
```

<a id="unreal.MoviePipelineGameOverrideSetting.view_distance_scale"></a>

#### view_distance_scale

```python
@property
def view_distance_scale() -> int
```

(int32):  [Read-Write] Controls the view distance scale. A primitive's MaxDrawDistance is scaled by this value.

<a id="unreal.MoviePipelineGameOverrideSetting.view_distance_scale"></a>

#### view_distance_scale

```python
@view_distance_scale.setter
def view_distance_scale(value: int) -> None
```

<a id="unreal.MoviePipelineGameOverrideSetting.flush_grass_streaming"></a>

#### flush_grass_streaming

```python
@property
def flush_grass_streaming() -> bool
```

(bool):  [Read-Write] Flushing grass streaming (combined with override view distance scale) prevents visible pop-in/culling of grace instances.

<a id="unreal.MoviePipelineGameOverrideSetting.flush_grass_streaming"></a>

#### flush_grass_streaming

```python
@flush_grass_streaming.setter
def flush_grass_streaming(value: bool) -> None
```

<a id="unreal.MoviePipelineGameOverrideSetting.flush_streaming_managers"></a>

#### flush_streaming_managers

```python
@property
def flush_streaming_managers() -> bool
```

(bool):  [Read-Write] Experimental. If true flush the streaming managers (Texture Streaming) each frame. Allows Texture Streaming to not have visible pop-in in final frames.

<a id="unreal.MoviePipelineGameOverrideSetting.flush_streaming_managers"></a>

#### flush_streaming_managers

```python
@flush_streaming_managers.setter
def flush_streaming_managers(value: bool) -> None
```

<a id="unreal.MoviePipelineGameOverrideSetting.override_virtual_texture_feedback_factor"></a>

#### override_virtual_texture_feedback_factor

```python
@property
def override_virtual_texture_feedback_factor() -> bool
```

(bool):  [Read-Write] If true then override the virtual texture feedback resolution factor. Otherwise the value from the project renderer settings will be used.

<a id="unreal.MoviePipelineGameOverrideSetting.override_virtual_texture_feedback_factor"></a>

#### override_virtual_texture_feedback_factor

```python
@override_virtual_texture_feedback_factor.setter
def override_virtual_texture_feedback_factor(value: bool) -> None
```

<a id="unreal.MoviePipelineGameOverrideSetting.virtual_texture_feedback_factor"></a>

#### virtual_texture_feedback_factor

```python
@property
def virtual_texture_feedback_factor() -> int
```

(int32):  [Read-Write] The virtual texture feedback resolution factor. A lower factor will increase virtual texture feedback resolution.

<a id="unreal.MoviePipelineGameOverrideSetting.virtual_texture_feedback_factor"></a>

#### virtual_texture_feedback_factor

```python
@virtual_texture_feedback_factor.setter
def virtual_texture_feedback_factor(value: int) -> None
```

<a id="unreal.MoviePipelineLinearExecutorBase"></a>