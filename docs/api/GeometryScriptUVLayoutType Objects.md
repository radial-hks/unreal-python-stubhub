## GeometryScriptUVLayoutType Objects

```python
class GeometryScriptUVLayoutType(EnumBase)
```

EGeometry Script UVLayout Type

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshUVFunctions.h

<a id="unreal.GeometryScriptUVLayoutType.TRANSFORM"></a>

#### TRANSFORM

0: Apply Scale and Translation properties to all UV values

<a id="unreal.GeometryScriptUVLayoutType.STACK"></a>

#### STACK

1: Uniformly scale and translate each UV island individually to pack it into the unit square, i.e. fit between 0 and 1 with overlap

<a id="unreal.GeometryScriptUVLayoutType.REPACK"></a>

#### REPACK

2: Uniformly scale and translate UV islands collectively to pack them into the unit square, i.e. fit between 0 and 1 with no overlap

<a id="unreal.GeometryScriptUVLayoutType.NORMALIZE"></a>

#### NORMALIZE

3: Scale and translate UV islands to normalize the UV islands' area to match an average texel density.

<a id="unreal.GeometryScriptUVFlattenMethod"></a>