## EditorLevelLibrary Objects

```python
class EditorLevelLibrary(BlueprintFunctionLibrary)
```

Utility class to do most of the common functionalities in the World Editor.
The editor should not be in play in editor mode.

**C++ Source:**

- **Plugin**: EditorScriptingUtilities
- **Module**: EditorScriptingUtilities
- **File**: EditorLevelLibrary.h

<a id="unreal.EditorLevelLibrary.spawn_actor_from_object"></a>

#### spawn_actor_from_object

```python
@classmethod
def spawn_actor_from_object(cls,
                            object_to_use: Object,
                            location: Vector,
                            rotation: Rotator = [0.000000, 0.000000, 0.000000],
                            transient: bool = False) -> Actor
```

X.spawn_actor_from_object(object_to_use, location, rotation=[0.000000, 0.000000, 0.000000], transient=False) -> Actor
Spawn Actor from Object

Args:
    object_to_use (Object): 
    location (Vector): 
    rotation (Rotator): 
    transient (bool): 

Returns:
    Actor:

<a id="unreal.EditorLevelLibrary.spawn_actor_from_class"></a>

#### spawn_actor_from_class

```python
@classmethod
def spawn_actor_from_class(cls,
                           actor_class: Class,
                           location: Vector,
                           rotation: Rotator = [0.000000, 0.000000, 0.000000],
                           transient: bool = False) -> Actor
```

X.spawn_actor_from_class(actor_class, location, rotation=[0.000000, 0.000000, 0.000000], transient=False) -> Actor
Spawn Actor from Class

Args:
    actor_class (type(Class)): 
    location (Vector): 
    rotation (Rotator): 
    transient (bool): 

Returns:
    Actor:

<a id="unreal.EditorLevelLibrary.set_selected_level_actors"></a>

#### set_selected_level_actors

```python
@classmethod
def set_selected_level_actors(cls, actors_to_select: Array[Actor]) -> None
```

X.set_selected_level_actors(actors_to_select) -> None
Set Selected Level Actors
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Editor Actor Utilities Subsystem

Args:
    actors_to_select (Array[Actor]):

<a id="unreal.EditorLevelLibrary.set_level_viewport_camera_info"></a>

#### set_level_viewport_camera_info

```python
@classmethod
def set_level_viewport_camera_info(cls, camera_location: Vector,
                                   camera_rotation: Rotator) -> None
```

X.set_level_viewport_camera_info(camera_location, camera_rotation) -> None
Set Level Viewport Camera Info
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Unreal Editor Subsystem

Args:
    camera_location (Vector): 
    camera_rotation (Rotator):

<a id="unreal.EditorLevelLibrary.set_current_level_by_name"></a>

#### set_current_level_by_name

```python
@classmethod
def set_current_level_by_name(cls, level_name: Name) -> bool
```

X.set_current_level_by_name(level_name) -> bool
Set Current Level by Name
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Level Editor Subsystem

Args:
    level_name (Name): 

Returns:
    bool:

<a id="unreal.EditorLevelLibrary.set_actor_selection_state"></a>

#### set_actor_selection_state

```python
@classmethod
def set_actor_selection_state(cls, actor: Actor,
                              should_be_selected: bool) -> None
```

X.set_actor_selection_state(actor, should_be_selected) -> None
Set Actor Selection State
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Editor Actor Utilities Subsystem

Args:
    actor (Actor): 
    should_be_selected (bool):

<a id="unreal.EditorLevelLibrary.select_nothing"></a>

#### select_nothing

```python
@classmethod
def select_nothing(cls) -> None
```

X.select_nothing() -> None
Select Nothing
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Editor Actor Utilities Subsystem

<a id="unreal.EditorLevelLibrary.save_current_level"></a>

#### save_current_level

```python
@classmethod
def save_current_level(cls) -> bool
```

X.save_current_level() -> bool
Save Current Level
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Level Editor Subsystem

Returns:
    bool:

<a id="unreal.EditorLevelLibrary.save_all_dirty_levels"></a>

#### save_all_dirty_levels

```python
@classmethod
def save_all_dirty_levels(cls) -> bool
```

