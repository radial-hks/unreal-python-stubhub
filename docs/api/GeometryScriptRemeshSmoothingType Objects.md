## GeometryScriptRemeshSmoothingType Objects

```python
class GeometryScriptRemeshSmoothingType(EnumBase)
```

The Vertex Smoothing strategy used in a Remeshing operation

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshRemeshFunctions.h

<a id="unreal.GeometryScriptRemeshSmoothingType.UNIFORM"></a>

#### UNIFORM

0: Vertices move towards their 3D one-ring centroids, UVs are ignored. This produces the most regular mesh possible.

<a id="unreal.GeometryScriptRemeshSmoothingType.UV_PRESERVING"></a>

#### UV_PRESERVING

1: Vertices move towards the projection of their one-ring centroids onto their normal vectors, preserving UVs

<a id="unreal.GeometryScriptRemeshSmoothingType.MIXED"></a>

#### MIXED

2: Similar to UV Preserving, but allows some tangential drift (causing UV distortion) when vertices would otherwise be "stuck"

<a id="unreal.GeometryScriptFillHolesMethod"></a>