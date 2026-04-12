## glTFRuntimeAsset Objects

```python
class glTFRuntimeAsset(Object)
```

Gl TFRuntime Asset

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: glTFRuntime
- **File**: glTFRuntimeAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``materials_map`` (Map[EglTFRuntimeMaterialType, MaterialInterface]):  [Read-Write]
- ``on_error`` (glTFRuntimeError):  [Read-Write]
- ``on_skeletal_mesh_created`` (glTFRuntimeOnSkeletalMeshCreated):  [Read-Write]
- ``on_static_mesh_created`` (glTFRuntimeOnStaticMeshCreated):  [Read-Write]
- ``runtime_context_object`` (Object):  [Read-Write]
- ``runtime_context_string`` (str):  [Read-Write]

<a id="unreal.glTFRuntimeAsset.materials_map"></a>

#### materials\_map

```python
@property
def materials_map() -> Map[EglTFRuntimeMaterialType, MaterialInterface]
```

(Map[EglTFRuntimeMaterialType, MaterialInterface]):  [Read-Write]

<a id="unreal.glTFRuntimeAsset.materials_map"></a>

#### materials\_map

```python
@materials_map.setter
def materials_map(
        value: Map[EglTFRuntimeMaterialType, MaterialInterface]) -> None
```

<a id="unreal.glTFRuntimeAsset.on_error"></a>

#### on\_error

```python
@property
def on_error() -> glTFRuntimeError
```

(glTFRuntimeError):  [Read-Write]

<a id="unreal.glTFRuntimeAsset.on_error"></a>

#### on\_error

```python
@on_error.setter
def on_error(value: glTFRuntimeError) -> None
```

<a id="unreal.glTFRuntimeAsset.on_static_mesh_created"></a>

#### on\_static\_mesh\_created

```python
@property
def on_static_mesh_created() -> glTFRuntimeOnStaticMeshCreated
```

(glTFRuntimeOnStaticMeshCreated):  [Read-Write]

<a id="unreal.glTFRuntimeAsset.on_static_mesh_created"></a>

#### on\_static\_mesh\_created

```python
@on_static_mesh_created.setter
def on_static_mesh_created(value: glTFRuntimeOnStaticMeshCreated) -> None
```

<a id="unreal.glTFRuntimeAsset.on_skeletal_mesh_created"></a>

#### on\_skeletal\_mesh\_created

```python
@property
def on_skeletal_mesh_created() -> glTFRuntimeOnSkeletalMeshCreated
```

(glTFRuntimeOnSkeletalMeshCreated):  [Read-Write]

<a id="unreal.glTFRuntimeAsset.on_skeletal_mesh_created"></a>

#### on\_skeletal\_mesh\_created

```python
@on_skeletal_mesh_created.setter
def on_skeletal_mesh_created(value: glTFRuntimeOnSkeletalMeshCreated) -> None
```

<a id="unreal.glTFRuntimeAsset.runtime_context_object"></a>

#### runtime\_context\_object

```python
@property
def runtime_context_object() -> Object
```

(Object):  [Read-Write]

<a id="unreal.glTFRuntimeAsset.runtime_context_object"></a>

#### runtime\_context\_object

```python
@runtime_context_object.setter
def runtime_context_object(value: Object) -> None
```

<a id="unreal.glTFRuntimeAsset.runtime_context_string"></a>

#### runtime\_context\_string

```python
@property
def runtime_context_string() -> str
```

(str):  [Read-Write]

<a id="unreal.glTFRuntimeAsset.runtime_context_string"></a>

#### runtime\_context\_string

```python
@runtime_context_string.setter
def runtime_context_string(value: str) -> None
```

<a id="unreal.glTFRuntimeAsset.to_json_string"></a>

#### to\_json\_string

```python
def to_json_string() -> str
```

x.to_json_string() -> str
To Json String

Returns:
    str:

<a id="unreal.glTFRuntimeAsset.node_is_bone"></a>

#### node\_is\_bone

```python
def node_is_bone(node_index: int) -> bool
```

x.node_is_bone(node_index) -> bool
Node Is Bone

Args:
    node_index (int32): 

Returns:
    bool:

<a id="unreal.glTFRuntimeAsset.mesh_has_morph_targets"></a>

#### mesh\_has\_morph\_targets

```python
def mesh_has_morph_targets(mesh_index: int) -> bool
```

x.mesh_has_morph_targets(mesh_index) -> bool
Mesh Has Morph Targets

Args:
    mesh_index (int32): 

Returns:
    bool:

<a id="unreal.glTFRuntimeAsset.load_static_mesh_recursive_async"></a>

#### load\_static\_mesh\_recursive\_async

```python
def load_static_mesh_recursive_async(
        node_name: str, exclude_nodes: Array[str],
        async_callback: glTFRuntimeStaticMeshAsync,
        static_mesh_config: glTFRuntimeStaticMeshConfig) -> None
```

x.load_static_mesh_recursive_async(node_name, exclude_nodes, async_callback, static_mesh_config) -> None
Load Static Mesh Recursive Async

Args:
    node_name (str): 
    exclude_nodes (Array[str]): 
    async_callback (glTFRuntimeStaticMeshAsync): 
    static_mesh_config (glTFRuntimeStaticMeshConfig):

<a id="unreal.glTFRuntimeAsset.load_static_mesh_recursive"></a>

#### load\_static\_mesh\_recursive

```python
def load_static_mesh_recursive(
        node_name: str, exclude_nodes: Array[str],
        static_mesh_config: glTFRuntimeStaticMeshConfig) -> StaticMesh
```

x.load_static_mesh_recursive(node_name, exclude_nodes, static_mesh_config) -> StaticMesh
Load Static Mesh Recursive

Args:
    node_name (str): 
    exclude_nodes (Array[str]): 
    static_mesh_config (glTFRuntimeStaticMeshConfig): 

Returns:
    StaticMesh:

<a id="unreal.glTFRuntimeAsset.load_static_mesh_lo_ds_async"></a>

#### load\_static\_mesh\_lo\_ds\_async

```python
def load_static_mesh_lo_ds_async(
        mesh_indices: Array[int], async_callback: glTFRuntimeStaticMeshAsync,
        static_mesh_config: glTFRuntimeStaticMeshConfig) -> None
```

x.load_static_mesh_lo_ds_async(mesh_indices, async_callback, static_mesh_config) -> None
Load Static Mesh LODs Async

Args:
    mesh_indices (Array[int32]): 
    async_callback (glTFRuntimeStaticMeshAsync): 
    static_mesh_config (glTFRuntimeStaticMeshConfig):

