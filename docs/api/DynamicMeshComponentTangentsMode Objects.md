## DynamicMeshComponentTangentsMode Objects

```python
class DynamicMeshComponentTangentsMode(EnumBase)
```

Tangent calculation modes

**C++ Source:**

- **Module**: GeometryFramework
- **File**: BaseDynamicMeshComponent.h

<a id="unreal.DynamicMeshComponentTangentsMode.NO_TANGENTS"></a>

#### NO_TANGENTS

0: Tangents are not used/available, proceed accordingly (eg generate arbitrary orthogonal basis)

<a id="unreal.DynamicMeshComponentTangentsMode.AUTO_CALCULATED"></a>

#### AUTO_CALCULATED

1: Tangents will be automatically calculated on demand. Note that mesh changes due to tangents calculation will *not* be broadcast via MeshChange events!

<a id="unreal.DynamicMeshComponentTangentsMode.EXTERNALLY_PROVIDED"></a>

#### EXTERNALLY_PROVIDED

2: Tangents are externally provided via the FDynamicMesh3 AttributeSet

<a id="unreal.DynamicMeshComponentTangentsMode.DEFAULT"></a>

#### DEFAULT

255: Tangents mode will be set to the most commonly-useful default -- currently "From Dynamic Mesh"

<a id="unreal.DynamicMeshComponentColorOverrideMode"></a>