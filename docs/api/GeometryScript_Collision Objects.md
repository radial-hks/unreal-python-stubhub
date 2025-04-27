## GeometryScript_Collision Objects

```python
class GeometryScript_Collision(BlueprintFunctionLibrary)
```

Geometry Script Library Collision Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: CollisionFunctions.h

<a id="unreal.GeometryScript_Collision.transform_simple_collision_shapes"></a>

#### transform_simple_collision_shapes

```python
@classmethod
def transform_simple_collision_shapes(
    cls,
    simple_collision: GeometryScriptSimpleCollision,
    transform: Transform,
    transform_options: GeometryScriptTransformCollisionOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[GeometryScriptSimpleCollision, bool]
```

X.transform_simple_collision_shapes(simple_collision, transform, transform_options, debug=None) -> (GeometryScriptSimpleCollision, success=bool)
* Transform simple collision shapes
*

Args:
    simple_collision (GeometryScriptSimpleCollision): 
    transform (Transform): 
    transform_options (GeometryScriptTransformCollisionOptions): 
    debug (GeometryScriptDebug): 

Returns:
    bool: 

    success (bool): Indicates whether all collision shapes were accurately transformed. On failure, shapes will still be copied over and a best-effort transform will still be applied.

<a id="unreal.GeometryScript_Collision.static_mesh_has_customized_collision"></a>

#### static_mesh_has_customized_collision

```python
@classmethod
def static_mesh_has_customized_collision(
        cls, static_mesh_asset: StaticMesh) -> bool
```

X.static_mesh_has_customized_collision(static_mesh_asset) -> bool
*

Args:
    static_mesh_asset (StaticMesh): 

Returns:
    bool: true if the static mesh has customized collision. If no editor data is available, returns false.

<a id="unreal.GeometryScript_Collision.simplify_convex_hulls"></a>

#### simplify_convex_hulls

```python
@classmethod
def simplify_convex_hulls(
    cls,
    simple_collision: GeometryScriptSimpleCollision,
    simplify_options: GeometryScriptConvexHullSimplificationOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[GeometryScriptSimpleCollision, bool]
```

X.simplify_convex_hulls(simple_collision, simplify_options, debug=None) -> (simple_collision=GeometryScriptSimpleCollision, has_simplified=bool)
Simplify any convex hulls in the given simple collision representation. Updates the passed-in Simple Collision.

Args:
    simple_collision (GeometryScriptSimpleCollision): The collision in which to attempt to simplify the convex hulls
    simplify_options (GeometryScriptConvexHullSimplificationOptions): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    simple_collision (GeometryScriptSimpleCollision): The collision in which to attempt to simplify the convex hulls

    has_simplified (bool): Indicates whether any convex hulls were modified

<a id="unreal.GeometryScript_Collision.set_static_mesh_custom_complex_collision"></a>

#### set_static_mesh_custom_complex_collision

```python
@classmethod
def set_static_mesh_custom_complex_collision(
        cls,
        static_mesh_asset: StaticMesh,
        static_mesh_collision_asset: StaticMesh,
        emit_transaction: bool,
        mark_collision_as_customized: bool = True,
        debug: GeometryScriptDebug = None) -> bool
```

X.set_static_mesh_custom_complex_collision(static_mesh_asset, static_mesh_collision_asset, emit_transaction, mark_collision_as_customized=True, debug=None) -> bool
Set a static mesh as the custom collision for another static mesh to use.
Note: Only works if editor-only data is available.

Args:
    static_mesh_asset (StaticMesh): 
    static_mesh_collision_asset (StaticMesh): 
    emit_transaction (bool): 
    mark_collision_as_customized (bool): 
    debug (GeometryScriptDebug): 

Returns:
    bool: true on success.

<a id="unreal.GeometryScript_Collision.set_static_mesh_collision_from_mesh"></a>

#### set_static_mesh_collision_from_mesh

```python
@classmethod
def set_static_mesh_collision_from_mesh(
        cls,
        from_dynamic_mesh: DynamicMesh,
        to_static_mesh_asset: StaticMesh,
        options: GeometryScriptCollisionFromMeshOptions,
        static_mesh_collision_options:
    GeometryScriptSetStaticMeshCollisionOptions = [True],
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.set_static_mesh_collision_from_mesh(from_dynamic_mesh, to_static_mesh_asset, options, static_mesh_collision_options=[True], debug=None) -> DynamicMesh
Generates Simple Collision shapes for a Static Mesh Asset based on the input Dynamic Mesh.

Args:
    from_dynamic_mesh (DynamicMesh): 
    to_static_mesh_asset (StaticMesh): 
    options (GeometryScriptCollisionFromMeshOptions): 
    static_mesh_collision_options (GeometryScriptSetStaticMeshCollisionOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Collision.set_static_mesh_collision_from_component"></a>

#### set_static_mesh_collision_from_component

```python
@classmethod
def set_static_mesh_collision_from_component(
        cls,
        static_mesh_asset: StaticMesh,
        source_component: PrimitiveComponent,
        options: GeometryScriptSetSimpleCollisionOptions = [True],
        static_mesh_collision_options:
    GeometryScriptSetStaticMeshCollisionOptions = [True],
        debug: GeometryScriptDebug = None) -> None
