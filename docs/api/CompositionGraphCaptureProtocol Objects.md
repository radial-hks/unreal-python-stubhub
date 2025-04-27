## CompositionGraphCaptureProtocol Objects

```python
class CompositionGraphCaptureProtocol(MovieSceneImageCaptureProtocolBase)
```

Composition Graph Capture Protocol

**C++ Source:**

- **Module**: MovieSceneCapture
- **File**: CompositionGraphCaptureProtocol.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``capture_frames_in_hdr`` (bool):  [Read-Write] Whether to capture the frames as HDR textures (*.exr format)
- ``capture_gamut`` (HDRCaptureGamut):  [Read-Write] The color gamut to use when storing HDR captured data. The gamut depends on whether the bCaptureFramesInHDR option is enabled.
- ``disable_screen_percentage`` (bool):  [Read-Write] Whether to disable screen percentage
- ``hdr_compression_quality`` (int32):  [Read-Write] Compression Quality for HDR Frames (0 for no compression, 1 for default compression which can be slow)
- ``include_render_passes`` (CompositionGraphCapturePasses):  [Read-Write] A list of render passes to include in the capture. Leave empty to export all available passes.
- ``post_processing_material`` (SoftObjectPath):  [Read-Write] Custom post processing material to use for rendering

<a id="unreal.CompositionGraphCaptureProtocol.include_render_passes"></a>

#### include_render_passes

```python
@property
def include_render_passes() -> CompositionGraphCapturePasses
```

(CompositionGraphCapturePasses):  [Read-Write] A list of render passes to include in the capture. Leave empty to export all available passes.

<a id="unreal.CompositionGraphCaptureProtocol.include_render_passes"></a>

#### include_render_passes

```python
@include_render_passes.setter
def include_render_passes(value: CompositionGraphCapturePasses) -> None
```

<a id="unreal.CompositionGraphCaptureProtocol.capture_frames_in_hdr"></a>

#### capture_frames_in_hdr

```python
@property
def capture_frames_in_hdr() -> bool
```

(bool):  [Read-Write] Whether to capture the frames as HDR textures (*.exr format)

<a id="unreal.CompositionGraphCaptureProtocol.capture_frames_in_hdr"></a>

#### capture_frames_in_hdr

```python
@capture_frames_in_hdr.setter
def capture_frames_in_hdr(value: bool) -> None
```

<a id="unreal.CompositionGraphCaptureProtocol.hdr_compression_quality"></a>

#### hdr_compression_quality

```python
@property
def hdr_compression_quality() -> int
```

(int32):  [Read-Write] Compression Quality for HDR Frames (0 for no compression, 1 for default compression which can be slow)

<a id="unreal.CompositionGraphCaptureProtocol.hdr_compression_quality"></a>

#### hdr_compression_quality

```python
@hdr_compression_quality.setter
def hdr_compression_quality(value: int) -> None
```

<a id="unreal.CompositionGraphCaptureProtocol.capture_gamut"></a>

#### capture_gamut

```python
@property
def capture_gamut() -> HDRCaptureGamut
```

(HDRCaptureGamut):  [Read-Write] The color gamut to use when storing HDR captured data. The gamut depends on whether the bCaptureFramesInHDR option is enabled.

<a id="unreal.CompositionGraphCaptureProtocol.capture_gamut"></a>

#### capture_gamut

```python
@capture_gamut.setter
def capture_gamut(value: HDRCaptureGamut) -> None
```

<a id="unreal.CompositionGraphCaptureProtocol.post_processing_material"></a>

#### post_processing_material

```python
@property
def post_processing_material() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write] Custom post processing material to use for rendering

<a id="unreal.CompositionGraphCaptureProtocol.post_processing_material"></a>

#### post_processing_material

```python
@post_processing_material.setter
def post_processing_material(value: SoftObjectPath) -> None
```

<a id="unreal.CompositionGraphCaptureProtocol.disable_screen_percentage"></a>

#### disable_screen_percentage

```python
@property
def disable_screen_percentage() -> bool
```

(bool):  [Read-Write] Whether to disable screen percentage

<a id="unreal.CompositionGraphCaptureProtocol.disable_screen_percentage"></a>

#### disable_screen_percentage

```python
@disable_screen_percentage.setter
def disable_screen_percentage(value: bool) -> None
```

<a id="unreal.FrameGrabberProtocol"></a>