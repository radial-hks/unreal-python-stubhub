## LightmassMaterialInterfaceSettings Objects

```python
class LightmassMaterialInterfaceSettings(StructBase)
```

UMaterial interface settings for Lightmass

**C++ Source:**

- **Module**: Engine
- **File**: MaterialInterface.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cast_shadow_as_masked`` (bool):  [Read-Write] If true, forces translucency to cast static shadows as if the material were masked.
- ``diffuse_boost`` (float):  [Read-Write] Scales the diffuse contribution of this material to static lighting.
- ``export_resolution_scale`` (float):  [Read-Write] Scales the resolution that this material's attributes were exported at.
  This is useful for increasing material resolution when details are needed.

<a id="unreal.LightmassMaterialInterfaceSettings.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.MaterialOverrideNanite"></a>