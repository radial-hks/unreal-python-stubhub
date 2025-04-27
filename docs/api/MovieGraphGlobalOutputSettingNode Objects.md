## MovieGraphGlobalOutputSettingNode Objects

```python
class MovieGraphGlobalOutputSettingNode(MovieGraphSettingNode)
```

Movie Graph Global Output Setting Node

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphGlobalOutputSettingNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``custom_playback_range_end_frame`` (int32):  [Read-Write]
- ``custom_playback_range_start_frame`` (int32):  [Read-Write]
- ``custom_timecode_start`` (Timecode):  [Read-Write] Start the timecode at a specific value, rather than the value coming from the Level Sequence. Only applicable to output formats that support timecode.
- ``drop_frame_timecode`` (bool):  [Read-Write] Whether the embedded timecode track should be written using drop-frame format. Only applicable to output formats that support timecode, and when the sequence framerate is 29.97.
- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``flush_disk_writes_per_shot`` (bool):  [Read-Write] If true, the game thread will stall at the end of each shot to flush the rendering queue, and then flush any outstanding writes to disk, finalizing any
  outstanding videos and generally completing the work. This is only relevant for scripting where scripts may do post-shot callback work.
- ``frame_number_offset`` (int32):  [Read-Write] How many frames should we offset the output frame number by? This is useful when using handle frames on Sequences that start at frame 0,
  as the output would start in negative numbers. This can be used to offset by a fixed amount to ensure there's no negative numbers.
- ``handle_frame_count`` (int32):  [Read-Write] Top level shot track sections will automatically be expanded by this many frames in both directions, and the resulting
  additional time will be rendered as part of that shot. The inner sequence should have sections long enough to cover
  this expanded range, otherwise these tracks will not evaluate during handle frames and may produce unexpected results.
  This can be used to generate handle frames for traditional non linear editing tools.
- ``output_directory`` (DirectoryPath):  [Read-Write] What directory should all of our output files be relative to.
- ``output_frame_rate`` (FrameRate):  [Read-Write] What frame rate should the output files be exported at? This overrides the Display Rate of the target sequence. If not overwritten, uses the default Sequence Display Rate.
- ``output_resolution`` (MovieGraphNamedResolution):  [Read-Write] What resolution should our output files be exported at?
- ``override_b_drop_frame_timecode`` (bool):  [Read-Write]
- ``override_b_flush_disk_writes_per_shot`` (bool):  [Read-Write]
- ``override_b_overwrite_existing_output`` (bool):  [Read-Write]
- ``override_custom_playback_range_end_frame`` (bool):  [Read-Write]
- ``override_custom_playback_range_start_frame`` (bool):  [Read-Write]
- ``override_custom_timecode_start`` (bool):  [Read-Write]
- ``override_frame_number_offset`` (bool):  [Read-Write]
- ``override_handle_frame_count`` (bool):  [Read-Write]
- ``override_output_directory`` (bool):  [Read-Write]
- ``override_output_frame_rate`` (bool):  [Read-Write]
- ``override_output_resolution`` (bool):  [Read-Write]
- ``override_versioning_settings`` (bool):  [Read-Write]
- ``override_zero_pad_frame_numbers`` (bool):  [Read-Write]
- ``overwrite_existing_output`` (bool):  [Read-Write] If true, output containers should attempt to override any existing files with the same name.
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.
- ``versioning_settings`` (MovieGraphVersioningSettings):  [Read-Write] Determines how versioning should be handled (Auto Version, Version Number, etc.).
- ``zero_pad_frame_numbers`` (int32):  [Read-Write] How many digits should all output frame numbers be padded to? MySequence_1.png -> MySequence_0001.png. Useful for software that struggles to recognize frame ranges when non-padded.

<a id="unreal.MovieGraphGlobalOutputSettingNode.override_output_directory"></a>

#### override_output_directory

