## MovieGraphCommandLineEncoderNode Objects

```python
class MovieGraphCommandLineEncoderNode(MovieGraphSettingNode)
```

A node which kicks off an encode process after all renders have completed.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphCommandLineEncoderNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``audio_codec`` (str):  [Read-Write] Which audio codec should we use? Run 'MovieRenderPipeline.DumpCLIEncoderCodecs' for options.
- ``audio_input_string_format`` (str):  [Read-Write] Format string used for each audio input.
- ``command_line_format`` (str):  [Read-Write] The format string used when building the final command line argument to launch.
- ``delete_source_files`` (bool):  [Read-Write] Whether the source files should be deleted on disk after encoding.
- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``encode_settings`` (str):  [Read-Write] Additional flags used for specifying encode quality.
- ``file_name_format`` (str):  [Read-Write] File name format string override. If specified it will override the FileNameFormat from the Output setting.
  If {shot_name} or {camera_name} is used, encoding will begin after each shot finishes rendering.
  Can be different from the main one in the Output setting so you can render out frames to individual
  shot folders but encode to one file.
- ``output_file_extension`` (str):  [Read-Write] Extension for the output files. Many encoders use this to determine the container type they are placed in. Should be without dot, ie: "webm".
- ``override_audio_codec`` (bool):  [Read-Write]
- ``override_audio_input_string_format`` (bool):  [Read-Write]
- ``override_b_delete_source_files`` (bool):  [Read-Write]
- ``override_b_retain_input_text_files`` (bool):  [Read-Write]
- ``override_b_skip_encode_on_render_canceled`` (bool):  [Read-Write]
- ``override_command_line_format`` (bool):  [Read-Write]
- ``override_encode_settings`` (bool):  [Read-Write]
- ``override_file_name_format`` (bool):  [Read-Write]
- ``override_output_file_extension`` (bool):  [Read-Write]
- ``override_video_codec`` (bool):  [Read-Write]
- ``override_video_input_string_format`` (bool):  [Read-Write]
- ``retain_input_text_files`` (bool):  [Read-Write] Retain the intermediate audio and video input text files that are passed to the encoder.
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.
- ``skip_encode_on_render_canceled`` (bool):  [Read-Write] Whether encoding should be skipped on frames produced if rendering was canceled before finishing.
- ``video_codec`` (str):  [Read-Write] Which video codec should we use? Run 'MovieRenderPipeline.DumpCLIEncoderCodecs' for options.
- ``video_input_string_format`` (str):  [Read-Write] Format string used for each video input.

<a id="unreal.MovieGraphCommandLineEncoderNode.override_file_name_format"></a>

#### override_file_name_format

```python
@property
def override_file_name_format() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphCommandLineEncoderNode.override_file_name_format"></a>

#### override_file_name_format

```python
@override_file_name_format.setter
def override_file_name_format(value: bool) -> None
```

<a id="unreal.MovieGraphCommandLineEncoderNode.b_override_file_name_format_override"></a>

#### b_override_file_name_format_override

```python
@property
def b_override_file_name_format_override() -> bool
```

deprecated: 'b_override_file_name_format_override' was renamed to 'override_file_name_format'.

<a id="unreal.MovieGraphCommandLineEncoderNode.b_override_file_name_format_override"></a>

#### b_override_file_name_format_override

```python
@b_override_file_name_format_override.setter
def b_override_file_name_format_override(value: bool) -> None
```

<a id="unreal.MovieGraphCommandLineEncoderNode.override_b_delete_source_files"></a>

#### override_b_delete_source_files

```python
@property
def override_b_delete_source_files() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphCommandLineEncoderNode.override_b_delete_source_files"></a>

#### override_b_delete_source_files

```python
@override_b_delete_source_files.setter
def override_b_delete_source_files(value: bool) -> None
```

<a id="unreal.MovieGraphCommandLineEncoderNode.override_b_skip_encode_on_render_canceled"></a>

#### override_b_skip_encode_on_render_canceled

```python
@property
def override_b_skip_encode_on_render_canceled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphCommandLineEncoderNode.override_b_skip_encode_on_render_canceled"></a>

#### override_b_skip_encode_on_render_canceled

```python
@override_b_skip_encode_on_render_canceled.setter
def override_b_skip_encode_on_render_canceled(value: bool) -> None
```

<a id="unreal.MovieGraphCommandLineEncoderNode.override_video_codec"></a>

#### override_video_codec

```python
@property
def override_video_codec() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphCommandLineEncoderNode.override_video_codec"></a>

