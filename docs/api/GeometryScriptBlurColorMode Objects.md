## GeometryScriptBlurColorMode Objects

```python
class GeometryScriptBlurColorMode(EnumBase)
```

EGeometry Script Blur Color Mode

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshVertexColorFunctions.h

<a id="unreal.GeometryScriptBlurColorMode.UNIFORM"></a>

#### UNIFORM

0: Blur the attributes where each neighbor is weighted equally.

<a id="unreal.GeometryScriptBlurColorMode.EDGE_LENGTH"></a>

#### EDGE_LENGTH

1: Blur the attributes where each neighbor is weighted proportionally to the shared edge length.

<a id="unreal.GeometryScriptBlurColorMode.COTAN_WEIGHTS"></a>

#### COTAN_WEIGHTS

2: Blur the attributes where each neighbor is weighted proportionally to the cotangent weight of the shared edge.

<a id="unreal.GeometryScriptGridSizingMethod"></a>