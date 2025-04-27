## MaterialEditorInstanceConstant Objects

```python
class MaterialEditorInstanceConstant(MaterialEditorParameters)
```

Material Editor Instance Constant

**C++ Source:**

- **Module**: UnrealEd
- **File**: MaterialEditorInstanceConstant.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_property_overrides`` (MaterialInstanceBasePropertyOverrides):  [Read-Write]
- ``lightmass_settings`` (LightmassParameterizedMaterialSettings):  [Read-Write] The Lightmass override settings for this object.
- ``nanite_override`` (bool):  [Read-Write] When set we will use the override from NaniteOverrideMaterial. Otherwise we inherit any override on the parent.
- ``nanite_override_material`` (MaterialInterface):  [Read-Write] An override material which will be used instead of this one when rendering with nanite.
- ``override_subsurface_profile`` (bool):  [Read-Write] Defines if SubsurfaceProfile from tis instance is used or it uses the parent one.
- ``parameter_groups`` (Array[EditorParameterGroup]):  [Read-Write]
- ``parent`` (MaterialInterface):  [Read-Write] since the Parent may point across levels and the property editor needs to import this text, it must be marked lazy so it doesn't set itself to NULL in FindImportedObject
- ``phys_material`` (PhysicalMaterial):  [Read-Write] Physical material to use for this graphics material. Used for sounds, effects etc.
- ``post_process_overrides`` (MaterialEditorPostProcessOverrides):  [Read-Write] Overrides specific to Post Process domain materials.
- ``refraction_depth_bias`` (float):  [Read-Write] This is the refraction depth bias, larger values offset distortion to prevent closer objects from rendering into the distorted surface at acute viewing angles but increases the disconnect between surface and where the refraction starts.
- ``subsurface_profile`` (SubsurfaceProfile):  [Read-Write] SubsurfaceProfile, for Screen Space Subsurface Scattering
- ``use_old_style_mic_editor_groups`` (bool):  [Read-Write] Should we use old style typed arrays for unassigned parameters instead of a None group (new style)?

<a id="unreal.MaterialEditorInstanceConstant.subsurface_profile"></a>

#### subsurface_profile

```python
@property
def subsurface_profile() -> SubsurfaceProfile
```

(SubsurfaceProfile):  [Read-Only] SubsurfaceProfile, for Screen Space Subsurface Scattering

<a id="unreal.MaterialEditorMeshComponent"></a>