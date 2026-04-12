## DynamicMeshVertexColorTransformMode Objects

```python
class DynamicMeshVertexColorTransformMode(EnumBase)
```

Color Transform to apply to Vertex Colors when converting from internal DynamicMesh
Color attributes (eg Color Overlay stored in FVector4f) to RHI Render Buffers (FColor).

Note that UStaticMesh assumes the Source Mesh colors are Linear and always converts to SRGB.

**C++ Source:**

- **Module**: GeometryFramework
- **File**: BaseDynamicMeshComponent.h

<a id="unreal.DynamicMeshVertexColorTransformMode.NO_TRANSFORM"></a>

#### NO\_TRANSFORM

0: Do not apply any color-space transform to Vertex Colors

<a id="unreal.DynamicMeshVertexColorTransformMode.LINEAR_TO_SRGB"></a>

#### LINEAR\_TO\_SRGB

1: Assume Vertex Colors are in Linear space and transform to SRGB

<a id="unreal.DynamicMeshVertexColorTransformMode.SRGB_TO_LINEAR"></a>

#### SRGB\_TO\_LINEAR

2: Assume Vertex Colors are in SRGB space and convert to Linear

<a id="unreal.DynamicMeshChangeType"></a>