<a id="unreal.glTFRuntimeAsset.load_static_mesh_lo_ds"></a>

#### load\_static\_mesh\_lo\_ds

```python
def load_static_mesh_lo_ds(
        mesh_indices: Array[int],
        static_mesh_config: glTFRuntimeStaticMeshConfig) -> StaticMesh
```

x.load_static_mesh_lo_ds(mesh_indices, static_mesh_config) -> StaticMesh
Load Static Mesh LODs

Args:
    mesh_indices (Array[int32]): 
    static_mesh_config (glTFRuntimeStaticMeshConfig): 

Returns:
    StaticMesh:

<a id="unreal.glTFRuntimeAsset.load_static_mesh_into_procedural_mesh_component"></a>

#### load\_static\_mesh\_into\_procedural\_mesh\_component

```python
def load_static_mesh_into_procedural_mesh_component(
        mesh_index: int, procedural_mesh_component: ProceduralMeshComponent,
        procedural_mesh_config: glTFRuntimeProceduralMeshConfig) -> bool
```

x.load_static_mesh_into_procedural_mesh_component(mesh_index, procedural_mesh_component, procedural_mesh_config) -> bool
Load Static Mesh Into Procedural Mesh Component

Args:
    mesh_index (int32): 
    procedural_mesh_component (ProceduralMeshComponent): 
    procedural_mesh_config (glTFRuntimeProceduralMeshConfig): 

Returns:
    bool:

<a id="unreal.glTFRuntimeAsset.load_static_mesh_from_runtime_lo_ds_async"></a>

#### load\_static\_mesh\_from\_runtime\_lo\_ds\_async

```python
def load_static_mesh_from_runtime_lo_ds_async(
        runtime_lo_ds: Array[glTFRuntimeMeshLOD],
        async_callback: glTFRuntimeStaticMeshAsync,
        static_mesh_config: glTFRuntimeStaticMeshConfig) -> None
```

x.load_static_mesh_from_runtime_lo_ds_async(runtime_lo_ds, async_callback, static_mesh_config) -> None
Load Static Mesh from Runtime LODs Async

Args:
    runtime_lo_ds (Array[glTFRuntimeMeshLOD]): 
    async_callback (glTFRuntimeStaticMeshAsync): 
    static_mesh_config (glTFRuntimeStaticMeshConfig):

<a id="unreal.glTFRuntimeAsset.load_static_mesh_from_runtime_lo_ds"></a>

#### load\_static\_mesh\_from\_runtime\_lo\_ds

```python
def load_static_mesh_from_runtime_lo_ds(
        runtime_lo_ds: Array[glTFRuntimeMeshLOD],
        static_mesh_config: glTFRuntimeStaticMeshConfig) -> StaticMesh
```

x.load_static_mesh_from_runtime_lo_ds(runtime_lo_ds, static_mesh_config) -> StaticMesh
Load Static Mesh from Runtime LODs

Args:
    runtime_lo_ds (Array[glTFRuntimeMeshLOD]): 
    static_mesh_config (glTFRuntimeStaticMeshConfig): 

Returns:
    StaticMesh:

<a id="unreal.glTFRuntimeAsset.load_static_meshes_from_primitives"></a>

#### load\_static\_meshes\_from\_primitives

```python
def load_static_meshes_from_primitives(
        mesh_index: int,
        static_mesh_config: glTFRuntimeStaticMeshConfig) -> Array[StaticMesh]
```

x.load_static_meshes_from_primitives(mesh_index, static_mesh_config) -> Array[StaticMesh]
Load Static Meshes from Primitives

Args:
    mesh_index (int32): 
    static_mesh_config (glTFRuntimeStaticMeshConfig): 

Returns:
    Array[StaticMesh]:

<a id="unreal.glTFRuntimeAsset.load_static_mesh_by_node_name"></a>

#### load\_static\_mesh\_by\_node\_name

```python
def load_static_mesh_by_node_name(
        node_name: str,
        static_mesh_config: glTFRuntimeStaticMeshConfig) -> StaticMesh
```

x.load_static_mesh_by_node_name(node_name, static_mesh_config) -> StaticMesh
Load Static Mesh by Node Name

Args:
    node_name (str): 
    static_mesh_config (glTFRuntimeStaticMeshConfig): 

Returns:
    StaticMesh:

<a id="unreal.glTFRuntimeAsset.load_static_mesh_by_name"></a>

#### load\_static\_mesh\_by\_name

```python
def load_static_mesh_by_name(
        mesh_name: str,
        static_mesh_config: glTFRuntimeStaticMeshConfig) -> StaticMesh
```

x.load_static_mesh_by_name(mesh_name, static_mesh_config) -> StaticMesh
Load Static Mesh by Name

Args:
    mesh_name (str): 
    static_mesh_config (glTFRuntimeStaticMeshConfig): 

Returns:
    StaticMesh:

<a id="unreal.glTFRuntimeAsset.load_static_mesh_async"></a>

#### load\_static\_mesh\_async

```python
def load_static_mesh_async(
        mesh_index: int, async_callback: glTFRuntimeStaticMeshAsync,
        static_mesh_config: glTFRuntimeStaticMeshConfig) -> None
```

x.load_static_mesh_async(mesh_index, async_callback, static_mesh_config) -> None
Load Static Mesh Async

Args:
    mesh_index (int32): 
    async_callback (glTFRuntimeStaticMeshAsync): 
    static_mesh_config (glTFRuntimeStaticMeshConfig):

<a id="unreal.glTFRuntimeAsset.load_static_mesh"></a>

#### load\_static\_mesh

```python
def load_static_mesh(
        mesh_index: int,
        static_mesh_config: glTFRuntimeStaticMeshConfig) -> StaticMesh
```

x.load_static_mesh(mesh_index, static_mesh_config) -> StaticMesh
Load Static Mesh

Args:
    mesh_index (int32): 
    static_mesh_config (glTFRuntimeStaticMeshConfig): 

Returns:
    StaticMesh:

<a id="unreal.glTFRuntimeAsset.load_skinned_mesh_recursive_as_runtime_lod"></a>

#### load\_skinned\_mesh\_recursive\_as\_runtime\_lod

