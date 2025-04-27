## MoviePipelineOutputSetting Objects

```python
class MoviePipelineOutputSetting(MoviePipelineSetting)
```

Movie Pipeline Output Setting

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MoviePipelineOutputSetting.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_version`` (bool):  [Read-Write] If true, version tokens will automatically be incremented with each local render. If false, the custom version number below will be used.
- ``custom_end_frame`` (int32):  [Read-Write] Used when overriding the playback range. In Display Rate frames. If bUseCustomPlaybackRange is false range will come from Sequence.
- ``custom_start_frame`` (int32):  [Read-Write] Used when overriding the playback range. In Display Rate frames. If bUseCustomPlaybackRange is false range will come from Sequence.
- ``file_name_format`` (str):  [Read-Write] What format string should the final files use? Can include folder prefixes, and format string ({shot_name}, etc.)
- ``flush_disk_writes_per_shot`` (bool):  [Read-Write] If true, the game thread will stall at the end of each shot to flush the rendering queue, and then flush any outstanding writes to disk, finalizing any
  outstanding videos and generally completing the work. This is intentionally not exposed to the user interface as it is only relevant for scripting where
  scripts may do post-shot callback work.
- ``frame_number_offset`` (int32):  [Read-Write] How many frames should we offset the output frame number by? This is useful when using handle frames on Sequences that start at frame 0,
  as the output would start in negative numbers. This can be used to offset by a fixed amount to ensure there's no negative numbers.
- ``handle_frame_count`` (int32):  [Read-Write] Top level shot track sections will automatically be expanded by this many frames in both directions, and the resulting
  additional time will be rendered as part of that shot. The inner sequence should have sections long enough to cover
  this expanded range, otherwise these tracks will not evaluate during handle frames and may produce unexpected results.
  This can be used to generate handle frames for traditional non linear editing tools.
- ``output_directory`` (DirectoryPath):  [Read-Write] What directory should all of our output files be relative to.
- ``output_frame_rate`` (FrameRate):  [Read-Write] What frame rate should the output files be exported at? This overrides the Display Rate of the target sequence.
- ``output_frame_step`` (int32):  [Read-Write] Render every Nth frame. ie: Setting this value to 2 renders every other frame. Game Thread is still evaluated on 'skipped' frames for accuracy between renders of different OutputFrameSteps.
- ``output_resolution`` (IntPoint):  [Read-Write] What resolution should our output files be exported at?
- ``override_existing_output`` (bool):  [Read-Write] If true, output containers should attempt to override any existing files with the same name.
- ``use_custom_frame_rate`` (bool):  [Read-Write] Should we use the custom frame rate specified by OutputFrameRate? Otherwise defaults to Sequence frame rate.
- ``use_custom_playback_range`` (bool):  [Read-Write] If true, override the Playback Range start/end bounds with the bounds specified below.
- ``version_number`` (int32):  [Read-Write] The value to use for the version token if versions are not automatically incremented.
- ``zero_pad_frame_numbers`` (int32):  [Read-Write] How many digits should all output frame numbers be padded to? MySequence_1.png -> MySequence_0001.png. Useful for software that struggles to recognize frame ranges when non-padded.

<a id="unreal.MoviePipelineOutputSetting.output_directory"></a>

#### output_directory

```python
@property
def output_directory() -> DirectoryPath
```

(DirectoryPath):  [Read-Write] What directory should all of our output files be relative to.

<a id="unreal.MoviePipelineOutputSetting.output_directory"></a>

#### output_directory

```python
@output_directory.setter
def output_directory(value: DirectoryPath) -> None
```

<a id="unreal.MoviePipelineOutputSetting.file_name_format"></a>

#### file_name_format

```python
@property
def file_name_format() -> str
```

(str):  [Read-Write] What format string should the final files use? Can include folder prefixes, and format string ({shot_name}, etc.)

<a id="unreal.MoviePipelineOutputSetting.file_name_format"></a>

#### file_name_format

```python
@file_name_format.setter
def file_name_format(value: str) -> None
```

<a id="unreal.MoviePipelineOutputSetting.output_resolution"></a>

#### output_resolution

```python
@property
def output_resolution() -> IntPoint
```

(IntPoint):  [Read-Write] What resolution should our output files be exported at?

<a id="unreal.MoviePipelineOutputSetting.output_resolution"></a>

#### output_resolution

```python
@output_resolution.setter
def output_resolution(value: IntPoint) -> None
```

<a id="unreal.MoviePipelineOutputSetting.use_custom_frame_rate"></a>

#### use_custom_frame_rate

```python
@property
def use_custom_frame_rate() -> bool
```

(bool):  [Read-Write] Should we use the custom frame rate specified by OutputFrameRate? Otherwise defaults to Sequence frame rate.

<a id="unreal.MoviePipelineOutputSetting.use_custom_frame_rate"></a>

#### use_custom_frame_rate

```python
@use_custom_frame_rate.setter
def use_custom_frame_rate(value: bool) -> None
```

<a id="unreal.MoviePipelineOutputSetting.output_frame_rate"></a>

#### output_frame_rate

```python
@property
def output_frame_rate() -> FrameRate
```

(FrameRate):  [Read-Write] What frame rate should the output files be exported at? This overrides the Display Rate of the target sequence.

<a id="unreal.MoviePipelineOutputSetting.output_frame_rate"></a>

#### output_frame_rate

```python
@output_frame_rate.setter
def output_frame_rate(value: FrameRate) -> None
```

<a id="unreal.MoviePipelineOutputSetting.override_existing_output"></a>

#### override_existing_output

```python
@property
def override_existing_output() -> bool
```

(bool):  [Read-Write] If true, output containers should attempt to override any existing files with the same name.

