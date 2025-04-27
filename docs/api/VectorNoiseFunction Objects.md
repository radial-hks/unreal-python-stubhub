## VectorNoiseFunction Objects

```python
class VectorNoiseFunction(EnumBase)
```

EVector Noise Function

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionVectorNoise.h

<a id="unreal.VectorNoiseFunction.VNF_CELLNOISE_ALU"></a>

#### VNF_CELLNOISE_ALU

0: Random color for each unit cell in 3D space.
RGB output range 0 to 1
R only = 9 instructions, RGB = 11 instructions

<a id="unreal.VectorNoiseFunction.VNF_VECTOR_ALU"></a>

#### VNF_VECTOR_ALU

1: Perlin-style noise with 3D vector/color output.
RGB output range -1 to 1
R only = ~83 instructions, RGB = ~125 instructions

<a id="unreal.VectorNoiseFunction.VNF_GRADIENT_ALU"></a>

#### VNF_GRADIENT_ALU

2: Gradient of Perlin noise, useful for bumps.
RGB = Gradient of scalar noise (signed 3D vector)
A = Base scalar noise with range -1 to 1
A only = ~83 instructions, RGBA = ~106 instructions

<a id="unreal.VectorNoiseFunction.VNF_CURL_ALU"></a>

#### VNF_CURL_ALU

3: Curl of Perlin noise, useful for 3D flow directions.
RGB = signed curl vector
~162 instructions

<a id="unreal.VectorNoiseFunction.VNF_VORONOI_ALU"></a>

#### VNF_VORONOI_ALU

4: Also known as Worley or Cellular noise.
RGB = *position* of closest point at center of Voronoi cell
A = distance to closest point with range 0 to about 4
Quality levels 1-4 search 8, 16, 27 & 32 cells
All ~20 instructions per cell searched

<a id="unreal.MaterialExposedViewProperty"></a>