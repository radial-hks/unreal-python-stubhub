## PCGMeshSamplingMethod Objects

```python
class PCGMeshSamplingMethod(EnumBase)
```

EPCGMesh Sampling Method

**C++ Source:**

- **Plugin**: PCGGeometryScriptInterop
- **Module**: PCGGeometryScriptInterop
- **File**: PCGMeshSampler.h

<a id="unreal.PCGMeshSamplingMethod.ONE_POINT_PER_TRIANGLE"></a>

#### ONE_POINT_PER_TRIANGLE

0: Sample one point (at the center) of each triangle of the mesh.

<a id="unreal.PCGMeshSamplingMethod.ONE_POINT_PER_VERTEX"></a>

#### ONE_POINT_PER_VERTEX

1: Sample one point per vertex on the mesh.

<a id="unreal.PCGMeshSamplingMethod.POISSON_SAMPLING"></a>

#### POISSON_SAMPLING

2: Use Poisson sampling to sample points on the mesh. Can be expensive and therefore it is not framebound.

<a id="unreal.TextureRotationDirection"></a>