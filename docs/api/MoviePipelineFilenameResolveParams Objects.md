## MoviePipelineFilenameResolveParams Objects

```python
class MoviePipelineFilenameResolveParams(StructBase)
```

Movie Pipeline Filename Resolve Params

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieRenderPipelineDataTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``additional_frame_number_offset`` (int32):  [Read-Write] Additional offset added onto the offset provided by the Output Settings in the Job. Required for some internal things (FCPXML).
- ``camera_name_override`` (str):  [Read-Write] Name used by the {camera_name} format tag. If specified, this will override the camera name (which is normally pulled from the ShotOverride object).
- ``file_metadata`` (Map[str, str]):  [Read-Write] A key/value pair that maps metadata names to their values. Output is only supported in exr formats at the moment.
- ``file_name_format_overrides`` (Map[str, str]):  [Read-Write] A map between "{format}" tokens and their values. These are applied after the auto-generated ones from the system,
  which allows the caller to override things like {.ext} depending or {render_pass} which have dummy names by default.
- ``file_name_override`` (str):  [Read-Write] Optional. If specified this is the filename that will be used instead of automatically building it from the Job's Output Setting.
- ``force_relative_frame_numbers`` (bool):  [Read-Write] If true, force format strings (like {frame_number}) to resolve using the relative version. Used when slow-mo is detected as frame numbers would overlap.
- ``frame_number`` (int32):  [Read-Write] Frame Number for the Root (matching what you see in the Sequencer timeline. ie: If the Sequence PlaybackRange starts on 50, this value would be 50 on the first frame.
- ``frame_number_rel`` (int32):  [Read-Write] Frame Number for the Root (relative to 0, not what you would see in the Sequencer timeline. ie: If sequence PlaybackRange starts on 50, this value would be 0 on the first frame.
- ``frame_number_shot`` (int32):  [Read-Write] Frame Number for the Shot (matching what you would see in Sequencer at the sub-sequence level.
- ``frame_number_shot_rel`` (int32):  [Read-Write] Frame Number for the Shot (relative to 0, not what you would see in the Sequencer timeline.
- ``initialization_time`` (DateTime):  [Read-Write] The initialization time for this job. Used to resolve time-based format arguments.
- ``initialization_time_offset`` (Timespan):  [Read-Write] What offset should be applied to InitializationTime when generating {time} related filename tokens? Likely your offset from UTC if you want local time.
- ``initialization_version`` (int32):  [Read-Write] The version for this job. Used to resolve version format arguments.
- ``job`` (MoviePipelineExecutorJob):  [Read-Write] Required. This is the job all of the settings should be pulled from.
- ``shot_name_override`` (str):  [Read-Write] Name used by the {shot_name} format tag. If specified, this will override the shot name (which is normally pulled from the ShotOverride object)
- ``shot_override`` (MoviePipelineExecutorShot):  [Read-Write] Optional. If specified, settings will be pulled from this shot (if overriden by the shot). If null, always use the root configuration in the job.
- ``zero_pad_frame_number_count`` (int32):  [Read-Write] When converitng frame numbers to strings, how many digits should we pad them up to? ie: 5 => 0005 with a count of 4.

<a id="unreal.MoviePipelineFilenameResolveParams.__init__"></a>

#### __init__

```python
def __init__(frame_number: int = 0,
             frame_number_shot: int = 0,
             frame_number_rel: int = 0,
             frame_number_shot_rel: int = 0,
             camera_name_override: str = "",
             shot_name_override: str = "",
             zero_pad_frame_number_count: int = 0,
             force_relative_frame_numbers: bool = False,
             file_name_override: str = "",
             file_name_format_overrides: Map[str, str] = {},
             file_metadata: Map[str, str] = {},
             initialization_time: DateTime = [],
             initialization_time_offset: Timespan = [0, 0, 0, 0, 0],
             initialization_version: int = 0,
             job: MoviePipelineExecutorJob = None,
             shot_override: MoviePipelineExecutorShot = None,
             additional_frame_number_offset: int = 0) -> None
```

<a id="unreal.MoviePipelineFilenameResolveParams.frame_number"></a>

#### frame_number

```python
@property
def frame_number() -> int
```

(int32):  [Read-Write] Frame Number for the Root (matching what you see in the Sequencer timeline. ie: If the Sequence PlaybackRange starts on 50, this value would be 50 on the first frame.

<a id="unreal.MoviePipelineFilenameResolveParams.frame_number"></a>

#### frame_number

```python
@frame_number.setter
def frame_number(value: int) -> None
```

<a id="unreal.MoviePipelineFilenameResolveParams.frame_number_shot"></a>

#### frame_number_shot

```python
@property
def frame_number_shot() -> int
```

(int32):  [Read-Write] Frame Number for the Shot (matching what you would see in Sequencer at the sub-sequence level.

<a id="unreal.MoviePipelineFilenameResolveParams.frame_number_shot"></a>

#### frame_number_shot

```python
@frame_number_shot.setter
def frame_number_shot(value: int) -> None
```

<a id="unreal.MoviePipelineFilenameResolveParams.frame_number_rel"></a>

#### frame_number_rel

```python
@property
def frame_number_rel() -> int
```

(int32):  [Read-Write] Frame Number for the Root (relative to 0, not what you would see in the Sequencer timeline. ie: If sequence PlaybackRange starts on 50, this value would be 0 on the first frame.

<a id="unreal.MoviePipelineFilenameResolveParams.frame_number_rel"></a>

#### frame_number_rel

```python
@frame_number_rel.setter
def frame_number_rel(value: int) -> None
```

<a id="unreal.MoviePipelineFilenameResolveParams.frame_number_shot_rel"></a>

#### frame_number_shot_rel

```python
@property
def frame_number_shot_rel() -> int
```

(int32):  [Read-Write] Frame Number for the Shot (relative to 0, not what you would see in the Sequencer timeline.

<a id="unreal.MoviePipelineFilenameResolveParams.frame_number_shot_rel"></a>

#### frame_number_shot_rel

```python
@frame_number_shot_rel.setter
def frame_number_shot_rel(value: int) -> None
```

<a id="unreal.MoviePipelineFilenameResolveParams.camera_name_override"></a>

#### camera_name_override

```python
@property
def camera_name_override() -> str
```

(str):  [Read-Write] Name used by the {camera_name} format tag. If specified, this will override the camera name (which is normally pulled from the ShotOverride object).

<a id="unreal.MoviePipelineFilenameResolveParams.camera_name_override"></a>

#### camera_name_override

```python
@camera_name_override.setter
def camera_name_override(value: str) -> None
```

<a id="unreal.MoviePipelineFilenameResolveParams.shot_name_override"></a>

#### shot_name_override

```python
@property
def shot_name_override() -> str
```

(str):  [Read-Write] Name used by the {shot_name} format tag. If specified, this will override the shot name (which is normally pulled from the ShotOverride object)

<a id="unreal.MoviePipelineFilenameResolveParams.shot_name_override"></a>

#### shot_name_override

```python
@shot_name_override.setter
def shot_name_override(value: str) -> None
```

<a id="unreal.MoviePipelineFilenameResolveParams.zero_pad_frame_number_count"></a>

#### zero_pad_frame_number_count

```python
@property
def zero_pad_frame_number_count() -> int
```

(int32):  [Read-Write] When converitng frame numbers to strings, how many digits should we pad them up to? ie: 5 => 0005 with a count of 4.

<a id="unreal.MoviePipelineFilenameResolveParams.zero_pad_frame_number_count"></a>

#### zero_pad_frame_number_count

```python
@zero_pad_frame_number_count.setter
def zero_pad_frame_number_count(value: int) -> None
```

<a id="unreal.MoviePipelineFilenameResolveParams.force_relative_frame_numbers"></a>

#### force_relative_frame_numbers

```python
@property
def force_relative_frame_numbers() -> bool
```

(bool):  [Read-Write] If true, force format strings (like {frame_number}) to resolve using the relative version. Used when slow-mo is detected as frame numbers would overlap.

<a id="unreal.MoviePipelineFilenameResolveParams.force_relative_frame_numbers"></a>

#### force_relative_frame_numbers

```python
@force_relative_frame_numbers.setter
def force_relative_frame_numbers(value: bool) -> None
```

<a id="unreal.MoviePipelineFilenameResolveParams.file_name_override"></a>

#### file_name_override

```python
@property
def file_name_override() -> str
```

(str):  [Read-Write] Optional. If specified this is the filename that will be used instead of automatically building it from the Job's Output Setting.

<a id="unreal.MoviePipelineFilenameResolveParams.file_name_override"></a>

#### file_name_override

```python
@file_name_override.setter
def file_name_override(value: str) -> None
```

<a id="unreal.MoviePipelineFilenameResolveParams.file_name_format_overrides"></a>

#### file_name_format_overrides

```python
@property
def file_name_format_overrides() -> Map[str, str]
```

(Map[str, str]):  [Read-Write] A map between "{format}" tokens and their values. These are applied after the auto-generated ones from the system,
which allows the caller to override things like {.ext} depending or {render_pass} which have dummy names by default.

<a id="unreal.MoviePipelineFilenameResolveParams.file_name_format_overrides"></a>

#### file_name_format_overrides

```python
@file_name_format_overrides.setter
def file_name_format_overrides(value: Map[str, str]) -> None
```

<a id="unreal.MoviePipelineFilenameResolveParams.file_metadata"></a>

#### file_metadata

```python
@property
def file_metadata() -> Map[str, str]
```

(Map[str, str]):  [Read-Write] A key/value pair that maps metadata names to their values. Output is only supported in exr formats at the moment.

<a id="unreal.MoviePipelineFilenameResolveParams.file_metadata"></a>

#### file_metadata

```python
@file_metadata.setter
def file_metadata(value: Map[str, str]) -> None
```

<a id="unreal.MoviePipelineFilenameResolveParams.initialization_time"></a>

#### initialization_time

```python
@property
def initialization_time() -> DateTime
```

(DateTime):  [Read-Write] The initialization time for this job. Used to resolve time-based format arguments.

<a id="unreal.MoviePipelineFilenameResolveParams.initialization_time"></a>

#### initialization_time

```python
@initialization_time.setter
def initialization_time(value: DateTime) -> None
```

<a id="unreal.MoviePipelineFilenameResolveParams.initialization_time_offset"></a>

#### initialization_time_offset

```python
@property
def initialization_time_offset() -> Timespan
```

(Timespan):  [Read-Write] What offset should be applied to InitializationTime when generating {time} related filename tokens? Likely your offset from UTC if you want local time.

<a id="unreal.MoviePipelineFilenameResolveParams.initialization_time_offset"></a>

#### initialization_time_offset

```python
@initialization_time_offset.setter
def initialization_time_offset(value: Timespan) -> None
```

<a id="unreal.MoviePipelineFilenameResolveParams.initialization_version"></a>

#### initialization_version

```python
@property
def initialization_version() -> int
```

(int32):  [Read-Write] The version for this job. Used to resolve version format arguments.

<a id="unreal.MoviePipelineFilenameResolveParams.initialization_version"></a>

#### initialization_version

```python
@initialization_version.setter
def initialization_version(value: int) -> None
```

<a id="unreal.MoviePipelineFilenameResolveParams.job"></a>

#### job

```python
@property
def job() -> MoviePipelineExecutorJob
```

(MoviePipelineExecutorJob):  [Read-Write] Required. This is the job all of the settings should be pulled from.

<a id="unreal.MoviePipelineFilenameResolveParams.job"></a>

#### job

```python
@job.setter
def job(value: MoviePipelineExecutorJob) -> None
```

<a id="unreal.MoviePipelineFilenameResolveParams.shot_override"></a>

#### shot_override

```python
@property
def shot_override() -> MoviePipelineExecutorShot
```

(MoviePipelineExecutorShot):  [Read-Write] Optional. If specified, settings will be pulled from this shot (if overriden by the shot). If null, always use the root configuration in the job.

<a id="unreal.MoviePipelineFilenameResolveParams.shot_override"></a>

#### shot_override

```python
@shot_override.setter
def shot_override(value: MoviePipelineExecutorShot) -> None
```

<a id="unreal.MoviePipelineFilenameResolveParams.additional_frame_number_offset"></a>

#### additional_frame_number_offset

```python
@property
def additional_frame_number_offset() -> int
```

(int32):  [Read-Write] Additional offset added onto the offset provided by the Output Settings in the Job. Required for some internal things (FCPXML).

<a id="unreal.MoviePipelineFilenameResolveParams.additional_frame_number_offset"></a>

#### additional_frame_number_offset

```python
@additional_frame_number_offset.setter
def additional_frame_number_offset(value: int) -> None
```

<a id="unreal.AvaMRQRundownPage"></a>