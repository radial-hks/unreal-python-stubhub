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

#### MSM\_UNLIT

0

<a id="unreal.MaterialShadingModel.MSM_DEFAULT_LIT"></a>

#### MSM\_DEFAULT\_LIT

1

<a id="unreal.MaterialShadingModel.MSM_SUBSURFACE"></a>

#### MSM\_SUBSURFACE

2

<a id="unreal.MaterialShadingModel.MSM_PREINTEGRATED_SKIN"></a>

#### MSM\_PREINTEGRATED\_SKIN

3

<a id="unreal.MaterialShadingModel.MSM_CLEAR_COAT"></a>

#### MSM\_CLEAR\_COAT

4

<a id="unreal.MaterialShadingModel.MSM_SUBSURFACE_PROFILE"></a>

#### MSM\_SUBSURFACE\_PROFILE

5

<a id="unreal.MaterialShadingModel.MSM_TWO_SIDED_FOLIAGE"></a>

#### MSM\_TWO\_SIDED\_FOLIAGE

6

<a id="unreal.MaterialShadingModel.MSM_HAIR"></a>

#### MSM\_HAIR

7

<a id="unreal.MaterialShadingModel.MSM_CLOTH"></a>

#### MSM\_CLOTH

8

<a id="unreal.MaterialShadingModel.MSM_EYE"></a>

#### MSM\_EYE

9

<a id="unreal.MaterialShadingModel.MSM_SINGLE_LAYER_WATER"></a>

#### MSM\_SINGLE\_LAYER\_WATER

10

<a id="unreal.MaterialShadingModel.MSM_THIN_TRANSLUCENT"></a>

#### MSM\_THIN\_TRANSLUCENT

11

<a id="unreal.MaterialShadingModel.MSM_FROM_MATERIAL_EXPRESSION"></a>

#### MSM\_FROM\_MATERIAL\_EXPRESSION

14: Shading model will be determined by the Material Expression Graph,
              by utilizing the 'Shading Model' MaterialAttribute output pin.

<a id="unreal.MaterialLightingModel"></a>