#### override_video_codec

```python
@override_video_codec.setter
def override_video_codec(value: bool) -> None
```

<a id="unreal.MovieGraphCommandLineEncoderNode.override_audio_codec"></a>

#### override_audio_codec

```python
@property
def override_audio_codec() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphCommandLineEncoderNode.override_audio_codec"></a>

#### override_audio_codec

```python
@override_audio_codec.setter
def override_audio_codec(value: bool) -> None
```

<a id="unreal.MovieGraphCommandLineEncoderNode.override_output_file_extension"></a>

#### override_output_file_extension

```python
@property
def override_output_file_extension() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphCommandLineEncoderNode.override_output_file_extension"></a>

#### override_output_file_extension

```python
@override_output_file_extension.setter
def override_output_file_extension(value: bool) -> None
```

<a id="unreal.MovieGraphCommandLineEncoderNode.override_command_line_format"></a>

#### override_command_line_format

```python
@property
def override_command_line_format() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphCommandLineEncoderNode.override_command_line_format"></a>

#### override_command_line_format

```python
@override_command_line_format.setter
def override_command_line_format(value: bool) -> None
```

<a id="unreal.MovieGraphCommandLineEncoderNode.override_video_input_string_format"></a>

#### override_video_input_string_format

```python
@property
def override_video_input_string_format() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphCommandLineEncoderNode.override_video_input_string_format"></a>

#### override_video_input_string_format

```python
@override_video_input_string_format.setter
def override_video_input_string_format(value: bool) -> None
```

<a id="unreal.MovieGraphCommandLineEncoderNode.override_audio_input_string_format"></a>

#### override_audio_input_string_format

```python
@property
def override_audio_input_string_format() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphCommandLineEncoderNode.override_audio_input_string_format"></a>

#### override_audio_input_string_format

```python
@override_audio_input_string_format.setter
def override_audio_input_string_format(value: bool) -> None
```

<a id="unreal.MovieGraphCommandLineEncoderNode.override_encode_settings"></a>

#### override_encode_settings

```python
@property
def override_encode_settings() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphCommandLineEncoderNode.override_encode_settings"></a>

#### override_encode_settings

```python
@override_encode_settings.setter
def override_encode_settings(value: bool) -> None
```

<a id="unreal.MovieGraphCommandLineEncoderNode.override_b_retain_input_text_files"></a>

#### override_b_retain_input_text_files

