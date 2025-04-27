## MovieGraphGlobalGameOverridesNode Objects

```python
class MovieGraphGlobalGameOverridesNode(MovieGraphSettingNode)
```

A node which configures the global game overrides.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphGlobalGameOverrides.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``disable_hlo_ds`` (bool):  [Read-Write] Determines if hierarchical LODs should be disabled and their real meshes used instead, regardless of distance.
  Note that this does not affect World Partition HLODs.
- ``disable_lo_ds`` (bool):  [Read-Write] Disabling LODs will use the highest quality LOD for meshes and particle systems, regardless of distance. Note
  that this does not affect Nanite.

  Configures the following cvars:
  - r.ForceLOD
  - r.SkeletalMeshLODBias
  - r.ParticleLODBias
  - foliage.DitheredLOD
  - foliage.ForceLOD
- ``disable_texture_streaming`` (bool):  [Read-Write] Toggles whether texture streaming is disabled. Can solve objects being blurry after camera cuts.

  Configures the following cvars:
  - r.TextureStreaming
- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``flush_asset_compiler`` (bool):  [Read-Write] This ensures that any asynchronously compiled assets (static meshes, distance fields, etc.) required for rendering the frame
  are completed before rendering the frame. This feature generally only adds to render times on the frames where a new asset
  is introduced (ie, spawned) that may not be fully compiled. Results are stored in the DDC on subsequent uses.
- ``flush_grass_streaming`` (bool):  [Read-Write] Flushing grass streaming prevents visible pop-in/culling of grass instances, but may come at a high GPU memory
  cost (depending on rendering feature set), and grass density. Try turning this off if you are low on GPU memory
  and have dense grass.
- ``flush_level_streaming`` (bool):  [Read-Write] Flushing level streaming ensures that any pending changes to sub-levels or world partition are fully processed before we render
  the frame. This feature generally only adds to render times on the frames that have level visibility state changes, so generally
  safe to leave turned on all the time.
- ``flush_shader_compiler`` (bool):  [Read-Write] This ensures that any asynchronously compiled shader permutations are completed before rendering the frame. When using
  On Demand Shader Compilation the editor will skip compiling currently unneeded permutations for the material graph to
  decrease artist iteration time, but these permutations need to be compiled when rendering. Results are stored in the DDC on
  subsequent uses.
- ``flush_streaming_managers`` (bool):  [Read-Write] This ensures that we wait on any streaming managers that may have outstanding work to finish their work before we render
  the frame. Many GPU-based features rely on a feedback loop where a frame is rendered, then results are read back from the GPU
  to the CPU. These results are analyzed, and additional data is loaded to be used in a subsequent frame. This feature ensures
  that the data is fully loaded before we render the next frame, but does NOT solve issues related to generating the those
  feedback requests in the first place. Virtual Textures and Nanite must render the frame to generate the request --
  this option cannot solve that; it only helps ensure that the requests that are made are fully processed before
  the frame is rendered.

  Configures the following cvars:
  - r.Streaming.SyncStatesWhenBlocking
- ``game_mode_override`` (type(Class)):  [Read-Write]
  deprecated: Please use the SoftGameModeOverride property instead.
- ``override_b_disable_hlo_ds`` (bool):  [Read-Write]
- ``override_b_disable_lo_ds`` (bool):  [Read-Write]
- ``override_b_disable_texture_streaming`` (bool):  [Read-Write]
- ``override_b_flush_asset_compiler`` (bool):  [Read-Write]
- ``override_b_flush_grass_streaming`` (bool):  [Read-Write]
- ``override_b_flush_level_streaming`` (bool):  [Read-Write]
- ``override_b_flush_shader_compiler`` (bool):  [Read-Write]
- ``override_b_flush_streaming_managers`` (bool):  [Read-Write]
- ``override_game_mode_override`` (bool):  [Read-Write]
  deprecated: Please use the bOverride_SoftGameModeOverride property instead.