```

X.set_static_mesh_collision_from_component(static_mesh_asset, source_component, options=[True], static_mesh_collision_options=[True], debug=None) -> None
Copy the Simple Collision Geometry from the Source Component to the Static Mesh Asset.

Args:
    static_mesh_asset (StaticMesh): 
    source_component (PrimitiveComponent): 
    options (GeometryScriptSetSimpleCollisionOptions): 
    static_mesh_collision_options (GeometryScriptSetStaticMeshCollisionOptions): 
    debug (GeometryScriptDebug):

<a id="unreal.GeometryScript_Collision.set_simple_collision_of_static_mesh"></a>

#### set_simple_collision_of_static_mesh

```python
@classmethod
def set_simple_collision_of_static_mesh(
        cls,
        simple_collision: GeometryScriptSimpleCollision,
        static_mesh: StaticMesh,
        options: GeometryScriptSetSimpleCollisionOptions,
        static_mesh_collision_options:
    GeometryScriptSetStaticMeshCollisionOptions = [True],
        debug: GeometryScriptDebug = None) -> None
```

X.set_simple_collision_of_static_mesh(simple_collision, static_mesh, options, static_mesh_collision_options=[True], debug=None) -> None
* Set the simple collision on a Static Mesh

Args:
    simple_collision (GeometryScriptSimpleCollision): 
    static_mesh (StaticMesh): 
    options (GeometryScriptSetSimpleCollisionOptions): 
    static_mesh_collision_options (GeometryScriptSetStaticMeshCollisionOptions): 
    debug (GeometryScriptDebug):

<a id="unreal.GeometryScript_Collision.set_simple_collision_of_dynamic_mesh_component"></a>

#### set_simple_collision_of_dynamic_mesh_component

```python
@classmethod
def set_simple_collision_of_dynamic_mesh_component(
        cls,
        simple_collision: GeometryScriptSimpleCollision,
        dynamic_mesh_component: DynamicMeshComponent,
        options: GeometryScriptSetSimpleCollisionOptions,
        debug: GeometryScriptDebug = None) -> None
