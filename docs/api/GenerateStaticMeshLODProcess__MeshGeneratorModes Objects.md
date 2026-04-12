## GenerateStaticMeshLODProcess\_MeshGeneratorModes Objects

```python
class GenerateStaticMeshLODProcess_MeshGeneratorModes(EnumBase)
```

EGenerate Static Mesh LODProcess Mesh Generator Modes

**C++ Source:**

- **Plugin**: MeshLODToolset
- **Module**: MeshLODToolset
- **File**: GenerateStaticMeshLODProcess.h

<a id="unreal.GenerateStaticMeshLODProcess_MeshGeneratorModes.SOLIDIFY"></a>

#### SOLIDIFY

0: Generate a mesh using Marching Cubes to remesh the input shape.
Use Winding Numbers to determine what is inside

<a id="unreal.GenerateStaticMeshLODProcess_MeshGeneratorModes.SOLIDIFY_AND_CLOSE"></a>

#### SOLIDIFY\_AND\_CLOSE

1: Like Solidify, but Dilate and Contract the shape to delete small
negative features (sharp inner corners, small holes) before remeshing

<a id="unreal.GenerateStaticMeshLODProcess_MeshGeneratorModes.CLEAN_AND_SIMPLIFY"></a>

#### CLEAN\_AND\_SIMPLIFY

2: Generate a mesh by simplifying input Mesh attributes and filling small holes

<a id="unreal.GenerateStaticMeshLODProcess_MeshGeneratorModes.CONVEX_HULL"></a>

#### CONVEX\_HULL

3: Generate a mesh by calculating the Convex Hull of the input shape

<a id="unreal.GenerateStaticMeshLODProcess_SimplifyMethod"></a>