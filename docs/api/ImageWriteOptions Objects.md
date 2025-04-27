## ImageWriteOptions Objects

```python
class ImageWriteOptions(StructBase)
```

Options specific to writing image files to disk

**C++ Source:**

- **Module**: ImageWriteQueue
- **File**: ImageWriteBlueprintLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``async_`` (bool):  [Read-Write] Whether to perform the writing asynchronously, or to block the game thread until it is complete
- ``compression_quality`` (int32):  [Read-Write] An image format specific compression setting. Either 0 (Default) or 1 (Uncompressed) for EXRs, or a value between 0 and 100.
- ``format`` (DesiredImageFormat):  [Read-Write] The desired output image format to write to disk
- ``on_complete`` (OnImageWriteComplete):  [Read-Write] A callback to invoke when the image has been written, or there was an error
- ``overwrite_file`` (bool):  [Read-Write] Whether to overwrite the image if it already exists

<a id="unreal.ImageWriteOptions.__init__"></a>

#### __init__

```python
def __init__(format: DesiredImageFormat = DesiredImageFormat.PNG,
             on_complete: OnImageWriteComplete = OnImageWriteComplete(),
             compression_quality: int = 0,
             overwrite_file: bool = False,
             async_: bool = False) -> None
```

<a id="unreal.ImageWriteOptions.format"></a>

#### format

```python
@property
def format() -> DesiredImageFormat
```

(DesiredImageFormat):  [Read-Write] The desired output image format to write to disk

<a id="unreal.ImageWriteOptions.format"></a>

#### format

```python
@format.setter
def format(value: DesiredImageFormat) -> None
```

<a id="unreal.ImageWriteOptions.on_complete"></a>

#### on_complete

```python
@property
def on_complete() -> OnImageWriteComplete
```

(OnImageWriteComplete):  [Read-Write] A callback to invoke when the image has been written, or there was an error

<a id="unreal.ImageWriteOptions.on_complete"></a>

#### on_complete

```python
@on_complete.setter
def on_complete(value: OnImageWriteComplete) -> None
```

<a id="unreal.ImageWriteOptions.compression_quality"></a>

#### compression_quality

```python
@property
def compression_quality() -> int
```

(int32):  [Read-Write] An image format specific compression setting. Either 0 (Default) or 1 (Uncompressed) for EXRs, or a value between 0 and 100.

<a id="unreal.ImageWriteOptions.compression_quality"></a>

#### compression_quality

```python
@compression_quality.setter
def compression_quality(value: int) -> None
```

<a id="unreal.ImageWriteOptions.overwrite_file"></a>

#### overwrite_file

```python
@property
def overwrite_file() -> bool
```

(bool):  [Read-Write] Whether to overwrite the image if it already exists

<a id="unreal.ImageWriteOptions.overwrite_file"></a>

#### overwrite_file

```python
@overwrite_file.setter
def overwrite_file(value: bool) -> None
```

<a id="unreal.ImageWriteOptions.async_"></a>

#### async_

```python
@property
def async_() -> bool
```

(bool):  [Read-Write] Whether to perform the writing asynchronously, or to block the game thread until it is complete

<a id="unreal.ImageWriteOptions.async_"></a>

#### async_

```python
@async_.setter
def async_(value: bool) -> None
```

<a id="unreal.GrassVariety"></a>