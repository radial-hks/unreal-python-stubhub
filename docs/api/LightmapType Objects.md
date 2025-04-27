## LightmapType Objects

```python
class LightmapType(EnumBase)
```

Type of lightmap that is used for primitive components

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

<a id="unreal.LightmapType.DEFAULT"></a>

#### DEFAULT

0: Use the default based on Mobility: Surface Lightmap for Static components, Volumetric Lightmap for Movable components.

<a id="unreal.LightmapType.FORCE_SURFACE"></a>

#### FORCE_SURFACE

1: Force Surface Lightmap, even if the component moves, which should otherwise change the lighting.  This is only supported on components which support surface lightmaps, like static meshes.

<a id="unreal.LightmapType.FORCE_VOLUMETRIC"></a>

#### FORCE_VOLUMETRIC

2: Force Volumetric Lightmaps, even if the component is static and could have supported surface lightmaps.
Volumetric Lightmaps have better directionality and no Lightmap UV seams, but are much lower resolution than Surface Lightmaps and frequently have self-occlusion and leaking problems.
Note: Lightmass currently requires valid lightmap UVs and sufficient lightmap resolution to compute bounce lighting, even though the Volumetric Lightmap will be used at runtime.

<a id="unreal.HLODBatchingPolicy"></a>