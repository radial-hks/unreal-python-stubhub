## LayersSubsystem Objects

```python
class LayersSubsystem(EditorSubsystem)
```

Layers Subsystem

**C++ Source:**

- **Module**: UnrealEd
- **File**: LayersSubsystem.h

<a id="unreal.LayersSubsystem.update_all_view_visibility"></a>

#### update_all_view_visibility

```python
def update_all_view_visibility(layer_that_changed: Name) -> None
```

x.update_all_view_visibility(layer_that_changed) -> None
Updates the visibility for all actors for all views.

Args:
    layer_that_changed (Name): If one layer was changed (toggled in view pop-up, etc), then we only need to modify actors that use that layer.

<a id="unreal.LayersSubsystem.update_all_actors_visibility"></a>

#### update_all_actors_visibility

```python
def update_all_actors_visibility(notify_selection_change: bool,
                                 redraw_viewports: bool) -> bool
```

x.update_all_actors_visibility(notify_selection_change, redraw_viewports) -> bool
Updates the visibility of all actors in the viewports

Args:
    notify_selection_change (bool): If true the Editor is notified of the selection change; if false, the Editor will not be notified
    redraw_viewports (bool): If true the viewports will be redrawn; if false, they will not

Returns:
    bool:

<a id="unreal.LayersSubsystem.update_actor_visibility"></a>

#### update_actor_visibility

```python
def update_actor_visibility(
        actor: Actor, notify_selection_change: bool,
        redraw_viewports: bool) -> Optional[Tuple[bool, bool]]
```

x.update_actor_visibility(actor, notify_selection_change, redraw_viewports) -> (out_selection_changed=bool, out_actor_modified=bool) or None
Updates the provided actors visibility in the viewports

Args:
    actor (Actor): Actor to update
    notify_selection_change (bool): If true the Editor is notified of the selection change; if false, the Editor will not be notified
    redraw_viewports (bool): If true the viewports will be redrawn; if false, they will not

Returns:
    tuple or None: 

    out_selection_changed (bool): [OUT]      Whether the Editors selection changed

    out_actor_modified (bool): [OUT]         Whether the actor was modified

<a id="unreal.LayersSubsystem.update_actor_all_views_visibility"></a>

#### update_actor_all_views_visibility

```python
def update_actor_all_views_visibility(actor: Actor) -> None
```

x.update_actor_all_views_visibility(actor) -> None
Updates per-view visibility for the given actor for all views

Args:
    actor (Actor): Actor to update

<a id="unreal.LayersSubsystem.try_get_layer"></a>

#### try_get_layer

```python
def try_get_layer(layer_name: Name) -> Optional[Layer]
```

x.try_get_layer(layer_name) -> Layer or None
Attempts to get the ULayer Object of the provided layer name.

Args:
    layer_name (Name): The name of the layer whose ULayer Object to retrieve

Returns:
    Layer or None: If true a valid ULayer Object was found and set to OutLayer; if false, a valid ULayer object was not found and invalid set to OutLayer

    out_layer (Layer):

<a id="unreal.LayersSubsystem.toggle_layer_visibility"></a>

#### toggle_layer_visibility

```python
def toggle_layer_visibility(layer_name: Name) -> None
```

x.toggle_layer_visibility(layer_name) -> None
Toggles the named layer's visibility

Args:
    layer_name (Name): The name of the layer to affect

<a id="unreal.LayersSubsystem.toggle_layers_visibility"></a>

#### toggle_layers_visibility

```python
def toggle_layers_visibility(layer_names: Array[Name]) -> None
```

x.toggle_layers_visibility(layer_names) -> None
Toggles the visibility of all of the named layers

Args:
    layer_names (Array[Name]): The names of the layers to affect

<a id="unreal.LayersSubsystem.set_layer_visibility"></a>

#### set_layer_visibility

```python
def set_layer_visibility(layer_name: Name, is_visible: bool) -> None
```

x.set_layer_visibility(layer_name, is_visible) -> None
Changes the named layer's visibility to the provided state

Args:
    layer_name (Name): The name of the layer to affect.
    is_visible (bool): If true the layer will be visible; if false, the layer will not be visible.

<a id="unreal.LayersSubsystem.set_layers_visibility"></a>

#### set_layers_visibility

