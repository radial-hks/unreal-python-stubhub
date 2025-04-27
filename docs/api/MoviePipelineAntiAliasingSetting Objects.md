## MoviePipelineAntiAliasingSetting Objects

```python
class MoviePipelineAntiAliasingSetting(MoviePipelineSetting)
```

Movie Pipeline Anti Aliasing Setting

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MoviePipelineAntiAliasingSetting.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``anti_aliasing_method`` (AntiAliasingMethod):  [Read-Write] If we are overriding the AA method, what do we use? None will turn off anti-aliasing.
- ``engine_warm_up_count`` (int32):  [Read-Write] The number of frames at the start of each shot that the engine will run without rendering. This allows pre-warming
  systems (such as particle systems, or level loading) which need time to run before you want to start capturing frames.
  This ticks the game thread but does not submit anything to the GPU to be rendered.

  This is more cheaper than RenderWarmUpCount and is the preferred way to have time pass at the start of a shot.
- ``override_anti_aliasing`` (bool):  [Read-Write] Should we override the Project's anti-aliasing setting during a movie render? This can be useful to have
  TAA on during normal work in the editor but force it off for high quality renders /w many spatial samples.
- ``render_warm_up_count`` (int32):  [Read-Write] The number of frames at the start of each shot that the engine will render and then discard. This is useful for
  ensuring there is history for temporal effects (such as anti-aliasing). It can be set to a lower number if not
  using temporal effects.

  This is more expensive than EngineWarmUpCount (which should be used for particle warm-ups, etc.)
- ``render_warm_up_frames`` (bool):  [Read-Write] Should we submit the warm-up frames to the GPU? Generally you want this disabled (as it is more performant), but
  some systems (such as gpu particles) need to be rendered to actually perform their warm-up. Enabling this will
  cause any warm up frames to also be submitted to the GPU which resolves this issue.
- ``spatial_sample_count`` (int32):  [Read-Write] How many frames should we accumulate together before contributing to one overall sample. This lets you
  increase the anti-aliasing quality of an sample, or have high quality anti-aliasing if you don't want
  any motion blur due to accumulation over time in SampleCount.
- ``temporal_sample_count`` (int32):  [Read-Write] The number of frames we should combine together to produce each output frame. This blends the
  results of this many sub-steps together to produce one output frame. See CameraShutterAngle to
  control how much time passes between each sub-frame. See SpatialSampleCount to see how many
  samples we average together to produce a sub-step. (This means rendering complexity is
  SampleCount * TileCount^2 * SpatialSampleCount * NumPasses).
- ``use_camera_cut_for_warm_up`` (bool):  [Read-Write] Should we use the excess in the camera cut track to determine engine warmup? When disabled, the sequence is evaluated
  once at the first frame and then waits there for EngineWarmUpCount many frames. When this is enabled, the number of
  warmup frames is based on how much excess there is in the camera cut track outside of the playback range AND
  the sequence is evaluated for each frame which can allow time for skeletal meshes to animate from a bind pose, etc.

<a id="unreal.MoviePipelineAntiAliasingSetting.spatial_sample_count"></a>

#### spatial_sample_count

```python
@property
def spatial_sample_count() -> int
```

(int32):  [Read-Write] How many frames should we accumulate together before contributing to one overall sample. This lets you
increase the anti-aliasing quality of an sample, or have high quality anti-aliasing if you don't want
any motion blur due to accumulation over time in SampleCount.

<a id="unreal.MoviePipelineAntiAliasingSetting.spatial_sample_count"></a>

#### spatial_sample_count

```python
@spatial_sample_count.setter
def spatial_sample_count(value: int) -> None
```

<a id="unreal.MoviePipelineAntiAliasingSetting.temporal_sample_count"></a>

#### temporal_sample_count

```python
@property
def temporal_sample_count() -> int
```

(int32):  [Read-Write] The number of frames we should combine together to produce each output frame. This blends the
results of this many sub-steps together to produce one output frame. See CameraShutterAngle to
control how much time passes between each sub-frame. See SpatialSampleCount to see how many
samples we average together to produce a sub-step. (This means rendering complexity is
SampleCount * TileCount^2 * SpatialSampleCount * NumPasses).

<a id="unreal.MoviePipelineAntiAliasingSetting.temporal_sample_count"></a>

#### temporal_sample_count

```python
@temporal_sample_count.setter
def temporal_sample_count(value: int) -> None
```