X.save_all_dirty_levels() -> bool
Save All Dirty Levels
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Level Editor Subsystem

Returns:
    bool:

<a id="unreal.EditorLevelLibrary.replace_selected_actors"></a>

#### replace_selected_actors

```python
@classmethod
def replace_selected_actors(cls, asset_path: str) -> None
```

X.replace_selected_actors(asset_path) -> None
Replaces the selected Actors with the same number of a different kind of Actor using the specified factory to spawn the new Actors
note that only Location, Rotation, Drawscale, Drawscale3D, Tag, and Group are copied from the old Actors

Args:
    asset_path (str):

<a id="unreal.EditorLevelLibrary.replace_mesh_components_meshes_on_actors"></a>

#### replace_mesh_components_meshes_on_actors

```python
@classmethod
def replace_mesh_components_meshes_on_actors(cls, actors: Array[Actor],
                                             mesh_to_be_replaced: StaticMesh,
                                             new_mesh: StaticMesh) -> None
```

X.replace_mesh_components_meshes_on_actors(actors, mesh_to_be_replaced, new_mesh) -> None
Replace Mesh Components Meshes on Actors
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    actors (Array[Actor]): 
    mesh_to_be_replaced (StaticMesh): 
    new_mesh (StaticMesh):

<a id="unreal.EditorLevelLibrary.replace_mesh_components_meshes"></a>

#### replace_mesh_components_meshes

```python
@classmethod
def replace_mesh_components_meshes(cls,
                                   mesh_components: Array[StaticMeshComponent],
                                   mesh_to_be_replaced: StaticMesh,
                                   new_mesh: StaticMesh) -> None
```

X.replace_mesh_components_meshes(mesh_components, mesh_to_be_replaced, new_mesh) -> None
Replace Mesh Components Meshes
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    mesh_components (Array[StaticMeshComponent]): 
    mesh_to_be_replaced (StaticMesh): 
    new_mesh (StaticMesh):

<a id="unreal.EditorLevelLibrary.replace_mesh_components_materials_on_actors"></a>

#### replace_mesh_components_materials_on_actors

```python
@classmethod
def replace_mesh_components_materials_on_actors(
        cls, actors: Array[Actor], material_to_be_replaced: MaterialInterface,
        new_material: MaterialInterface) -> None
```

X.replace_mesh_components_materials_on_actors(actors, material_to_be_replaced, new_material) -> None
Replace Mesh Components Materials on Actors
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    actors (Array[Actor]): 
    material_to_be_replaced (MaterialInterface): 
    new_material (MaterialInterface):

<a id="unreal.EditorLevelLibrary.replace_mesh_components_materials"></a>

#### replace_mesh_components_materials

```python
@classmethod
def replace_mesh_components_materials(
        cls, mesh_components: Array[MeshComponent],
        material_to_be_replaced: MaterialInterface,
        new_material: MaterialInterface) -> None
```

X.replace_mesh_components_materials(mesh_components, material_to_be_replaced, new_material) -> None
Replace Mesh Components Materials
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    mesh_components (Array[MeshComponent]): 
    material_to_be_replaced (MaterialInterface): 
    new_material (MaterialInterface):

<a id="unreal.EditorLevelLibrary.pilot_level_actor"></a>

#### pilot_level_actor

```python
@classmethod
def pilot_level_actor(cls, actor_to_pilot: Actor) -> None
```

X.pilot_level_actor(actor_to_pilot) -> None
Pilot Level Actor
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Level Editor Subsystem

Args:
    actor_to_pilot (Actor):

<a id="unreal.EditorLevelLibrary.new_level_from_template"></a>

#### new_level_from_template

```python
@classmethod
def new_level_from_template(cls, asset_path: str,
                            template_asset_path: str) -> bool
```

X.new_level_from_template(asset_path, template_asset_path) -> bool
New Level from Template
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Level Editor Subsystem

Args:
    asset_path (str): 
    template_asset_path (str): 

Returns:
    bool:

<a id="unreal.EditorLevelLibrary.new_level"></a>

#### new_level

