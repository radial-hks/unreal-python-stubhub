## MoviePipelineCommandLineEncoder Objects

```python
class MoviePipelineCommandLineEncoder(MoviePipelineSetting)
```

Movie Pipeline Command Line Encoder

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MoviePipelineCommandLineEncoder.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``additional_command_line_args`` (str):  [Read-Write] Any additional arguments to pass to the CLI encode for this particular job.
- ``delete_source_files`` (bool):  [Read-Write] Should we delete the source files from disk after encoding?
- ``file_name_format_override`` (str):  [Read-Write] File name format string override. If specified it will override the FileNameFormat from the Output setting.
  If {shot_name} or {camera_name} is used, encoding will begin after each shot finishes rendering.
  Can be different from the main one in the Output setting so you can render out frames to individual
  shot folders but encode to one file.
- ``quality`` (MoviePipelineEncodeQuality):  [Read-Write] What encoding quality to use for this job? Exact command line arguments for each one are specified in Project Settings.
- ``skip_encode_on_render_canceled`` (bool):  [Read-Write] If a render was canceled (via hitting escape mid render) should we skip trying to encode the files we did produce?
- ``write_each_frame_duration`` (bool):  [Read-Write] Write the duration for each frame into the generated text file. Needed for some input types on some CLI encoding software.

<a id="unreal.MoviePipelineCommandLineEncoder.file_name_format_override"></a>

#### file_name_format_override

```python
@property
def file_name_format_override() -> str
```

(str):  [Read-Write] File name format string override. If specified it will override the FileNameFormat from the Output setting.
If {shot_name} or {camera_name} is used, encoding will begin after each shot finishes rendering.
Can be different from the main one in the Output setting so you can render out frames to individual
shot folders but encode to one file.

<a id="unreal.MoviePipelineCommandLineEncoder.file_name_format_override"></a>

#### file_name_format_override

```python
@file_name_format_override.setter
def file_name_format_override(value: str) -> None
```

<a id="unreal.MoviePipelineCommandLineEncoder.quality"></a>

#### quality

```python
@property
def quality() -> MoviePipelineEncodeQuality
```

(MoviePipelineEncodeQuality):  [Read-Write] What encoding quality to use for this job? Exact command line arguments for each one are specified in Project Settings.

<a id="unreal.MoviePipelineCommandLineEncoder.quality"></a>

#### quality

```python
@quality.setter
def quality(value: MoviePipelineEncodeQuality) -> None
```

<a id="unreal.MoviePipelineCommandLineEncoder.additional_command_line_args"></a>

#### additional_command_line_args

```python
@property
def additional_command_line_args() -> str
```

(str):  [Read-Write] Any additional arguments to pass to the CLI encode for this particular job.

<a id="unreal.MoviePipelineCommandLineEncoder.additional_command_line_args"></a>

#### additional_command_line_args

```python
@additional_command_line_args.setter
def additional_command_line_args(value: str) -> None
```

<a id="unreal.MoviePipelineCommandLineEncoder.delete_source_files"></a>

#### delete_source_files

```python
@property
def delete_source_files() -> bool
```

(bool):  [Read-Write] Should we delete the source files from disk after encoding?

<a id="unreal.MoviePipelineCommandLineEncoder.delete_source_files"></a>

#### delete_source_files

```python
@delete_source_files.setter
def delete_source_files(value: bool) -> None
```

<a id="unreal.MoviePipelineCommandLineEncoder.skip_encode_on_render_canceled"></a>

#### skip_encode_on_render_canceled

```python
@property
def skip_encode_on_render_canceled() -> bool
```

(bool):  [Read-Write] If a render was canceled (via hitting escape mid render) should we skip trying to encode the files we did produce?

<a id="unreal.MoviePipelineCommandLineEncoder.skip_encode_on_render_canceled"></a>

#### skip_encode_on_render_canceled

```python
@skip_encode_on_render_canceled.setter
def skip_encode_on_render_canceled(value: bool) -> None
```

<a id="unreal.MoviePipelineCommandLineEncoder.write_each_frame_duration"></a>

#### write_each_frame_duration

```python
@property
def write_each_frame_duration() -> bool
```

(bool):  [Read-Write] Write the duration for each frame into the generated text file. Needed for some input types on some CLI encoding software.

<a id="unreal.MoviePipelineCommandLineEncoder.write_each_frame_duration"></a>

#### write_each_frame_duration

```python
@write_each_frame_duration.setter
def write_each_frame_duration(value: bool) -> None
```

<a id="unreal.MoviePipelineCommandLineEncoderSettings"></a>