```python
@property
def override_output_directory() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphGlobalOutputSettingNode.override_output_directory"></a>

#### override_output_directory

```python
@override_output_directory.setter
def override_output_directory(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalOutputSettingNode.override_output_resolution"></a>

#### override_output_resolution

```python
@property
def override_output_resolution() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphGlobalOutputSettingNode.override_output_resolution"></a>

#### override_output_resolution

```python
@override_output_resolution.setter
def override_output_resolution(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalOutputSettingNode.override_output_frame_rate"></a>

#### override_output_frame_rate

```python
@property
def override_output_frame_rate() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphGlobalOutputSettingNode.override_output_frame_rate"></a>

#### override_output_frame_rate

```python
@override_output_frame_rate.setter
def override_output_frame_rate(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalOutputSettingNode.override_b_overwrite_existing_output"></a>

#### override_b_overwrite_existing_output

```python
@property
def override_b_overwrite_existing_output() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphGlobalOutputSettingNode.override_b_overwrite_existing_output"></a>

#### override_b_overwrite_existing_output

```python
@override_b_overwrite_existing_output.setter
def override_b_overwrite_existing_output(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalOutputSettingNode.override_zero_pad_frame_numbers"></a>

#### override_zero_pad_frame_numbers

```python
@property
def override_zero_pad_frame_numbers() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphGlobalOutputSettingNode.override_zero_pad_frame_numbers"></a>

#### override_zero_pad_frame_numbers

```python
@override_zero_pad_frame_numbers.setter
def override_zero_pad_frame_numbers(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalOutputSettingNode.override_frame_number_offset"></a>

#### override_frame_number_offset

```python
@property
def override_frame_number_offset() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphGlobalOutputSettingNode.override_frame_number_offset"></a>

#### override_frame_number_offset

```python
@override_frame_number_offset.setter
def override_frame_number_offset(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalOutputSettingNode.override_handle_frame_count"></a>

#### override_handle_frame_count

```python
@property
def override_handle_frame_count() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphGlobalOutputSettingNode.override_handle_frame_count"></a>

#### override_handle_frame_count

```python
@override_handle_frame_count.setter
def override_handle_frame_count(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalOutputSettingNode.override_custom_playback_range_start_frame"></a>

#### override_custom_playback_range_start_frame

```python
@property
def override_custom_playback_range_start_frame() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphGlobalOutputSettingNode.override_custom_playback_range_start_frame"></a>

#### override_custom_playback_range_start_frame

```python
@override_custom_playback_range_start_frame.setter
def override_custom_playback_range_start_frame(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalOutputSettingNode.override_custom_playback_range_end_frame"></a>

#### override_custom_playback_range_end_frame

```python
@property
def override_custom_playback_range_end_frame() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphGlobalOutputSettingNode.override_custom_playback_range_end_frame"></a>

#### override_custom_playback_range_end_frame

```python
@override_custom_playback_range_end_frame.setter
def override_custom_playback_range_end_frame(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalOutputSettingNode.override_custom_timecode_start"></a>

#### override_custom_timecode_start

```python
@property
def override_custom_timecode_start() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphGlobalOutputSettingNode.override_custom_timecode_start"></a>

#### override_custom_timecode_start

```python
@override_custom_timecode_start.setter
def override_custom_timecode_start(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalOutputSettingNode.override_b_drop_frame_timecode"></a>

#### override_b_drop_frame_timecode

```python
@property
def override_b_drop_frame_timecode() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphGlobalOutputSettingNode.override_b_drop_frame_timecode"></a>

#### override_b_drop_frame_timecode

```python
@override_b_drop_frame_timecode.setter
def override_b_drop_frame_timecode(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalOutputSettingNode.override_versioning_settings"></a>

#### override_versioning_settings

```python
@property
def override_versioning_settings() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphGlobalOutputSettingNode.override_versioning_settings"></a>

#### override_versioning_settings

```python
@override_versioning_settings.setter
def override_versioning_settings(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalOutputSettingNode.override_b_flush_disk_writes_per_shot"></a>

#### override_b_flush_disk_writes_per_shot

```python
@property
def override_b_flush_disk_writes_per_shot() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphGlobalOutputSettingNode.override_b_flush_disk_writes_per_shot"></a>

#### override_b_flush_disk_writes_per_shot

```python
@override_b_flush_disk_writes_per_shot.setter
def override_b_flush_disk_writes_per_shot(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalOutputSettingNode.output_directory"></a>

#### output_directory

```python
@property
def output_directory() -> DirectoryPath
```

(DirectoryPath):  [Read-Write] What directory should all of our output files be relative to.

<a id="unreal.MovieGraphGlobalOutputSettingNode.output_directory"></a>

#### output_directory

```python
@output_directory.setter
def output_directory(value: DirectoryPath) -> None
```

<a id="unreal.MovieGraphGlobalOutputSettingNode.output_resolution"></a>

#### output_resolution

```python
@property
def output_resolution() -> MovieGraphNamedResolution
```

(MovieGraphNamedResolution):  [Read-Write] What resolution should our output files be exported at?

<a id="unreal.MovieGraphGlobalOutputSettingNode.output_resolution"></a>

#### output_resolution

```python
@output_resolution.setter
def output_resolution(value: MovieGraphNamedResolution) -> None
```

<a id="unreal.MovieGraphGlobalOutputSettingNode.output_frame_rate"></a>

#### output_frame_rate

```python
@property
def output_frame_rate() -> FrameRate
```

(FrameRate):  [Read-Write] What frame rate should the output files be exported at? This overrides the Display Rate of the target sequence. If not overwritten, uses the default Sequence Display Rate.

<a id="unreal.MovieGraphGlobalOutputSettingNode.output_frame_rate"></a>

#### output_frame_rate

```python
@output_frame_rate.setter
def output_frame_rate(value: FrameRate) -> None
```

<a id="unreal.MovieGraphGlobalOutputSettingNode.overwrite_existing_output"></a>

#### overwrite_existing_output

```python
@property
def overwrite_existing_output() -> bool
```

(bool):  [Read-Write] If true, output containers should attempt to override any existing files with the same name.

<a id="unreal.MovieGraphGlobalOutputSettingNode.overwrite_existing_output"></a>

#### overwrite_existing_output

```python
@overwrite_existing_output.setter
def overwrite_existing_output(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalOutputSettingNode.zero_pad_frame_numbers"></a>

#### zero_pad_frame_numbers

```python
@property
def zero_pad_frame_numbers() -> int
```

(int32):  [Read-Write] How many digits should all output frame numbers be padded to? MySequence_1.png -> MySequence_0001.png. Useful for software that struggles to recognize frame ranges when non-padded.

<a id="unreal.MovieGraphGlobalOutputSettingNode.zero_pad_frame_numbers"></a>

#### zero_pad_frame_numbers

```python
@zero_pad_frame_numbers.setter
def zero_pad_frame_numbers(value: int) -> None
```

<a id="unreal.MovieGraphGlobalOutputSettingNode.frame_number_offset"></a>

#### frame_number_offset

```python
@property
def frame_number_offset() -> int
```

(int32):  [Read-Write] How many frames should we offset the output frame number by? This is useful when using handle frames on Sequences that start at frame 0,
as the output would start in negative numbers. This can be used to offset by a fixed amount to ensure there's no negative numbers.

<a id="unreal.MovieGraphGlobalOutputSettingNode.frame_number_offset"></a>

#### frame_number_offset

```python
@frame_number_offset.setter
def frame_number_offset(value: int) -> None
```

<a id="unreal.MovieGraphGlobalOutputSettingNode.handle_frame_count"></a>

#### handle_frame_count

```python
@property
def handle_frame_count() -> int
```

(int32):  [Read-Write] Top level shot track sections will automatically be expanded by this many frames in both directions, and the resulting
additional time will be rendered as part of that shot. The inner sequence should have sections long enough to cover
this expanded range, otherwise these tracks will not evaluate during handle frames and may produce unexpected results.
This can be used to generate handle frames for traditional non linear editing tools.

<a id="unreal.MovieGraphGlobalOutputSettingNode.handle_frame_count"></a>

#### handle_frame_count

```python
@handle_frame_count.setter
def handle_frame_count(value: int) -> None
```

<a id="unreal.MovieGraphGlobalOutputSettingNode.custom_playback_range_start_frame"></a>

#### custom_playback_range_start_frame

```python
@property
def custom_playback_range_start_frame() -> int
```

(int32):  [Read-Write]

<a id="unreal.MovieGraphGlobalOutputSettingNode.custom_playback_range_start_frame"></a>

#### custom_playback_range_start_frame

```python
@custom_playback_range_start_frame.setter
def custom_playback_range_start_frame(value: int) -> None
```

<a id="unreal.MovieGraphGlobalOutputSettingNode.custom_playback_range_end_frame"></a>

#### custom_playback_range_end_frame

```python
@property
def custom_playback_range_end_frame() -> int
```

(int32):  [Read-Write]

<a id="unreal.MovieGraphGlobalOutputSettingNode.custom_playback_range_end_frame"></a>

#### custom_playback_range_end_frame

```python
@custom_playback_range_end_frame.setter
def custom_playback_range_end_frame(value: int) -> None
```

<a id="unreal.MovieGraphGlobalOutputSettingNode.custom_timecode_start"></a>

#### custom_timecode_start

```python
@property
def custom_timecode_start() -> Timecode
```

(Timecode):  [Read-Write] Start the timecode at a specific value, rather than the value coming from the Level Sequence. Only applicable to output formats that support timecode.

<a id="unreal.MovieGraphGlobalOutputSettingNode.custom_timecode_start"></a>

#### custom_timecode_start

```python
@custom_timecode_start.setter
def custom_timecode_start(value: Timecode) -> None
```

<a id="unreal.MovieGraphGlobalOutputSettingNode.drop_frame_timecode"></a>

#### drop_frame_timecode

```python
@property
def drop_frame_timecode() -> bool
```

(bool):  [Read-Write] Whether the embedded timecode track should be written using drop-frame format. Only applicable to output formats that support timecode, and when the sequence framerate is 29.97.

<a id="unreal.MovieGraphGlobalOutputSettingNode.drop_frame_timecode"></a>

#### drop_frame_timecode

```python
@drop_frame_timecode.setter
def drop_frame_timecode(value: bool) -> None
```

<a id="unreal.MovieGraphGlobalOutputSettingNode.versioning_settings"></a>

#### versioning_settings

```python
@property
def versioning_settings() -> MovieGraphVersioningSettings
```

(MovieGraphVersioningSettings):  [Read-Write] Determines how versioning should be handled (Auto Version, Version Number, etc.).

<a id="unreal.MovieGraphGlobalOutputSettingNode.versioning_settings"></a>

#### versioning_settings

```python
@versioning_settings.setter
def versioning_settings(value: MovieGraphVersioningSettings) -> None
```

<a id="unreal.MovieGraphGlobalOutputSettingNode.flush_disk_writes_per_shot"></a>

#### flush_disk_writes_per_shot

```python
@property
def flush_disk_writes_per_shot() -> bool
```

(bool):  [Read-Write] If true, the game thread will stall at the end of each shot to flush the rendering queue, and then flush any outstanding writes to disk, finalizing any
outstanding videos and generally completing the work. This is only relevant for scripting where scripts may do post-shot callback work.

<a id="unreal.MovieGraphGlobalOutputSettingNode.flush_disk_writes_per_shot"></a>

#### flush_disk_writes_per_shot

```python
@flush_disk_writes_per_shot.setter
def flush_disk_writes_per_shot(value: bool) -> None
```

<a id="unreal.MovieGraphOutputSettingNode"></a>