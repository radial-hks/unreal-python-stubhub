## FileMediaOutput Objects

```python
class FileMediaOutput(MediaOutput)
```

Output information for a file media capture.
note: 'Frame Buffer Pixel Format' must be set to at least 8 bits of alpha to enabled the Key.
note: 'Enable alpha channel support in post-processing' must be set to 'Allow through tonemapper' to enabled the Key.

**C++ Source:**

- **Plugin**: MediaIOFramework
- **Module**: MediaIOCore
- **File**: FileMediaOutput.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_file_name`` (str):  [Read-Write] The base file name of the images. The frame number will be append to the base file name.
- ``desired_pixel_format`` (FileMediaOutputPixelFormat):  [Read-Write] Use the default back buffer pixel format or specify a specific the pixel format to capture.
- ``desired_size`` (IntPoint):  [Read-Write] Use the default back buffer size or specify a specific size to capture.
- ``file_path`` (DirectoryPath):  [Read-Write] The file path for the images.
- ``invert_alpha`` (bool):  [Read-Write] Invert the alpha for formats that support alpha.
- ``number_of_texture_buffers`` (int32):  [Read-Write] Number of texture used to transfer the texture from the GPU to the system memory.
  A smaller number is most likely to block the GPU (wait for the transfer to complete).
  A bigger number is most likely to increase latency.
  note: Some Capture are not are executed on the GPU. If it's the case then no buffer will be needed and no buffer will be created.
- ``override_desired_size`` (bool):  [Read-Write] Use the default back buffer size or specify a specific size to capture.
- ``override_pixel_format`` (bool):  [Read-Write] Use the default back buffer pixel format or specify a specific the pixel format to capture.
- ``write_options`` (ImageWriteOptions):  [Read-Write] Options on how to save the images.

<a id="unreal.FileMediaOutput.write_options"></a>

#### write_options

```python
@property
def write_options() -> ImageWriteOptions
```

(ImageWriteOptions):  [Read-Write] Options on how to save the images.

<a id="unreal.FileMediaOutput.write_options"></a>

#### write_options

```python
@write_options.setter
def write_options(value: ImageWriteOptions) -> None
```

<a id="unreal.FileMediaOutput.file_path"></a>

#### file_path

```python
@property
def file_path() -> DirectoryPath
```

(DirectoryPath):  [Read-Write] The file path for the images.

<a id="unreal.FileMediaOutput.file_path"></a>

#### file_path

```python
@file_path.setter
def file_path(value: DirectoryPath) -> None
```

<a id="unreal.FileMediaOutput.base_file_name"></a>

#### base_file_name

```python
@property
def base_file_name() -> str
```

(str):  [Read-Write] The base file name of the images. The frame number will be append to the base file name.

<a id="unreal.FileMediaOutput.base_file_name"></a>

#### base_file_name

```python
@base_file_name.setter
def base_file_name(value: str) -> None
```

<a id="unreal.FileMediaOutput.override_desired_size"></a>

#### override_desired_size

```python
@property
def override_desired_size() -> bool
```

(bool):  [Read-Write] Use the default back buffer size or specify a specific size to capture.

<a id="unreal.FileMediaOutput.override_desired_size"></a>

#### override_desired_size

```python
@override_desired_size.setter
def override_desired_size(value: bool) -> None
```

<a id="unreal.FileMediaOutput.desired_size"></a>

#### desired_size

```python
@property
def desired_size() -> IntPoint
```

(IntPoint):  [Read-Write] Use the default back buffer size or specify a specific size to capture.

<a id="unreal.FileMediaOutput.desired_size"></a>

#### desired_size

```python
@desired_size.setter
def desired_size(value: IntPoint) -> None
```

<a id="unreal.FileMediaOutput.override_pixel_format"></a>

#### override_pixel_format

```python
@property
def override_pixel_format() -> bool
```

(bool):  [Read-Write] Use the default back buffer pixel format or specify a specific the pixel format to capture.

<a id="unreal.FileMediaOutput.override_pixel_format"></a>

#### override_pixel_format

```python
@override_pixel_format.setter
def override_pixel_format(value: bool) -> None
```

<a id="unreal.FileMediaOutput.desired_pixel_format"></a>

#### desired_pixel_format

```python
@property
def desired_pixel_format() -> FileMediaOutputPixelFormat
```

(FileMediaOutputPixelFormat):  [Read-Write] Use the default back buffer pixel format or specify a specific the pixel format to capture.

<a id="unreal.FileMediaOutput.desired_pixel_format"></a>

#### desired_pixel_format

```python
@desired_pixel_format.setter
def desired_pixel_format(value: FileMediaOutputPixelFormat) -> None
```

<a id="unreal.FileMediaOutput.invert_alpha"></a>

#### invert_alpha

```python
@property
def invert_alpha() -> bool
```

(bool):  [Read-Write] Invert the alpha for formats that support alpha.

<a id="unreal.FileMediaOutput.invert_alpha"></a>

#### invert_alpha

```python
@invert_alpha.setter
def invert_alpha(value: bool) -> None
```

<a id="unreal.AvaBroadcast"></a>