<a id="unreal.MoviePipelineOutputSetting.override_existing_output"></a>

#### override_existing_output

```python
@override_existing_output.setter
def override_existing_output(value: bool) -> None
```

<a id="unreal.MoviePipelineOutputSetting.handle_frame_count"></a>

#### handle_frame_count

```python
@property
def handle_frame_count() -> int
```

(int32):  [Read-Write] Top level shot track sections will automatically be expanded by this many frames in both directions, and the resulting
additional time will be rendered as part of that shot. The inner sequence should have sections long enough to cover
this expanded range, otherwise these tracks will not evaluate during handle frames and may produce unexpected results.
This can be used to generate handle frames for traditional non linear editing tools.

<a id="unreal.MoviePipelineOutputSetting.handle_frame_count"></a>

#### handle_frame_count

```python
@handle_frame_count.setter
def handle_frame_count(value: int) -> None
```

<a id="unreal.MoviePipelineOutputSetting.output_frame_step"></a>

#### output_frame_step

```python
@property
def output_frame_step() -> int
```

(int32):  [Read-Write] Render every Nth frame. ie: Setting this value to 2 renders every other frame. Game Thread is still evaluated on 'skipped' frames for accuracy between renders of different OutputFrameSteps.

<a id="unreal.MoviePipelineOutputSetting.output_frame_step"></a>

#### output_frame_step

```python
@output_frame_step.setter
def output_frame_step(value: int) -> None
```

<a id="unreal.MoviePipelineOutputSetting.use_custom_playback_range"></a>

#### use_custom_playback_range

```python
@property
def use_custom_playback_range() -> bool
```

(bool):  [Read-Write] If true, override the Playback Range start/end bounds with the bounds specified below.

<a id="unreal.MoviePipelineOutputSetting.use_custom_playback_range"></a>

#### use_custom_playback_range

```python
@use_custom_playback_range.setter
def use_custom_playback_range(value: bool) -> None
```

<a id="unreal.MoviePipelineOutputSetting.custom_start_frame"></a>

#### custom_start_frame

```python
@property
def custom_start_frame() -> int
```

(int32):  [Read-Write] Used when overriding the playback range. In Display Rate frames. If bUseCustomPlaybackRange is false range will come from Sequence.

<a id="unreal.MoviePipelineOutputSetting.custom_start_frame"></a>

#### custom_start_frame

```python
@custom_start_frame.setter
def custom_start_frame(value: int) -> None
```

<a id="unreal.MoviePipelineOutputSetting.custom_end_frame"></a>

#### custom_end_frame

```python
@property
def custom_end_frame() -> int
```

(int32):  [Read-Write] Used when overriding the playback range. In Display Rate frames. If bUseCustomPlaybackRange is false range will come from Sequence.

<a id="unreal.MoviePipelineOutputSetting.custom_end_frame"></a>

#### custom_end_frame

```python
@custom_end_frame.setter
def custom_end_frame(value: int) -> None
```

<a id="unreal.MoviePipelineOutputSetting.version_number"></a>

#### version_number

```python
@property
def version_number() -> int
```

(int32):  [Read-Write] The value to use for the version token if versions are not automatically incremented.

<a id="unreal.MoviePipelineOutputSetting.version_number"></a>

#### version_number

```python
@version_number.setter
def version_number(value: int) -> None
```

<a id="unreal.MoviePipelineOutputSetting.auto_version"></a>

#### auto_version

```python
@property
def auto_version() -> bool
```

(bool):  [Read-Write] If true, version tokens will automatically be incremented with each local render. If false, the custom version number below will be used.

<a id="unreal.MoviePipelineOutputSetting.auto_version"></a>

#### auto_version

```python
@auto_version.setter
def auto_version(value: bool) -> None
```

<a id="unreal.MoviePipelineOutputSetting.zero_pad_frame_numbers"></a>

#### zero_pad_frame_numbers

```python
@property
def zero_pad_frame_numbers() -> int
```

(int32):  [Read-Write] How many digits should all output frame numbers be padded to? MySequence_1.png -> MySequence_0001.png. Useful for software that struggles to recognize frame ranges when non-padded.

<a id="unreal.MoviePipelineOutputSetting.zero_pad_frame_numbers"></a>

#### zero_pad_frame_numbers

```python
@zero_pad_frame_numbers.setter
def zero_pad_frame_numbers(value: int) -> None
```

<a id="unreal.MoviePipelineOutputSetting.frame_number_offset"></a>

#### frame_number_offset

```python
@property
def frame_number_offset() -> int
```

(int32):  [Read-Write] How many frames should we offset the output frame number by? This is useful when using handle frames on Sequences that start at frame 0,
as the output would start in negative numbers. This can be used to offset by a fixed amount to ensure there's no negative numbers.

<a id="unreal.MoviePipelineOutputSetting.frame_number_offset"></a>

#### frame_number_offset

```python
@frame_number_offset.setter
def frame_number_offset(value: int) -> None
```

<a id="unreal.MoviePipelineOutputSetting.flush_disk_writes_per_shot"></a>

#### flush_disk_writes_per_shot

```python
@property
def flush_disk_writes_per_shot() -> bool
```

(bool):  [Read-Write] If true, the game thread will stall at the end of each shot to flush the rendering queue, and then flush any outstanding writes to disk, finalizing any
outstanding videos and generally completing the work. This is intentionally not exposed to the user interface as it is only relevant for scripting where
scripts may do post-shot callback work.

<a id="unreal.MoviePipelineOutputSetting.flush_disk_writes_per_shot"></a>

#### flush_disk_writes_per_shot

```python
@flush_disk_writes_per_shot.setter
def flush_disk_writes_per_shot(value: bool) -> None
```

<a id="unreal.MoviePipelinePrimaryConfig"></a>