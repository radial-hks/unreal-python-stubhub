## MaterialExpressionSubstrateSlabBSDF Objects

```python
class MaterialExpressionSubstrateSlabBSDF(MaterialExpressionSubstrateBSDF)
```

Material Expression Substrate Slab BSDF

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionSubstrate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]
- ``specular_profile`` (SpecularProfile):  [Read-Write] SpecularProfile, for modulating specular appearance and simulating more complex visuals such as iridescence.
- ``subsurface_profile`` (SubsurfaceProfile):  [Read-Write] SubsurfaceProfile, for Screen Space Subsurface Scattering. The profile needs to be set up on both the Substrate diffuse node, and the material node at the moment.
- ``use_sss_diffusion`` (bool):  [Read-Write] Whether to use light diffusion (i.e., SSS diffusion) or wrap-approximation for material with scattering behavior. This option trades quality over performance and will result into visual differences.

<a id="unreal.MaterialExpressionSubstrateSlabBSDF.subsurface_profile"></a>

#### subsurface_profile

```python
@property
def subsurface_profile() -> SubsurfaceProfile
```

(SubsurfaceProfile):  [Read-Only] SubsurfaceProfile, for Screen Space Subsurface Scattering. The profile needs to be set up on both the Substrate diffuse node, and the material node at the moment.

<a id="unreal.MaterialExpressionSubstrateSlabBSDF.specular_profile"></a>

#### specular_profile

```python
@property
def specular_profile() -> SpecularProfile
```

(SpecularProfile):  [Read-Only] SpecularProfile, for modulating specular appearance and simulating more complex visuals such as iridescence.

<a id="unreal.MaterialExpressionStrataSlabBSDF"></a>