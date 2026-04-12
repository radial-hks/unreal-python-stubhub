## EditorActorSubsystem Objects

```python
class EditorActorSubsystem(EditorSubsystem)
```

UEditorActorUtilitiesSubsystem
Subsystem for exposing actor related utilities to scripts,

**C++ Source:**

- **Module**: UnrealEd
- **File**: EditorActorSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_actor_label_changed`` (OnActorLabelChanged):  [Read-Write]
- ``on_delete_actors_begin`` (OnDeleteActorsBegin):  [Read-Write]
- ``on_delete_actors_end`` (OnDeleteActorsEnd):  [Read-Write]
- ``on_duplicate_actors_begin`` (OnEditCutActorsBegin):  [Read-Write]
- ``on_duplicate_actors_end`` (OnDuplicateActorsEnd):  [Read-Write]
- ``on_edit_copy_actors_begin`` (OnEditCopyActorsBegin):  [Read-Write]
- ``on_edit_copy_actors_end`` (OnEditCopyActorsEnd):  [Read-Write]
- ``on_edit_cut_actors_begin`` (OnEditCutActorsBegin):  [Read-Write]
- ``on_edit_cut_actors_end`` (OnEditCutActorsEnd):  [Read-Write]
- ``on_edit_paste_actors_begin`` (OnEditPasteActorsBegin):  [Read-Write]
- ``on_edit_paste_actors_end`` (OnEditPasteActorsEnd):  [Read-Write]
- ``on_new_actors_dropped`` (OnEditNewActorsDropped):  [Read-Write]
- ``on_new_actors_placed`` (OnEditNewActorsPlaced):  [Read-Write]

<a id="unreal.EditorActorSubsystem.on_new_actors_dropped"></a>

#### on\_new\_actors\_dropped

```python
@property
def on_new_actors_dropped() -> OnEditNewActorsDropped
```

(OnEditNewActorsDropped):  [Read-Write]

<a id="unreal.EditorActorSubsystem.on_new_actors_dropped"></a>

#### on\_new\_actors\_dropped

```python
@on_new_actors_dropped.setter
def on_new_actors_dropped(value: OnEditNewActorsDropped) -> None
```

<a id="unreal.EditorActorSubsystem.on_new_actors_placed"></a>

#### on\_new\_actors\_placed

```python
@property
def on_new_actors_placed() -> OnEditNewActorsPlaced
```

(OnEditNewActorsPlaced):  [Read-Write]

<a id="unreal.EditorActorSubsystem.on_new_actors_placed"></a>

#### on\_new\_actors\_placed

```python
@on_new_actors_placed.setter
def on_new_actors_placed(value: OnEditNewActorsPlaced) -> None
```

<a id="unreal.EditorActorSubsystem.on_edit_cut_actors_begin"></a>

#### on\_edit\_cut\_actors\_begin

```python
@property
def on_edit_cut_actors_begin() -> OnEditCutActorsBegin
```

(OnEditCutActorsBegin):  [Read-Write]

<a id="unreal.EditorActorSubsystem.on_edit_cut_actors_begin"></a>

#### on\_edit\_cut\_actors\_begin

```python
@on_edit_cut_actors_begin.setter
def on_edit_cut_actors_begin(value: OnEditCutActorsBegin) -> None
```

<a id="unreal.EditorActorSubsystem.on_edit_cut_actors_end"></a>

#### on\_edit\_cut\_actors\_end

```python
@property
def on_edit_cut_actors_end() -> OnEditCutActorsEnd
```

(OnEditCutActorsEnd):  [Read-Write]

<a id="unreal.EditorActorSubsystem.on_edit_cut_actors_end"></a>

#### on\_edit\_cut\_actors\_end

```python
@on_edit_cut_actors_end.setter
def on_edit_cut_actors_end(value: OnEditCutActorsEnd) -> None
```

<a id="unreal.EditorActorSubsystem.on_edit_copy_actors_begin"></a>

#### on\_edit\_copy\_actors\_begin

```python
@property
def on_edit_copy_actors_begin() -> OnEditCopyActorsBegin
```

(OnEditCopyActorsBegin):  [Read-Write]

<a id="unreal.EditorActorSubsystem.on_edit_copy_actors_begin"></a>

#### on\_edit\_copy\_actors\_begin

```python
@on_edit_copy_actors_begin.setter
def on_edit_copy_actors_begin(value: OnEditCopyActorsBegin) -> None
```

<a id="unreal.EditorActorSubsystem.on_edit_copy_actors_end"></a>

#### on\_edit\_copy\_actors\_end

```python
@property
def on_edit_copy_actors_end() -> OnEditCopyActorsEnd
```

(OnEditCopyActorsEnd):  [Read-Write]

