## NiagaraFunctionLibrary Objects

```python
class NiagaraFunctionLibrary(BlueprintFunctionLibrary)
```

A C++ and Blueprint accessible library of utility functions for accessing Niagara simulations
All positions & orientations are returned in Unreal reference frame & units, assuming the Leap device is located at the origin.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraFunctionLibrary.h

<a id="unreal.NiagaraFunctionLibrary.spawn_system_attached_with_params"></a>

#### spawn_system_attached_with_params

```python
@classmethod
def spawn_system_attached_with_params(
        cls, spawn_params: FXSystemSpawnParameters) -> NiagaraComponent
```

X.spawn_system_attached_with_params(spawn_params) -> NiagaraComponent
Spawn System Attached with Params

Args:
    spawn_params (FXSystemSpawnParameters): 

Returns:
    NiagaraComponent:

<a id="unreal.NiagaraFunctionLibrary.spawn_system_attached"></a>

#### spawn_system_attached

```python
@classmethod
def spawn_system_attached(cls,
                          system_template: NiagaraSystem,
                          attach_to_component: SceneComponent,
                          attach_point_name: Name,
                          location: Vector,
                          rotation: Rotator,
                          location_type: AttachLocation,
                          auto_destroy: bool,
                          auto_activate: bool = True,
                          pooling_method: NCPoolMethod = NCPoolMethod.NONE,
                          pre_cull_check: bool = True) -> NiagaraComponent
```

X.spawn_system_attached(system_template, attach_to_component, attach_point_name, location, rotation, location_type, auto_destroy, auto_activate=True, pooling_method=NCPoolMethod.NONE, pre_cull_check=True) -> NiagaraComponent
Spawn System Attached

Args:
    system_template (NiagaraSystem): 
    attach_to_component (SceneComponent): 
    attach_point_name (Name): 
    location (Vector): 
    rotation (Rotator): 
    location_type (AttachLocation): 
    auto_destroy (bool): 
    auto_activate (bool): 
    pooling_method (NCPoolMethod): 
    pre_cull_check (bool): 

Returns:
    NiagaraComponent:

<a id="unreal.NiagaraFunctionLibrary.spawn_system_at_location_with_params"></a>

#### spawn_system_at_location_with_params

```python
@classmethod
def spawn_system_at_location_with_params(
        cls, spawn_params: FXSystemSpawnParameters) -> NiagaraComponent
```

X.spawn_system_at_location_with_params(spawn_params) -> NiagaraComponent
Spawn System at Location with Params

Args:
    spawn_params (FXSystemSpawnParameters): 

Returns:
    NiagaraComponent:

<a id="unreal.NiagaraFunctionLibrary.spawn_system_at_location"></a>

#### spawn_system_at_location

```python
@classmethod
def spawn_system_at_location(cls,
                             world_context_object: Object,
                             system_template: NiagaraSystem,
                             location: Vector,
                             rotation: Rotator = [
                                 0.000000, 0.000000, 0.000000
                             ],
                             scale: Vector = [1.000000, 1.000000, 1.000000],
                             auto_destroy: bool = True,
                             auto_activate: bool = True,
                             pooling_method: NCPoolMethod = NCPoolMethod.NONE,
                             pre_cull_check: bool = True) -> NiagaraComponent
```

X.spawn_system_at_location(world_context_object, system_template, location, rotation=[0.000000, 0.000000, 0.000000], scale=[1.000000, 1.000000, 1.000000], auto_destroy=True, auto_activate=True, pooling_method=NCPoolMethod.NONE, pre_cull_check=True) -> NiagaraComponent
Spawns a Niagara System at the specified world location/rotation

Args:
    world_context_object (Object): 
    system_template (NiagaraSystem): 
    location (Vector): 
    rotation (Rotator): 
    scale (Vector): 
    auto_destroy (bool): 
    auto_activate (bool): 
    pooling_method (NCPoolMethod): 
    pre_cull_check (bool): 

Returns:
    NiagaraComponent: The spawned UNiagaraComponent

<a id="unreal.NiagaraFunctionLibrary.set_volume_texture_object"></a>

#### set_volume_texture_object

```python
@classmethod
def set_volume_texture_object(cls, niagara_system: NiagaraComponent,
                              override_name: str,
                              texture: VolumeTexture) -> None
```

X.set_volume_texture_object(niagara_system, override_name, texture) -> None
Overrides the Volume Texture for a Niagara Volume Texture Data Interface User Parameter.

Args:
    niagara_system (NiagaraComponent): 
    override_name (str): 
    texture (VolumeTexture):

<a id="unreal.NiagaraFunctionLibrary.set_texture_object"></a>

#### set_texture_object

```python
@classmethod
def set_texture_object(cls, niagara_system: NiagaraComponent,
                       override_name: str, texture: Texture) -> None
```

X.set_texture_object(niagara_system, override_name, texture) -> None
Overrides the Texture Object for a Niagara Texture Data Interface User Parameter.

