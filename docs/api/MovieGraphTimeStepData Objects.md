## MovieGraphTimeStepData Objects

```python
class MovieGraphTimeStepData(StructBase)
```

This data structure needs to be filled out each frame by the UMovieGraphTimeStepBase,
which will eventually be passed to the renderer. It controls per-sample behavior such
as the delta time, if this is the first/last sample for an output frame, etc.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphTimeStepData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``discard_output`` (bool):  [Read-Write] Should the rendered result be discarded after a render? This will skip any
  accumulators or readback and is used for frames that are only produced to
  warm up the renderer.
- ``evaluated_config`` (MovieGraphEvaluatedConfig):  [Read-Write] The evaluated config holds the configuration used for this given frame. This pointer
  can potentially change each frame (if the graph for that frame is different) but
  users can rely on the EvaluatedConfig being correct for a given frame, thus all
  resolves (such as filenames) should use the config for that frame, not the latest
  one available.
- ``frame_delta_time`` (float):  [Read-Write]
- ``frame_rate`` (FrameRate):  [Read-Write]
- ``is_first_temporal_sample_for_frame`` (bool):  [Read-Write] Should be set to true for the first sample of each output frame. Used to determine
  if various systems need to reset or gather data for a new frame. Can be true at
  the same time as bIsLastTemporalSampleForFrame (ie: 1TS)
- ``is_last_temporal_sample_for_frame`` (bool):  [Read-Write] Should be set to true for the last sample of each output frame. Can be true at
  the same time as bIsFirstTemporalSampleForFrame (ie: 1TS)
- ``motion_blur_fraction`` (float):  [Read-Write]
- ``output_frame_number`` (int32):  [Read-Write] * Relative to zero for the entire render.
- ``rendered_frame_number`` (int32):  [Read-Write]
- ``requires_accumulator`` (bool):  [Read-Write] Should be set to true for every sample if there is more than one temporal sample
  making up this render. This will cause the renderer to allocate accumulators
  to store the multi-frame data into.
- ``root_frame_number`` (FrameNumber):  [Read-Write] * The current frame number at the root (sequence) level.
  * This is the same number as what is shown in sequencer when viewing the sequence.
- ``root_time_code`` (Timecode):  [Read-Write] The current timecode at the root (sequence) level. Note that this is adjusted according to the timecode settings on the Global Output Settings node.
- ``shot_frame_number`` (FrameNumber):  [Read-Write] * The current frame number at the shot level.
  * This is the same number as what is shown in sequencer when viewing the shot.
- ``shot_output_frame_number`` (int32):  [Read-Write] * Relative to zero for the current shot.
- ``shot_time_code`` (Timecode):  [Read-Write] The current timecode at the shot level. Note that this is adjusted according to the timecode settings on the Global Output Settings node.
- ``spatial_sample_count`` (int32):  [Read-Write] The maximum number of Spatial Samples this frame is expected to be able to process.
- ``spatial_sample_index`` (int32):  [Read-Write] Index out of SpatialSampleCount that we're on.
- ``temporal_sample_count`` (int32):  [Read-Write] * What is the maximum number of Temporal Samples this frame is expected to be able to process.
- ``temporal_sample_index`` (int32):  [Read-Write] * Index out of TemporalSampleCount we're on. No guarantee that we'll ever reach Index == Count-1,
  * if bIsLastTemporalSampleForFrame has priority over that (to allow early outs)
- ``world_seconds`` (float):  [Read-Write]
- ``world_time_dilation`` (float):  [Read-Write]

<a id="unreal.MovieGraphTimeStepData.__init__"></a>

#### __init__

```python
def __init__(output_frame_number: int = 0,
             shot_output_frame_number: int = 0,
             rendered_frame_number: int = 0,
             frame_delta_time: float = 0.000000,
             world_time_dilation: float = 0.000000,
             world_seconds: float = 0.000000,
             motion_blur_fraction: float = 0.000000,
             frame_rate: FrameRate = [60000, 1],
             temporal_sample_index: int = 0,
             temporal_sample_count: int = 0,
             spatial_sample_index: int = 0,
             spatial_sample_count: int = 0,
             is_first_temporal_sample_for_frame: bool = False,
             is_last_temporal_sample_for_frame: bool = False,
             discard_output: bool = False,
             requires_accumulator: bool = False,
             evaluated_config: MovieGraphEvaluatedConfig = None,
             root_time_code: Timecode = [0, 0, 0, 0, 0.000000, False],
             root_frame_number: FrameNumber = [0],
             shot_time_code: Timecode = [0, 0, 0, 0, 0.000000, False],
             shot_frame_number: FrameNumber = [0]) -> None
```

<a id="unreal.MovieGraphTimeStepData.output_frame_number"></a>

#### output_frame_number

```python
@property
def output_frame_number() -> int
```

(int32):  [Read-Write] * Relative to zero for the entire render.

<a id="unreal.MovieGraphTimeStepData.output_frame_number"></a>

#### output_frame_number

