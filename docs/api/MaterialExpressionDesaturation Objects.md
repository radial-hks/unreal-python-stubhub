## MaterialExpressionDesaturation Objects

```python
class MaterialExpressionDesaturation(MaterialExpression)
```

Material Expression Desaturation

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionDesaturation.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``luminance_factors`` (LinearColor):  [Read-Write] * Luminance factors for converting a color to greyscale.
  *
  * The default luminance factors values are now derived from the working color space. For uses cases
  * outside scene rendering, users are responsible for updating these factors accordingly. For example,
  * factors derived from an AP1 working color space would not be applicable to UI domain materials that
  * remain in sRGB/Rec.709 and thus should instead use approximately [0.2126, 0.7152, 0.0722].
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]

<a id="unreal.MaterialExpressionDistance"></a>