```python
def set_layers_visibility(layer_names: Array[Name], is_visible: bool) -> None
```

x.set_layers_visibility(layer_names, is_visible) -> None
Changes visibility of the named layers to the provided state

Args:
    layer_names (Array[Name]): The names of the layers to affect
    is_visible (bool): If true the layers will be visible; if false, the layers will not be visible

<a id="unreal.LayersSubsystem.select_actors_in_layers"></a>

#### select_actors_in_layers

```python
def select_actors_in_layers(layer_names: Array[Name],
                            select: bool,
                            notify: bool,
                            select_even_if_hidden: bool = False) -> bool
```

x.select_actors_in_layers(layer_names, select, notify, select_even_if_hidden=False) -> bool
Selects/de-selects actors belonging to the named layers.

Args:
    layer_names (Array[Name]): A valid list of layer names.
    select (bool): If true actors are selected; if false, actors are deselected.
    notify (bool): If true the Editor is notified of the selection change; if false, the Editor will not be notified
    select_even_if_hidden (bool): [optional]      If true even hidden actors will be selected; if false, hidden actors won't be selected.

Returns:
    bool: true if at least one actor was selected/deselected.

<a id="unreal.LayersSubsystem.select_actors_in_layer"></a>

#### select_actors_in_layer

```python
def select_actors_in_layer(layer_name: Name,
                           select: bool,
                           notify: bool,
                           select_even_if_hidden: bool = False) -> bool
```

x.select_actors_in_layer(layer_name, select, notify, select_even_if_hidden=False) -> bool
Selects/de-selects actors belonging to the named layer.

Args:
    layer_name (Name): A valid layer name.
    select (bool): If true actors are selected; if false, actors are deselected.
    notify (bool): If true the Editor is notified of the selection change; if false, the Editor will not be notified.
    select_even_if_hidden (bool): [optional]      If true even hidden actors will be selected; if false, hidden actors won't be selected.

Returns:
    bool: true if at least one actor was selected/deselected.

<a id="unreal.LayersSubsystem.rename_layer"></a>

#### rename_layer

```python
def rename_layer(original_layer_name: Name, new_layer_name: Name) -> bool
```

x.rename_layer(original_layer_name, new_layer_name) -> bool
Renames the provided originally named layer to the provided new name

Args:
    original_layer_name (Name): The name of the layer to be renamed
    new_layer_name (Name): The new name for the layer to be renamed

Returns:
    bool:

<a id="unreal.LayersSubsystem.remove_selected_actors_from_layers"></a>

#### remove_selected_actors_from_layers

```python
def remove_selected_actors_from_layers(layer_names: Array[Name]) -> bool
```

x.remove_selected_actors_from_layers(layer_names) -> bool
Removes selected actors from the named layers.

Args:
    layer_names (Array[Name]): A valid list of layer names.

Returns:
    bool: true if at least one actor was removed.

<a id="unreal.LayersSubsystem.remove_selected_actors_from_layer"></a>

#### remove_selected_actors_from_layer

```python
def remove_selected_actors_from_layer(layer_name: Name) -> bool
```

x.remove_selected_actors_from_layer(layer_name) -> bool
Removes the selected actors from the named layer.

Args:
    layer_name (Name): A layer name.

Returns:
    bool: true if at least one actor was added.  false is returned if all selected actors already belong to the named layer.

<a id="unreal.LayersSubsystem.remove_level_layer_information"></a>

#### remove_level_layer_information

```python
def remove_level_layer_information(level: Level) -> None
```

x.remove_level_layer_information(level) -> None
Purges any information regarding layers associated with the level and it contents

Args:
    level (Level): The process

<a id="unreal.LayersSubsystem.remove_actors_from_layers"></a>

#### remove_actors_from_layers

```python
def remove_actors_from_layers(actors: Array[Actor],
                              layer_names: Array[Name],
                              update_stats: bool = True) -> bool
```

x.remove_actors_from_layers(actors, layer_names, update_stats=True) -> bool
Remove the actors to the named layers

Args:
    actors (Array[Actor]): The actors to remove to the named layers
    layer_names (Array[Name]): A valid list of layer names.
    update_stats (bool): 

Returns:
    bool: true if at least one actor was removed from at least one layer.  false is returned if none of the actors belonged to any of the specified layers.