```python
@classmethod
def new_level(cls, asset_path: str) -> bool
```

X.new_level(asset_path) -> bool
New Level
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Level Editor Subsystem

Args:
    asset_path (str): 

Returns:
    bool:

<a id="unreal.EditorLevelLibrary.merge_static_mesh_actors"></a>

#### merge_static_mesh_actors

```python
@classmethod
def merge_static_mesh_actors(
        cls, actors_to_merge: Array[StaticMeshActor],
        merge_options: MergeStaticMeshActorsOptions
) -> Optional[StaticMeshActor]
```

X.merge_static_mesh_actors(actors_to_merge, merge_options) -> StaticMeshActor or None
Merge Static Mesh Actors
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    actors_to_merge (Array[StaticMeshActor]): 
    merge_options (MergeStaticMeshActorsOptions): 

Returns:
    StaticMeshActor or None: 

    out_merged_actor (StaticMeshActor):

<a id="unreal.EditorLevelLibrary.load_level"></a>

#### load_level

```python
@classmethod
def load_level(cls, asset_path: str) -> bool
```

X.load_level(asset_path) -> bool
Load Level
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Level Editor Subsystem

Args:
    asset_path (str): 

Returns:
    bool:

<a id="unreal.EditorLevelLibrary.join_static_mesh_actors"></a>

#### join_static_mesh_actors

```python
@classmethod
def join_static_mesh_actors(
        cls, actors_to_join: Array[StaticMeshActor],
        join_options: JoinStaticMeshActorsOptions) -> Actor
```

X.join_static_mesh_actors(actors_to_join, join_options) -> Actor
Join Static Mesh Actors
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    actors_to_join (Array[StaticMeshActor]): 
    join_options (JoinStaticMeshActorsOptions): 

Returns:
    Actor:

<a id="unreal.EditorLevelLibrary.get_selected_level_actors"></a>

#### get_selected_level_actors

```python
@classmethod
def get_selected_level_actors(cls) -> Array[Actor]
```

X.get_selected_level_actors() -> Array[Actor]
Get Selected Level Actors
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Editor Actor Utilities Subsystem

Returns:
    Array[Actor]:

<a id="unreal.EditorLevelLibrary.get_pie_worlds"></a>

#### get_pie_worlds

```python
@classmethod
def get_pie_worlds(cls, include_dedicated_server: bool) -> Array[World]
```

X.get_pie_worlds(include_dedicated_server) -> Array[World]
Get PIEWorlds

Args:
    include_dedicated_server (bool): 

Returns:
    Array[World]:

<a id="unreal.EditorLevelLibrary.get_level_viewport_camera_info"></a>

#### get_level_viewport_camera_info

```python
@classmethod
def get_level_viewport_camera_info(cls) -> Optional[Tuple[Vector, Rotator]]
```

X.get_level_viewport_camera_info() -> (camera_location=Vector, camera_rotation=Rotator) or None
Get Level Viewport Camera Info
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Unreal Editor Subsystem

Returns:
    tuple or None: 

    camera_location (Vector): 

    camera_rotation (Rotator):

<a id="unreal.EditorLevelLibrary.get_game_world"></a>

#### get_game_world

```python
@classmethod
def get_game_world(cls) -> World
```

X.get_game_world() -> World
Get Game World
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Unreal Editor Subsystem

Returns:
    World:

<a id="unreal.EditorLevelLibrary.get_editor_world"></a>

#### get_editor_world

```python
@classmethod
def get_editor_world(cls) -> World
```

X.get_editor_world() -> World
Get Editor World
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Unreal Editor Subsystem

Returns:
    World:

<a id="unreal.EditorLevelLibrary.get_all_level_actors_components"></a>

#### get_all_level_actors_components

```python
@classmethod
def get_all_level_actors_components(cls) -> Array[ActorComponent]
```

X.get_all_level_actors_components() -> Array[ActorComponent]
Get All Level Actors Components
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Editor Actor Utilities Subsystem

Returns:
    Array[ActorComponent]:

<a id="unreal.EditorLevelLibrary.get_all_level_actors"></a>

#### get_all_level_actors

