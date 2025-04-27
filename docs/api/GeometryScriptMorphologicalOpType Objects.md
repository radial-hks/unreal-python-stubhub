## GeometryScriptMorphologicalOpType Objects

```python
class GeometryScriptMorphologicalOpType(EnumBase)
```

EGeometry Script Morphological Op Type

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshVoxelFunctions.h

<a id="unreal.GeometryScriptMorphologicalOpType.DILATE"></a>

#### DILATE

0: Expand the shapes outward

<a id="unreal.GeometryScriptMorphologicalOpType.CONTRACT"></a>

#### CONTRACT

1: Shrink the shapes inward

<a id="unreal.GeometryScriptMorphologicalOpType.CLOSE"></a>

#### CLOSE

2: Dilate and then contract, to delete small negative features (sharp inner corners, small holes)

<a id="unreal.GeometryScriptMorphologicalOpType.OPEN"></a>

#### OPEN

3: Contract and then dilate, to delete small positive features (sharp outer corners, small isolated pieces)

<a id="unreal.GeometryScriptInitKMeansMethod"></a>