```python
def load_skinned_mesh_recursive_as_runtime_lod(
    node_name: str,
    exclude_nodes: Array[str],
    materials_config: glTFRuntimeMaterialsConfig,
    skeleton_config: glTFRuntimeSkeletonConfig,
    override_skin_index: int = -1,
    transform_apply_recursive_mode:
    EglTFRuntimeRecursiveMode = EglTFRuntimeRecursiveMode.IGNORE
) -> Optional[Tuple[glTFRuntimeMeshLOD, int]]
```

x.load_skinned_mesh_recursive_as_runtime_lod(node_name, exclude_nodes, materials_config, skeleton_config, override_skin_index=-1, transform_apply_recursive_mode=EglTFRuntimeRecursiveMode.IGNORE) -> (runtime_lod=glTFRuntimeMeshLOD, skin_index=int32) or None
Load Skinned Mesh Recursive as Runtime LOD

Args:
    node_name (str): 
    exclude_nodes (Array[str]): 
    materials_config (glTFRuntimeMaterialsConfig): 
    skeleton_config (glTFRuntimeSkeletonConfig): 
    override_skin_index (int32): 
    transform_apply_recursive_mode (EglTFRuntimeRecursiveMode): 

Returns:
    tuple or None: 

    runtime_lod (glTFRuntimeMeshLOD): 

    skin_index (int32):

<a id="unreal.glTFRuntimeAsset.load_skeleton_from_node_tree_by_name"></a>

#### load\_skeleton\_from\_node\_tree\_by\_name

```python
def load_skeleton_from_node_tree_by_name(
        node_name: str,
        skeleton_config: glTFRuntimeSkeletonConfig) -> Skeleton
```

x.load_skeleton_from_node_tree_by_name(node_name, skeleton_config) -> Skeleton
Load Skeleton from Node Tree by Name

Args:
    node_name (str): 
    skeleton_config (glTFRuntimeSkeletonConfig): 

Returns:
    Skeleton:

<a id="unreal.glTFRuntimeAsset.load_skeleton_from_node_tree"></a>

#### load\_skeleton\_from\_node\_tree

```python
def load_skeleton_from_node_tree(
        node_index: int,
        skeleton_config: glTFRuntimeSkeletonConfig) -> Skeleton
```

x.load_skeleton_from_node_tree(node_index, skeleton_config) -> Skeleton
Load Skeleton from Node Tree

Args:
    node_index (int32): 
    skeleton_config (glTFRuntimeSkeletonConfig): 

Returns:
    Skeleton:

<a id="unreal.glTFRuntimeAsset.load_skeleton"></a>

#### load\_skeleton

```python
def load_skeleton(skin_index: int,
                  skeleton_config: glTFRuntimeSkeletonConfig) -> Skeleton
```

x.load_skeleton(skin_index, skeleton_config) -> Skeleton
Load Skeleton

Args:
    skin_index (int32): 
    skeleton_config (glTFRuntimeSkeletonConfig): 

Returns:
    Skeleton:

<a id="unreal.glTFRuntimeAsset.load_skeletal_mesh_recursive_async"></a>

#### load\_skeletal\_mesh\_recursive\_async

```python
def load_skeletal_mesh_recursive_async(
    node_name: str,
    exclude_nodes: Array[str],
    async_callback: glTFRuntimeSkeletalMeshAsync,
    skeletal_mesh_config: glTFRuntimeSkeletalMeshConfig,
    transform_apply_recursive_mode:
    EglTFRuntimeRecursiveMode = EglTFRuntimeRecursiveMode.IGNORE
) -> None
```

x.load_skeletal_mesh_recursive_async(node_name, exclude_nodes, async_callback, skeletal_mesh_config, transform_apply_recursive_mode=EglTFRuntimeRecursiveMode.IGNORE) -> None
Load Skeletal Mesh Recursive Async

Args:
    node_name (str): 
    exclude_nodes (Array[str]): 
    async_callback (glTFRuntimeSkeletalMeshAsync): 
    skeletal_mesh_config (glTFRuntimeSkeletalMeshConfig): 
    transform_apply_recursive_mode (EglTFRuntimeRecursiveMode):

<a id="unreal.glTFRuntimeAsset.load_skeletal_mesh_recursive"></a>

#### load\_skeletal\_mesh\_recursive

```python
def load_skeletal_mesh_recursive(
    node_name: str,
    exclude_nodes: Array[str],
    skeletal_mesh_config: glTFRuntimeSkeletalMeshConfig,
    transform_apply_recursive_mode:
    EglTFRuntimeRecursiveMode = EglTFRuntimeRecursiveMode.IGNORE
) -> SkeletalMesh
```

x.load_skeletal_mesh_recursive(node_name, exclude_nodes, skeletal_mesh_config, transform_apply_recursive_mode=EglTFRuntimeRecursiveMode.IGNORE) -> SkeletalMesh
Load Skeletal Mesh Recursive

Args:
    node_name (str): 
    exclude_nodes (Array[str]): 
    skeletal_mesh_config (glTFRuntimeSkeletalMeshConfig): 
    transform_apply_recursive_mode (EglTFRuntimeRecursiveMode): 

Returns:
    SkeletalMesh:

<a id="unreal.glTFRuntimeAsset.load_skeletal_mesh_lo_ds"></a>

#### load\_skeletal\_mesh\_lo\_ds

```python
def load_skeletal_mesh_lo_ds(
        mesh_indices: Array[int], skin_index: int,
        skeletal_mesh_config: glTFRuntimeSkeletalMeshConfig) -> SkeletalMesh
```

x.load_skeletal_mesh_lo_ds(mesh_indices, skin_index, skeletal_mesh_config) -> SkeletalMesh
Load Skeletal Mesh LODs

Args:
    mesh_indices (Array[int32]): 
    skin_index (int32): 
    skeletal_mesh_config (glTFRuntimeSkeletalMeshConfig): 

Returns:
    SkeletalMesh:

<a id="unreal.glTFRuntimeAsset.load_skeletal_mesh_from_runtime_lo_ds_async"></a>

#### load\_skeletal\_mesh\_from\_runtime\_lo\_ds\_async

```python
def load_skeletal_mesh_from_runtime_lo_ds_async(
        runtime_lo_ds: Array[glTFRuntimeMeshLOD], skin_index: int,
        async_callback: glTFRuntimeSkeletalMeshAsync,
        skeletal_mesh_config: glTFRuntimeSkeletalMeshConfig) -> None
```

x.load_skeletal_mesh_from_runtime_lo_ds_async(runtime_lo_ds, skin_index, async_callback, skeletal_mesh_config) -> None
Load Skeletal Mesh from Runtime LODs Async