```python
@classmethod
def get_all_level_actors(cls) -> Array[Actor]
```

X.get_all_level_actors() -> Array[Actor]
Get All Level Actors
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Editor Actor Utilities Subsystem

Returns:
    Array[Actor]:

<a id="unreal.EditorLevelLibrary.get_actor_reference"></a>

#### get_actor_reference

```python
@classmethod
def get_actor_reference(cls, path_to_actor: str) -> Actor
```

X.get_actor_reference(path_to_actor) -> Actor
Get Actor Reference
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Editor Actor Utilities Subsystem

Args:
    path_to_actor (str): 

Returns:
    Actor:

<a id="unreal.EditorLevelLibrary.eject_pilot_level_actor"></a>

#### eject_pilot_level_actor

```python
@classmethod
def eject_pilot_level_actor(cls) -> None
```

X.eject_pilot_level_actor() -> None
Eject Pilot Level Actor
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Level Editor Subsystem

<a id="unreal.EditorLevelLibrary.editor_set_game_view"></a>

#### editor_set_game_view

```python
@classmethod
def editor_set_game_view(cls, game_view: bool) -> None
```

X.editor_set_game_view(game_view) -> None
Editor Set Game View
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Level Editor Subsystem

Args:
    game_view (bool):

<a id="unreal.EditorLevelLibrary.editor_play_simulate"></a>

#### editor_play_simulate

```python
@classmethod
def editor_play_simulate(cls) -> None
```

X.editor_play_simulate() -> None
Editor Play Simulate
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Level Editor Subsystem

<a id="unreal.EditorLevelLibrary.editor_invalidate_viewports"></a>

#### editor_invalidate_viewports

```python
@classmethod
def editor_invalidate_viewports(cls) -> None
```

X.editor_invalidate_viewports() -> None
Editor Invalidate Viewports
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Level Editor Subsystem

<a id="unreal.EditorLevelLibrary.editor_end_play"></a>

#### editor_end_play

```python
@classmethod
def editor_end_play(cls) -> None
```

X.editor_end_play() -> None
Editor End Play

<a id="unreal.EditorLevelLibrary.destroy_actor"></a>

#### destroy_actor

```python
@classmethod
def destroy_actor(cls, actor_to_destroy: Actor) -> bool
```

X.destroy_actor(actor_to_destroy) -> bool
Destroy Actor
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Editor Actor Utilities Subsystem

Args:
    actor_to_destroy (Actor): 

Returns:
    bool:

<a id="unreal.EditorLevelLibrary.create_proxy_mesh_actor"></a>

#### create_proxy_mesh_actor

```python
@classmethod
def create_proxy_mesh_actor(
        cls, actors_to_merge: Array[StaticMeshActor],
        merge_options: CreateProxyMeshActorOptions
) -> Optional[StaticMeshActor]
```

X.create_proxy_mesh_actor(actors_to_merge, merge_options) -> StaticMeshActor or None
Create Proxy Mesh Actor
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    actors_to_merge (Array[StaticMeshActor]): 
    merge_options (CreateProxyMeshActorOptions): 

Returns:
    StaticMeshActor or None: 

    out_merged_actor (StaticMeshActor):

<a id="unreal.EditorLevelLibrary.convert_actors"></a>

#### convert_actors

```python
@classmethod
def convert_actors(cls, actors: Array[Actor], actor_class: Class,
                   static_mesh_package_path: str) -> Array[Actor]
```

X.convert_actors(actors, actor_class, static_mesh_package_path) -> Array[Actor]
Convert Actors
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Editor Actor Utilities Subsystem

Args:
    actors (Array[Actor]): 
    actor_class (type(Class)): 
    static_mesh_package_path (str): 

Returns:
    Array[Actor]:

<a id="unreal.EditorLevelLibrary.clear_actor_selection_set"></a>

#### clear_actor_selection_set

```python
@classmethod
def clear_actor_selection_set(cls) -> None
```

X.clear_actor_selection_set() -> None
Clear Actor Selection Set
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Editor Actor Utilities Subsystem

<a id="unreal.EditorSkeletalMeshLibrary"></a>