<a id="unreal.EditorActorSubsystem.on_edit_copy_actors_end"></a>

#### on\_edit\_copy\_actors\_end

```python
@on_edit_copy_actors_end.setter
def on_edit_copy_actors_end(value: OnEditCopyActorsEnd) -> None
```

<a id="unreal.EditorActorSubsystem.on_edit_paste_actors_begin"></a>

#### on\_edit\_paste\_actors\_begin

```python
@property
def on_edit_paste_actors_begin() -> OnEditPasteActorsBegin
```

(OnEditPasteActorsBegin):  [Read-Write]

<a id="unreal.EditorActorSubsystem.on_edit_paste_actors_begin"></a>

#### on\_edit\_paste\_actors\_begin

```python
@on_edit_paste_actors_begin.setter
def on_edit_paste_actors_begin(value: OnEditPasteActorsBegin) -> None
```

<a id="unreal.EditorActorSubsystem.on_edit_paste_actors_end"></a>

#### on\_edit\_paste\_actors\_end

```python
@property
def on_edit_paste_actors_end() -> OnEditPasteActorsEnd
```

(OnEditPasteActorsEnd):  [Read-Write]

<a id="unreal.EditorActorSubsystem.on_edit_paste_actors_end"></a>

#### on\_edit\_paste\_actors\_end

```python
@on_edit_paste_actors_end.setter
def on_edit_paste_actors_end(value: OnEditPasteActorsEnd) -> None
```

<a id="unreal.EditorActorSubsystem.on_duplicate_actors_begin"></a>

#### on\_duplicate\_actors\_begin

```python
@property
def on_duplicate_actors_begin() -> OnEditCutActorsBegin
```

(OnEditCutActorsBegin):  [Read-Write]

<a id="unreal.EditorActorSubsystem.on_duplicate_actors_begin"></a>

#### on\_duplicate\_actors\_begin

```python
@on_duplicate_actors_begin.setter
def on_duplicate_actors_begin(value: OnEditCutActorsBegin) -> None
```

<a id="unreal.EditorActorSubsystem.on_duplicate_actors_end"></a>

#### on\_duplicate\_actors\_end

```python
@property
def on_duplicate_actors_end() -> OnDuplicateActorsEnd
```

(OnDuplicateActorsEnd):  [Read-Write]

<a id="unreal.EditorActorSubsystem.on_duplicate_actors_end"></a>

#### on\_duplicate\_actors\_end

```python
@on_duplicate_actors_end.setter
def on_duplicate_actors_end(value: OnDuplicateActorsEnd) -> None
```

<a id="unreal.EditorActorSubsystem.on_delete_actors_begin"></a>

#### on\_delete\_actors\_begin

```python
@property
def on_delete_actors_begin() -> OnDeleteActorsBegin
```

(OnDeleteActorsBegin):  [Read-Write]

<a id="unreal.EditorActorSubsystem.on_delete_actors_begin"></a>

#### on\_delete\_actors\_begin

```python
@on_delete_actors_begin.setter
def on_delete_actors_begin(value: OnDeleteActorsBegin) -> None
```

<a id="unreal.EditorActorSubsystem.on_delete_actors_end"></a>

#### on\_delete\_actors\_end

```python
@property
def on_delete_actors_end() -> OnDeleteActorsEnd
```

(OnDeleteActorsEnd):  [Read-Write]

<a id="unreal.EditorActorSubsystem.on_delete_actors_end"></a>

#### on\_delete\_actors\_end

```python
@on_delete_actors_end.setter
def on_delete_actors_end(value: OnDeleteActorsEnd) -> None
```

<a id="unreal.EditorActorSubsystem.on_actor_label_changed"></a>

#### on\_actor\_label\_changed

```python
@property
def on_actor_label_changed() -> OnActorLabelChanged
```

(OnActorLabelChanged):  [Read-Write]

<a id="unreal.EditorActorSubsystem.on_actor_label_changed"></a>

#### on\_actor\_label\_changed

```python
@on_actor_label_changed.setter
def on_actor_label_changed(value: OnActorLabelChanged) -> None
```

<a id="unreal.EditorActorSubsystem.spawn_actor_from_object"></a>

#### spawn\_actor\_from\_object

```python
def spawn_actor_from_object(object_to_use: Object,
                            location: Vector,
                            rotation: Rotator = [0.000000, 0.000000, 0.000000],
                            transient: bool = False) -> Actor
```

x.spawn_actor_from_object(object_to_use, location, rotation=[0.000000, 0.000000, 0.000000], transient=False) -> Actor
Create an actor and place it in the world editor. The Actor can be created from a Factory, Archetype, Blueprint, Class or an Asset.
The actor will be created in the current level and will be selected.