<a id="unreal.MoviePipelineAntiAliasingSetting.override_anti_aliasing"></a>

#### override_anti_aliasing

```python
@property
def override_anti_aliasing() -> bool
```

(bool):  [Read-Write] Should we override the Project's anti-aliasing setting during a movie render? This can be useful to have
TAA on during normal work in the editor but force it off for high quality renders /w many spatial samples.

<a id="unreal.MoviePipelineAntiAliasingSetting.override_anti_aliasing"></a>

#### override_anti_aliasing

```python
@override_anti_aliasing.setter
def override_anti_aliasing(value: bool) -> None
```

<a id="unreal.MoviePipelineAntiAliasingSetting.anti_aliasing_method"></a>

#### anti_aliasing_method

```python
@property
def anti_aliasing_method() -> AntiAliasingMethod
```

(AntiAliasingMethod):  [Read-Write] If we are overriding the AA method, what do we use? None will turn off anti-aliasing.

<a id="unreal.MoviePipelineAntiAliasingSetting.anti_aliasing_method"></a>

#### anti_aliasing_method

```python
@anti_aliasing_method.setter
def anti_aliasing_method(value: AntiAliasingMethod) -> None
```

<a id="unreal.MoviePipelineAntiAliasingSetting.render_warm_up_count"></a>

#### render_warm_up_count

```python
@property
def render_warm_up_count() -> int
```

(int32):  [Read-Write] The number of frames at the start of each shot that the engine will render and then discard. This is useful for
ensuring there is history for temporal effects (such as anti-aliasing). It can be set to a lower number if not
using temporal effects.

This is more expensive than EngineWarmUpCount (which should be used for particle warm-ups, etc.)

<a id="unreal.MoviePipelineAntiAliasingSetting.render_warm_up_count"></a>

#### render_warm_up_count

```python
@render_warm_up_count.setter
def render_warm_up_count(value: int) -> None
```

<a id="unreal.MoviePipelineAntiAliasingSetting.use_camera_cut_for_warm_up"></a>

#### use_camera_cut_for_warm_up

```python
@property
def use_camera_cut_for_warm_up() -> bool
```

(bool):  [Read-Write] Should we use the excess in the camera cut track to determine engine warmup? When disabled, the sequence is evaluated
once at the first frame and then waits there for EngineWarmUpCount many frames. When this is enabled, the number of
warmup frames is based on how much excess there is in the camera cut track outside of the playback range AND
the sequence is evaluated for each frame which can allow time for skeletal meshes to animate from a bind pose, etc.

<a id="unreal.MoviePipelineAntiAliasingSetting.use_camera_cut_for_warm_up"></a>

#### use_camera_cut_for_warm_up

```python
@use_camera_cut_for_warm_up.setter
def use_camera_cut_for_warm_up(value: bool) -> None
```

<a id="unreal.MoviePipelineAntiAliasingSetting.engine_warm_up_count"></a>

#### engine_warm_up_count

```python
@property
def engine_warm_up_count() -> int
```

(int32):  [Read-Write] The number of frames at the start of each shot that the engine will run without rendering. This allows pre-warming
systems (such as particle systems, or level loading) which need time to run before you want to start capturing frames.
This ticks the game thread but does not submit anything to the GPU to be rendered.

This is more cheaper than RenderWarmUpCount and is the preferred way to have time pass at the start of a shot.

<a id="unreal.MoviePipelineAntiAliasingSetting.engine_warm_up_count"></a>

#### engine_warm_up_count

```python
@engine_warm_up_count.setter
def engine_warm_up_count(value: int) -> None
```

<a id="unreal.MoviePipelineAntiAliasingSetting.render_warm_up_frames"></a>

#### render_warm_up_frames

```python
@property
def render_warm_up_frames() -> bool
```

(bool):  [Read-Write] Should we submit the warm-up frames to the GPU? Generally you want this disabled (as it is more performant), but
some systems (such as gpu particles) need to be rendered to actually perform their warm-up. Enabling this will
cause any warm up frames to also be submitted to the GPU which resolves this issue.

<a id="unreal.MoviePipelineAntiAliasingSetting.render_warm_up_frames"></a>

#### render_warm_up_frames

```python
@render_warm_up_frames.setter
def render_warm_up_frames(value: bool) -> None
```

<a id="unreal.MoviePipelineLibrary"></a>