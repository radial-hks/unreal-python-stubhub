## MoviePipelineCommandLineEncoderSettings Objects

```python
class MoviePipelineCommandLineEncoderSettings(DeveloperSettings)
```

Movie Pipeline Command Line Encoder Settings

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MoviePipelineCommandLineEncoderSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``audio_codec`` (str):  [Read-Write] Which audio codec should we use? Run 'MovieRenderPipeline.DumpCLIEncoderCodecs' for options.
- ``audio_input_string_format`` (str):  [Read-Write] Format string used for each audio input.
- ``codec_help_text`` (Text):  [Read-Write]
- ``command_line_format`` (str):  [Read-Write] The format string used when building the final command line argument to launch.
- ``encode_settings_epic`` (str):  [Read-Write] The flags used for epic quality encoding.
- ``encode_settings_high`` (str):  [Read-Write] The flags used for high quality encoding.
- ``encode_settings_low`` (str):  [Read-Write] The flags used for low quality encoding.
- ``encode_settings_med`` (str):  [Read-Write] The flags used for medium quality encoding.
- ``executable_path`` (str):  [Read-Write] Path to the executable (including extension). Can just be "ffmpeg.exe" if it can be located via PATH directories.
- ``output_file_extension`` (str):  [Read-Write] Extension for the output files. Many encoders use this to determine the container type they are placed in. Should be without dot, ie: "webm".
- ``video_codec`` (str):  [Read-Write] Which video codec should we use? Run 'MovieRenderPipeline.DumpCLIEncoderCodecs' for options.
- ``video_input_string_format`` (str):  [Read-Write] Format string used for each video input.

<a id="unreal.MoviePipelineCommandLineEncoderSettings.executable_path"></a>

#### executable_path

```python
@property
def executable_path() -> str
```

(str):  [Read-Write] Path to the executable (including extension). Can just be "ffmpeg.exe" if it can be located via PATH directories.

<a id="unreal.MoviePipelineCommandLineEncoderSettings.executable_path"></a>

#### executable_path

```python
@executable_path.setter
def executable_path(value: str) -> None
```

<a id="unreal.MoviePipelineCommandLineEncoderSettings.video_codec"></a>

#### video_codec

```python
@property
def video_codec() -> str
```

(str):  [Read-Write] Which video codec should we use? Run 'MovieRenderPipeline.DumpCLIEncoderCodecs' for options.

<a id="unreal.MoviePipelineCommandLineEncoderSettings.video_codec"></a>

#### video_codec

```python
@video_codec.setter
def video_codec(value: str) -> None
```

<a id="unreal.MoviePipelineCommandLineEncoderSettings.audio_codec"></a>

#### audio_codec

```python
@property
def audio_codec() -> str
```

(str):  [Read-Write] Which audio codec should we use? Run 'MovieRenderPipeline.DumpCLIEncoderCodecs' for options.

<a id="unreal.MoviePipelineCommandLineEncoderSettings.audio_codec"></a>

#### audio_codec

```python
@audio_codec.setter
def audio_codec(value: str) -> None
```

<a id="unreal.MoviePipelineCommandLineEncoderSettings.output_file_extension"></a>

#### output_file_extension

```python
@property
def output_file_extension() -> str
```

(str):  [Read-Write] Extension for the output files. Many encoders use this to determine the container type they are placed in. Should be without dot, ie: "webm".

<a id="unreal.MoviePipelineCommandLineEncoderSettings.output_file_extension"></a>

#### output_file_extension

```python
@output_file_extension.setter
def output_file_extension(value: str) -> None
```

<a id="unreal.MoviePipelineCommandLineEncoderSettings.command_line_format"></a>

#### command_line_format

```python
@property
def command_line_format() -> str
```

(str):  [Read-Write] The format string used when building the final command line argument to launch.

<a id="unreal.MoviePipelineCommandLineEncoderSettings.command_line_format"></a>

#### command_line_format

```python
@command_line_format.setter
def command_line_format(value: str) -> None
```

<a id="unreal.MoviePipelineCommandLineEncoderSettings.video_input_string_format"></a>

#### video_input_string_format

```python
@property
def video_input_string_format() -> str
```

(str):  [Read-Write] Format string used for each video input.

<a id="unreal.MoviePipelineCommandLineEncoderSettings.video_input_string_format"></a>

#### video_input_string_format

```python
@video_input_string_format.setter
def video_input_string_format(value: str) -> None
```

<a id="unreal.MoviePipelineCommandLineEncoderSettings.audio_input_string_format"></a>

#### audio_input_string_format

```python
@property
def audio_input_string_format() -> str
```

(str):  [Read-Write] Format string used for each audio input.

<a id="unreal.MoviePipelineCommandLineEncoderSettings.audio_input_string_format"></a>

#### audio_input_string_format

```python
@audio_input_string_format.setter
def audio_input_string_format(value: str) -> None
```

<a id="unreal.MoviePipelineCommandLineEncoderSettings.encode_settings_low"></a>

#### encode_settings_low

```python
@property
def encode_settings_low() -> str
```

(str):  [Read-Write] The flags used for low quality encoding.

<a id="unreal.MoviePipelineCommandLineEncoderSettings.encode_settings_low"></a>

#### encode_settings_low

```python
@encode_settings_low.setter
def encode_settings_low(value: str) -> None
```

<a id="unreal.MoviePipelineCommandLineEncoderSettings.encode_settings_med"></a>

#### encode_settings_med

```python
@property
def encode_settings_med() -> str
```

(str):  [Read-Write] The flags used for medium quality encoding.

<a id="unreal.MoviePipelineCommandLineEncoderSettings.encode_settings_med"></a>

#### encode_settings_med

```python
@encode_settings_med.setter
def encode_settings_med(value: str) -> None
```

<a id="unreal.MoviePipelineCommandLineEncoderSettings.encode_settings_high"></a>

#### encode_settings_high

```python
@property
def encode_settings_high() -> str
```

(str):  [Read-Write] The flags used for high quality encoding.

<a id="unreal.MoviePipelineCommandLineEncoderSettings.encode_settings_high"></a>

#### encode_settings_high

```python
@encode_settings_high.setter
def encode_settings_high(value: str) -> None
```

<a id="unreal.MoviePipelineCommandLineEncoderSettings.encode_settings_epic"></a>

#### encode_settings_epic

```python
@property
def encode_settings_epic() -> str
```

(str):  [Read-Write] The flags used for epic quality encoding.

<a id="unreal.MoviePipelineCommandLineEncoderSettings.encode_settings_epic"></a>

#### encode_settings_epic

```python
@encode_settings_epic.setter
def encode_settings_epic(value: str) -> None
```

<a id="unreal.MoviePipelineConfigBase"></a>