- ``override_scalability_quality_level`` (bool):  [Read-Write]
- ``override_soft_game_mode_override`` (bool):  [Read-Write]
- ``override_virtual_texture_feedback_factor`` (bool):  [Read-Write]
- ``scalability_quality_level`` (MovieGraphScalabilityQualityLevel):  [Read-Write] The scalability quality level that should be used in renders. See the Scalability Reference documentation for
  information on how to edit cvars to add/change default quality values.
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.
- ``soft_game_mode_override`` (Class):  [Read-Write] Optional game mode to override the map's default game mode with. This can be useful if the game's normal mode
  displays UI elements or loading screens that you don't want captured.
- ``virtual_texture_feedback_factor`` (int32):  [Read-Write] The virtual texture feedback resolution factor. A lower factor will increase virtual texture feedback resolution.

<a id="unreal.MovieGraphGlobalGameOverridesNode.override_game_mode_override"></a>

#### override_game_mode_override

```python
@property
def override_game_mode_override() -> bool
```

(bool):  [Read-Write]
deprecated: Please use the bOverride_SoftGameModeOverride property instead.

<a id="unreal.MovieGraphGlobalGameOverridesNode.override_game_mode_override"></a>

#### override_game_mode_override

```python
@override_game_mode_override.setter
def override_game_mode_override(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalGameOverridesNode.override_soft_game_mode_override"></a>

#### override_soft_game_mode_override

```python
@property
def override_soft_game_mode_override() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphGlobalGameOverridesNode.override_soft_game_mode_override"></a>

#### override_soft_game_mode_override

```python
@override_soft_game_mode_override.setter
def override_soft_game_mode_override(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalGameOverridesNode.override_scalability_quality_level"></a>

#### override_scalability_quality_level

```python
@property
def override_scalability_quality_level() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphGlobalGameOverridesNode.override_scalability_quality_level"></a>

#### override_scalability_quality_level

```python
@override_scalability_quality_level.setter
def override_scalability_quality_level(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalGameOverridesNode.override_b_disable_texture_streaming"></a>

#### override_b_disable_texture_streaming

```python
@property
def override_b_disable_texture_streaming() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphGlobalGameOverridesNode.override_b_disable_texture_streaming"></a>

#### override_b_disable_texture_streaming

```python
@override_b_disable_texture_streaming.setter
def override_b_disable_texture_streaming(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalGameOverridesNode.override_b_disable_lo_ds"></a>

#### override_b_disable_lo_ds

```python
@property
def override_b_disable_lo_ds() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphGlobalGameOverridesNode.override_b_disable_lo_ds"></a>

#### override_b_disable_lo_ds

```python
@override_b_disable_lo_ds.setter
def override_b_disable_lo_ds(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalGameOverridesNode.override_b_disable_hlo_ds"></a>

#### override_b_disable_hlo_ds

```python
@property
def override_b_disable_hlo_ds() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphGlobalGameOverridesNode.override_b_disable_hlo_ds"></a>

#### override_b_disable_hlo_ds

```python
@override_b_disable_hlo_ds.setter
def override_b_disable_hlo_ds(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalGameOverridesNode.override_b_flush_level_streaming"></a>

#### override_b_flush_level_streaming

```python
@property
def override_b_flush_level_streaming() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphGlobalGameOverridesNode.override_b_flush_level_streaming"></a>

#### override_b_flush_level_streaming

```python
@override_b_flush_level_streaming.setter
def override_b_flush_level_streaming(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalGameOverridesNode.override_b_flush_asset_compiler"></a>

#### override_b_flush_asset_compiler

```python
@property
def override_b_flush_asset_compiler() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphGlobalGameOverridesNode.override_b_flush_asset_compiler"></a>

#### override_b_flush_asset_compiler

```python
@override_b_flush_asset_compiler.setter
def override_b_flush_asset_compiler(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalGameOverridesNode.override_b_flush_shader_compiler"></a>

#### override_b_flush_shader_compiler

```python
@property
def override_b_flush_shader_compiler() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphGlobalGameOverridesNode.override_b_flush_shader_compiler"></a>

#### override_b_flush_shader_compiler

```python
@override_b_flush_shader_compiler.setter
def override_b_flush_shader_compiler(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalGameOverridesNode.override_b_flush_grass_streaming"></a>

#### override_b_flush_grass_streaming

```python
@property
def override_b_flush_grass_streaming() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphGlobalGameOverridesNode.override_b_flush_grass_streaming"></a>

#### override_b_flush_grass_streaming