Args:
    runtime_lo_ds (Array[glTFRuntimeMeshLOD]): 
    skin_index (int32): 
    async_callback (glTFRuntimeSkeletalMeshAsync): 
    skeletal_mesh_config (glTFRuntimeSkeletalMeshConfig):

<a id="unreal.glTFRuntimeAsset.load_skeletal_mesh_from_runtime_lo_ds"></a>

#### load\_skeletal\_mesh\_from\_runtime\_lo\_ds

```python
def load_skeletal_mesh_from_runtime_lo_ds(
        runtime_lo_ds: Array[glTFRuntimeMeshLOD], skin_index: int,
        skeletal_mesh_config: glTFRuntimeSkeletalMeshConfig) -> SkeletalMesh
```

x.load_skeletal_mesh_from_runtime_lo_ds(runtime_lo_ds, skin_index, skeletal_mesh_config) -> SkeletalMesh
Load Skeletal Mesh from Runtime LODs

Args:
    runtime_lo_ds (Array[glTFRuntimeMeshLOD]): 
    skin_index (int32): 
    skeletal_mesh_config (glTFRuntimeSkeletalMeshConfig): 

Returns:
    SkeletalMesh:

<a id="unreal.glTFRuntimeAsset.load_skeletal_mesh_async"></a>

#### load\_skeletal\_mesh\_async

```python
def load_skeletal_mesh_async(
        mesh_index: int, skin_index: int,
        async_callback: glTFRuntimeSkeletalMeshAsync,
        skeletal_mesh_config: glTFRuntimeSkeletalMeshConfig) -> None
```

x.load_skeletal_mesh_async(mesh_index, skin_index, async_callback, skeletal_mesh_config) -> None
Load Skeletal Mesh Async

Args:
    mesh_index (int32): 
    skin_index (int32): 
    async_callback (glTFRuntimeSkeletalMeshAsync): 
    skeletal_mesh_config (glTFRuntimeSkeletalMeshConfig):

<a id="unreal.glTFRuntimeAsset.load_skeletal_mesh"></a>

#### load\_skeletal\_mesh

```python
def load_skeletal_mesh(
        mesh_index: int, skin_index: int,
        skeletal_mesh_config: glTFRuntimeSkeletalMeshConfig) -> SkeletalMesh
```

x.load_skeletal_mesh(mesh_index, skin_index, skeletal_mesh_config) -> SkeletalMesh
Load Skeletal Mesh

Args:
    mesh_index (int32): 
    skin_index (int32): 
    skeletal_mesh_config (glTFRuntimeSkeletalMeshConfig): 

Returns:
    SkeletalMesh:

<a id="unreal.glTFRuntimeAsset.load_skeletal_animation_by_name"></a>

#### load\_skeletal\_animation\_by\_name

```python
def load_skeletal_animation_by_name(
    skeletal_mesh: SkeletalMesh, animation_name: str,
    skeletal_animation_config: glTFRuntimeSkeletalAnimationConfig
) -> AnimSequence
```

x.load_skeletal_animation_by_name(skeletal_mesh, animation_name, skeletal_animation_config) -> AnimSequence
Load Skeletal Animation by Name

Args:
    skeletal_mesh (SkeletalMesh): 
    animation_name (str): 
    skeletal_animation_config (glTFRuntimeSkeletalAnimationConfig): 

Returns:
    AnimSequence:

<a id="unreal.glTFRuntimeAsset.load_skeletal_animation_as_montage"></a>

#### load\_skeletal\_animation\_as\_montage

```python
def load_skeletal_animation_as_montage(
    skeletal_mesh: SkeletalMesh, animation_index: int, slot_node_name: str,
    skeletal_animation_config: glTFRuntimeSkeletalAnimationConfig
) -> AnimMontage
```

x.load_skeletal_animation_as_montage(skeletal_mesh, animation_index, slot_node_name, skeletal_animation_config) -> AnimMontage
Load Skeletal Animation as Montage

Args:
    skeletal_mesh (SkeletalMesh): 
    animation_index (int32): 
    slot_node_name (str): 
    skeletal_animation_config (glTFRuntimeSkeletalAnimationConfig): 

Returns:
    AnimMontage:

<a id="unreal.glTFRuntimeAsset.load_skeletal_animation"></a>

#### load\_skeletal\_animation

```python
def load_skeletal_animation(
    skeletal_mesh: SkeletalMesh, animation_index: int,
    skeletal_animation_config: glTFRuntimeSkeletalAnimationConfig
) -> AnimSequence
```

x.load_skeletal_animation(skeletal_mesh, animation_index, skeletal_animation_config) -> AnimSequence
Load Skeletal Animation

Args:
    skeletal_mesh (SkeletalMesh): 
    animation_index (int32): 
    skeletal_animation_config (glTFRuntimeSkeletalAnimationConfig): 

Returns:
    AnimSequence:

<a id="unreal.glTFRuntimeAsset.load_punctual_light"></a>

#### load\_punctual\_light

```python
def load_punctual_light(
        punctual_light_index: int, actor: Actor,
        light_config: glTFRuntimeLightConfig) -> LightComponent
```

x.load_punctual_light(punctual_light_index, actor, light_config) -> LightComponent
Load Punctual Light

Args:
    punctual_light_index (int32): 
    actor (Actor): 
    light_config (glTFRuntimeLightConfig): 

Returns:
    LightComponent:

<a id="unreal.glTFRuntimeAsset.load_node_skeletal_animations_map"></a>

#### load\_node\_skeletal\_animations\_map

```python
def load_node_skeletal_animations_map(
    skeletal_mesh: SkeletalMesh, node_index: int,
    skeletal_animation_config: glTFRuntimeSkeletalAnimationConfig
) -> Map[str, AnimSequence]
```

x.load_node_skeletal_animations_map(skeletal_mesh, node_index, skeletal_animation_config) -> Map[str, AnimSequence]
Load Node Skeletal Animations Map

Args:
    skeletal_mesh (SkeletalMesh): 
    node_index (int32): 
    skeletal_animation_config (glTFRuntimeSkeletalAnimationConfig): 

Returns:
    Map[str, AnimSequence]:

<a id="unreal.glTFRuntimeAsset.load_node_skeletal_animation"></a>

#### load\_node\_skeletal\_animation

```python
def load_node_skeletal_animation(
    skeletal_mesh: SkeletalMesh, node_index: int,
    skeletal_animation_config: glTFRuntimeSkeletalAnimationConfig
) -> AnimSequence
```

x.load_node_skeletal_animation(skeletal_mesh, node_index, skeletal_animation_config) -> AnimSequence
Load Node Skeletal Animation

