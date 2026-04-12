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

#### VMI\_BRUSH\_WIREFRAME

0: Wireframe w/ brushes.

<a id="unreal.ViewModeIndex.VMI_WIREFRAME"></a>

#### VMI\_WIREFRAME

1: Wireframe w/ BSP.

<a id="unreal.ViewModeIndex.VMI_UNLIT"></a>

#### VMI\_UNLIT

2: Unlit.

<a id="unreal.ViewModeIndex.VMI_LIT"></a>

#### VMI\_LIT

3: Lit.

<a id="unreal.ViewModeIndex.VMI_LIT_DETAIL_LIGHTING"></a>

#### VMI\_LIT\_DETAIL\_LIGHTING

4

<a id="unreal.ViewModeIndex.VMI_LIGHTING_ONLY"></a>

#### VMI\_LIGHTING\_ONLY

5: Lit wo/ materials.

<a id="unreal.ViewModeIndex.VMI_LIGHT_COMPLEXITY"></a>

#### VMI\_LIGHT\_COMPLEXITY

6: Colored according to light count.

<a id="unreal.ViewModeIndex.VMI_SHADER_COMPLEXITY"></a>

#### VMI\_SHADER\_COMPLEXITY

8: Colored according to shader complexity.

<a id="unreal.ViewModeIndex.VMI_LIGHTMAP_DENSITY"></a>

#### VMI\_LIGHTMAP\_DENSITY

9: Colored according to world-space LightMap texture density.

<a id="unreal.ViewModeIndex.VMI_LIT_LIGHTMAP_DENSITY"></a>

#### VMI\_LIT\_LIGHTMAP\_DENSITY

10: Colored according to light count - showing lightmap texel density on texture mapped objects.

<a id="unreal.ViewModeIndex.VMI_REFLECTION_OVERRIDE"></a>

#### VMI\_REFLECTION\_OVERRIDE

11

<a id="unreal.ViewModeIndex.VMI_VISUALIZE_BUFFER"></a>

#### VMI\_VISUALIZE\_BUFFER

12

<a id="unreal.ViewModeIndex.VMI_STATIONARY_LIGHT_OVERLAP"></a>

#### VMI\_STATIONARY\_LIGHT\_OVERLAP

14: Colored according to stationary light overlap.

<a id="unreal.ViewModeIndex.VMI_COLLISION_PAWN"></a>

#### VMI\_COLLISION\_PAWN

15

<a id="unreal.ViewModeIndex.VMI_COLLISION_VISIBILITY"></a>

#### VMI\_COLLISION\_VISIBILITY

16

<a id="unreal.ViewModeIndex.VMI_LOD_COLORATION"></a>

#### VMI\_LOD\_COLORATION

18: Colored according to the current LOD index.

<a id="unreal.ViewModeIndex.VMI_QUAD_OVERDRAW"></a>

#### VMI\_QUAD\_OVERDRAW

19: Colored according to the quad coverage.

<a id="unreal.ViewModeIndex.VMI_PRIMITIVE_DISTANCE_ACCURACY"></a>

#### VMI\_PRIMITIVE\_DISTANCE\_ACCURACY

20: Visualize the accuracy of the primitive distance computed for texture streaming.

<a id="unreal.ViewModeIndex.VMI_MESH_UV_DENSITY_ACCURACY"></a>

#### VMI\_MESH\_UV\_DENSITY\_ACCURACY

21: Visualize the accuracy of the mesh UV densities computed for texture streaming.

<a id="unreal.ViewModeIndex.VMI_SHADER_COMPLEXITY_WITH_QUAD_OVERDRAW"></a>

#### VMI\_SHADER\_COMPLEXITY\_WITH\_QUAD\_OVERDRAW

22: Colored according to shader complexity, including quad overdraw.

<a id="unreal.ViewModeIndex.VMI_HLOD_COLORATION"></a>

#### VMI\_HLOD\_COLORATION

23: Colored according to the current HLOD index.

<a id="unreal.ViewModeIndex.VMI_GROUP_LOD_COLORATION"></a>

#### VMI\_GROUP\_LOD\_COLORATION

24: Group item for LOD and HLOD coloration

<a id="unreal.ViewModeIndex.VMI_MATERIAL_TEXTURE_SCALE_ACCURACY"></a>

#### VMI\_MATERIAL\_TEXTURE\_SCALE\_ACCURACY

25: Visualize the accuracy of the material texture scales used for texture streaming.

<a id="unreal.ViewModeIndex.VMI_REQUIRED_TEXTURE_RESOLUTION"></a>

#### VMI\_REQUIRED\_TEXTURE\_RESOLUTION

26: Compare the required texture resolution to the actual resolution.

<a id="unreal.ViewModeIndex.VMI_PATH_TRACING"></a>

#### VMI\_PATH\_TRACING

27: Run path tracing pipeline

<a id="unreal.ViewModeIndex.VMI_RAY_TRACING_DEBUG"></a>

#### VMI\_RAY\_TRACING\_DEBUG

28: Run ray tracing debug pipeline

<a id="unreal.ViewModeIndex.VMI_VISUALIZE_NANITE"></a>

#### VMI\_VISUALIZE\_NANITE

29: Visualize various aspects of Nanite

<a id="unreal.ViewModeIndex.VMI_VIRTUAL_TEXTURE_PENDING_MIPS"></a>

#### VMI\_VIRTUAL\_TEXTURE\_PENDING\_MIPS

30: Compare the required texture resolution to the actual resolution.

<a id="unreal.ViewModeIndex.VMI_VISUALIZE_LUMEN"></a>

#### VMI\_VISUALIZE\_LUMEN

31: Visualize Lumen debug views

<a id="unreal.ViewModeIndex.VMI_VISUALIZE_VIRTUAL_SHADOW_MAP"></a>

#### VMI\_VISUALIZE\_VIRTUAL\_SHADOW\_MAP

32: Visualize virtual shadow map

<a id="unreal.ViewModeIndex.VMI_VISUALIZE_GPU_SKIN_CACHE"></a>

#### VMI\_VISUALIZE\_GPU\_SKIN\_CACHE

33: Visualize Skin Cache.

<a id="unreal.ViewModeIndex.VMI_VISUALIZE_SUBSTRATE"></a>

#### VMI\_VISUALIZE\_SUBSTRATE

34: Visualize Substrate debug views

<a id="unreal.ViewModeIndex.VMI_VISUALIZE_GROOM"></a>

#### VMI\_VISUALIZE\_GROOM

35: Visualize Groom debug views

<a id="unreal.ViewModeIndex.VMI_LWC_COMPLEXITY"></a>

#### VMI\_LWC\_COMPLEXITY

36

<a id="unreal.ViewModeIndex.VMI_LIT_WIREFRAME"></a>

#### VMI\_LIT\_WIREFRAME

37: Lit Wireframe.

<a id="unreal.ViewModeIndex.VMI_VISUALIZE_ACTOR_COLORATION"></a>

#### VMI\_VISUALIZE\_ACTOR\_COLORATION

38: Visualize Actor Coloration.

<a id="unreal.ViewModeIndex.VMI_UNKNOWN"></a>

#### VMI\_UNKNOWN

255: VMI_Unknown - The value assigned to VMI_Unknown must be the highest possible of any member of EViewModeIndex, or GetViewModeName might seg-fault

<a id="unreal.WidgetTestAppearLocation"></a>