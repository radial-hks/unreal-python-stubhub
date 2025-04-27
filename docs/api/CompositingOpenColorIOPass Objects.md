## CompositingOpenColorIOPass Objects

```python
class CompositingOpenColorIOPass(CompositingElementTransform)
```

UCompositingOpenColorIOPass

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: CompositingElementTransforms.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color_conversion_settings`` (OpenColorIOColorConversionSettings):  [Read-Write] Color grading settings.
- ``enabled`` (bool):  [Read-Write]
- ``intermediate`` (bool):  [Read-Write] Marks this pass for 'internal use only' - prevents it from being exposed to parent elements.
  When set, render target resources used by this element will be reused. For transforms, all 'Intermediate'
  passes are available to the next transform pass, and released after that.
- ``pass_name`` (Name):  [Read-Write]

<a id="unreal.CompositingOpenColorIOPass.color_conversion_settings"></a>

#### color_conversion_settings

```python
@property
def color_conversion_settings() -> OpenColorIOColorConversionSettings
```

(OpenColorIOColorConversionSettings):  [Read-Write] Color grading settings.

<a id="unreal.CompositingOpenColorIOPass.color_conversion_settings"></a>

#### color_conversion_settings

```python
@color_conversion_settings.setter
def color_conversion_settings(
        value: OpenColorIOColorConversionSettings) -> None
```

<a id="unreal.ComposureLibrary"></a>