Args:
    skeletal_mesh (SkeletalMesh): 
    node_index (int32): 
    skeletal_animation_config (glTFRuntimeSkeletalAnimationConfig): 

Returns:
    AnimSequence:

<a id="unreal.glTFRuntimeAsset.load_node_camera"></a>

#### load\_node\_camera

```python
def load_node_camera(world_context_object: Object, node_index: int,
                     camera_actor_class: Class) -> CameraActor
```

x.load_node_camera(world_context_object, node_index, camera_actor_class) -> CameraActor
Load Node Camera

Args:
    world_context_object (Object): 
    node_index (int32): 
    camera_actor_class (type(Class)): 

Returns:
    CameraActor:

<a id="unreal.glTFRuntimeAsset.load_node_animation_curve"></a>

#### load\_node\_animation\_curve

```python
def load_node_animation_curve(node_index: int) -> glTFRuntimeAnimationCurve
```

x.load_node_animation_curve(node_index) -> glTFRuntimeAnimationCurve
Load Node Animation Curve

Args:
    node_index (int32): 

Returns:
    glTFRuntimeAnimationCurve:

<a id="unreal.glTFRuntimeAsset.load_mips_from_blob"></a>

#### load\_mips\_from\_blob

```python
def load_mips_from_blob(images_config: glTFRuntimeImagesConfig) -> Texture2D
```

x.load_mips_from_blob(images_config) -> Texture2D
Load Mips from Blob

Args:
    images_config (glTFRuntimeImagesConfig): 

Returns:
    Texture2D:

<a id="unreal.glTFRuntimeAsset.load_mesh_as_runtime_lod_async"></a>

#### load\_mesh\_as\_runtime\_lod\_async

```python
def load_mesh_as_runtime_lod_async(
        mesh_index: int, async_callback: glTFRuntimeMeshLODAsync,
        materials_config: glTFRuntimeMaterialsConfig) -> None
```

x.load_mesh_as_runtime_lod_async(mesh_index, async_callback, materials_config) -> None
Load Mesh as Runtime LODAsync

Args:
    mesh_index (int32): 
    async_callback (glTFRuntimeMeshLODAsync): 
    materials_config (glTFRuntimeMaterialsConfig):

<a id="unreal.glTFRuntimeAsset.load_mesh_as_runtime_lod"></a>

#### load\_mesh\_as\_runtime\_lod

```python
def load_mesh_as_runtime_lod(
    mesh_index: int, materials_config: glTFRuntimeMaterialsConfig
) -> Optional[glTFRuntimeMeshLOD]
```

x.load_mesh_as_runtime_lod(mesh_index, materials_config) -> glTFRuntimeMeshLOD or None
Load Mesh as Runtime LOD

Args:
    mesh_index (int32): 
    materials_config (glTFRuntimeMaterialsConfig): 

Returns:
    glTFRuntimeMeshLOD or None: 

    runtime_lod (glTFRuntimeMeshLOD):

<a id="unreal.glTFRuntimeAsset.load_material"></a>

#### load\_material

```python
def load_material(material_index: int,
                  materials_config: glTFRuntimeMaterialsConfig,
                  use_vertex_colors: bool) -> MaterialInterface
```

x.load_material(material_index, materials_config, use_vertex_colors) -> MaterialInterface
Load Material

Args:
    material_index (int32): 
    materials_config (glTFRuntimeMaterialsConfig): 
    use_vertex_colors (bool): 

Returns:
    MaterialInterface:

<a id="unreal.glTFRuntimeAsset.load_image_from_blob_async"></a>

#### load\_image\_from\_blob\_async

```python
def load_image_from_blob_async(async_callback: glTFRuntimeTexture2DAsync,
                               images_config: glTFRuntimeImagesConfig) -> None
```

x.load_image_from_blob_async(async_callback, images_config) -> None
Load Image from Blob Async

Args:
    async_callback (glTFRuntimeTexture2DAsync): 
    images_config (glTFRuntimeImagesConfig):

<a id="unreal.glTFRuntimeAsset.load_image_from_blob"></a>

#### load\_image\_from\_blob

```python
def load_image_from_blob(images_config: glTFRuntimeImagesConfig) -> Texture2D
```

x.load_image_from_blob(images_config) -> Texture2D
Load Image from Blob

Args:
    images_config (glTFRuntimeImagesConfig): 

Returns:
    Texture2D:

<a id="unreal.glTFRuntimeAsset.load_image_array_from_blob_async"></a>

#### load\_image\_array\_from\_blob\_async

```python
def load_image_array_from_blob_async(
        async_callback: glTFRuntimeTexture2DArrayAsync,
        images_config: glTFRuntimeImagesConfig) -> None
```

x.load_image_array_from_blob_async(async_callback, images_config) -> None
Load Image Array from Blob Async

Args:
    async_callback (glTFRuntimeTexture2DArrayAsync): 
    images_config (glTFRuntimeImagesConfig):

<a id="unreal.glTFRuntimeAsset.load_image_array_from_blob"></a>

#### load\_image\_array\_from\_blob

```python
def load_image_array_from_blob(
        images_config: glTFRuntimeImagesConfig) -> Texture2DArray
```

x.load_image_array_from_blob(images_config) -> Texture2DArray
Load Image Array from Blob

Args:
    images_config (glTFRuntimeImagesConfig): 

Returns:
    Texture2DArray:

<a id="unreal.glTFRuntimeAsset.load_image_array"></a>

#### load\_image\_array

```python
def load_image_array(image_indices: Array[int],
                     images_config: glTFRuntimeImagesConfig) -> Texture2DArray
```

x.load_image_array(image_indices, images_config) -> Texture2DArray
Load Image Array

Args:
    image_indices (Array[int32]): 
    images_config (glTFRuntimeImagesConfig): 

Returns:
    Texture2DArray:

<a id="unreal.glTFRuntimeAsset.load_image"></a>

#### load\_image

```python
def load_image(image_index: int,
               images_config: glTFRuntimeImagesConfig) -> Texture2D
```

x.load_image(image_index, images_config) -> Texture2D
Load Image

Args:
    image_index (int32): 
    images_config (glTFRuntimeImagesConfig): 

Returns:
    Texture2D:

<a id="unreal.glTFRuntimeAsset.load_emitter_into_audio_component"></a>

#### load\_emitter\_into\_audio\_component

```python
def load_emitter_into_audio_component(emitter: glTFRuntimeAudioEmitter,
                                      audio_component: AudioComponent) -> bool
```

