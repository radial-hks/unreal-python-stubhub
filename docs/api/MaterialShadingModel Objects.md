## MaterialShadingModel Objects

```python
class MaterialShadingModel(EnumBase)
```

Specifies the overal rendering/shading model for a material
warning: Check UMaterialInstance::Serialize if changed!

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

<a id="unreal.MaterialShadingModel.MSM_UNLIT"></a>

#### MSM_UNLIT

0

<a id="unreal.MaterialShadingModel.MSM_DEFAULT_LIT"></a>

#### MSM_DEFAULT_LIT

1

<a id="unreal.MaterialShadingModel.MSM_SUBSURFACE"></a>

#### MSM_SUBSURFACE

2

<a id="unreal.MaterialShadingModel.MSM_PREINTEGRATED_SKIN"></a>

#### MSM_PREINTEGRATED_SKIN

3

<a id="unreal.MaterialShadingModel.MSM_CLEAR_COAT"></a>

#### MSM_CLEAR_COAT

4

<a id="unreal.MaterialShadingModel.MSM_SUBSURFACE_PROFILE"></a>

#### MSM_SUBSURFACE_PROFILE

5

<a id="unreal.MaterialShadingModel.MSM_TWO_SIDED_FOLIAGE"></a>

#### MSM_TWO_SIDED_FOLIAGE

6

<a id="unreal.MaterialShadingModel.MSM_HAIR"></a>

#### MSM_HAIR

7

<a id="unreal.MaterialShadingModel.MSM_CLOTH"></a>

#### MSM_CLOTH

8

<a id="unreal.MaterialShadingModel.MSM_EYE"></a>

#### MSM_EYE

9

<a id="unreal.MaterialShadingModel.MSM_SINGLE_LAYER_WATER"></a>

#### MSM_SINGLE_LAYER_WATER

10

<a id="unreal.MaterialShadingModel.MSM_THIN_TRANSLUCENT"></a>

#### MSM_THIN_TRANSLUCENT

11

<a id="unreal.MaterialShadingModel.MSM_FROM_MATERIAL_EXPRESSION"></a>

#### MSM_FROM_MATERIAL_EXPRESSION

14: Shading model will be determined by the Material Expression Graph,
              by utilizing the 'Shading Model' MaterialAttribute output pin.

<a id="unreal.MaterialLightingModel"></a>