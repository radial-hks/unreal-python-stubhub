## GeometryScript_SceneUtils Objects

```python
class GeometryScript_SceneUtils(BlueprintFunctionLibrary)
```

Geometry Script Library Scene Utility Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: SceneUtilityFunctions.h

<a id="unreal.GeometryScript_SceneUtils.set_component_material_list"></a>

#### set_component_material_list

```python
@classmethod
def set_component_material_list(cls,
                                component: PrimitiveComponent,
                                material_list: Array[MaterialInterface],
                                debug: GeometryScriptDebug = None) -> None
```

X.set_component_material_list(component, material_list, debug=None) -> None
Configure the Material set on a PrimitiveComponent, by repeatedly calling SetMaterial.
This is a simple utility function and it's behavior will depend on the specifics of the Component.

Args:
    component (PrimitiveComponent): 
    material_list (Array[MaterialInterface]): 
    debug (GeometryScriptDebug):

<a id="unreal.GeometryScript_SceneUtils.determine_mesh_occlusion"></a>

#### determine_mesh_occlusion

```python
@classmethod
def determine_mesh_occlusion(
        cls,
        source_meshes: Array[DynamicMesh],
        source_mesh_transforms: Array[Transform],
        transparent_meshes: Array[DynamicMesh],
        transparent_mesh_transforms: Array[Transform],
        occlude_meshes: Array[DynamicMesh],
        occlude_mesh_transforms: Array[Transform],
        occlusion_options: GeometryScriptDetermineMeshOcclusionOptions,
        debug: GeometryScriptDebug = None) -> Tuple[Array[bool], Array[bool]]
```

X.determine_mesh_occlusion(source_meshes, source_mesh_transforms, transparent_meshes, transparent_mesh_transforms, occlude_meshes, occlude_mesh_transforms, occlusion_options, debug=None) -> (out_mesh_is_hidden=Array[bool], out_transparent_mesh_is_hidden=Array[bool])
Determine which meshes are entirely hidden by other meshes in the set, when viewed from outside.

Args:
    source_meshes (Array[DynamicMesh]): Meshes to test for occlusion. Note: The same mesh may appear multiple times in this array, if it is instanced with different transforms.
    source_mesh_transforms (Array[Transform]): A transform for each source mesh. Array must have the same length as SourceMeshes.
    transparent_meshes (Array[DynamicMesh]): Transparent source meshes, to test for occlusion but which do not occlude.
    transparent_mesh_transforms (Array[Transform]): Array of transforms for each transparent mesh
    occlude_meshes (Array[DynamicMesh]): Array of optional meshes which can occlude SourceMeshes, but for which we will not test occlusion.
    occlude_mesh_transforms (Array[Transform]): Array of transforms for each occlude mesh. Array must have the same length as OccludeMeshes.
    occlusion_options (GeometryScriptDetermineMeshOcclusionOptions): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    out_mesh_is_hidden (Array[bool]): Array will be filled with a bool per source mesh, indicating whether that mesh is hidden (true) or visible (false)

    out_transparent_mesh_is_hidden (Array[bool]): Array will be filled with a bool per transparent mesh, indicating whether that mesh is hidden (true) or visible (false)

<a id="unreal.GeometryScript_SceneUtils.create_dynamic_mesh_pool"></a>

#### create_dynamic_mesh_pool

```python
@classmethod
def create_dynamic_mesh_pool(cls) -> DynamicMeshPool
```

X.create_dynamic_mesh_pool() -> DynamicMeshPool
Create a new UDynamicMeshPool object.
Caller needs to create a UProperty reference to the returned object, or it will be garbage-collected.

Returns:
    DynamicMeshPool:

<a id="unreal.GeometryScript_SceneUtils.copy_mesh_from_component"></a>

#### copy_mesh_from_component

```python
@classmethod
def copy_mesh_from_component(
    cls,
    component: SceneComponent,
    to_dynamic_mesh: DynamicMesh,
    options: GeometryScriptCopyMeshFromComponentOptions,
    transform_to_world: bool,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, Transform, GeometryScriptOutcomePins]
```

X.copy_mesh_from_component(component, to_dynamic_mesh, options, transform_to_world, debug=None) -> (DynamicMesh, local_to_world=Transform, outcome=GeometryScriptOutcomePins)
Copy the mesh from a given Component to a Dynamic Mesh.
StaticMeshComponent, DynamicMeshCompnent, and BrushComponent are supported.
This function offers minimal control over the copying, if more control is needed for Static Meshes, use CopyMeshFromStaticMesh.

Args:
    component (SceneComponent): 
    to_dynamic_mesh (DynamicMesh): 
    options (GeometryScriptCopyMeshFromComponentOptions): 
    transform_to_world (bool): if true, output mesh is in World space
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    local_to_world (Transform): local-to-world transform is returned here (whether mesh is in local or world space)

    outcome (GeometryScriptOutcomePins):

<a id="unreal.GeometryScript_SceneUtils.copy_collision_meshes_from_object"></a>

#### copy_collision_meshes_from_object

```python
@classmethod
def copy_collision_meshes_from_object(
    cls,
    from_object: Object,
    to_dynamic_mesh: DynamicMesh,
    transform_to_world: bool,
    use_complex_collision: bool = False,
    sphere_resolution: int = 16,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, Transform, GeometryScriptOutcomePins]
```

X.copy_collision_meshes_from_object(from_object, to_dynamic_mesh, transform_to_world, use_complex_collision=False, sphere_resolution=16, debug=None) -> (DynamicMesh, local_to_world=Transform, outcome=GeometryScriptOutcomePins)
Extract the Collision Geometry from FromObject and copy/approximate it with meshes stored in ToDynamicMesh.
For Simple Collision, FromObject can be a StaticMesh Asset or any PrimitiveComponent
For Complex Collision, FromObject can be a StaticMesh Asset, StaticMeshComponent, or DynamicMeshComponent

Args:
    from_object (Object): 
    to_dynamic_mesh (DynamicMesh): 
    transform_to_world (bool): if true, output mesh is in World space
    use_complex_collision (bool): if true, complex collision is extracted, otherwise Simple collision shapes are meshed
    sphere_resolution (int32): determines tessellation density of sphere and capsule shapes
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    local_to_world (Transform): local-to-world transform is returned here (whether mesh is in local or world space)

    outcome (GeometryScriptOutcomePins):

<a id="unreal.GeometryScript_Transform"></a>