x.load_emitter_into_audio_component(emitter, audio_component) -> bool
Load Emitter Into Audio Component

Args:
    emitter (glTFRuntimeAudioEmitter): 
    audio_component (AudioComponent): 

Returns:
    bool:

<a id="unreal.glTFRuntimeAsset.load_cube_map_from_blob_async"></a>

#### load\_cube\_map\_from\_blob\_async

```python
def load_cube_map_from_blob_async(
        spherical: bool, auto_rotate: bool,
        async_callback: glTFRuntimeTextureCubeAsync,
        images_config: glTFRuntimeImagesConfig) -> None
```

x.load_cube_map_from_blob_async(spherical, auto_rotate, async_callback, images_config) -> None
Load Cube Map from Blob Async

Args:
    spherical (bool): 
    auto_rotate (bool): 
    async_callback (glTFRuntimeTextureCubeAsync): 
    images_config (glTFRuntimeImagesConfig):

<a id="unreal.glTFRuntimeAsset.load_cube_map_from_blob"></a>

#### load\_cube\_map\_from\_blob

```python
def load_cube_map_from_blob(
        spherical: bool, auto_rotate: bool,
        images_config: glTFRuntimeImagesConfig) -> TextureCube
```

x.load_cube_map_from_blob(spherical, auto_rotate, images_config) -> TextureCube
Load Cube Map from Blob

Args:
    spherical (bool): 
    auto_rotate (bool): 
    images_config (glTFRuntimeImagesConfig): 

Returns:
    TextureCube:

<a id="unreal.glTFRuntimeAsset.load_cube_map"></a>

#### load\_cube\_map

```python
def load_cube_map(image_index_xp: int, image_index_xn: int,
                  image_index_yp: int, image_index_yn: int,
                  image_index_zp: int, image_index_zn: int, auto_rotate: bool,
                  images_config: glTFRuntimeImagesConfig) -> TextureCube
```

x.load_cube_map(image_index_xp, image_index_xn, image_index_yp, image_index_yn, image_index_zp, image_index_zn, auto_rotate, images_config) -> TextureCube
Load Cube Map

Args:
    image_index_xp (int32): 
    image_index_xn (int32): 
    image_index_yp (int32): 
    image_index_yn (int32): 
    image_index_zp (int32): 
    image_index_zn (int32): 
    auto_rotate (bool): 
    images_config (glTFRuntimeImagesConfig): 

Returns:
    TextureCube:

<a id="unreal.glTFRuntimeAsset.load_camera"></a>

#### load\_camera

```python
def load_camera(camera_index: int, camera_component: CameraComponent) -> bool
```

x.load_camera(camera_index, camera_component) -> bool
Load Camera

Args:
    camera_index (int32): 
    camera_component (CameraComponent): 

Returns:
    bool:

<a id="unreal.glTFRuntimeAsset.load_audio_emitter"></a>

#### load\_audio\_emitter

```python
def load_audio_emitter(
        emitter_index: int) -> Optional[glTFRuntimeAudioEmitter]
```

x.load_audio_emitter(emitter_index) -> glTFRuntimeAudioEmitter or None
Load Audio Emitter

Args:
    emitter_index (int32): 

Returns:
    glTFRuntimeAudioEmitter or None: 

    emitter (glTFRuntimeAudioEmitter):

<a id="unreal.glTFRuntimeAsset.load_all_node_animation_curves"></a>

#### load\_all\_node\_animation\_curves

```python
def load_all_node_animation_curves(
        node_index: int) -> Array[glTFRuntimeAnimationCurve]
```

x.load_all_node_animation_curves(node_index) -> Array[glTFRuntimeAnimationCurve]
Load All Node Animation Curves

Args:
    node_index (int32): 

Returns:
    Array[glTFRuntimeAnimationCurve]:

<a id="unreal.glTFRuntimeAsset.is_archive"></a>

#### is\_archive

```python
def is_archive() -> bool
```

x.is_archive() -> bool
Is Archive

Returns:
    bool:

<a id="unreal.glTFRuntimeAsset.has_errors"></a>

#### has\_errors

```python
def has_errors() -> bool
```

x.has_errors() -> bool
Has Errors

Returns:
    bool:

<a id="unreal.glTFRuntimeAsset.get_version"></a>

#### get\_version

```python
def get_version() -> str
```

x.get_version() -> str
Get Version

Returns:
    str:

<a id="unreal.glTFRuntimeAsset.get_string_map_from_extras"></a>

#### get\_string\_map\_from\_extras

```python
def get_string_map_from_extras(key: str) -> Optional[Map[str, str]]
```

x.get_string_map_from_extras(key) -> Map[str, str] or None
Get String Map from Extras

Args:
    key (str): 

Returns:
    Map[str, str] or None: 

    string_map (Map[str, str]):

<a id="unreal.glTFRuntimeAsset.get_string_from_path"></a>

#### get\_string\_from\_path

```python
def get_string_from_path(path: Array[glTFRuntimePathItem]) -> Tuple[str, bool]
```

x.get_string_from_path(path) -> (str, found=bool)
Get String from Path

Args:
    path (Array[glTFRuntimePathItem]): 

Returns:
    bool: 

    found (bool):

<a id="unreal.glTFRuntimeAsset.get_string_from_extras"></a>

#### get\_string\_from\_extras

```python
def get_string_from_extras(key: str) -> Optional[str]
```

x.get_string_from_extras(key) -> str or None
Get String from Extras

Args:
    key (str): 

Returns:
    str or None: 

    value (str):

<a id="unreal.glTFRuntimeAsset.get_string_array_from_extras"></a>

#### get\_string\_array\_from\_extras

```python
def get_string_array_from_extras(key: str) -> Optional[Array[str]]
```

x.get_string_array_from_extras(key) -> Array[str] or None
Get String Array from Extras

Args:
    key (str): 

Returns:
    Array[str] or None: 

    string_array (Array[str]):

<a id="unreal.glTFRuntimeAsset.get_scenes"></a>

#### get\_scenes

```python
def get_scenes() -> Array[glTFRuntimeScene]
```

x.get_scenes() -> Array[glTFRuntimeScene]
Get Scenes

Returns:
    Array[glTFRuntimeScene]:

<a id="unreal.glTFRuntimeAsset.get_num_meshes"></a>

#### get\_num\_meshes

```python
def get_num_meshes() -> int
```

x.get_num_meshes() -> int32
Get Num Meshes

Returns:
    int32:

