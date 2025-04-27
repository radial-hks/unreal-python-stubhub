## LightmassDirectionalLightSettings Objects

```python
class LightmassDirectionalLightSettings(LightmassLightSettings)
```

Directional light settings for Lightmass

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``indirect_lighting_saturation`` (float):  [Read-Write] 0 will be completely desaturated, 1 will be unchanged
- ``light_source_angle`` (float):  [Read-Write] Angle that the directional light's emissive surface extends relative to a receiver, affects penumbra sizes.
- ``shadow_exponent`` (float):  [Read-Write] Controls the falloff of shadow penumbras
- ``use_area_shadows_for_stationary_light`` (bool):  [Read-Write] Whether to use area shadows for stationary light precomputed shadowmaps.
  Area shadows get softer the further they are from shadow casters, but require higher lightmap resolution to get the same quality where the shadow is sharp.

<a id="unreal.LightmassDirectionalLightSettings.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.LightmassPointLightSettings"></a>