## MeshCutterCutDistribution Objects

```python
class MeshCutterCutDistribution(EnumBase)
```

EMesh Cutter Cut Distribution

**C++ Source:**

- **Plugin**: Fracture
- **Module**: FractureEngine
- **File**: FractureEngineFracturing.h

<a id="unreal.MeshCutterCutDistribution.SINGLE_CUT"></a>

#### SINGLE_CUT

0: Cut only once, at the cutting mesh's current location in the level

<a id="unreal.MeshCutterCutDistribution.UNIFORM_RANDOM"></a>

#### UNIFORM_RANDOM

1: Scatter the cutting mesh in a uniform random distribution around the geometry bounding box

<a id="unreal.MeshCutterCutDistribution.GRID"></a>

#### GRID

2: Arrange the cutting mesh in a regular grid pattern

<a id="unreal.NonUniformSamplingDistributionMode"></a>