Args:
    object_to_use (Object): Asset to attempt to use for an actor to place.
    location (Vector): Location of the new actor.
    rotation (Rotator): 
    transient (bool): 

Returns:
    Actor: The created actor.

<a id="unreal.EditorActorSubsystem.spawn_actor_from_class"></a>

#### spawn\_actor\_from\_class

```python
def spawn_actor_from_class(actor_class: Class,
                           location: Vector,
                           rotation: Rotator = [0.000000, 0.000000, 0.000000],
                           transient: bool = False) -> Actor
```

x.spawn_actor_from_class(actor_class, location, rotation=[0.000000, 0.000000, 0.000000], transient=False) -> Actor
Create an actor and place it in the world editor. Can be created from a Blueprint or a Class.
The actor will be created in the current level and will be selected.

Args:
    actor_class (type(Class)): Asset to attempt to use for an actor to place.
    location (Vector): Location of the new actor.
    rotation (Rotator): 
    transient (bool): 

Returns:
    Actor: The created actor.

<a id="unreal.EditorActorSubsystem.set_selected_level_actors"></a>

#### set\_selected\_level\_actors

```python
def set_selected_level_actors(actors_to_select: Array[Actor]) -> None
```

x.set_selected_level_actors(actors_to_select) -> None
Clear the current world editor selection and select the provided actors. Exclude actor that are pending kill, in PIE, PreviewEditor, ...

Args:
    actors_to_select (Array[Actor]): Actor that should be selected in the world editor.

<a id="unreal.EditorActorSubsystem.set_component_transform"></a>

#### set\_component\_transform

```python
def set_component_transform(scene_component: SceneComponent,
                            world_transform: Transform) -> bool
```

x.set_component_transform(scene_component, world_transform) -> bool
Sets the world transform of the given component, if possible.

Args:
    scene_component (SceneComponent): 
    world_transform (Transform): 

Returns:
    bool: false if the world transform could not be set.

<a id="unreal.EditorActorSubsystem.set_actor_transform"></a>

#### set\_actor\_transform

```python
def set_actor_transform(actor: Actor, world_transform: Transform) -> bool
```

x.set_actor_transform(actor, world_transform) -> bool
Sets the world transform of the given actor, if possible.

Args:
    actor (Actor): 
    world_transform (Transform): 

Returns:
    bool: false if the world transform could not be set.

<a id="unreal.EditorActorSubsystem.set_actor_selection_state"></a>

#### set\_actor\_selection\_state

```python
def set_actor_selection_state(actor: Actor, should_be_selected: bool) -> None
```

x.set_actor_selection_state(actor, should_be_selected) -> None
Set the selection state for the selected actor

Args:
    actor (Actor): 
    should_be_selected (bool):

<a id="unreal.EditorActorSubsystem.select_nothing"></a>

#### select\_nothing

```python
def select_nothing() -> None
```

x.select_nothing() -> None
Selects nothing in the editor (another way to clear the selection)

<a id="unreal.EditorActorSubsystem.select_all_children"></a>

#### select\_all\_children

```python
def select_all_children(recurse_children: bool) -> None
```

x.select_all_children(recurse_children) -> None
Select all children actors of the current selection.

Args:
    recurse_children (bool): True to recurse through all descendants of the children

<a id="unreal.EditorActorSubsystem.select_all"></a>

#### select\_all

```python
def select_all(world: World) -> None
```

x.select_all(world) -> None
Select all actors and BSP models in the given world, except those which are hidden

Args:
    world (World): The world the actors are to be selected in.

<a id="unreal.EditorActorSubsystem.invert_selection"></a>

#### invert\_selection

```python
def invert_selection(world: World) -> None
```

x.invert_selection(world) -> None
Invert the selection in the given world

Args:
    world (World): The world the selection is in.

<a id="unreal.EditorActorSubsystem.get_selected_level_actors"></a>

#### get\_selected\_level\_actors

```python
def get_selected_level_actors() -> Array[Actor]
```

x.get_selected_level_actors() -> Array[Actor]
Find all loaded Actors that are selected in the world editor. Exclude actor that are pending kill, in PIE, PreviewEditor, ...

Returns:
    Array[Actor]: List of found Actors

<a id="unreal.EditorActorSubsystem.get_all_level_actors_components"></a>

#### get\_all\_level\_actors\_components

```python
def get_all_level_actors_components() -> Array[ActorComponent]
```

x.get_all_level_actors_components() -> Array[ActorComponent]
Find all loaded ActorComponent own by an actor in the world editor. Exclude actor that are pending kill, in PIE, PreviewEditor, ...

Returns:
    Array[ActorComponent]: List of found ActorComponent

<a id="unreal.EditorActorSubsystem.get_all_level_actors"></a>

#### get\_all\_level\_actors