```python
@output_frame_number.setter
def output_frame_number(value: int) -> None
```

<a id="unreal.MovieGraphTimeStepData.shot_output_frame_number"></a>

#### shot_output_frame_number

```python
@property
def shot_output_frame_number() -> int
```

(int32):  [Read-Write] * Relative to zero for the current shot.

<a id="unreal.MovieGraphTimeStepData.shot_output_frame_number"></a>

#### shot_output_frame_number

```python
@shot_output_frame_number.setter
def shot_output_frame_number(value: int) -> None
```

<a id="unreal.MovieGraphTimeStepData.rendered_frame_number"></a>

#### rendered_frame_number

```python
@property
def rendered_frame_number() -> int
```

(int32):  [Read-Write]

<a id="unreal.MovieGraphTimeStepData.rendered_frame_number"></a>

#### rendered_frame_number

```python
@rendered_frame_number.setter
def rendered_frame_number(value: int) -> None
```

<a id="unreal.MovieGraphTimeStepData.frame_delta_time"></a>

#### frame_delta_time

```python
@property
def frame_delta_time() -> float
```

(float):  [Read-Write]

<a id="unreal.MovieGraphTimeStepData.frame_delta_time"></a>

#### frame_delta_time

```python
@frame_delta_time.setter
def frame_delta_time(value: float) -> None
```

<a id="unreal.MovieGraphTimeStepData.world_time_dilation"></a>

#### world_time_dilation

```python
@property
def world_time_dilation() -> float
```

(float):  [Read-Write]

<a id="unreal.MovieGraphTimeStepData.world_time_dilation"></a>

#### world_time_dilation

```python
@world_time_dilation.setter
def world_time_dilation(value: float) -> None
```

<a id="unreal.MovieGraphTimeStepData.world_seconds"></a>

#### world_seconds

```python
@property
def world_seconds() -> float
```

(float):  [Read-Write]

<a id="unreal.MovieGraphTimeStepData.world_seconds"></a>

#### world_seconds

```python
@world_seconds.setter
def world_seconds(value: float) -> None
```

<a id="unreal.MovieGraphTimeStepData.motion_blur_fraction"></a>

#### motion_blur_fraction

```python
@property
def motion_blur_fraction() -> float
```

(float):  [Read-Write]

<a id="unreal.MovieGraphTimeStepData.motion_blur_fraction"></a>

#### motion_blur_fraction

```python
@motion_blur_fraction.setter
def motion_blur_fraction(value: float) -> None
```

<a id="unreal.MovieGraphTimeStepData.frame_rate"></a>

#### frame_rate

```python
@property
def frame_rate() -> FrameRate
```

(FrameRate):  [Read-Write]

<a id="unreal.MovieGraphTimeStepData.frame_rate"></a>

#### frame_rate

```python
@frame_rate.setter
def frame_rate(value: FrameRate) -> None
```

<a id="unreal.MovieGraphTimeStepData.temporal_sample_index"></a>

#### temporal_sample_index

```python
@property
def temporal_sample_index() -> int
```

(int32):  [Read-Write] * Index out of TemporalSampleCount we're on. No guarantee that we'll ever reach Index == Count-1,
* if bIsLastTemporalSampleForFrame has priority over that (to allow early outs)

<a id="unreal.MovieGraphTimeStepData.temporal_sample_index"></a>

#### temporal_sample_index

```python
@temporal_sample_index.setter
def temporal_sample_index(value: int) -> None
```

<a id="unreal.MovieGraphTimeStepData.temporal_sample_count"></a>

#### temporal_sample_count

```python
@property
def temporal_sample_count() -> int
```

(int32):  [Read-Write] * What is the maximum number of Temporal Samples this frame is expected to be able to process.

<a id="unreal.MovieGraphTimeStepData.temporal_sample_count"></a>

#### temporal_sample_count

```python
@temporal_sample_count.setter
def temporal_sample_count(value: int) -> None
```

<a id="unreal.MovieGraphTimeStepData.spatial_sample_index"></a>

#### spatial_sample_index

```python
@property
def spatial_sample_index() -> int
```

(int32):  [Read-Write] Index out of SpatialSampleCount that we're on.

<a id="unreal.MovieGraphTimeStepData.spatial_sample_index"></a>

#### spatial_sample_index

```python
@spatial_sample_index.setter
def spatial_sample_index(value: int) -> None
```

<a id="unreal.MovieGraphTimeStepData.spatial_sample_count"></a>

#### spatial_sample_count

```python
@property
def spatial_sample_count() -> int
```

(int32):  [Read-Write] The maximum number of Spatial Samples this frame is expected to be able to process.

<a id="unreal.MovieGraphTimeStepData.spatial_sample_count"></a>

#### spatial_sample_count

```python
@spatial_sample_count.setter
def spatial_sample_count(value: int) -> None
```

<a id="unreal.MovieGraphTimeStepData.is_first_temporal_sample_for_frame"></a>

#### is_first_temporal_sample_for_frame

