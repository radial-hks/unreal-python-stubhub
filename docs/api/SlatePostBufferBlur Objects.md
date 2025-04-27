## SlatePostBufferBlur Objects

```python
class SlatePostBufferBlur(SlateRHIPostBufferProcessor)
```

Slate Post Buffer Processor that performs a simple gaussian blur to the backbuffer

Create a new asset deriving from this class to use / modify settings.

**C++ Source:**

- **Module**: SlateRHIRenderer
- **File**: SlatePostBufferBlur.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``gaussian_blur_strength`` (float):  [Read-Write]

<a id="unreal.SlatePostBufferBlur.gaussian_blur_strength"></a>

#### gaussian_blur_strength

```python
@property
def gaussian_blur_strength() -> float
```

(float):  [Read-Write]

<a id="unreal.SlatePostBufferBlur.gaussian_blur_strength"></a>

#### gaussian_blur_strength

```python
@gaussian_blur_strength.setter
def gaussian_blur_strength(value: float) -> None
```

<a id="unreal.SlateRHIRendererSettings"></a>