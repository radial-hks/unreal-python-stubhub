## GeometryScript_OpenSubdiv Objects

```python
class GeometryScript_OpenSubdiv(BlueprintFunctionLibrary)
```

Geometry Script Library Open Subdiv Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingEditor
- **File**: OpenSubdivUtilityFunctions.h

<a id="unreal.GeometryScript_OpenSubdiv.apply_triangle_loop_sub_d"></a>

#### apply_triangle_loop_sub_d

```python
@classmethod
def apply_triangle_loop_sub_d(
        cls,
        from_dynamic_mesh: DynamicMesh,
        subdivisions: int,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_triangle_loop_sub_d(from_dynamic_mesh, subdivisions, debug=None) -> DynamicMesh
Apply Triangle Loop Sub D

Args:
    from_dynamic_mesh (DynamicMesh): 
    subdivisions (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_OpenSubdiv.apply_polygroup_catmull_clark_sub_d"></a>

#### apply_polygroup_catmull_clark_sub_d

```python
@classmethod
def apply_polygroup_catmull_clark_sub_d(
        cls,
        from_dynamic_mesh: DynamicMesh,
        subdivisions: int,
        group_layer: GeometryScriptGroupLayer,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_polygroup_catmull_clark_sub_d(from_dynamic_mesh, subdivisions, group_layer, debug=None) -> DynamicMesh
Apply Polygroup Catmull Clark Sub D

Args:
    from_dynamic_mesh (DynamicMesh): 
    subdivisions (int32): 
    group_layer (GeometryScriptGroupLayer): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.SVGBaseDynamicMeshComponent"></a>