<a id="unreal.LayersSubsystem.remove_actors_from_layer"></a>

#### remove_actors_from_layer

```python
def remove_actors_from_layer(actors: Array[Actor],
                             layer_name: Name,
                             update_stats: bool = True) -> bool
```

x.remove_actors_from_layer(actors, layer_name, update_stats=True) -> bool
Removes the actors from the specified layer.

Args:
    actors (Array[Actor]): The actors to remove from the provided layer
    layer_name (Name): 
    update_stats (bool): 

Returns:
    bool: true if at least one actor was removed from the layer.  false is returned if all the actors already belonged to the layer.

<a id="unreal.LayersSubsystem.remove_actor_from_layers"></a>

#### remove_actor_from_layers

```python
def remove_actor_from_layers(actor: Actor,
                             layer_names: Array[Name],
                             update_stats: bool = True) -> bool
```

x.remove_actor_from_layers(actor, layer_names, update_stats=True) -> bool
Removes the provided actor from the named layers.

Args:
    actor (Actor): The actor to remove from the provided layers
    layer_names (Array[Name]): A valid list of layer names.
    update_stats (bool): 

Returns:
    bool: true if the actor was removed from at least one of the provided layers.

<a id="unreal.LayersSubsystem.remove_actor_from_layer"></a>

#### remove_actor_from_layer

```python
def remove_actor_from_layer(actor: Actor,
                            layer_to_remove: Name,
                            update_stats: bool = True) -> bool
```

x.remove_actor_from_layer(actor, layer_to_remove, update_stats=True) -> bool
Removes an actor from the specified layer.

Args:
    actor (Actor): The actor to remove from the provided layer
    layer_to_remove (Name): The name of the layer to remove the actor from
    update_stats (bool): 

Returns:
    bool: true if the actor was removed from the layer.  false is returned if the actor already belonged to the layer.

<a id="unreal.LayersSubsystem.make_all_layers_visible"></a>

#### make_all_layers_visible

```python
def make_all_layers_visible() -> None
```

x.make_all_layers_visible() -> None
Set the visibility of all layers to true

<a id="unreal.LayersSubsystem.is_layer"></a>

#### is_layer

```python
def is_layer(layer_name: Name) -> bool
```

x.is_layer(layer_name) -> bool
Checks whether the ULayer Object of the provided layer name exists.

Args:
    layer_name (Name): The name of the layer whose ULayer Object to retrieve

Returns:
    bool: If true a valid ULayer Object was found; if false, a valid ULayer object was not found

<a id="unreal.LayersSubsystem.is_actor_valid_for_layer"></a>

#### is_actor_valid_for_layer

```python
def is_actor_valid_for_layer(actor: Actor) -> bool
```

x.is_actor_valid_for_layer(actor) -> bool
Checks to see if the specified actor is in an appropriate state to interact with layers

Args:
    actor (Actor): The actor to validate

Returns:
    bool:

<a id="unreal.LayersSubsystem.initialize_new_actor_layers"></a>

#### initialize_new_actor_layers

```python
def initialize_new_actor_layers(actor: Actor) -> bool
```

x.initialize_new_actor_layers(actor) -> bool
Synchronizes an newly created Actor's layers with the layer system

Args:
    actor (Actor): The actor to initialize

Returns:
    bool:

<a id="unreal.LayersSubsystem.get_world"></a>

#### get_world

```python
def get_world() -> World
```

x.get_world() -> World
Get the current UWorld object.

Returns:
    World: The UWorld* object

<a id="unreal.LayersSubsystem.get_selected_actors"></a>

#### get_selected_actors

```python
def get_selected_actors() -> Array[Actor]
```

x.get_selected_actors() -> Array[Actor]
Find and return the selected actors.

Returns:
    Array[Actor]: The selected AActor's as a TArray.

<a id="unreal.LayersSubsystem.get_layer"></a>

#### get_layer

```python
def get_layer(layer_name: Name) -> Layer
```

x.get_layer(layer_name) -> Layer
Gets the ULayer Object of the named layer

Args:
    layer_name (Name): The name of the layer whose ULayer Object is returned

Returns:
    Layer: The ULayer Object of the provided layer name

<a id="unreal.LayersSubsystem.get_actors_from_layers"></a>

