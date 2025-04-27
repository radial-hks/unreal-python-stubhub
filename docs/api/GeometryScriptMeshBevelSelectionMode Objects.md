## GeometryScriptMeshBevelSelectionMode Objects

```python
class GeometryScriptMeshBevelSelectionMode(EnumBase)
```

Mode passed to ApplyMeshBevelSelection to control how the input Selection should
be interpreted as selecting an area of the mesh to Bevel

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshModelingFunctions.h

<a id="unreal.GeometryScriptMeshBevelSelectionMode.TRIANGLE_AREA"></a>

#### TRIANGLE_AREA

0: Convert the selection to Triangles and bevel the boundary edge loops of the triangle set

<a id="unreal.GeometryScriptMeshBevelSelectionMode.ALL_POLYGROUP_EDGES"></a>

#### ALL_POLYGROUP_EDGES

1: Convert the selection to PolyGroups and bevel all the PolyGroup Edges of the selected PolyGroups

<a id="unreal.GeometryScriptMeshBevelSelectionMode.SHARED_POLYGROUP_EDGES"></a>

#### SHARED_POLYGROUP_EDGES

2: Convert the selection to PolyGroups and bevel all the PolyGroup Edges that are between selected PolyGroups

<a id="unreal.GeometryScriptMeshBevelSelectionMode.SELECTED_EDGES"></a>

#### SELECTED_EDGES

3: Convert the selection to Edges (if needed) and bevel them

<a id="unreal.GeometryScriptTangentTypes"></a>