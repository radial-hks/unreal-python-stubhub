## ViewModeIndex Objects

```python
class ViewModeIndex(EnumBase)
```

Define view modes to get specific show flag settings (some on, some off and some are not altered)
Don't change the order, the ID is serialized with the editor

**C++ Source:**

- **Module**: Engine
- **File**: EngineBaseTypes.h

<a id="unreal.ViewModeIndex.VMI_BRUSH_WIREFRAME"></a>

#### VMI_BRUSH_WIREFRAME

0: Wireframe w/ brushes.

<a id="unreal.ViewModeIndex.VMI_WIREFRAME"></a>

#### VMI_WIREFRAME

1: Wireframe w/ BSP.

<a id="unreal.ViewModeIndex.VMI_UNLIT"></a>

#### VMI_UNLIT

2: Unlit.

<a id="unreal.ViewModeIndex.VMI_LIT"></a>

#### VMI_LIT

3: Lit.

<a id="unreal.ViewModeIndex.VMI_LIT_DETAIL_LIGHTING"></a>

#### VMI_LIT_DETAIL_LIGHTING

4

<a id="unreal.ViewModeIndex.VMI_LIGHTING_ONLY"></a>

#### VMI_LIGHTING_ONLY

5: Lit wo/ materials.

<a id="unreal.ViewModeIndex.VMI_LIGHT_COMPLEXITY"></a>

#### VMI_LIGHT_COMPLEXITY

6: Colored according to light count.

<a id="unreal.ViewModeIndex.VMI_SHADER_COMPLEXITY"></a>

#### VMI_SHADER_COMPLEXITY

8: Colored according to shader complexity.

<a id="unreal.ViewModeIndex.VMI_LIGHTMAP_DENSITY"></a>

#### VMI_LIGHTMAP_DENSITY

9: Colored according to world-space LightMap texture density.

<a id="unreal.ViewModeIndex.VMI_LIT_LIGHTMAP_DENSITY"></a>

#### VMI_LIT_LIGHTMAP_DENSITY

10: Colored according to light count - showing lightmap texel density on texture mapped objects.

<a id="unreal.ViewModeIndex.VMI_REFLECTION_OVERRIDE"></a>

#### VMI_REFLECTION_OVERRIDE

11

<a id="unreal.ViewModeIndex.VMI_VISUALIZE_BUFFER"></a>

#### VMI_VISUALIZE_BUFFER

12

<a id="unreal.ViewModeIndex.VMI_STATIONARY_LIGHT_OVERLAP"></a>

#### VMI_STATIONARY_LIGHT_OVERLAP

14: Colored according to stationary light overlap.

<a id="unreal.ViewModeIndex.VMI_COLLISION_PAWN"></a>

#### VMI_COLLISION_PAWN

15

<a id="unreal.ViewModeIndex.VMI_COLLISION_VISIBILITY"></a>

#### VMI_COLLISION_VISIBILITY

16

<a id="unreal.ViewModeIndex.VMI_LOD_COLORATION"></a>

#### VMI_LOD_COLORATION

18: Colored according to the current LOD index.

<a id="unreal.ViewModeIndex.VMI_QUAD_OVERDRAW"></a>

#### VMI_QUAD_OVERDRAW

19: Colored according to the quad coverage.

<a id="unreal.ViewModeIndex.VMI_PRIMITIVE_DISTANCE_ACCURACY"></a>

#### VMI_PRIMITIVE_DISTANCE_ACCURACY

20: Visualize the accuracy of the primitive distance computed for texture streaming.

<a id="unreal.ViewModeIndex.VMI_MESH_UV_DENSITY_ACCURACY"></a>

#### VMI_MESH_UV_DENSITY_ACCURACY

21: Visualize the accuracy of the mesh UV densities computed for texture streaming.

<a id="unreal.ViewModeIndex.VMI_SHADER_COMPLEXITY_WITH_QUAD_OVERDRAW"></a>

#### VMI_SHADER_COMPLEXITY_WITH_QUAD_OVERDRAW

22: Colored according to shader complexity, including quad overdraw.

<a id="unreal.ViewModeIndex.VMI_HLOD_COLORATION"></a>

#### VMI_HLOD_COLORATION

23: Colored according to the current HLOD index.

<a id="unreal.ViewModeIndex.VMI_GROUP_LOD_COLORATION"></a>

#### VMI_GROUP_LOD_COLORATION

24: Group item for LOD and HLOD coloration

<a id="unreal.ViewModeIndex.VMI_MATERIAL_TEXTURE_SCALE_ACCURACY"></a>

#### VMI_MATERIAL_TEXTURE_SCALE_ACCURACY

25: Visualize the accuracy of the material texture scales used for texture streaming.

<a id="unreal.ViewModeIndex.VMI_REQUIRED_TEXTURE_RESOLUTION"></a>

#### VMI_REQUIRED_TEXTURE_RESOLUTION

26: Compare the required texture resolution to the actual resolution.

<a id="unreal.ViewModeIndex.VMI_PATH_TRACING"></a>

#### VMI_PATH_TRACING

27: Run path tracing pipeline

<a id="unreal.ViewModeIndex.VMI_RAY_TRACING_DEBUG"></a>

#### VMI_RAY_TRACING_DEBUG

28: Run ray tracing debug pipeline

<a id="unreal.ViewModeIndex.VMI_VISUALIZE_NANITE"></a>

#### VMI_VISUALIZE_NANITE

29: Visualize various aspects of Nanite

<a id="unreal.ViewModeIndex.VMI_VIRTUAL_TEXTURE_PENDING_MIPS"></a>

#### VMI_VIRTUAL_TEXTURE_PENDING_MIPS

30: Compare the required texture resolution to the actual resolution.

<a id="unreal.ViewModeIndex.VMI_VISUALIZE_LUMEN"></a>

#### VMI_VISUALIZE_LUMEN

31: Visualize Lumen debug views

<a id="unreal.ViewModeIndex.VMI_VISUALIZE_VIRTUAL_SHADOW_MAP"></a>

#### VMI_VISUALIZE_VIRTUAL_SHADOW_MAP

32: Visualize virtual shadow map

<a id="unreal.ViewModeIndex.VMI_VISUALIZE_GPU_SKIN_CACHE"></a>

#### VMI_VISUALIZE_GPU_SKIN_CACHE

33: Visualize Skin Cache.

<a id="unreal.ViewModeIndex.VMI_VISUALIZE_SUBSTRATE"></a>

#### VMI_VISUALIZE_SUBSTRATE

34: Visualize Substrate debug views

<a id="unreal.ViewModeIndex.VMI_VISUALIZE_GROOM"></a>

#### VMI_VISUALIZE_GROOM

35: Visualize Groom debug views

<a id="unreal.ViewModeIndex.VMI_LWC_COMPLEXITY"></a>

#### VMI_LWC_COMPLEXITY

36

<a id="unreal.ViewModeIndex.VMI_LIT_WIREFRAME"></a>

#### VMI_LIT_WIREFRAME

37: Lit Wireframe.

<a id="unreal.ViewModeIndex.VMI_VISUALIZE_ACTOR_COLORATION"></a>

#### VMI_VISUALIZE_ACTOR_COLORATION

38: Visualize Actor Coloration.

<a id="unreal.ViewModeIndex.VMI_UNKNOWN"></a>

#### VMI_UNKNOWN

255: VMI_Unknown - The value assigned to VMI_Unknown must be the highest possible of any member of EViewModeIndex, or GetViewModeName might seg-fault

<a id="unreal.WidgetTestAppearLocation"></a>