#### get_actors_from_layers

```python
def get_actors_from_layers(layer_names: Array[Name]) -> Array[Actor]
```

x.get_actors_from_layers(layer_names) -> Array[Actor]
Gets all the actors associated with ANY of the specified layers. Analog to AppendActorsFromLayers but it returns rather than appends the actors.

Args:
    layer_names (Array[Name]): The layers to find actors for.

Returns:
    Array[Actor]: The list to assign the found actors to.

<a id="unreal.LayersSubsystem.get_actors_from_layer"></a>

#### get_actors_from_layer

```python
def get_actors_from_layer(layer_name: Name) -> Array[Actor]
```

x.get_actors_from_layer(layer_name) -> Array[Actor]
Gets all the actors associated with the specified layer. Analog to AppendActorsFromLayer but it returns rather than appends the actors.

Args:
    layer_name (Name): The layer to find actors for.

Returns:
    Array[Actor]: The list to assign the found actors to.

<a id="unreal.LayersSubsystem.editor_refresh_layer_browser"></a>

#### editor_refresh_layer_browser

```python
def editor_refresh_layer_browser() -> None
```

x.editor_refresh_layer_browser() -> None
Delegate handler for FEditorDelegates::RefreshLayerBrowser. It internally calls UpdateAllActorsVisibility to refresh the actors of each layer.

<a id="unreal.LayersSubsystem.editor_map_change"></a>

#### editor_map_change

```python
def editor_map_change() -> None
```

x.editor_map_change() -> None
Delegate handler for FEditorDelegates::MapChange. It internally calls LayersChanged.Broadcast.

<a id="unreal.LayersSubsystem.disassociate_actors_from_layers"></a>

#### disassociate_actors_from_layers

```python
def disassociate_actors_from_layers(actors: Array[Actor]) -> bool
```

x.disassociate_actors_from_layers(actors) -> bool
Disassociates actors from the layer system, generally used before deleting the Actors

Args:
    actors (Array[Actor]): The actors to disassociate from the layer system

Returns:
    bool:

<a id="unreal.LayersSubsystem.disassociate_actor_from_layers"></a>

#### disassociate_actor_from_layers

```python
def disassociate_actor_from_layers(actor: Actor) -> bool
```

x.disassociate_actor_from_layers(actor) -> bool
Disassociates an Actor's layers from the layer system, general used before deleting the Actor

Args:
    actor (Actor): The actor to disassociate from the layer system

Returns:
    bool:

<a id="unreal.LayersSubsystem.delete_layers"></a>

#### delete_layers

```python
def delete_layers(layers_to_delete: Array[Name]) -> None
```

x.delete_layers(layers_to_delete) -> None
Deletes all of the provided layers, disassociating all actors from them

Args:
    layers_to_delete (Array[Name]): A valid list of layer names.

<a id="unreal.LayersSubsystem.delete_layer"></a>

#### delete_layer

```python
def delete_layer(layer_to_delete: Name) -> None
```

x.delete_layer(layer_to_delete) -> None
Deletes the provided layer, disassociating all actors from them

Args:
    layer_to_delete (Name): A valid layer name

<a id="unreal.LayersSubsystem.create_layer"></a>

#### create_layer

```python
def create_layer(layer_name: Name) -> Layer
```

x.create_layer(layer_name) -> Layer
Creates a ULayer Object for the named layer

Args:
    layer_name (Name): The name of the layer to create

Returns:
    Layer: The newly created ULayer Object for the named layer

<a id="unreal.LayersSubsystem.append_actors_from_layers"></a>

#### append_actors_from_layers

```python
def append_actors_from_layers(layer_names: Array[Name]) -> Array[Actor]
```

x.append_actors_from_layers(layer_names) -> Array[Actor]
Appends all the actors associated with ANY of the specified layers.

Args:
    layer_names (Array[Name]): The layers to find actors for.

Returns:
    Array[Actor]: 

    out_actors (Array[Actor]): The list to append the found actors to.

<a id="unreal.LayersSubsystem.append_actors_from_layer"></a>

#### append_actors_from_layer

```python
def append_actors_from_layer(layer_name: Name) -> Array[Actor]
```

x.append_actors_from_layer(layer_name) -> Array[Actor]
Appends all the actors associated with the specified layer.

