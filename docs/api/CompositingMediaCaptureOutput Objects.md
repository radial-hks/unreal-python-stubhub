## CompositingMediaCaptureOutput Objects

```python
class CompositingMediaCaptureOutput(ColorConverterOutputPass)
```

Compositing Media Capture Output

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: CompositingElementOutputs.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``capture_output`` (MediaOutput):  [Read-Write]
- ``color_converter`` (CompositingElementTransform):  [Read-Write]
- ``enabled`` (bool):  [Read-Write]
- ``pass_name`` (Name):  [Read-Write]

<a id="unreal.CompositingMediaCaptureOutput.capture_output"></a>

#### capture_output

```python
@property
def capture_output() -> MediaOutput
```

(MediaOutput):  [Read-Write]

<a id="unreal.CompositingMediaCaptureOutput.capture_output"></a>

#### capture_output

```python
@capture_output.setter
def capture_output(value: MediaOutput) -> None
```

<a id="unreal.RenderTargetCompositingOutput"></a>