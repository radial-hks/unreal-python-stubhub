## MaterialExpressionSubstrateShadingModels Objects

```python
class MaterialExpressionSubstrateShadingModels(MaterialExpressionSubstrateBSDF
                                               )
```

Material Expression Substrate Shading Models

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionSubstrate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]
- ``shading_model_override`` (MaterialShadingModel):  [Read-Write] Always show at the bottom of the pin list
- ``subsurface_profile`` (SubsurfaceProfile):  [Read-Write] SubsurfaceProfile, for Screen Space Subsurface Scattering. The profile needs to be set up on both the Substrate diffuse node, and the material node at the moment.

<a id="unreal.MaterialExpressionSubstrateShadingModels.subsurface_profile"></a>

#### subsurface_profile

```python
@property
def subsurface_profile() -> SubsurfaceProfile
```

(SubsurfaceProfile):  [Read-Only] SubsurfaceProfile, for Screen Space Subsurface Scattering. The profile needs to be set up on both the Substrate diffuse node, and the material node at the moment.

<a id="unreal.MaterialExpressionStrataLegacyConversion"></a>