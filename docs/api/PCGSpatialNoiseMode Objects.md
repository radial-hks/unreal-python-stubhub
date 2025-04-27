## PCGSpatialNoiseMode Objects

```python
class PCGSpatialNoiseMode(EnumBase)
```

PCGSpatial Noise Mode

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSpatialNoise.h

<a id="unreal.PCGSpatialNoiseMode.PERLIN2D"></a>

#### PERLIN2D

0: Your classic perlin noise.

<a id="unreal.PCGSpatialNoiseMode.CAUSTIC2D"></a>

#### CAUSTIC2D

1: Based on underwater fake caustic rendering, gives swirly look.

<a id="unreal.PCGSpatialNoiseMode.VORONOI2D"></a>

#### VORONOI2D

2: Voronoi noise, result a the distance to edge and cell ID.

<a id="unreal.PCGSpatialNoiseMode.FRACTIONAL_BROWNIAN2D"></a>

#### FRACTIONAL_BROWNIAN2D

3: Based on fractional brownian motion.

<a id="unreal.PCGSpatialNoiseMode.EDGE_MASK2D"></a>

#### EDGE_MASK2D

4: Used to create masks to blend out edges.

<a id="unreal.PCGSpatialNoiseMask2DMode"></a>