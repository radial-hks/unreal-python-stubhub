## FontFacePlatformRasterizationOverrides Objects

```python
class FontFacePlatformRasterizationOverrides(StructBase)
```

Remapping of rasterization modes

**C++ Source:**

- **Module**: Engine
- **File**: FontFace.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``msdf_override`` (FontRasterizationMode):  [Read-Write] Rasterization mode to be used instead of Sharp (Multi-Channel SDF)
- ``sdf_approximation_override`` (FontRasterizationMode):  [Read-Write] Rasterization mode to be used instead of Fast (Approximate SDF)
- ``sdf_override`` (FontRasterizationMode):  [Read-Write] Rasterization mode to be used instead of Smooth (Plain SDF)

<a id="unreal.FontFacePlatformRasterizationOverrides.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.DeviceColorData"></a>