Args:
    niagara_system (NiagaraComponent): 
    override_name (str): 
    texture (Texture):

<a id="unreal.NiagaraFunctionLibrary.set_texture2d_array_object"></a>

#### set_texture2d_array_object

```python
@classmethod
def set_texture2d_array_object(cls, niagara_system: NiagaraComponent,
                               override_name: str,
                               texture: Texture2DArray) -> None
```

X.set_texture2d_array_object(niagara_system, override_name, texture) -> None
Overrides the 2D Array Texture for a Niagara 2D Array Texture Data Interface User Parameter.

Args:
    niagara_system (NiagaraComponent): 
    override_name (str): 
    texture (Texture2DArray):

<a id="unreal.NiagaraFunctionLibrary.set_skeletal_mesh_data_interface_sampling_regions"></a>

#### set_skeletal_mesh_data_interface_sampling_regions

```python
@classmethod
def set_skeletal_mesh_data_interface_sampling_regions(
        cls, niagara_system: NiagaraComponent, override_name: str,
        sampling_regions: Array[Name]) -> None
```

X.set_skeletal_mesh_data_interface_sampling_regions(niagara_system, override_name, sampling_regions) -> None
Sets the SamplingRegion to use on the skeletal mesh data interface, this is destructive as it modifies the data interface.

Args:
    niagara_system (NiagaraComponent): 
    override_name (str): 
    sampling_regions (Array[Name]):

<a id="unreal.NiagaraFunctionLibrary.set_skeletal_mesh_data_interface_filtered_sockets"></a>

#### set_skeletal_mesh_data_interface_filtered_sockets

```python
@classmethod
def set_skeletal_mesh_data_interface_filtered_sockets(
        cls, niagara_system: NiagaraComponent, override_name: str,
        filtered_sockets: Array[Name]) -> None
```

X.set_skeletal_mesh_data_interface_filtered_sockets(niagara_system, override_name, filtered_sockets) -> None
Sets the Filtered Sockets to use on the skeletal mesh data interface, this is destructive as it modifies the data interface.

Args:
    niagara_system (NiagaraComponent): 
    override_name (str): 
    filtered_sockets (Array[Name]):

<a id="unreal.NiagaraFunctionLibrary.set_skeletal_mesh_data_interface_filtered_bones"></a>

#### set_skeletal_mesh_data_interface_filtered_bones

```python
@classmethod
def set_skeletal_mesh_data_interface_filtered_bones(
        cls, niagara_system: NiagaraComponent, override_name: str,
        filtered_bones: Array[Name]) -> None
```

X.set_skeletal_mesh_data_interface_filtered_bones(niagara_system, override_name, filtered_bones) -> None
Sets the Filtered Bones to use on the skeletal mesh data interface, this is destructive as it modifies the data interface.

Args:
    niagara_system (NiagaraComponent): 
    override_name (str): 
    filtered_bones (Array[Name]):

<a id="unreal.NiagaraFunctionLibrary.set_scene_capture2d_data_interface_managed_mode"></a>

#### set_scene_capture2d_data_interface_managed_mode

```python
@classmethod
def set_scene_capture2d_data_interface_managed_mode(
        cls, niagara_system: NiagaraComponent, di_name: Name,
        managed_capture_source: SceneCaptureSource,
        managed_texture_size: IntPoint,
        managed_texture_format: TextureRenderTargetFormat,
        managed_projection_type: CameraProjectionMode,
        managed_fov_angle: float, managed_ortho_width: float,
        managed_capture_every_frame: bool, managed_capture_on_movement: bool,
        show_only_actors: Array[Actor]) -> None
```

X.set_scene_capture2d_data_interface_managed_mode(niagara_system, di_name, managed_capture_source, managed_texture_size, managed_texture_format, managed_projection_type, managed_fov_angle, managed_ortho_width, managed_capture_every_frame, managed_capture_on_movement, show_only_actors) -> None
Sets managed mode parameters for the Scene capture 2D  data interface, this is destructive as it modifies the data interface.

Args:
    niagara_system (NiagaraComponent): 
    di_name (Name): 
    managed_capture_source (SceneCaptureSource): 
    managed_texture_size (IntPoint): 
    managed_texture_format (TextureRenderTargetFormat): 
    managed_projection_type (CameraProjectionMode): 
    managed_fov_angle (float): 
    managed_ortho_width (float): 
    managed_capture_every_frame (bool): 
    managed_capture_on_movement (bool): 
    show_only_actors (Array[Actor]):

<a id="unreal.NiagaraFunctionLibrary.set_component_niagara_gpu_ray_traced_collision_group"></a>

#### set_component_niagara_gpu_ray_traced_collision_group

```python
@classmethod
def set_component_niagara_gpu_ray_traced_collision_group(
        cls, world_context_object: Object, primitive: PrimitiveComponent,
        collision_group: int) -> None
```

