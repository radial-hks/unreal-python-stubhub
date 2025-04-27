## SceneTextureId Objects

```python
class SceneTextureId(EnumBase)
```

like EPassInputId but can expose more e.g. GBuffer

**C++ Source:**

- **Module**: Engine
- **File**: MaterialSceneTextureId.h

<a id="unreal.SceneTextureId.PPI_SCENE_COLOR"></a>

#### PPI_SCENE_COLOR

0: Scene color, normal post process passes should use PostProcessInput0

<a id="unreal.SceneTextureId.PPI_SCENE_DEPTH"></a>

#### PPI_SCENE_DEPTH

1: Scene depth, single channel, contains the linear depth of the opaque objects

<a id="unreal.SceneTextureId.PPI_DIFFUSE_COLOR"></a>

#### PPI_DIFFUSE_COLOR

2: Material diffuse, RGB color (computed from GBuffer)

<a id="unreal.SceneTextureId.PPI_SPECULAR_COLOR"></a>

#### PPI_SPECULAR_COLOR

3: Material specular, RGB color (computed from GBuffer)

<a id="unreal.SceneTextureId.PPI_SUBSURFACE_COLOR"></a>

#### PPI_SUBSURFACE_COLOR

4: Material subsurface, RGB color (GBuffer, only for some ShadingModels)

<a id="unreal.SceneTextureId.PPI_BASE_COLOR"></a>

#### PPI_BASE_COLOR

5: Material base, RGB color (GBuffer), can be modified on read by the ShadingModel, consider StoredBasedColor

<a id="unreal.SceneTextureId.PPI_SPECULAR"></a>

#### PPI_SPECULAR

6: Material specular, single channel (GBuffer), can be modified on read by the ShadingModel, consider StoredSpecular

<a id="unreal.SceneTextureId.PPI_METALLIC"></a>

#### PPI_METALLIC

7: Material metallic, single channel (GBuffer)

<a id="unreal.SceneTextureId.PPI_WORLD_NORMAL"></a>

#### PPI_WORLD_NORMAL

8: Normal, RGB in -1..1 range, not normalized (GBuffer)

<a id="unreal.SceneTextureId.PPI_SEPARATE_TRANSLUCENCY"></a>

#### PPI_SEPARATE_TRANSLUCENCY

9: Not yet supported

<a id="unreal.SceneTextureId.PPI_OPACITY"></a>

#### PPI_OPACITY

10: Material opacity, single channel (GBuffer)

<a id="unreal.SceneTextureId.PPI_ROUGHNESS"></a>

#### PPI_ROUGHNESS

11: Material roughness, single channel (GBuffer)

<a id="unreal.SceneTextureId.PPI_MATERIAL_AO"></a>

#### PPI_MATERIAL_AO

12: Material ambient occlusion, single channel (GBuffer)

<a id="unreal.SceneTextureId.PPI_CUSTOM_DEPTH"></a>

#### PPI_CUSTOM_DEPTH

13: Scene depth, single channel, contains the linear depth of the opaque objects rendered with CustomDepth (mesh property)

<a id="unreal.SceneTextureId.PPI_POST_PROCESS_INPUT0"></a>

#### PPI_POST_PROCESS_INPUT0

14: Input #0 of this postprocess pass, usually the only one hooked up

<a id="unreal.SceneTextureId.PPI_POST_PROCESS_INPUT1"></a>

#### PPI_POST_PROCESS_INPUT1

15: Input #1 of this postprocess pass, usually not used

<a id="unreal.SceneTextureId.PPI_POST_PROCESS_INPUT2"></a>

#### PPI_POST_PROCESS_INPUT2

16: Input #2 of this postprocess pass, usually not used

<a id="unreal.SceneTextureId.PPI_POST_PROCESS_INPUT3"></a>

#### PPI_POST_PROCESS_INPUT3

17: Input #3 of this postprocess pass, usually not used

<a id="unreal.SceneTextureId.PPI_POST_PROCESS_INPUT4"></a>

#### PPI_POST_PROCESS_INPUT4

18: Input #4 of this postprocess pass, usually not used

<a id="unreal.SceneTextureId.PPI_POST_PROCESS_INPUT5"></a>

#### PPI_POST_PROCESS_INPUT5

19: Input #5 of this postprocess pass, usually not used

<a id="unreal.SceneTextureId.PPI_POST_PROCESS_INPUT6"></a>

#### PPI_POST_PROCESS_INPUT6

20: Input #6 of this postprocess pass, usually not used

<a id="unreal.SceneTextureId.PPI_DECAL_MASK"></a>

#### PPI_DECAL_MASK

21: Decal Mask, single bit (was moved to stencil for better performance, not accessible at the moment)

<a id="unreal.SceneTextureId.PPI_SHADING_MODEL_COLOR"></a>

#### PPI_SHADING_MODEL_COLOR

22: Shading model

<a id="unreal.SceneTextureId.PPI_SHADING_MODEL_ID"></a>

#### PPI_SHADING_MODEL_ID

23: Shading model ID

<a id="unreal.SceneTextureId.PPI_AMBIENT_OCCLUSION"></a>

#### PPI_AMBIENT_OCCLUSION

24: Ambient Occlusion, single channel

<a id="unreal.SceneTextureId.PPI_CUSTOM_STENCIL"></a>

#### PPI_CUSTOM_STENCIL

25: Scene stencil, contains CustomStencil mesh property of the opaque objects rendered with CustomDepth

<a id="unreal.SceneTextureId.PPI_STORED_BASE_COLOR"></a>

#### PPI_STORED_BASE_COLOR

26: Material base, RGB color (GBuffer)

<a id="unreal.SceneTextureId.PPI_STORED_SPECULAR"></a>

#### PPI_STORED_SPECULAR

27: Material specular, single channel (GBuffer)

<a id="unreal.SceneTextureId.PPI_VELOCITY"></a>

#### PPI_VELOCITY

28: Scene Velocity

<a id="unreal.SceneTextureId.PPI_WORLD_TANGENT"></a>

#### PPI_WORLD_TANGENT

29: Tangent, RGB in -1..1 range, not normalized (GBuffer)

<a id="unreal.SceneTextureId.PPI_ANISOTROPY"></a>

#### PPI_ANISOTROPY

30: Material anisotropy, single channel (GBuffer)

<a id="unreal.SpeedTreeGeometryType"></a>