```

X.set_simple_collision_of_dynamic_mesh_component(simple_collision, dynamic_mesh_component, options, debug=None) -> None
* Set the simple collision on a Dynamic Mesh Component

Args:
    simple_collision (GeometryScriptSimpleCollision): 
    dynamic_mesh_component (DynamicMeshComponent): 
    options (GeometryScriptSetSimpleCollisionOptions): 
    debug (GeometryScriptDebug):

<a id="unreal.GeometryScript_Collision.set_dynamic_mesh_collision_from_mesh"></a>

#### set_dynamic_mesh_collision_from_mesh

```python
@classmethod
def set_dynamic_mesh_collision_from_mesh(
        cls,
        from_dynamic_mesh: DynamicMesh,
        to_dynamic_mesh_component: DynamicMeshComponent,
        options: GeometryScriptCollisionFromMeshOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.set_dynamic_mesh_collision_from_mesh(from_dynamic_mesh, to_dynamic_mesh_component, options, debug=None) -> DynamicMesh
Generate Simple Collision shapes for a Dynamic Mesh Component based on the input Dynamic Mesh.

Args:
    from_dynamic_mesh (DynamicMesh): 
    to_dynamic_mesh_component (DynamicMeshComponent): 
    options (GeometryScriptCollisionFromMeshOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Collision.reset_simple_collision"></a>

#### reset_simple_collision

```python
@classmethod
def reset_simple_collision(
    cls, simple_collision: GeometryScriptSimpleCollision
) -> GeometryScriptSimpleCollision
```

X.reset_simple_collision(simple_collision) -> GeometryScriptSimpleCollision
Clears the Simple Collision shapes

Args:
    simple_collision (GeometryScriptSimpleCollision): 

Returns:
    GeometryScriptSimpleCollision: 

    simple_collision (GeometryScriptSimpleCollision):

<a id="unreal.GeometryScript_Collision.reset_dynamic_mesh_collision"></a>

#### reset_dynamic_mesh_collision

```python
@classmethod
def reset_dynamic_mesh_collision(cls,
                                 component: DynamicMeshComponent,
                                 emit_transaction: bool = False,
                                 debug: GeometryScriptDebug = None) -> None
```

X.reset_dynamic_mesh_collision(component, emit_transaction=False, debug=None) -> None
Clears Simple Collisions from the Dynamic Mesh Component.

Args:
    component (DynamicMeshComponent): 
    emit_transaction (bool): 
    debug (GeometryScriptDebug):

<a id="unreal.GeometryScript_Collision.merge_simple_collision_shapes"></a>

#### merge_simple_collision_shapes

```python
@classmethod
def merge_simple_collision_shapes(
    cls,
    simple_collision: GeometryScriptSimpleCollision,
    merge_options: GeometryScriptMergeSimpleCollisionOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[GeometryScriptSimpleCollision, bool]
```

X.merge_simple_collision_shapes(simple_collision, merge_options, debug=None) -> (GeometryScriptSimpleCollision, has_merged=bool)
Attempt to merge collision shapes to create a representation with fewer overall shapes.

Args:
    simple_collision (GeometryScriptSimpleCollision): The collision to attempt to simplify by merging shapes
    merge_options (GeometryScriptMergeSimpleCollisionOptions): Options controlling how shapes can be merged
    debug (GeometryScriptDebug): 

Returns:
    bool: Simple Collision with collision shapes merged, as allowed by settings

    has_merged (bool): Indicates whether any shapes have been merged

<a id="unreal.GeometryScript_Collision.get_simple_collision_shape_count"></a>

#### get_simple_collision_shape_count

```python
@classmethod
def get_simple_collision_shape_count(
        cls, simple_collision: GeometryScriptSimpleCollision) -> int
```

X.get_simple_collision_shape_count(simple_collision) -> int32
* Count of number of simple collision shapes

Args:
    simple_collision (GeometryScriptSimpleCollision): 

Returns:
    int32:

<a id="unreal.GeometryScript_Collision.get_simple_collision_from_static_mesh"></a>

#### get_simple_collision_from_static_mesh

```python
@classmethod
def get_simple_collision_from_static_mesh(
        cls,
        static_mesh: StaticMesh,
        debug: GeometryScriptDebug = None) -> GeometryScriptSimpleCollision
```

X.get_simple_collision_from_static_mesh(static_mesh, debug=None) -> GeometryScriptSimpleCollision
* Get the simple collision from a Static Mesh

Args:
    static_mesh (StaticMesh): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptSimpleCollision:

<a id="unreal.GeometryScript_Collision.get_simple_collision_from_component"></a>

#### get_simple_collision_from_component

```python
@classmethod
def get_simple_collision_from_component(
        cls,
        component: PrimitiveComponent,
        debug: GeometryScriptDebug = None) -> GeometryScriptSimpleCollision
```

X.get_simple_collision_from_component(component, debug=None) -> GeometryScriptSimpleCollision
* Get the simple collision from a Primitive Component

Args:
    component (PrimitiveComponent): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptSimpleCollision:

<a id="unreal.GeometryScript_Collision.generate_collision_from_mesh"></a>

#### generate_collision_from_mesh

```python
@classmethod
def generate_collision_from_mesh(
        cls,
        from_dynamic_mesh: DynamicMesh,
        options: GeometryScriptCollisionFromMeshOptions,
        debug: GeometryScriptDebug = None) -> GeometryScriptSimpleCollision
```

X.generate_collision_from_mesh(from_dynamic_mesh, options, debug=None) -> GeometryScriptSimpleCollision
Generate Simple Collision shapes for an input Dynamic Mesh shape

Args:
    from_dynamic_mesh (DynamicMesh): 
    options (GeometryScriptCollisionFromMeshOptions): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptSimpleCollision:

<a id="unreal.GeometryScript_Collision.conv_sphere_array_to_geometry_script_sphere_covering"></a>

#### conv_sphere_array_to_geometry_script_sphere_covering

```python
@classmethod
def conv_sphere_array_to_geometry_script_sphere_covering(
        cls, spheres: Array[Sphere]) -> GeometryScriptSphereCovering
```

X.conv_sphere_array_to_geometry_script_sphere_covering(spheres) -> GeometryScriptSphereCovering


Args:
    spheres (Array[Sphere]): 

Returns:
    GeometryScriptSphereCovering: A sphere covering containing the spheres in the given Spheres array

<a id="unreal.GeometryScript_Collision.conv_geometry_script_sphere_covering_to_sphere_array"></a>

#### conv_geometry_script_sphere_covering_to_sphere_array

```python
@classmethod
def conv_geometry_script_sphere_covering_to_sphere_array(
        cls, sphere_covering: GeometryScriptSphereCovering) -> Array[Sphere]
```

X.conv_geometry_script_sphere_covering_to_sphere_array(sphere_covering) -> Array[Sphere]


Args:
    sphere_covering (GeometryScriptSphereCovering): 

Returns:
    Array[Sphere]: An array of the spheres in the given Sphere Covering

<a id="unreal.GeometryScript_Collision.compute_negative_space"></a>

#### compute_negative_space

```python
@classmethod
def compute_negative_space(
        cls,
        mesh_bvh: GeometryScriptDynamicMeshBVH,
        negative_space_options: ComputeNegativeSpaceOptions,
        debug: GeometryScriptDebug = None) -> GeometryScriptSphereCovering
```

X.compute_negative_space(mesh_bvh, negative_space_options, debug=None) -> GeometryScriptSphereCovering
Compute the negative space of an input mesh surface that should be protected when merging simple collision shapes

Args:
    mesh_bvh (GeometryScriptDynamicMeshBVH): A Dynamic Mesh BVH structure of the surface for which we will compute negative space
    negative_space_options (ComputeNegativeSpaceOptions): Options controlling how the negative space is generated
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptSphereCovering: A set of spheres that cover the negative space of the input shape

<a id="unreal.GeometryScript_Collision.compute_navigable_convex_decomposition"></a>

#### compute_navigable_convex_decomposition

```python
@classmethod
def compute_navigable_convex_decomposition(
        cls,
        target_mesh: DynamicMesh,
        options: NavigableConvexDecompositionOptions,
        debug: GeometryScriptDebug = None) -> GeometryScriptSimpleCollision
```

X.compute_navigable_convex_decomposition(target_mesh, options, debug=None) -> GeometryScriptSimpleCollision
Compute the 'navigable' convex decomposition of an input mesh surface, i.e. a convex decomposition
appropriate for a character of (or larger than) a given size

Args:
    target_mesh (DynamicMesh): Mesh to decompose to convex hulls
    options (NavigableConvexDecompositionOptions): Options controlling the convex decomposition
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptSimpleCollision: The resulting convex hulls as simple collision shapes

<a id="unreal.GeometryScript_Collision.combine_simple_collision_array"></a>

#### combine_simple_collision_array

```python
@classmethod
def combine_simple_collision_array(
        cls,
        simple_collision_array: Array[GeometryScriptSimpleCollision],
        debug: GeometryScriptDebug = None) -> GeometryScriptSimpleCollision
```

X.combine_simple_collision_array(simple_collision_array, debug=None) -> GeometryScriptSimpleCollision
* Combine the SimpleCollisionArray collision shapes into a single SimpleCollision

Args:
    simple_collision_array (Array[GeometryScriptSimpleCollision]): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptSimpleCollision: 

    simple_collision (GeometryScriptSimpleCollision):

<a id="unreal.GeometryScript_Collision.combine_simple_collision"></a>

#### combine_simple_collision

```python
@classmethod
def combine_simple_collision(
        cls,
        collision_to_update: GeometryScriptSimpleCollision,
        append_collision: GeometryScriptSimpleCollision,
        debug: GeometryScriptDebug = None) -> GeometryScriptSimpleCollision
```

X.combine_simple_collision(collision_to_update, append_collision, debug=None) -> GeometryScriptSimpleCollision
* Add simple collision shapes from AppendCollision to CollisionToUpdate

Args:
    collision_to_update (GeometryScriptSimpleCollision): 
    append_collision (GeometryScriptSimpleCollision): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptSimpleCollision: 

    collision_to_update (GeometryScriptSimpleCollision):

<a id="unreal.GeometryScript_Collision.approximate_convex_hulls_with_simpler_collision_shapes"></a>

#### approximate_convex_hulls_with_simpler_collision_shapes

```python
@classmethod
def approximate_convex_hulls_with_simpler_collision_shapes(
    cls,
    simple_collision: GeometryScriptSimpleCollision,
    approximate_options: GeometryScriptConvexHullApproximationOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[GeometryScriptSimpleCollision, bool]
```

X.approximate_convex_hulls_with_simpler_collision_shapes(simple_collision, approximate_options, debug=None) -> (simple_collision=GeometryScriptSimpleCollision, has_approximated=bool)
Attempt to approximate any convex hulls in the given simple collision representation. Updates the passed-in Simple Collision.
Convex hulls that aren't well approximated (to tolerances set in ApproximateOptions) will remain as convex hulls.

Args:
    simple_collision (GeometryScriptSimpleCollision): The collision in which to attempt to approximate the convex hulls
    approximate_options (GeometryScriptConvexHullApproximationOptions): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    simple_collision (GeometryScriptSimpleCollision): The collision in which to attempt to approximate the convex hulls

    has_approximated (bool): Indicates whether any convex hulls were replaced with simpler approximations

<a id="unreal.GeometryScript_Containment"></a>