```python
@property
def override_b_retain_input_text_files() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphCommandLineEncoderNode.override_b_retain_input_text_files"></a>

#### override_b_retain_input_text_files

```python
@override_b_retain_input_text_files.setter
def override_b_retain_input_text_files(value: bool) -> None
```

<a id="unreal.MovieGraphCommandLineEncoderNode.file_name_format"></a>

#### file_name_format

```python
@property
def file_name_format() -> str
```

(str):  [Read-Write] File name format string override. If specified it will override the FileNameFormat from the Output setting.
If {shot_name} or {camera_name} is used, encoding will begin after each shot finishes rendering.
Can be different from the main one in the Output setting so you can render out frames to individual
shot folders but encode to one file.

<a id="unreal.MovieGraphCommandLineEncoderNode.file_name_format"></a>

#### file_name_format

```python
@file_name_format.setter
def file_name_format(value: str) -> None
```

<a id="unreal.MovieGraphCommandLineEncoderNode.file_name_format_override"></a>

#### file_name_format_override

```python
@property
def file_name_format_override() -> str
```

deprecated: 'file_name_format_override' was renamed to 'file_name_format'.

<a id="unreal.MovieGraphCommandLineEncoderNode.file_name_format_override"></a>

#### file_name_format_override

```python
@file_name_format_override.setter
def file_name_format_override(value: str) -> None
```

<a id="unreal.MovieGraphCommandLineEncoderNode.delete_source_files"></a>

#### delete_source_files

```python
@property
def delete_source_files() -> bool
```

(bool):  [Read-Write] Whether the source files should be deleted on disk after encoding.

<a id="unreal.MovieGraphCommandLineEncoderNode.delete_source_files"></a>

#### delete_source_files

```python
@delete_source_files.setter
def delete_source_files(value: bool) -> None
```

<a id="unreal.MovieGraphCommandLineEncoderNode.skip_encode_on_render_canceled"></a>

#### skip_encode_on_render_canceled

```python
@property
def skip_encode_on_render_canceled() -> bool
```

(bool):  [Read-Write] Whether encoding should be skipped on frames produced if rendering was canceled before finishing.

<a id="unreal.MovieGraphCommandLineEncoderNode.skip_encode_on_render_canceled"></a>

#### skip_encode_on_render_canceled

```python
@skip_encode_on_render_canceled.setter
def skip_encode_on_render_canceled(value: bool) -> None
```

<a id="unreal.MovieGraphCommandLineEncoderNode.video_codec"></a>

#### video_codec

```python
@property
def video_codec() -> str
```

(str):  [Read-Write] Which video codec should we use? Run 'MovieRenderPipeline.DumpCLIEncoderCodecs' for options.

<a id="unreal.MovieGraphCommandLineEncoderNode.video_codec"></a>

#### video_codec

```python
@video_codec.setter
def video_codec(value: str) -> None
```

<a id="unreal.MovieGraphCommandLineEncoderNode.audio_codec"></a>

#### audio_codec

```python
@property
def audio_codec() -> str
```

(str):  [Read-Write] Which audio codec should we use? Run 'MovieRenderPipeline.DumpCLIEncoderCodecs' for options.

<a id="unreal.MovieGraphCommandLineEncoderNode.audio_codec"></a>

#### audio_codec

```python
@audio_codec.setter
def audio_codec(value: str) -> None
```

<a id="unreal.MovieGraphCommandLineEncoderNode.output_file_extension"></a>

#### output_file_extension

```python
@property
def output_file_extension() -> str
```

(str):  [Read-Write] Extension for the output files. Many encoders use this to determine the container type they are placed in. Should be without dot, ie: "webm".

<a id="unreal.MovieGraphCommandLineEncoderNode.output_file_extension"></a>

#### output_file_extension

```python
@output_file_extension.setter
def output_file_extension(value: str) -> None
```

<a id="unreal.MovieGraphCommandLineEncoderNode.command_line_format"></a>

#### command_line_format

```python
@property
def command_line_format() -> str
```

(str):  [Read-Write] The format string used when building the final command line argument to launch.

<a id="unreal.MovieGraphCommandLineEncoderNode.command_line_format"></a>

#### command_line_format

```python
@command_line_format.setter
def command_line_format(value: str) -> None
```

<a id="unreal.MovieGraphCommandLineEncoderNode.video_input_string_format"></a>

#### video_input_string_format

```python
@property
def video_input_string_format() -> str
```

(str):  [Read-Write] Format string used for each video input.

<a id="unreal.MovieGraphCommandLineEncoderNode.video_input_string_format"></a>

#### video_input_string_format

```python
@video_input_string_format.setter
def video_input_string_format(value: str) -> None
```

<a id="unreal.MovieGraphCommandLineEncoderNode.audio_input_string_format"></a>

#### audio_input_string_format

```python
@property
def audio_input_string_format() -> str
```

(str):  [Read-Write] Format string used for each audio input.

<a id="unreal.MovieGraphCommandLineEncoderNode.audio_input_string_format"></a>

#### audio_input_string_format

```python
@audio_input_string_format.setter
def audio_input_string_format(value: str) -> None
```

<a id="unreal.MovieGraphCommandLineEncoderNode.encode_settings"></a>

#### encode_settings

```python
@property
def encode_settings() -> str
```

(str):  [Read-Write] Additional flags used for specifying encode quality.

<a id="unreal.MovieGraphCommandLineEncoderNode.encode_settings"></a>

#### encode_settings

```python
@encode_settings.setter
def encode_settings(value: str) -> None
```

<a id="unreal.MovieGraphCommandLineEncoderNode.retain_input_text_files"></a>

#### retain_input_text_files

```python
@property
def retain_input_text_files() -> bool
```

(bool):  [Read-Write] Retain the intermediate audio and video input text files that are passed to the encoder.

<a id="unreal.MovieGraphCommandLineEncoderNode.retain_input_text_files"></a>

#### retain_input_text_files

```python
@retain_input_text_files.setter
def retain_input_text_files(value: bool) -> None
```

<a id="unreal.MovieGraphValueContainer"></a>