<a id="unreal.glTFRuntimeAsset.get_num_images"></a>

#### get\_num\_images

```python
def get_num_images() -> int
```

x.get_num_images() -> int32
Get Num Images

Returns:
    int32:

<a id="unreal.glTFRuntimeAsset.get_number_from_extras"></a>

#### get\_number\_from\_extras

```python
def get_number_from_extras(key: str) -> Optional[float]
```

x.get_number_from_extras(key) -> float or None
Get Number from Extras

Args:
    key (str): 

Returns:
    float or None: 

    value (float):

<a id="unreal.glTFRuntimeAsset.get_num_animations"></a>

#### get\_num\_animations

```python
def get_num_animations() -> int
```

x.get_num_animations() -> int32
Get Num Animations

Returns:
    int32:

<a id="unreal.glTFRuntimeAsset.get_nodes"></a>

#### get\_nodes

```python
def get_nodes() -> Array[glTFRuntimeNode]
```

x.get_nodes() -> Array[glTFRuntimeNode]
Get Nodes

Returns:
    Array[glTFRuntimeNode]:

<a id="unreal.glTFRuntimeAsset.get_node_gpu_instancing_transforms"></a>

#### get\_node\_gpu\_instancing\_transforms

```python
def get_node_gpu_instancing_transforms(
        node_index: int) -> Optional[Array[Transform]]
```

x.get_node_gpu_instancing_transforms(node_index) -> Array[Transform] or None
Get Node GPUInstancing Transforms

Args:
    node_index (int32): 

Returns:
    Array[Transform] or None: 

    transforms (Array[Transform]):

<a id="unreal.glTFRuntimeAsset.get_node_extras_numbers"></a>

#### get\_node\_extras\_numbers

```python
def get_node_extras_numbers(node_index: int,
                            key: str) -> Optional[Array[float]]
```

x.get_node_extras_numbers(node_index, key) -> Array[float] or None
Get Node Extras Numbers

Args:
    node_index (int32): 
    key (str): 

Returns:
    Array[float] or None: 

    values (Array[float]):

<a id="unreal.glTFRuntimeAsset.get_node_extension_indices"></a>

#### get\_node\_extension\_indices

```python
def get_node_extension_indices(node_index: int, extension_name: str,
                               field_name: str) -> Optional[Array[int]]
```

x.get_node_extension_indices(node_index, extension_name, field_name) -> Array[int32] or None
Get Node Extension Indices

Args:
    node_index (int32): 
    extension_name (str): 
    field_name (str): 

Returns:
    Array[int32] or None: 

    indices (Array[int32]):

<a id="unreal.glTFRuntimeAsset.get_node_extension_index"></a>

#### get\_node\_extension\_index

```python
def get_node_extension_index(node_index: int, extension_name: str,
                             field_name: str) -> Optional[int]
```

x.get_node_extension_index(node_index, extension_name, field_name) -> int32 or None
Get Node Extension Index

Args:
    node_index (int32): 
    extension_name (str): 
    field_name (str): 

Returns:
    int32 or None: 

    index (int32):

<a id="unreal.glTFRuntimeAsset.get_node_by_name"></a>

#### get\_node\_by\_name

```python
def get_node_by_name(node_name: str) -> Optional[glTFRuntimeNode]
```

x.get_node_by_name(node_name) -> glTFRuntimeNode or None
Get Node by Name

Args:
    node_name (str): 

Returns:
    glTFRuntimeNode or None: 

    node (glTFRuntimeNode):

<a id="unreal.glTFRuntimeAsset.get_node"></a>

#### get\_node

```python
def get_node(node_index: int) -> Optional[glTFRuntimeNode]
```

x.get_node(node_index) -> glTFRuntimeNode or None
Get Node

Args:
    node_index (int32): 

Returns:
    glTFRuntimeNode or None: 

    node (glTFRuntimeNode):

<a id="unreal.glTFRuntimeAsset.get_materials_variants"></a>

#### get\_materials\_variants

```python
def get_materials_variants() -> Array[str]
```

x.get_materials_variants() -> Array[str]
Get Materials Variants

Returns:
    Array[str]:

<a id="unreal.glTFRuntimeAsset.get_integer_from_path"></a>

#### get\_integer\_from\_path

```python
def get_integer_from_path(
        path: Array[glTFRuntimePathItem]) -> Tuple[int, bool]
```

x.get_integer_from_path(path) -> (int64, found=bool)
Get Integer from Path

Args:
    path (Array[glTFRuntimePathItem]): 

Returns:
    bool: 

    found (bool):

<a id="unreal.glTFRuntimeAsset.get_generator"></a>

#### get\_generator

```python
def get_generator() -> str
```

x.get_generator() -> str
Get Generator

Returns:
    str:

<a id="unreal.glTFRuntimeAsset.get_float_from_path"></a>

#### get\_float\_from\_path

```python
def get_float_from_path(
        path: Array[glTFRuntimePathItem]) -> Tuple[float, bool]
```

x.get_float_from_path(path) -> (float, found=bool)
Get Float from Path

Args:
    path (Array[glTFRuntimePathItem]): 

Returns:
    bool: 

    found (bool):

<a id="unreal.glTFRuntimeAsset.get_extensions_used"></a>

#### get\_extensions\_used

```python
def get_extensions_used() -> Array[str]
```

x.get_extensions_used() -> Array[str]
Get Extensions Used

Returns:
    Array[str]:

<a id="unreal.glTFRuntimeAsset.get_extensions_required"></a>

#### get\_extensions\_required

```python
def get_extensions_required() -> Array[str]
```

x.get_extensions_required() -> Array[str]
Get Extensions Required

Returns:
    Array[str]:

<a id="unreal.glTFRuntimeAsset.get_errors"></a>

#### get\_errors

```python
def get_errors() -> Array[str]
```

x.get_errors() -> Array[str]
Get Errors

Returns:
    Array[str]:

<a id="unreal.glTFRuntimeAsset.get_download_time"></a>

#### get\_download\_time

```python
def get_download_time() -> float
```

x.get_download_time() -> float
Get Download Time

Returns:
    float:

<a id="unreal.glTFRuntimeAsset.get_cameras_names"></a>

#### get\_cameras\_names

```python
def get_cameras_names() -> Array[str]
```

x.get_cameras_names() -> Array[str]
Get Cameras Names

Returns:
    Array[str]:

<a id="unreal.glTFRuntimeAsset.get_camera_nodes_indices"></a>

#### get\_camera\_nodes\_indices