```python
@override_b_flush_grass_streaming.setter
def override_b_flush_grass_streaming(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalGameOverridesNode.override_b_flush_streaming_managers"></a>

#### override_b_flush_streaming_managers

```python
@property
def override_b_flush_streaming_managers() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphGlobalGameOverridesNode.override_b_flush_streaming_managers"></a>

#### override_b_flush_streaming_managers

```python
@override_b_flush_streaming_managers.setter
def override_b_flush_streaming_managers(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalGameOverridesNode.override_virtual_texture_feedback_factor"></a>

#### override_virtual_texture_feedback_factor

```python
@property
def override_virtual_texture_feedback_factor() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphGlobalGameOverridesNode.override_virtual_texture_feedback_factor"></a>

#### override_virtual_texture_feedback_factor

```python
@override_virtual_texture_feedback_factor.setter
def override_virtual_texture_feedback_factor(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalGameOverridesNode.game_mode_override"></a>

#### game_mode_override

```python
@property
def game_mode_override() -> Class
```

(type(Class)):  [Read-Write]
deprecated: Please use the SoftGameModeOverride property instead.

<a id="unreal.MovieGraphGlobalGameOverridesNode.game_mode_override"></a>

#### game_mode_override

```python
@game_mode_override.setter
def game_mode_override(value: Class) -> None
```

<a id="unreal.MovieGraphGlobalGameOverridesNode.soft_game_mode_override"></a>

#### soft_game_mode_override

```python
@property
def soft_game_mode_override() -> Class
```

(Class):  [Read-Write] Optional game mode to override the map's default game mode with. This can be useful if the game's normal mode
displays UI elements or loading screens that you don't want captured.

<a id="unreal.MovieGraphGlobalGameOverridesNode.soft_game_mode_override"></a>

#### soft_game_mode_override

```python
@soft_game_mode_override.setter
def soft_game_mode_override(value: Class) -> None
```

<a id="unreal.MovieGraphGlobalGameOverridesNode.scalability_quality_level"></a>

#### scalability_quality_level

```python
@property
def scalability_quality_level() -> MovieGraphScalabilityQualityLevel
```

(MovieGraphScalabilityQualityLevel):  [Read-Write] The scalability quality level that should be used in renders. See the Scalability Reference documentation for
information on how to edit cvars to add/change default quality values.

<a id="unreal.MovieGraphGlobalGameOverridesNode.scalability_quality_level"></a>

#### scalability_quality_level

```python
@scalability_quality_level.setter
def scalability_quality_level(
        value: MovieGraphScalabilityQualityLevel) -> None