X.set_component_niagara_gpu_ray_traced_collision_group(world_context_object, primitive, collision_group) -> None
Sets the Niagara GPU ray traced collision group for the give primitive component.

Args:
    world_context_object (Object): 
    primitive (PrimitiveComponent): 
    collision_group (int32):

<a id="unreal.NiagaraFunctionLibrary.set_actor_niagara_gpu_ray_traced_collision_group"></a>

#### set_actor_niagara_gpu_ray_traced_collision_group

```python
@classmethod
def set_actor_niagara_gpu_ray_traced_collision_group(
        cls, world_context_object: Object, actor: Actor,
        collision_group: int) -> None
```

X.set_actor_niagara_gpu_ray_traced_collision_group(world_context_object, actor, collision_group) -> None
Sets the Niagara GPU ray traced collision group for all primitive components on the given actor.

Args:
    world_context_object (Object): 
    actor (Actor): 
    collision_group (int32):

<a id="unreal.NiagaraFunctionLibrary.release_niagara_gpu_ray_traced_collision_group"></a>

#### release_niagara_gpu_ray_traced_collision_group

```python
@classmethod
def release_niagara_gpu_ray_traced_collision_group(
        cls, world_context_object: Object, collision_group: int) -> None
```

X.release_niagara_gpu_ray_traced_collision_group(world_context_object, collision_group) -> None
Releases a collision group back to the system for use by ohers.

Args:
    world_context_object (Object): 
    collision_group (int32):

<a id="unreal.NiagaraFunctionLibrary.override_system_user_variable_static_mesh_component"></a>

#### override_system_user_variable_static_mesh_component

```python
@classmethod
def override_system_user_variable_static_mesh_component(
        cls, niagara_system: NiagaraComponent, override_name: str,
        static_mesh_component: StaticMeshComponent) -> None
```

X.override_system_user_variable_static_mesh_component(niagara_system, override_name, static_mesh_component) -> None
Sets a Niagara StaticMesh parameter by name, overriding locally if necessary.

Args:
    niagara_system (NiagaraComponent): 
    override_name (str): 
    static_mesh_component (StaticMeshComponent):

<a id="unreal.NiagaraFunctionLibrary.override_system_user_variable_static_mesh"></a>

#### override_system_user_variable_static_mesh

```python
@classmethod
def override_system_user_variable_static_mesh(cls,
                                              niagara_system: NiagaraComponent,
                                              override_name: str,
                                              static_mesh: StaticMesh) -> None
```

X.override_system_user_variable_static_mesh(niagara_system, override_name, static_mesh) -> None
Override System User Variable Static Mesh

Args:
    niagara_system (NiagaraComponent): 
    override_name (str): 
    static_mesh (StaticMesh):

<a id="unreal.NiagaraFunctionLibrary.override_system_user_variable_skeletal_mesh_component"></a>

#### override_system_user_variable_skeletal_mesh_component

```python
@classmethod
def override_system_user_variable_skeletal_mesh_component(
        cls, niagara_system: NiagaraComponent, override_name: str,
        skeletal_mesh_component: SkeletalMeshComponent) -> None
```

X.override_system_user_variable_skeletal_mesh_component(niagara_system, override_name, skeletal_mesh_component) -> None
Sets a Niagara StaticMesh parameter by name, overriding locally if necessary.

Args:
    niagara_system (NiagaraComponent): 
    override_name (str): 
    skeletal_mesh_component (SkeletalMeshComponent):

<a id="unreal.NiagaraFunctionLibrary.get_niagara_parameter_collection"></a>

#### get_niagara_parameter_collection

```python
@classmethod
def get_niagara_parameter_collection(
    cls, world_context_object: Object, collection: NiagaraParameterCollection
) -> NiagaraParameterCollectionInstance
```

X.get_niagara_parameter_collection(world_context_object, collection) -> NiagaraParameterCollectionInstance
This is gonna be totally reworked
       UFUNCTION(BlueprintCallable, Category = Niagara, meta = (Keywords = "niagara System", UnsafeDuringActorConstruction = "true"))
       static void SetUpdateScriptConstant(UNiagaraComponent* Component, FName EmitterName, FName ConstantName, FVector Value);

Args:
    world_context_object (Object): 
    collection (NiagaraParameterCollection): 

Returns:
    NiagaraParameterCollectionInstance:

<a id="unreal.NiagaraFunctionLibrary.acquire_niagara_gpu_ray_traced_collision_group"></a>

#### acquire_niagara_gpu_ray_traced_collision_group

```python
@classmethod
def acquire_niagara_gpu_ray_traced_collision_group(
        cls, world_context_object: Object) -> int
```

X.acquire_niagara_gpu_ray_traced_collision_group(world_context_object) -> int32
Returns a free collision group for use in HWRT collision group filtering. Returns -1 on failure.

Args:
    world_context_object (Object): 

Returns:
    int32:

<a id="unreal.NiagaraLensEffectBase"></a>