Args:
    layer_name (Name): The layer to find actors for.

Returns:
    Array[Actor]: 

    out_actors (Array[Actor]): The list to append the found actors to.

<a id="unreal.LayersSubsystem.add_selected_actors_to_layers"></a>

#### add_selected_actors_to_layers

```python
def add_selected_actors_to_layers(layer_names: Array[Name]) -> bool
```

x.add_selected_actors_to_layers(layer_names) -> bool
Adds selected actors to the named layers.

Args:
    layer_names (Array[Name]): A valid list of layer names.

Returns:
    bool: true if at least one actor was added.  false is returned if all selected actors already belong to the named layers.

<a id="unreal.LayersSubsystem.add_selected_actors_to_layer"></a>

#### add_selected_actors_to_layer

```python
def add_selected_actors_to_layer(layer_name: Name) -> bool
```

x.add_selected_actors_to_layer(layer_name) -> bool
Adds selected actors to the named layer.

Args:
    layer_name (Name): A layer name.

Returns:
    bool: true if at least one actor was added.  false is returned if all selected actors already belong to the named layer.

<a id="unreal.LayersSubsystem.add_level_layer_information"></a>

#### add_level_layer_information

```python
def add_level_layer_information(level: Level) -> None
```

x.add_level_layer_information(level) -> None
Aggregates any information regarding layers associated with the level and it contents

Args:
    level (Level): The process

<a id="unreal.LayersSubsystem.add_all_layers_to"></a>

#### add_all_layers_to

```python
def add_all_layers_to() -> Array[Layer]
```

x.add_all_layers_to() -> Array[Layer]
Gets all known layers and appends them to the provided array

Returns:
    Array[Layer]: 

    out_layers (Array[Layer]):

<a id="unreal.LayersSubsystem.add_all_layer_names_to"></a>

#### add_all_layer_names_to

```python
def add_all_layer_names_to() -> Array[Name]
```

x.add_all_layer_names_to() -> Array[Name]
Gets all known layers and appends their names to the provide array

Returns:
    Array[Name]: 

    out_layer_names (Array[Name]):

<a id="unreal.LayersSubsystem.add_actor_to_layers"></a>

#### add_actor_to_layers

```python
def add_actor_to_layers(actor: Actor, layer_names: Array[Name]) -> bool
```

x.add_actor_to_layers(actor, layer_names) -> bool
Adds the provided actor to the named layers.

Args:
    actor (Actor): The actor to add to the provided layers
    layer_names (Array[Name]): A valid list of layer names.

Returns:
    bool: true if the actor was added to at least one of the provided layers.

<a id="unreal.LayersSubsystem.add_actor_to_layer"></a>

#### add_actor_to_layer

```python
def add_actor_to_layer(actor: Actor, layer_name: Name) -> bool
```

x.add_actor_to_layer(actor, layer_name) -> bool
Adds the actor to the named layer.

Args:
    actor (Actor): The actor to add to the named layer
    layer_name (Name): The name of the layer to add the actor to

Returns:
    bool: true if the actor was added.  false is returned if the actor already belongs to the layer.

<a id="unreal.LayersSubsystem.add_actors_to_layers"></a>

#### add_actors_to_layers

```python
def add_actors_to_layers(actors: Array[Actor],
                         layer_names: Array[Name]) -> bool
```

x.add_actors_to_layers(actors, layer_names) -> bool
Add the actors to the named layers

Args:
    actors (Array[Actor]): The actors to add to the named layers
    layer_names (Array[Name]): A valid list of layer names.

Returns:
    bool: true if at least one actor was added to at least one layer.  false is returned if all the actors already belonged to all specified layers.

<a id="unreal.LayersSubsystem.add_actors_to_layer"></a>

#### add_actors_to_layer

```python
def add_actors_to_layer(actors: Array[Actor], layer_name: Name) -> bool
```

x.add_actors_to_layer(actors, layer_name) -> bool
Add the actors to the named layer

Args:
    actors (Array[Actor]): The actors to add to the named layer
    layer_name (Name): The name of the layer to add to

Returns:
    bool: true if at least one actor was added to the layer.  false is returned if all the actors already belonged to the layer.

<a id="unreal.CommonResolutionMenuContext"></a>