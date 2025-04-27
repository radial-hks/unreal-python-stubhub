## InterchangeUsdTranslatorSettings Objects

```python
class InterchangeUsdTranslatorSettings(InterchangeTranslatorSettings)
```

Interchange Usd Translator Settings

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeImport
- **File**: InterchangeUsdTranslator.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``geometry_purpose`` (int32):  [Read-Write] Only import geometry prims with these specific purposes from the USD file
- ``interpolation_type`` (UsdInterpolationType):  [Read-Write] Describes how to interpolate between a timeSample value and the next
- ``material_purpose`` (Name):  [Read-Write] Specifies which material purpose to use when parsing USD material bindings, in addition to the "allPurpose" fallback
- ``override_stage_options`` (bool):  [Read-Write] Whether to use the specified StageOptions instead of the stage's own settings
- ``render_context`` (Name):  [Read-Write] Specifies which set of shaders to use when parsing USD materials, in addition to the universal render context.
- ``stage_options`` (UsdStageOptions):  [Read-Write] Custom StageOptions to use for the stage

<a id="unreal.InterchangeUSDTranslator"></a>