## ClothLODBiasMode Objects

```python
class ClothLODBiasMode(EnumBase)
```

Strategy used for storing additional cloth deformer mappings depending on the
desired use of the RaytracingMinLOD value and of the LODBias console variable.

**C++ Source:**

- **Module**: Engine
- **File**: SkeletalMesh.h

<a id="unreal.ClothLODBiasMode.MAPPINGS_TO_SAME_LOD"></a>

#### MAPPINGS_TO_SAME_LOD

0: Only store the strict minimum amount of cloth deformer mappings to save on memory usage.
Raytracing of cloth elements must never be of a different LOD to the one being rendered when using this mode.

<a id="unreal.ClothLODBiasMode.MAPPINGS_TO_MIN_LOD"></a>

#### MAPPINGS_TO_MIN_LOD

1: Store additional cloth deformer mappings to allow raytracing of the cloth elements at RayTracingMinLOD.
Raytracing of cloth elements must never be of a different LOD to the one being rendered, or to the one set in RayTracingMinLOD when using this mode.

<a id="unreal.ClothLODBiasMode.MAPPINGS_TO_ANY_LOD"></a>

#### MAPPINGS_TO_ANY_LOD

2: Store all cloth deformer mappings at the expense of memory usage, to allow raytracing of the cloth elements at any higher LOD.
Use this mode when the RayTracing LODBias console variable is in use.

<a id="unreal.HLODLayerType"></a>