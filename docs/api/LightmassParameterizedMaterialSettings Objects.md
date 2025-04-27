## LightmassParameterizedMaterialSettings Objects

```python
class LightmassParameterizedMaterialSettings(StructBase)
```

Structure for 'parameterized' Lightmass settings

**C++ Source:**

- **Module**: UnrealEd
- **File**: UnrealEdTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cast_shadow_as_masked`` (LightmassBooleanParameterValue):  [Read-Write] If true, forces translucency to cast static shadows as if the material were masked.
- ``diffuse_boost`` (LightmassScalarParameterValue):  [Read-Write] Scales the diffuse contribution of this material to static lighting.
- ``emissive_boost`` (LightmassScalarParameterValue):  [Read-Write] Scales the emissive contribution of this material to static lighting.
- ``export_resolution_scale`` (LightmassScalarParameterValue):  [Read-Write] Scales the resolution that this material's attributes were exported at.
  This is useful for increasing material resolution when details are needed.

<a id="unreal.LightmassParameterizedMaterialSettings.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.MaterialEditorPostProcessOverrides"></a>