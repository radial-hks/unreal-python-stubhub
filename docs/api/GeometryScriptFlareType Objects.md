## GeometryScriptFlareType Objects

```python
class GeometryScriptFlareType(EnumBase)
```

EGeometry Script Flare Type

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshDeformFunctions.h

<a id="unreal.GeometryScriptFlareType.SIN_MODE"></a>

#### SIN_MODE

0: Displaced by sin(pi x) with x in 0 to 1

<a id="unreal.GeometryScriptFlareType.SIN_SQUARED_MODE"></a>

#### SIN_SQUARED_MODE

1: Displaced by sin(pi x)*sin(pi x) with x in 0 to 1. This provides a smooth normal transition.

<a id="unreal.GeometryScriptFlareType.TRIANGLE_MODE"></a>

#### TRIANGLE_MODE

2: Displaced by piecewise-linear trianglular mode

<a id="unreal.GeometryScriptMathWarpType"></a>