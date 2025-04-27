## MovieSceneCaptureSettings Objects

```python
class MovieSceneCaptureSettings(StructBase)
```

Common movie-scene capture settings

**C++ Source:**

- **Module**: MovieSceneCapture
- **File**: MovieSceneCaptureSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_movement`` (bool):  [Read-Write] Whether to allow player movement whilst capturing
- ``allow_turning`` (bool):  [Read-Write] Whether to allow player rotation whilst capturing
- ``cinematic_engine_scalability`` (bool):  [Read-Write] Whether to enable cinematic engine scalability settings
- ``cinematic_mode`` (bool):  [Read-Write] Whether to enable cinematic mode whilst capturing
- ``custom_frame_rate`` (FrameRate):  [Read-Write] The custom frame rate at which to capture if "Use Custom Frame Rate" is enabled
- ``enable_texture_streaming`` (bool):  [Read-Write] Whether to texture streaming should be enabled while capturing.  Turning off texture streaming may cause much more memory to be used, but also reduces the chance of blurry textures in your captured video.
- ``frame_rate`` (FrameRate):  [Read-Only] The sequence's frame rate at which to capture if "Use Custom Frame Rate" is not enabled
- ``game_mode_override`` (type(Class)):  [Read-Write] Optional game mode to override the map's default game mode with.  This can be useful if the game's normal mode displays UI elements or loading screens that you don't want captured.
- ``handle_frames`` (int32):  [Read-Write] Number of frame handles to include for each shot
- ``movie_extension`` (str):  [Read-Write] Filename extension for movies referenced in the XMLs/EDLs
- ``output_directory`` (DirectoryPath):  [Read-Write] The directory to output the captured file(s) in
- ``output_format`` (str):  [Read-Write] The format to use for the resulting filename. Extension will be added automatically. Any tokens of the form {token} will be replaced with the corresponding value:
  {fps}                - The captured framerate
  {frame}              - The current frame number (only relevant for image sequences)
  {width}              - The width of the captured frames
  {height}             - The height of the captured frames
  {world}              - The name of the current world
  {quality}    - The image compression quality setting
  {material}   - The material/render pass
  {shot}       - The name of the level sequence asset shot being played
  {sequence}   - The name of the level sequence asset being played
  {camera}     - The name of the current camera
  {date}       - The date in the format of {year}.{month}.{day}
  {year}       - The current year
  {month}      - The current month
  {day}        - The current day
  {time}       - The current time in the format of hours.minutes.seconds
- ``overwrite_existing`` (bool):  [Read-Write] Whether to overwrite existing files or not
- ``path_tracer_sample_per_pixel`` (int32):  [Read-Write] Number of sampler per pixel to be used when rendering the scene with the path tracer (if supported)
- ``resolution`` (CaptureResolution):  [Read-Write] The resolution at which to capture
- ``show_hud`` (bool):  [Read-Write] Whether to show the in-game HUD whilst capturing
- ``show_player`` (bool):  [Read-Write] Whether to show the local player whilst capturing
- ``use_custom_frame_rate`` (bool):  [Read-Write] Specify using the custom frame rate as opposed to the sequence's display rate
- ``use_path_tracer`` (bool):  [Read-Write] Whether to use the path tracer (if supported) to render the scene
- ``use_relative_frame_numbers`` (bool):  [Read-Write] True if frame numbers in the output files should be relative to zero, rather than the actual frame numbers in the originating animation content.
- ``zero_pad_frame_numbers`` (uint8):  [Read-Write] How much to zero-pad frame numbers on filenames

<a id="unreal.MovieSceneCaptureSettings.__init__"></a>

#### __init__

```python
def __init__(output_directory: DirectoryPath = [""],
             game_mode_override: Class = None,
             output_format: str = "",
             overwrite_existing: bool = False,
             use_relative_frame_numbers: bool = False,
             handle_frames: int = 0,
             movie_extension: str = "",
             zero_pad_frame_numbers: int = 0,
             frame_rate: FrameRate = [60000, 1],
             use_custom_frame_rate: bool = False,
             custom_frame_rate: FrameRate = [60000, 1],
             resolution: CaptureResolution = [0, 0],
             enable_texture_streaming: bool = False,
             cinematic_engine_scalability: bool = False,
             cinematic_mode: bool = False,
             allow_movement: bool = False,
             allow_turning: bool = False,
             show_player: bool = False,
             show_hud: bool = False,
             use_path_tracer: bool = False,
             path_tracer_sample_per_pixel: int = 0) -> None
```

<a id="unreal.MovieSceneCaptureSettings.output_directory"></a>

#### output_directory

```python
@property
def output_directory() -> DirectoryPath
```

(DirectoryPath):  [Read-Write] The directory to output the captured file(s) in

<a id="unreal.MovieSceneCaptureSettings.output_directory"></a>

#### output_directory

