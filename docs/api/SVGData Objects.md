## SVGData Objects

```python
class SVGData(Object)
```

SVGData

**C++ Source:**

- **Plugin**: SVGImporter
- **Module**: SVGImporter
- **File**: SVGData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enable_override_quality`` (bool):  [Read-Write] Enable quality overriding option
- ``override_quality`` (SVGSplineConversionQuality):  [Read-Write] The quality used to convert SVG Spline Data into poly lines
  Changing this value will trigger a re-import (existing geometry will need to be re-generated).
- ``source_file_path`` (str):  [Read-Only]
- ``svg_file_content`` (str):  [Read-Only]
- ``svg_texture`` (Texture2D):  [Read-Only]

<a id="unreal.DaySequenceCollectionAsset"></a>