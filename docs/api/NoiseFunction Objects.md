## NoiseFunction Objects

```python
class NoiseFunction(EnumBase)
```

ENoise Function

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionNoise.h

<a id="unreal.NoiseFunction.NOISEFUNCTION_SIMPLEX_TEX"></a>

#### NOISEFUNCTION_SIMPLEX_TEX

0: High quality for direct use and bumps
~77 instructions per level, 4 texture lookups
Cannot tile

<a id="unreal.NoiseFunction.NOISEFUNCTION_GRADIENT_TEX"></a>

#### NOISEFUNCTION_GRADIENT_TEX

1: High quality for direct use and bumps
Non-tiled: ~61 instructions per level, 8 texture lookups
Tiling: ~74 instructions per level, 8 texture lookups
Even "non-tiled" mode has a repeat of 128. Useful Repeat Size range <= 128
Formerly labeled as Perlin noise

<a id="unreal.NoiseFunction.NOISEFUNCTION_GRADIENT_TEX3D"></a>

#### NOISEFUNCTION_GRADIENT_TEX3D

2: High quality for direct use, BAD for bumps; doesn't work on Mobile
~16 instructions per level, 1 texture lookup
Always tiles with a repeat of 16, "Tiling" mode is not an option for Fast Gradient noise

<a id="unreal.NoiseFunction.NOISEFUNCTION_GRADIENT_ALU"></a>

#### NOISEFUNCTION_GRADIENT_ALU

3: High quality for direct use and bumps
Non-tiled: ~80 instructions per level, no textures
Tiling: ~143 instructions per level, no textures

<a id="unreal.NoiseFunction.NOISEFUNCTION_VALUE_ALU"></a>

#### NOISEFUNCTION_VALUE_ALU

4: Low quality, but pure computation
Non-tiled: ~53 instructions per level, no textures
Tiling: ~118 instructions per level, no textures
Formerly mis-labeled as Gradient noise

<a id="unreal.NoiseFunction.NOISEFUNCTION_VORONOI_ALU"></a>

#### NOISEFUNCTION_VORONOI_ALU

5: Also known as Worley or Cellular noise
Quality=1 searches 8 cells, Quality=2 searches 16 cells
Quality=3 searches 27 cells, Quality=4 searches 32 cells
All are about 20 instructions per cell searched

<a id="unreal.PathTracingBufferTextureId"></a>