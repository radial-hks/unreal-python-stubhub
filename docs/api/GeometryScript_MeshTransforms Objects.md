## GeometryScript_MeshTransforms Objects

```python
class GeometryScript_MeshTransforms(BlueprintFunctionLibrary)
```

Geometry Script Library Mesh Transform Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshTransformFunctions.h

<a id="unreal.GeometryScript_MeshTransforms.translate_pivot_to_location"></a>

#### translate_pivot_to_location

```python
@classmethod
def translate_pivot_to_location(
        cls,
        target_mesh: DynamicMesh,
        pivot_location: Vector,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.translate_pivot_to_location(target_mesh, pivot_location, debug=None) -> DynamicMesh
Set the Pivot Location for the Mesh. Since the Pivot of a Mesh object is always the point at (0,0,0),
this function simply translates the mesh by -PivotLocation.

Args:
    target_mesh (DynamicMesh): 
    pivot_location (Vector): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshTransforms.translate_mesh_selection"></a>

#### translate_mesh_selection

```python
@classmethod
def translate_mesh_selection(cls,
                             target_mesh: DynamicMesh,
                             selection: GeometryScriptMeshSelection,
                             translation: Vector,
                             debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.translate_mesh_selection(target_mesh, selection, translation, debug=None) -> DynamicMesh
Applies the given Translation to the vertices identified by the Selection of the mesh.

Args:
    target_mesh (DynamicMesh): 
    selection (GeometryScriptMeshSelection): 
    translation (Vector): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshTransforms.translate_mesh"></a>

#### translate_mesh

```python
@classmethod
def translate_mesh(cls,
                   target_mesh: DynamicMesh,
                   translation: Vector,
                   debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.translate_mesh(target_mesh, translation, debug=None) -> DynamicMesh
Applies the provided Translation to the vertices of a Mesh.

Args:
    target_mesh (DynamicMesh): 
    translation (Vector): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshTransforms.transform_mesh_selection"></a>

#### transform_mesh_selection

```python
@classmethod
def transform_mesh_selection(cls,
                             target_mesh: DynamicMesh,
                             selection: GeometryScriptMeshSelection,
                             transform: Transform,
                             debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.transform_mesh_selection(target_mesh, selection, transform, debug=None) -> DynamicMesh
Applies the given Transform to the vertices identified by the Selection of the mesh.

Args:
    target_mesh (DynamicMesh): 
    selection (GeometryScriptMeshSelection): 
    transform (Transform): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshTransforms.transform_mesh"></a>

#### transform_mesh

```python
@classmethod
def transform_mesh(cls,
                   target_mesh: DynamicMesh,
                   transform: Transform,
                   fix_orientation_for_negative_scale: bool = True,
                   debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.transform_mesh(target_mesh, transform, fix_orientation_for_negative_scale=True, debug=None) -> DynamicMesh
Applies the provided Transform to the vertices of a Mesh.

Args:
    target_mesh (DynamicMesh): 
    transform (Transform): 
    fix_orientation_for_negative_scale (bool): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshTransforms.scale_mesh_selection"></a>

#### scale_mesh_selection

```python
@classmethod
def scale_mesh_selection(cls,
                         target_mesh: DynamicMesh,
                         selection: GeometryScriptMeshSelection,
                         scale: Vector = [1.000000, 1.000000, 1.000000],
                         scale_origin: Vector = [0.000000, 0.000000, 0.000000],
                         debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.scale_mesh_selection(target_mesh, selection, scale=[1.000000, 1.000000, 1.000000], scale_origin=[0.000000, 0.000000, 0.000000], debug=None) -> DynamicMesh
Applies the given Scale transform relative to the Scale Origin to the selection part of the mesh.

Args:
    target_mesh (DynamicMesh): 
    selection (GeometryScriptMeshSelection): 
    scale (Vector): 
    scale_origin (Vector): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshTransforms.scale_mesh"></a>

#### scale_mesh

```python
@classmethod
def scale_mesh(cls,
               target_mesh: DynamicMesh,
               scale: Vector = [1.000000, 1.000000, 1.000000],
               scale_origin: Vector = [0.000000, 0.000000, 0.000000],
               fix_orientation_for_negative_scale: bool = True,
               debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.scale_mesh(target_mesh, scale=[1.000000, 1.000000, 1.000000], scale_origin=[0.000000, 0.000000, 0.000000], fix_orientation_for_negative_scale=True, debug=None) -> DynamicMesh
Applies the provided Scale transformation relative to the Scale Origin to the vertices of a Mesh.

Args:
    target_mesh (DynamicMesh): 
    scale (Vector): 
    scale_origin (Vector): 
    fix_orientation_for_negative_scale (bool): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshTransforms.rotate_mesh_selection"></a>

#### rotate_mesh_selection

```python
@classmethod
def rotate_mesh_selection(cls,
                          target_mesh: DynamicMesh,
                          selection: GeometryScriptMeshSelection,
                          rotation: Rotator,
                          rotation_origin: Vector = [
                              0.000000, 0.000000, 0.000000
                          ],
                          debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.rotate_mesh_selection(target_mesh, selection, rotation, rotation_origin=[0.000000, 0.000000, 0.000000], debug=None) -> DynamicMesh
Rotates the selected part of the mesh relative to the specified Rotation Origin.

Args:
    target_mesh (DynamicMesh): 
    selection (GeometryScriptMeshSelection): 
    rotation (Rotator): 
    rotation_origin (Vector): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshTransforms.rotate_mesh"></a>

#### rotate_mesh

```python
@classmethod
def rotate_mesh(cls,
                target_mesh: DynamicMesh,
                rotation: Rotator,
                rotation_origin: Vector = [0.000000, 0.000000, 0.000000],
                debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.rotate_mesh(target_mesh, rotation, rotation_origin=[0.000000, 0.000000, 0.000000], debug=None) -> DynamicMesh
Rotates the mesh relative to the specified Rotation Origin.

Args:
    target_mesh (DynamicMesh): 
    rotation (Rotator): 
    rotation_origin (Vector): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_UVs"></a>