```python
@output_directory.setter
def output_directory(value: DirectoryPath) -> None
```

<a id="unreal.MovieSceneCaptureSettings.game_mode_override"></a>

#### game_mode_override

```python
@property
def game_mode_override() -> Class
```

(type(Class)):  [Read-Write] Optional game mode to override the map's default game mode with.  This can be useful if the game's normal mode displays UI elements or loading screens that you don't want captured.

<a id="unreal.MovieSceneCaptureSettings.game_mode_override"></a>

#### game_mode_override

```python
@game_mode_override.setter
def game_mode_override(value: Class) -> None
```

<a id="unreal.MovieSceneCaptureSettings.output_format"></a>

#### output_format

```python
@property
def output_format() -> str
```

(str):  [Read-Write] The format to use for the resulting filename. Extension will be added automatically. Any tokens of the form {token} will be replaced with the corresponding value:
{fps}                - The captured framerate
{frame}              - The current frame number (only relevant for image sequences)
{width}              - The width of the captured frames
{height}             - The height of the captured frames
{world}              - The name of the current world
{quality}    - The image compression quality setting
{material}   - The material/render pass
{shot}       - The name of the level sequence asset shot being played
{sequence}   - The name of the level sequence asset being played
{camera}     - The name of the current camera
{date}       - The date in the format of {year}.{month}.{day}
{year}       - The current year
{month}      - The current month
{day}        - The current day
{time}       - The current time in the format of hours.minutes.seconds

<a id="unreal.MovieSceneCaptureSettings.output_format"></a>

#### output_format

```python
@output_format.setter
def output_format(value: str) -> None
```

<a id="unreal.MovieSceneCaptureSettings.overwrite_existing"></a>

#### overwrite_existing

```python
@property
def overwrite_existing() -> bool
```

(bool):  [Read-Write] Whether to overwrite existing files or not

<a id="unreal.MovieSceneCaptureSettings.overwrite_existing"></a>

#### overwrite_existing

```python
@overwrite_existing.setter
def overwrite_existing(value: bool) -> None
```

<a id="unreal.MovieSceneCaptureSettings.use_relative_frame_numbers"></a>

#### use_relative_frame_numbers

```python
@property
def use_relative_frame_numbers() -> bool
```

(bool):  [Read-Write] True if frame numbers in the output files should be relative to zero, rather than the actual frame numbers in the originating animation content.

<a id="unreal.MovieSceneCaptureSettings.use_relative_frame_numbers"></a>

#### use_relative_frame_numbers

```python
@use_relative_frame_numbers.setter
def use_relative_frame_numbers(value: bool) -> None
```

<a id="unreal.MovieSceneCaptureSettings.handle_frames"></a>

#### handle_frames

```python
@property
def handle_frames() -> int
```

(int32):  [Read-Write] Number of frame handles to include for each shot

<a id="unreal.MovieSceneCaptureSettings.handle_frames"></a>

#### handle_frames

```python
@handle_frames.setter
def handle_frames(value: int) -> None
```

<a id="unreal.MovieSceneCaptureSettings.movie_extension"></a>

#### movie_extension

```python
@property
def movie_extension() -> str
```

(str):  [Read-Write] Filename extension for movies referenced in the XMLs/EDLs

<a id="unreal.MovieSceneCaptureSettings.movie_extension"></a>

#### movie_extension

```python
@movie_extension.setter
def movie_extension(value: str) -> None
```

<a id="unreal.MovieSceneCaptureSettings.zero_pad_frame_numbers"></a>

#### zero_pad_frame_numbers

```python
@property
def zero_pad_frame_numbers() -> int
```

(uint8):  [Read-Write] How much to zero-pad frame numbers on filenames

<a id="unreal.MovieSceneCaptureSettings.zero_pad_frame_numbers"></a>

#### zero_pad_frame_numbers

```python
@zero_pad_frame_numbers.setter
def zero_pad_frame_numbers(value: int) -> None
```

<a id="unreal.MovieSceneCaptureSettings.frame_rate"></a>

#### frame_rate

```python
@property
def frame_rate() -> FrameRate
```

(FrameRate):  [Read-Only] The sequence's frame rate at which to capture if "Use Custom Frame Rate" is not enabled

<a id="unreal.MovieSceneCaptureSettings.use_custom_frame_rate"></a>

#### use_custom_frame_rate

```python
@property
def use_custom_frame_rate() -> bool
```

(bool):  [Read-Write] Specify using the custom frame rate as opposed to the sequence's display rate

<a id="unreal.MovieSceneCaptureSettings.use_custom_frame_rate"></a>

#### use_custom_frame_rate

```python
@use_custom_frame_rate.setter
def use_custom_frame_rate(value: bool) -> None
```

<a id="unreal.MovieSceneCaptureSettings.custom_frame_rate"></a>

#### custom_frame_rate

```python
@property
def custom_frame_rate() -> FrameRate
```