```python
def get_camera_nodes_indices() -> Array[int]
```

x.get_camera_nodes_indices() -> Array[int32]
Get Camera Nodes Indices

Returns:
    Array[int32]:

<a id="unreal.glTFRuntimeAsset.get_boolean_from_path"></a>

#### get\_boolean\_from\_path

```python
def get_boolean_from_path(path: Array[glTFRuntimePathItem]) -> Optional[bool]
```

x.get_boolean_from_path(path) -> bool or None
Get Boolean from Path

Args:
    path (Array[glTFRuntimePathItem]): 

Returns:
    bool or None: 

    found (bool):

<a id="unreal.glTFRuntimeAsset.get_boolean_from_extras"></a>

#### get\_boolean\_from\_extras

```python
def get_boolean_from_extras(key: str) -> Optional[bool]
```

x.get_boolean_from_extras(key) -> bool or None
Get Boolean from Extras

Args:
    key (str): 

Returns:
    bool or None: 

    value (bool):

<a id="unreal.glTFRuntimeAsset.get_array_size_from_path"></a>

#### get\_array\_size\_from\_path

```python
def get_array_size_from_path(
        path: Array[glTFRuntimePathItem]) -> Tuple[int, bool]
```

x.get_array_size_from_path(path) -> (int32, found=bool)
Get Array Size from Path

Args:
    path (Array[glTFRuntimePathItem]): 

Returns:
    bool: 

    found (bool):

<a id="unreal.glTFRuntimeAsset.get_archive_items"></a>

#### get\_archive\_items

```python
def get_archive_items() -> Array[str]
```

x.get_archive_items() -> Array[str]
Get Archive Items

Returns:
    Array[str]:

<a id="unreal.glTFRuntimeAsset.get_animations_names"></a>

#### get\_animations\_names

```python
def get_animations_names(include_unnameds: bool = True) -> Array[str]
```

x.get_animations_names(include_unnameds=True) -> Array[str]
Get Animations Names

Args:
    include_unnameds (bool): 

Returns:
    Array[str]:

<a id="unreal.glTFRuntimeAsset.find_node_by_name_in_array"></a>

#### find\_node\_by\_name\_in\_array

```python
def find_node_by_name_in_array(node_indices: Array[int],
                               node_name: str) -> Optional[glTFRuntimeNode]
```

x.find_node_by_name_in_array(node_indices, node_name) -> glTFRuntimeNode or None
Find Node by Name in Array

Args:
    node_indices (Array[int32]): 
    node_name (str): 

Returns:
    glTFRuntimeNode or None: 

    node (glTFRuntimeNode):

<a id="unreal.glTFRuntimeAsset.create_skeletal_animation_from_path"></a>

#### create\_skeletal\_animation\_from\_path

```python
def create_skeletal_animation_from_path(
    skeletal_mesh: SkeletalMesh, bones_path: Array[glTFRuntimePathItem],
    morph_targets_path: Array[glTFRuntimePathItem],
    skeletal_animation_config: glTFRuntimeSkeletalAnimationConfig
) -> AnimSequence
```

x.create_skeletal_animation_from_path(skeletal_mesh, bones_path, morph_targets_path, skeletal_animation_config) -> AnimSequence
Create Skeletal Animation from Path

Args:
    skeletal_mesh (SkeletalMesh): 
    bones_path (Array[glTFRuntimePathItem]): 
    morph_targets_path (Array[glTFRuntimePathItem]): 
    skeletal_animation_config (glTFRuntimeSkeletalAnimationConfig): 

Returns:
    AnimSequence:

<a id="unreal.glTFRuntimeAsset.create_animation_from_pose"></a>

#### create\_animation\_from\_pose

```python
def create_animation_from_pose(
        skeletal_mesh: SkeletalMesh,
        skeletal_animation_config: glTFRuntimeSkeletalAnimationConfig,
        skin_index: int = -1) -> AnimSequence
```

x.create_animation_from_pose(skeletal_mesh, skeletal_animation_config, skin_index=-1) -> AnimSequence
Create Animation from Pose

Args:
    skeletal_mesh (SkeletalMesh): 
    skeletal_animation_config (glTFRuntimeSkeletalAnimationConfig): 
    skin_index (int32): 

Returns:
    AnimSequence:

<a id="unreal.glTFRuntimeAsset.clear_cache"></a>

#### clear\_cache

```python
def clear_cache() -> None
```

x.clear_cache() -> None
Clear Cache

<a id="unreal.glTFRuntimeAsset.build_transform_from_node_forward"></a>

#### build\_transform\_from\_node\_forward

```python
def build_transform_from_node_forward(
        node_index: int, last_node_index: int) -> Optional[Transform]
```

x.build_transform_from_node_forward(node_index, last_node_index) -> Transform or None
Build Transform from Node Forward

Args:
    node_index (int32): 
    last_node_index (int32): 

Returns:
    Transform or None: 

    transform (Transform):

<a id="unreal.glTFRuntimeAsset.build_transform_from_node_backward"></a>

#### build\_transform\_from\_node\_backward

```python
def build_transform_from_node_backward(node_index: int) -> Optional[Transform]
```

x.build_transform_from_node_backward(node_index) -> Transform or None
Build Transform from Node Backward

Args:
    node_index (int32): 

Returns:
    Transform or None: 

    transform (Transform):

<a id="unreal.glTFRuntimeAsset.add_used_extensions"></a>

#### add\_used\_extensions

```python
def add_used_extensions(extensions_names: Array[str]) -> None
```

x.add_used_extensions(extensions_names) -> None
Add Used Extensions

Args:
    extensions_names (Array[str]):

<a id="unreal.glTFRuntimeAsset.add_used_extension"></a>

#### add\_used\_extension

```python
def add_used_extension(extension_name: str) -> None
```

x.add_used_extension(extension_name) -> None
Add Used Extension

Args:
    extension_name (str):

<a id="unreal.glTFRuntimeAsset.add_required_extensions"></a>

#### add\_required\_extensions

```python
def add_required_extensions(extensions_names: Array[str]) -> None
```

x.add_required_extensions(extensions_names) -> None
Add Required Extensions

Args:
    extensions_names (Array[str]):

<a id="unreal.glTFRuntimeAsset.add_required_extension"></a>

#### add\_required\_extension

```python
def add_required_extension(extension_name: str) -> None
```

x.add_required_extension(extension_name) -> None
Add Required Extension

Args:
    extension_name (str):

<a id="unreal.glTFRuntimeAssetActor"></a>