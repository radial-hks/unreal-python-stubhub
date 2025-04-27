## GeometryScriptPolyOffsetJoinType Objects

```python
class GeometryScriptPolyOffsetJoinType(EnumBase)
```

Join types to define the shape of corners between polygon and polypath edges

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: PolygonFunctions.h

<a id="unreal.GeometryScriptPolyOffsetJoinType.SQUARE"></a>

#### SQUARE

0: Uniform squaring on all convex edge joins.

<a id="unreal.GeometryScriptPolyOffsetJoinType.ROUND"></a>

#### ROUND

1: Arcs on all convex edge joins.

<a id="unreal.GeometryScriptPolyOffsetJoinType.MITER"></a>

#### MITER

2: Squaring of convex edge joins with acute angles ("spikes"). Use in combination with MiterLimit.

<a id="unreal.GeometryScriptPathOffsetEndType"></a>