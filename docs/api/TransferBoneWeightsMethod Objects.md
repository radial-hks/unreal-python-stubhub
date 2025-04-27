## TransferBoneWeightsMethod Objects

```python
class TransferBoneWeightsMethod(EnumBase)
```

ETransfer Bone Weights Method

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshBoneWeightFunctions.h

<a id="unreal.TransferBoneWeightsMethod.CLOSEST_POINT_ON_SURFACE"></a>

#### CLOSEST_POINT_ON_SURFACE

0: For every vertex on the TargetMesh, find the closest point on the surface of the SourceMesh and transfer
bone weights from it. This is usually a point on the SourceMesh triangle where the bone weights are computed via
interpolation of the bone weights at the vertices of the triangle via barycentric coordinates.

<a id="unreal.TransferBoneWeightsMethod.INPAINT_WEIGHTS"></a>

#### INPAINT_WEIGHTS

1: For every vertex on the target mesh, find the closest point on the surface of the source mesh. If that point
is within the search radius (controlled via SearchPercentage), and their normals differ by less than the
NormalThreshold, then we directly copy the weights from the source point to the target mesh vertex
(same as the ClosestPointOnSurface method). For all the vertices we didn't copy the weights directly,
automatically compute the smooth weights.

<a id="unreal.OutputTargetMeshBones"></a>