```

<a id="unreal.MovieGraphGlobalGameOverridesNode.disable_texture_streaming"></a>

#### disable_texture_streaming

```python
@property
def disable_texture_streaming() -> bool
```

(bool):  [Read-Write] Toggles whether texture streaming is disabled. Can solve objects being blurry after camera cuts.

Configures the following cvars:
- r.TextureStreaming

<a id="unreal.MovieGraphGlobalGameOverridesNode.disable_texture_streaming"></a>

#### disable_texture_streaming

```python
@disable_texture_streaming.setter
def disable_texture_streaming(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalGameOverridesNode.disable_lo_ds"></a>

#### disable_lo_ds

```python
@property
def disable_lo_ds() -> bool
```

(bool):  [Read-Write] Disabling LODs will use the highest quality LOD for meshes and particle systems, regardless of distance. Note
that this does not affect Nanite.

Configures the following cvars:
- r.ForceLOD
- r.SkeletalMeshLODBias
- r.ParticleLODBias
- foliage.DitheredLOD
- foliage.ForceLOD

<a id="unreal.MovieGraphGlobalGameOverridesNode.disable_lo_ds"></a>

#### disable_lo_ds

```python
@disable_lo_ds.setter
def disable_lo_ds(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalGameOverridesNode.disable_hlo_ds"></a>

#### disable_hlo_ds

```python
@property
def disable_hlo_ds() -> bool
```

(bool):  [Read-Write] Determines if hierarchical LODs should be disabled and their real meshes used instead, regardless of distance.
Note that this does not affect World Partition HLODs.

<a id="unreal.MovieGraphGlobalGameOverridesNode.disable_hlo_ds"></a>

#### disable_hlo_ds

```python
@disable_hlo_ds.setter
def disable_hlo_ds(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalGameOverridesNode.flush_level_streaming"></a>

#### flush_level_streaming

```python
@property
def flush_level_streaming() -> bool
```

(bool):  [Read-Write] Flushing level streaming ensures that any pending changes to sub-levels or world partition are fully processed before we render
the frame. This feature generally only adds to render times on the frames that have level visibility state changes, so generally
safe to leave turned on all the time.

<a id="unreal.MovieGraphGlobalGameOverridesNode.flush_level_streaming"></a>

#### flush_level_streaming

```python
@flush_level_streaming.setter
def flush_level_streaming(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalGameOverridesNode.flush_asset_compiler"></a>

#### flush_asset_compiler

```python
@property
def flush_asset_compiler() -> bool
```

(bool):  [Read-Write] This ensures that any asynchronously compiled assets (static meshes, distance fields, etc.) required for rendering the frame
are completed before rendering the frame. This feature generally only adds to render times on the frames where a new asset
is introduced (ie, spawned) that may not be fully compiled. Results are stored in the DDC on subsequent uses.

<a id="unreal.MovieGraphGlobalGameOverridesNode.flush_asset_compiler"></a>

#### flush_asset_compiler

```python
@flush_asset_compiler.setter
def flush_asset_compiler(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalGameOverridesNode.flush_shader_compiler"></a>

#### flush_shader_compiler

```python
@property
def flush_shader_compiler() -> bool
```

(bool):  [Read-Write] This ensures that any asynchronously compiled shader permutations are completed before rendering the frame. When using
On Demand Shader Compilation the editor will skip compiling currently unneeded permutations for the material graph to
decrease artist iteration time, but these permutations need to be compiled when rendering. Results are stored in the DDC on
subsequent uses.

<a id="unreal.MovieGraphGlobalGameOverridesNode.flush_shader_compiler"></a>

#### flush_shader_compiler

```python
@flush_shader_compiler.setter
def flush_shader_compiler(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalGameOverridesNode.flush_grass_streaming"></a>

#### flush_grass_streaming

```python
@property
def flush_grass_streaming() -> bool
```

(bool):  [Read-Write] Flushing grass streaming prevents visible pop-in/culling of grass instances, but may come at a high GPU memory
cost (depending on rendering feature set), and grass density. Try turning this off if you are low on GPU memory
and have dense grass.

<a id="unreal.MovieGraphGlobalGameOverridesNode.flush_grass_streaming"></a>

#### flush_grass_streaming

```python
@flush_grass_streaming.setter
def flush_grass_streaming(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalGameOverridesNode.flush_streaming_managers"></a>

#### flush_streaming_managers

```python
@property
def flush_streaming_managers() -> bool
```

(bool):  [Read-Write] This ensures that we wait on any streaming managers that may have outstanding work to finish their work before we render
the frame. Many GPU-based features rely on a feedback loop where a frame is rendered, then results are read back from the GPU
to the CPU. These results are analyzed, and additional data is loaded to be used in a subsequent frame. This feature ensures
that the data is fully loaded before we render the next frame, but does NOT solve issues related to generating the those
feedback requests in the first place. Virtual Textures and Nanite must render the frame to generate the request --
this option cannot solve that; it only helps ensure that the requests that are made are fully processed before
the frame is rendered.

Configures the following cvars:
- r.Streaming.SyncStatesWhenBlocking

<a id="unreal.MovieGraphGlobalGameOverridesNode.flush_streaming_managers"></a>

#### flush_streaming_managers

```python
@flush_streaming_managers.setter
def flush_streaming_managers(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalGameOverridesNode.virtual_texture_feedback_factor"></a>

#### virtual_texture_feedback_factor

```python
@property
def virtual_texture_feedback_factor() -> int
```

(int32):  [Read-Write] The virtual texture feedback resolution factor. A lower factor will increase virtual texture feedback resolution.

<a id="unreal.MovieGraphGlobalGameOverridesNode.virtual_texture_feedback_factor"></a>

#### virtual_texture_feedback_factor

```python
@virtual_texture_feedback_factor.setter
def virtual_texture_feedback_factor(value: int) -> None
```

<a id="unreal.MovieGraphGlobalOutputSettingNode"></a>