```python
@property
def is_first_temporal_sample_for_frame() -> bool
```

(bool):  [Read-Write] Should be set to true for the first sample of each output frame. Used to determine
if various systems need to reset or gather data for a new frame. Can be true at
the same time as bIsLastTemporalSampleForFrame (ie: 1TS)

<a id="unreal.MovieGraphTimeStepData.is_first_temporal_sample_for_frame"></a>

#### is_first_temporal_sample_for_frame

```python
@is_first_temporal_sample_for_frame.setter
def is_first_temporal_sample_for_frame(value: bool) -> None
```

<a id="unreal.MovieGraphTimeStepData.is_last_temporal_sample_for_frame"></a>

#### is_last_temporal_sample_for_frame

```python
@property
def is_last_temporal_sample_for_frame() -> bool
```

(bool):  [Read-Write] Should be set to true for the last sample of each output frame. Can be true at
the same time as bIsFirstTemporalSampleForFrame (ie: 1TS)

<a id="unreal.MovieGraphTimeStepData.is_last_temporal_sample_for_frame"></a>

#### is_last_temporal_sample_for_frame

```python
@is_last_temporal_sample_for_frame.setter
def is_last_temporal_sample_for_frame(value: bool) -> None
```

<a id="unreal.MovieGraphTimeStepData.discard_output"></a>

#### discard_output

```python
@property
def discard_output() -> bool
```

(bool):  [Read-Write] Should the rendered result be discarded after a render? This will skip any
accumulators or readback and is used for frames that are only produced to
warm up the renderer.

<a id="unreal.MovieGraphTimeStepData.discard_output"></a>

#### discard_output

```python
@discard_output.setter
def discard_output(value: bool) -> None
```

<a id="unreal.MovieGraphTimeStepData.requires_accumulator"></a>

#### requires_accumulator

```python
@property
def requires_accumulator() -> bool
```

(bool):  [Read-Write] Should be set to true for every sample if there is more than one temporal sample
making up this render. This will cause the renderer to allocate accumulators
to store the multi-frame data into.

<a id="unreal.MovieGraphTimeStepData.requires_accumulator"></a>

#### requires_accumulator

```python
@requires_accumulator.setter
def requires_accumulator(value: bool) -> None
```

<a id="unreal.MovieGraphTimeStepData.evaluated_config"></a>

#### evaluated_config

```python
@property
def evaluated_config() -> MovieGraphEvaluatedConfig
```

(MovieGraphEvaluatedConfig):  [Read-Write] The evaluated config holds the configuration used for this given frame. This pointer
can potentially change each frame (if the graph for that frame is different) but
users can rely on the EvaluatedConfig being correct for a given frame, thus all
resolves (such as filenames) should use the config for that frame, not the latest
one available.

<a id="unreal.MovieGraphTimeStepData.evaluated_config"></a>

#### evaluated_config

```python
@evaluated_config.setter
def evaluated_config(value: MovieGraphEvaluatedConfig) -> None
```

<a id="unreal.MovieGraphTimeStepData.root_time_code"></a>

#### root_time_code

```python
@property
def root_time_code() -> Timecode
```

(Timecode):  [Read-Write] The current timecode at the root (sequence) level. Note that this is adjusted according to the timecode settings on the Global Output Settings node.

<a id="unreal.MovieGraphTimeStepData.root_time_code"></a>

#### root_time_code

```python
@root_time_code.setter
def root_time_code(value: Timecode) -> None
```

<a id="unreal.MovieGraphTimeStepData.root_frame_number"></a>

#### root_frame_number

```python
@property
def root_frame_number() -> FrameNumber
```

(FrameNumber):  [Read-Write] * The current frame number at the root (sequence) level.
* This is the same number as what is shown in sequencer when viewing the sequence.

<a id="unreal.MovieGraphTimeStepData.root_frame_number"></a>

#### root_frame_number

```python
@root_frame_number.setter
def root_frame_number(value: FrameNumber) -> None
```

<a id="unreal.MovieGraphTimeStepData.shot_time_code"></a>

#### shot_time_code

```python
@property
def shot_time_code() -> Timecode
```

(Timecode):  [Read-Write] The current timecode at the shot level. Note that this is adjusted according to the timecode settings on the Global Output Settings node.

<a id="unreal.MovieGraphTimeStepData.shot_time_code"></a>

#### shot_time_code

```python
@shot_time_code.setter
def shot_time_code(value: Timecode) -> None
```

<a id="unreal.MovieGraphTimeStepData.shot_frame_number"></a>

#### shot_frame_number

```python
@property
def shot_frame_number() -> FrameNumber
```

(FrameNumber):  [Read-Write] * The current frame number at the shot level.
* This is the same number as what is shown in sequencer when viewing the shot.

<a id="unreal.MovieGraphTimeStepData.shot_frame_number"></a>

#### shot_frame_number

```python
@shot_frame_number.setter
def shot_frame_number(value: FrameNumber) -> None
```

<a id="unreal.MovieGraphImagePreviewData"></a>