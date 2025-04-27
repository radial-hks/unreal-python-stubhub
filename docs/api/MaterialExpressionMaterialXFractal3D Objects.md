## MaterialExpressionMaterialXFractal3D Objects

```python
class MaterialExpressionMaterialXFractal3D(MaterialExpression)
```

Zero-centered 3D Fractal noise in 1, 2, 3 or 4 channels, created by summing several
octaves of 3D Perlin noise, increasing the frequency and decreasing the amplitude at each octave.

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeImport
- **File**: MaterialExpressionFractal3D.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``const_amplitude`` (float):  [Read-Write] only used if Amplitude is not hooked up
- ``const_diminish`` (float):  [Read-Write] only used if Diminish is not hooked up
- ``const_lacunarity`` (float):  [Read-Write] only used if Lacunarity is not hooked up
- ``const_octaves`` (int32):  [Read-Write] only used if Octaves is not hooked up
- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``levels`` (int32):  [Read-Write] 1 = fast but little detail, .. larger numbers cost more performance
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]
- ``output_max`` (float):  [Read-Write]
- ``output_min`` (float):  [Read-Write]
- ``scale`` (float):  [Read-Write] can also be done with a multiply on the Position
- ``turbulence`` (bool):  [Read-Write] How multiple frequencies are getting combined

<a id="unreal.MaterialExpressionFractal3D"></a>