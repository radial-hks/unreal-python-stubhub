## IndirectLightingCacheQuality Objects

```python
class IndirectLightingCacheQuality(EnumBase)
```

Quality of indirect lighting for Movable primitives. This has a large effect on Indirect Lighting Cache update time.

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

<a id="unreal.IndirectLightingCacheQuality.ILCQ_OFF"></a>

#### ILCQ_OFF

0: The indirect lighting cache will be disabled for this object, so no GI from stationary lights on movable objects.

<a id="unreal.IndirectLightingCacheQuality.ILCQ_POINT"></a>

#### ILCQ_POINT

1: A single indirect lighting sample computed at the bounds origin will be interpolated which fades over time to newer results.

<a id="unreal.IndirectLightingCacheQuality.ILCQ_VOLUME"></a>

#### ILCQ_VOLUME

2: The object will get a 5x5x5 stable volume of interpolated indirect lighting, which allows gradients of lighting intensity across the receiving object.

<a id="unreal.LightmapType"></a>