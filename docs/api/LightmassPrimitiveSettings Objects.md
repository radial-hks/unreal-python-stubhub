## LightmassPrimitiveSettings Objects

```python
class LightmassPrimitiveSettings(StructBase)
```

Per-object settings for Lightmass

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``diffuse_boost`` (float):  [Read-Write] Scales the diffuse contribution of all materials applied to this object.
- ``emissive_boost`` (float):  [Read-Write] Scales the emissive contribution of all materials applied to this object.
- ``fully_occluded_samples_fraction`` (float):  [Read-Write] Fraction of samples taken that must be occluded in order to reach full occlusion.
- ``shadow_indirect_only`` (bool):  [Read-Write] If true, this object will only shadow indirect lighting.
- ``use_emissive_for_static_lighting`` (bool):  [Read-Write] If true, allow using the emissive for static lighting.
- ``use_two_sided_lighting`` (bool):  [Read-Write] If true, this object will be lit as if it receives light from both sides of its polygons.
- ``use_vertex_normal_for_hemisphere_gather`` (bool):  [Read-Write] Typically the triangle normal is used for hemisphere gathering which prevents incorrect self-shadowing from artist-tweaked vertex normals.
  However in the case of foliage whose vertex normal has been setup to match the underlying terrain, gathering in the direction of the vertex normal is desired.

<a id="unreal.LightmassPrimitiveSettings.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.BlackboardEntry"></a>