## LumenRayLightingModeOverride Objects

```python
class LumenRayLightingModeOverride(EnumBase)
```

ELumen Ray Lighting Mode Override

**C++ Source:**

- **Module**: Engine
- **File**: Scene.h

<a id="unreal.LumenRayLightingModeOverride.DEFAULT"></a>

#### DEFAULT

0: Use the project default method

<a id="unreal.LumenRayLightingModeOverride.SURFACE_CACHE"></a>

#### SURFACE_CACHE

1: Use Lumen Surface Cache for ray hit lighting. This method gives the best GI and reflection performance, but quality will be limited by how well surface cache represents given scene.

<a id="unreal.LumenRayLightingModeOverride.HIT_LIGHTING_FOR_REFLECTIONS"></a>

#### HIT_LIGHTING_FOR_REFLECTIONS

2: Calculate lighting at a hit point for reflections. This will improve reflection quality, but increases GPU cost, as full material needs to be evaluated and shadow rays traced. Lumen Surface Cache will still be used for GI and secondary bounces, including GI seen in reflections.

<a id="unreal.LumenRayLightingModeOverride.HIT_LIGHTING"></a>

#### HIT_LIGHTING

3: Calculate lighting at a hit point for GI and reflections. This will improve both GI and reflection quality, but greatly increases GPU cost, as full material and lighting will be evaluated at every hit point. Lumen Surface Cache will still be used for secondary bounces.

<a id="unreal.ReflectionMethod"></a>