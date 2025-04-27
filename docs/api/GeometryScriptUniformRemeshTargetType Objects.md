## GeometryScriptUniformRemeshTargetType Objects

```python
class GeometryScriptUniformRemeshTargetType(EnumBase)
```

Goal types for Uniform Remeshing

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshRemeshFunctions.h

<a id="unreal.GeometryScriptUniformRemeshTargetType.TRIANGLE_COUNT"></a>

#### TRIANGLE_COUNT

0: Approximate Desired Triangle Count. This is used to compute a Target Edge Length, and is not an explicit target

<a id="unreal.GeometryScriptUniformRemeshTargetType.TARGET_EDGE_LENGTH"></a>

#### TARGET_EDGE_LENGTH

1: Attempt to Remesh such that all edges have approximately this length

<a id="unreal.GeometryScriptRemeshEdgeConstraintType"></a>