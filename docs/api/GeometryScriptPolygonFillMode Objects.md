## GeometryScriptPolygonFillMode Objects

```python
class GeometryScriptPolygonFillMode(EnumBase)
```

EGeometry Script Polygon Fill Mode

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshPrimitiveFunctions.h

<a id="unreal.GeometryScriptPolygonFillMode.ALL"></a>

#### ALL

0: Keep all triangles, regardless of whether they were enclosed by constrained edges

<a id="unreal.GeometryScriptPolygonFillMode.SOLID"></a>

#### SOLID

1: Fill everything inside the outer boundaries of constrained edges, ignoring edge orientation and any internal holes

<a id="unreal.GeometryScriptPolygonFillMode.POSITIVE_WINDING"></a>

#### POSITIVE_WINDING

2: Fill where the 'winding number' is positive

<a id="unreal.GeometryScriptPolygonFillMode.NON_ZERO_WINDING"></a>

#### NON_ZERO_WINDING

3: Fill where the 'winding number' is not zero

<a id="unreal.GeometryScriptPolygonFillMode.NEGATIVE_WINDING"></a>

#### NEGATIVE_WINDING

4: Fill where the 'winding number' is negative

<a id="unreal.GeometryScriptPolygonFillMode.ODD_WINDING"></a>

#### ODD_WINDING

5: Fill where the 'winding number' is an odd number

<a id="unreal.GeometryScriptUniformRemeshTargetType"></a>