(FrameRate):  [Read-Write] The custom frame rate at which to capture if "Use Custom Frame Rate" is enabled

<a id="unreal.MovieSceneCaptureSettings.custom_frame_rate"></a>

#### custom_frame_rate

```python
@custom_frame_rate.setter
def custom_frame_rate(value: FrameRate) -> None
```

<a id="unreal.MovieSceneCaptureSettings.resolution"></a>

#### resolution

```python
@property
def resolution() -> CaptureResolution
```

(CaptureResolution):  [Read-Write] The resolution at which to capture

<a id="unreal.MovieSceneCaptureSettings.resolution"></a>

#### resolution

```python
@resolution.setter
def resolution(value: CaptureResolution) -> None
```

<a id="unreal.MovieSceneCaptureSettings.enable_texture_streaming"></a>

#### enable_texture_streaming

```python
@property
def enable_texture_streaming() -> bool
```

(bool):  [Read-Write] Whether to texture streaming should be enabled while capturing.  Turning off texture streaming may cause much more memory to be used, but also reduces the chance of blurry textures in your captured video.

<a id="unreal.MovieSceneCaptureSettings.enable_texture_streaming"></a>

#### enable_texture_streaming

```python
@enable_texture_streaming.setter
def enable_texture_streaming(value: bool) -> None
```

<a id="unreal.MovieSceneCaptureSettings.cinematic_engine_scalability"></a>

#### cinematic_engine_scalability

```python
@property
def cinematic_engine_scalability() -> bool
```

(bool):  [Read-Write] Whether to enable cinematic engine scalability settings

<a id="unreal.MovieSceneCaptureSettings.cinematic_engine_scalability"></a>

#### cinematic_engine_scalability

```python
@cinematic_engine_scalability.setter
def cinematic_engine_scalability(value: bool) -> None
```

<a id="unreal.MovieSceneCaptureSettings.cinematic_mode"></a>

#### cinematic_mode

```python
@property
def cinematic_mode() -> bool
```

(bool):  [Read-Write] Whether to enable cinematic mode whilst capturing

<a id="unreal.MovieSceneCaptureSettings.cinematic_mode"></a>

#### cinematic_mode

```python
@cinematic_mode.setter
def cinematic_mode(value: bool) -> None
```

<a id="unreal.MovieSceneCaptureSettings.allow_movement"></a>

#### allow_movement

```python
@property
def allow_movement() -> bool
```

(bool):  [Read-Write] Whether to allow player movement whilst capturing

<a id="unreal.MovieSceneCaptureSettings.allow_movement"></a>

#### allow_movement

```python
@allow_movement.setter
def allow_movement(value: bool) -> None
```

<a id="unreal.MovieSceneCaptureSettings.allow_turning"></a>

#### allow_turning

```python
@property
def allow_turning() -> bool
```

(bool):  [Read-Write] Whether to allow player rotation whilst capturing

<a id="unreal.MovieSceneCaptureSettings.allow_turning"></a>

#### allow_turning

```python
@allow_turning.setter
def allow_turning(value: bool) -> None
```

<a id="unreal.MovieSceneCaptureSettings.show_player"></a>

#### show_player

```python
@property
def show_player() -> bool
```

(bool):  [Read-Write] Whether to show the local player whilst capturing

<a id="unreal.MovieSceneCaptureSettings.show_player"></a>

#### show_player

```python
@show_player.setter
def show_player(value: bool) -> None
```

<a id="unreal.MovieSceneCaptureSettings.show_hud"></a>

#### show_hud

```python
@property
def show_hud() -> bool
```

(bool):  [Read-Write] Whether to show the in-game HUD whilst capturing

<a id="unreal.MovieSceneCaptureSettings.show_hud"></a>

#### show_hud

```python
@show_hud.setter
def show_hud(value: bool) -> None
```

<a id="unreal.MovieSceneCaptureSettings.use_path_tracer"></a>

#### use_path_tracer

```python
@property
def use_path_tracer() -> bool
```

(bool):  [Read-Write] Whether to use the path tracer (if supported) to render the scene

<a id="unreal.MovieSceneCaptureSettings.use_path_tracer"></a>

#### use_path_tracer

```python
@use_path_tracer.setter
def use_path_tracer(value: bool) -> None
```

<a id="unreal.MovieSceneCaptureSettings.path_tracer_sample_per_pixel"></a>

#### path_tracer_sample_per_pixel

```python
@property
def path_tracer_sample_per_pixel() -> int
```

(int32):  [Read-Write] Number of sampler per pixel to be used when rendering the scene with the path tracer (if supported)

<a id="unreal.MovieSceneCaptureSettings.path_tracer_sample_per_pixel"></a>

#### path_tracer_sample_per_pixel

```python
@path_tracer_sample_per_pixel.setter
def path_tracer_sample_per_pixel(value: int) -> None
```

<a id="unreal.FrameMetrics"></a>