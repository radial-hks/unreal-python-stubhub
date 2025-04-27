## MaterialExpressionSubstrateEyeBSDF Objects

```python
class MaterialExpressionSubstrateEyeBSDF(MaterialExpressionSubstrateBSDF)
```

Material Expression Substrate Eye BSDF

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionSubstrate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]
- ``subsurface_profile`` (SubsurfaceProfile):  [Read-Write] SubsurfaceProfile, for Subsurface Scattering diffusion.

<a id="unreal.MaterialExpressionSubstrateEyeBSDF.subsurface_profile"></a>

#### subsurface_profile

```python
@property
def subsurface_profile() -> SubsurfaceProfile
```

(SubsurfaceProfile):  [Read-Only] SubsurfaceProfile, for Subsurface Scattering diffusion.

<a id="unreal.MaterialExpressionStrataEyeBSDF"></a>