## UserDefinedImageCaptureProtocol Objects

```python
class UserDefinedImageCaptureProtocol(UserDefinedCaptureProtocol)
```

A blueprintable capture protocol tailored to capturing and exporting frames as images

**C++ Source:**

- **Module**: MovieSceneCapture
- **File**: UserDefinedCaptureProtocol.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``compression_quality`` (int32):  [Read-Write] The compression quality for the image type. For EXRs, 0 = Default ZIP compression, 1 = No compression, PNGs and JPEGs expect a value between 0 and 100
- ``enable_compression`` (bool):  [Read-Write] Whether to save images with compression or not. Not supported for bitmaps.
- ``format`` (DesiredImageFormat):  [Read-Write] The image format to save as
- ``world`` (World):  [Read-Write] World pointer assigned on Setup

<a id="unreal.UserDefinedImageCaptureProtocol.format"></a>

#### format

```python
@property
def format() -> DesiredImageFormat
```

(DesiredImageFormat):  [Read-Write] The image format to save as

<a id="unreal.UserDefinedImageCaptureProtocol.format"></a>

#### format

```python
@format.setter
def format(value: DesiredImageFormat) -> None
```

<a id="unreal.UserDefinedImageCaptureProtocol.enable_compression"></a>

#### enable_compression

```python
@property
def enable_compression() -> bool
```

(bool):  [Read-Write] Whether to save images with compression or not. Not supported for bitmaps.

<a id="unreal.UserDefinedImageCaptureProtocol.enable_compression"></a>

#### enable_compression

```python
@enable_compression.setter
def enable_compression(value: bool) -> None
```

<a id="unreal.UserDefinedImageCaptureProtocol.compression_quality"></a>

#### compression_quality

```python
@property
def compression_quality() -> int
```

(int32):  [Read-Write] The compression quality for the image type. For EXRs, 0 = Default ZIP compression, 1 = No compression, PNGs and JPEGs expect a value between 0 and 100

<a id="unreal.UserDefinedImageCaptureProtocol.compression_quality"></a>

#### compression_quality

```python
@compression_quality.setter
def compression_quality(value: int) -> None
```

<a id="unreal.UserDefinedImageCaptureProtocol.write_image_to_disk"></a>

#### write_image_to_disk

```python
def write_image_to_disk(pixel_data: CapturedPixels,
                        stream_id: CapturedPixelsID,
                        frame_metrics: FrameMetrics,
                        copy_image_data: bool = False) -> None
```

x.write_image_to_disk(pixel_data, stream_id, frame_metrics, copy_image_data=False) -> None
* Generate a filename for the current frame using this protocol's file name formatter
*
*

Args:
    pixel_data (CapturedPixels): 
    stream_id (CapturedPixelsID): 
    frame_metrics (FrameMetrics): 
    copy_image_data (bool):

<a id="unreal.UserDefinedImageCaptureProtocol.generate_filename_for_current_frame"></a>

#### generate_filename_for_current_frame

```python
def generate_filename_for_current_frame() -> str
```

x.generate_filename_for_current_frame() -> str
* Generate a filename for the current frame using this protocol's file name formatter
*
*

Returns:
    str: A fully qualified file name for the current frame number

<a id="unreal.UserDefinedImageCaptureProtocol.generate_filename_for_buffer"></a>

#### generate_filename_for_buffer

```python
def generate_filename_for_buffer(buffer: Texture,
                                 stream_id: CapturedPixelsID) -> str
```

x.generate_filename_for_buffer(buffer, stream_id) -> str
* Generate a filename for the specified buffer using this protocol's file name formatter
*
*

Args:
    buffer (Texture): The desired buffer to generate a filename for *
    stream_id (CapturedPixelsID): The ID of the stream for this buffer (e.g. a composition pass name) *

Returns:
    str: A fully qualified file name

<a id="unreal.VideoCaptureProtocol"></a>