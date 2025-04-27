## EXRFileCompositingOutput Objects

```python
class EXRFileCompositingOutput(CompositingElementOutput)
```

EXRFile Compositing Output

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: CompositingElementOutputs.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``compression`` (ExrCompressionOptions):  [Read-Write]
- ``enabled`` (bool):  [Read-Write]
- ``filename_format`` (str):  [Read-Write] The format to use for the resulting filename. Extension will be added automatically. Any tokens of the form {token} will be replaced with the corresponding value:
  {frame} - The current frame number
- ``output_directiory`` (DirectoryPath):  [Read-Write]
- ``output_frame_rate`` (FrameRate):  [Read-Write]
- ``pass_name`` (Name):  [Read-Write]

<a id="unreal.EXRFileCompositingOutput.output_directiory"></a>

#### output_directiory

```python
@property
def output_directiory() -> DirectoryPath
```

(DirectoryPath):  [Read-Write]

<a id="unreal.EXRFileCompositingOutput.output_directiory"></a>

#### output_directiory

```python
@output_directiory.setter
def output_directiory(value: DirectoryPath) -> None
```

<a id="unreal.EXRFileCompositingOutput.filename_format"></a>

#### filename_format

```python
@property
def filename_format() -> str
```

(str):  [Read-Write] The format to use for the resulting filename. Extension will be added automatically. Any tokens of the form {token} will be replaced with the corresponding value:
{frame} - The current frame number

<a id="unreal.EXRFileCompositingOutput.filename_format"></a>

#### filename_format

```python
@filename_format.setter
def filename_format(value: str) -> None
```

<a id="unreal.EXRFileCompositingOutput.output_frame_rate"></a>

#### output_frame_rate

```python
@property
def output_frame_rate() -> FrameRate
```

(FrameRate):  [Read-Write]

<a id="unreal.EXRFileCompositingOutput.output_frame_rate"></a>

#### output_frame_rate

```python
@output_frame_rate.setter
def output_frame_rate(value: FrameRate) -> None
```

<a id="unreal.EXRFileCompositingOutput.compression"></a>

#### compression

```python
@property
def compression() -> ExrCompressionOptions
```

(ExrCompressionOptions):  [Read-Write]

<a id="unreal.EXRFileCompositingOutput.compression"></a>

#### compression

```python
@compression.setter
def compression(value: ExrCompressionOptions) -> None
```

<a id="unreal.CompositingElementTransform"></a>