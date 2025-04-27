## GeometryScriptRemeshEdgeConstraintType Objects

```python
class GeometryScriptRemeshEdgeConstraintType(EnumBase)
```

Types of edge constraints, specified for different mesh attributes

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshRemeshFunctions.h

<a id="unreal.GeometryScriptRemeshEdgeConstraintType.FIXED"></a>

#### FIXED

0: Constrained edges cannot be flipped, split or collapsed, and vertices will not move

<a id="unreal.GeometryScriptRemeshEdgeConstraintType.REFINE"></a>

#### REFINE

1: Constrained edges can be split, but not flipped or collapsed. Vertices will not move.

<a id="unreal.GeometryScriptRemeshEdgeConstraintType.FREE"></a>

#### FREE

2: Constrained edges cannot be flipped, but otherwise are free to move

<a id="unreal.GeometryScriptRemeshEdgeConstraintType.IGNORE"></a>

#### IGNORE

3: Edges are not constrained, ie the Attribute used to derive the Constraints will not be considered

<a id="unreal.GeometryScriptRemeshSmoothingType"></a>