```python
def get_all_level_actors() -> Array[Actor]
```

x.get_all_level_actors() -> Array[Actor]
Find all loaded Actors in the world editor. Exclude actor that are pending kill, in PIE, PreviewEditor, ...

Returns:
    Array[Actor]: List of found Actors

<a id="unreal.EditorActorSubsystem.get_actor_reference"></a>

#### get\_actor\_reference

```python
def get_actor_reference(path_to_actor: str) -> Actor
```

x.get_actor_reference(path_to_actor) -> Actor
Attempts to find the actor specified by PathToActor in the current editor world

Args:
    path_to_actor (str): The path to the actor (e.g. PersistentLevel.PlayerStart)

Returns:
    Actor: A reference to the actor, or none if it wasn't found

<a id="unreal.EditorActorSubsystem.duplicate_selected_actors"></a>

#### duplicate\_selected\_actors

```python
def duplicate_selected_actors(world: World) -> None
```

x.duplicate_selected_actors(world) -> None
Duplicate all the selected actors in the given world

Args:
    world (World): The world the actors are selected in.

<a id="unreal.EditorActorSubsystem.duplicate_actors"></a>

#### duplicate\_actors

```python
def duplicate_actors(
        actors_to_duplicate: Array[Actor],
        to_world: World = None,
        offset: Vector = [0.000000, 0.000000, 0.000000]) -> Array[Actor]
```

x.duplicate_actors(actors_to_duplicate, to_world=None, offset=[0.000000, 0.000000, 0.000000]) -> Array[Actor]
Duplicate actors from the world editor.

Args:
    actors_to_duplicate (Array[Actor]): Actors to duplicate.
    to_world (World): World to place the duplicated actors in. *
    offset (Vector): Translation to offset duplicated actors by.

Returns:
    Array[Actor]: The duplicated actors, or empty if it didn't succeed

<a id="unreal.EditorActorSubsystem.duplicate_actor"></a>

#### duplicate\_actor

```python
def duplicate_actor(actor_to_duplicate: Actor,
                    to_world: World = None,
                    offset: Vector = [0.000000, 0.000000, 0.000000]) -> Actor
```

x.duplicate_actor(actor_to_duplicate, to_world=None, offset=[0.000000, 0.000000, 0.000000]) -> Actor
Duplicate an actor from the world editor.

Args:
    actor_to_duplicate (Actor): Actor to duplicate.
    to_world (World): World to place the duplicated actor in.
    offset (Vector): Translation to offset duplicated actor by.

Returns:
    Actor: The duplicated actor, or none if it didn't succeed

<a id="unreal.EditorActorSubsystem.destroy_actors"></a>

#### destroy\_actors

```python
def destroy_actors(actors_to_destroy: Array[Actor]) -> bool
```

x.destroy_actors(actors_to_destroy) -> bool
Destroy the actors from the world editor. Notify the Editor that the actor got destroyed.

Args:
    actors_to_destroy (Array[Actor]): Actors to destroy.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorActorSubsystem.destroy_actor"></a>

#### destroy\_actor

```python
def destroy_actor(actor_to_destroy: Actor) -> bool
```

x.destroy_actor(actor_to_destroy) -> bool
Destroy the actor from the world editor. Notify the Editor that the actor got destroyed.

Args:
    actor_to_destroy (Actor): Actor to destroy.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.EditorActorSubsystem.delete_selected_actors"></a>

#### delete\_selected\_actors

```python
def delete_selected_actors(world: World) -> None
```

x.delete_selected_actors(world) -> None
Delete all the selected actors in the given world

Args:
    world (World): The world the actors are selected in.

<a id="unreal.EditorActorSubsystem.convert_actors"></a>

#### convert\_actors

```python
def convert_actors(actors: Array[Actor], actor_class: Class,
                   static_mesh_package_path: str) -> Array[Actor]
```

x.convert_actors(actors, actor_class, static_mesh_package_path) -> Array[Actor]
Replace in the level all Actors provided with a new actor of type ActorClass. Destroy all Actors provided.

Args:
    actors (Array[Actor]): List of Actors to replace.
    actor_class (type(Class)): Class/Blueprint of the new actor that will be spawn.
    static_mesh_package_path (str): If the list contains Brushes and it is requested to change them to StaticMesh, StaticMeshPackagePath is the package path to where the StaticMesh will be created. ie. /Game/MyFolder/

Returns:
    Array[Actor]:

<a id="unreal.EditorActorSubsystem.clear_actor_selection_set"></a>

#### clear\_actor\_selection\_set

```python
def clear_actor_selection_set() -> None
```

x.clear_actor_selection_set() -> None
Remove all actors from the selection set

<a id="unreal.EditorAnimBaseObj"></a>