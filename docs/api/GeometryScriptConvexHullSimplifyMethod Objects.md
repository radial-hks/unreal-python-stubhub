## GeometryScriptConvexHullSimplifyMethod Objects

```python
class GeometryScriptConvexHullSimplifyMethod(EnumBase)
```

Methods to simplify convex hulls, used by FGeometryScriptConvexHullSimplificationOptions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: CollisionFunctions.h

<a id="unreal.GeometryScriptConvexHullSimplifyMethod.MESH_Q_SLIM"></a>

#### MESH_Q_SLIM

0: Simplify convex hulls using a general mesh-based simplifier, and taking the convex hull of the simplified mesh

<a id="unreal.GeometryScriptConvexHullSimplifyMethod.ANGLE_TOLERANCE"></a>

#### ANGLE_TOLERANCE

1: Simplify convex hulls by merging hull faces that have similar normals

<a id="unreal.GeometryScriptMeshSelectionType"></a>