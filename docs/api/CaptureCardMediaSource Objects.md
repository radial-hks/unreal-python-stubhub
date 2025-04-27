## CaptureCardMediaSource Objects

```python
class CaptureCardMediaSource(TimeSynchronizableMediaSource)
```

Base class for media sources that are coming from a capture card.

**C++ Source:**

- **Plugin**: MediaIOFramework
- **Module**: MediaIOCore
- **File**: CaptureCardMediaSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color_conversion_settings`` (OpenColorIOColorConversionSettings):  [Read-Write] OCIO Settings used for applying a color conversion to the incoming source.
- ``deinterlacer`` (VideoDeinterlacer):  [Read-Write] How interlaced video should be treated.
- ``evaluation_type`` (MediaIOSampleEvaluationType):  [Read-Write] Sample evaluation type.
- ``frame_delay`` (int32):  [Read-Write] When using Time Synchronization, how many frame back should it read. Capped at 4 frames due to the potential issues with buffer sizes.
  Framelocked modes don't support this feature.
- ``framelock`` (bool):  [Read-Write] Should wait for some time until requested frame arrives? Requires JIT rendering.
- ``interlace_field_order`` (MediaIOInterlaceFieldOrder):  [Read-Write] The order in which interlace fields should be copied.
- ``override_source_color_space`` (bool):  [Read-Write] Whether to override the source color space or to use the metadata embedded in the ancillary data of the signal.
- ``override_source_color_space`` (TextureColorSpace):  [Read-Write] Color space of the source texture.
- ``override_source_encoding`` (MediaIOCoreSourceEncoding):  [Read-Write] Encoding of the source texture.
- ``override_source_encoding`` (bool):  [Read-Write] Whether to override the source encoding or to use the metadata embedded in the ancillary data of the signal.
- ``platform_player_names`` (Map[str, Name]):  [Read-Write] Override native media player plug-ins per platform (Empty = find one automatically).
- ``render_jit`` (bool):  [Read-Write] Should use JITR technique? It enables late sample picking for render.
- ``time_delay`` (double):  [Read-Write] When not using Time Synchronization, how far back it time should it read.
- ``use_time_synchronization`` (bool):  [Read-Write] Synchronize the media with the engine's timecode.
  The media player has be able to read timecode.
  The media player will try to play the corresponding frame, base on the frame's timecode value.

<a id="unreal.CaptureCardMediaSource.deinterlacer"></a>

#### deinterlacer

```python
@property
def deinterlacer() -> VideoDeinterlacer
```

(VideoDeinterlacer):  [Read-Only] How interlaced video should be treated.

<a id="unreal.CaptureCardMediaSource.interlace_field_order"></a>

#### interlace_field_order

```python
@property
def interlace_field_order() -> MediaIOInterlaceFieldOrder
```

(MediaIOInterlaceFieldOrder):  [Read-Only] The order in which interlace fields should be copied.

<a id="unreal.CaptureCardMediaSource.override_source_encoding"></a>

#### override_source_encoding

```python
@property
def override_source_encoding() -> MediaIOCoreSourceEncoding
```

(MediaIOCoreSourceEncoding):  [Read-Only] Encoding of the source texture.

<a id="unreal.CaptureCardMediaSource.override_source_color_space"></a>

#### override_source_color_space

```python
@property
def override_source_color_space() -> TextureColorSpace
```

(TextureColorSpace):  [Read-Only] Color space of the source texture.

<a id="unreal.CaptureCardMediaSource.color_conversion_settings"></a>

#### color_conversion_settings

```python
@property
def color_conversion_settings() -> OpenColorIOColorConversionSettings
```

(OpenColorIOColorConversionSettings):  [Read-Write] OCIO Settings used for applying a color conversion to the incoming source.

<a id="unreal.CaptureCardMediaSource.color_conversion_settings"></a>

#### color_conversion_settings

```python
@color_conversion_settings.setter
def color_conversion_settings(
        value: OpenColorIOColorConversionSettings) -> None
```

<a id="unreal.MediaCapture"></a>