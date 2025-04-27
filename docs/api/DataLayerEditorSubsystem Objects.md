## DataLayerEditorSubsystem Objects

```python
class DataLayerEditorSubsystem(EditorSubsystem)
```

Data Layer Editor Subsystem

**C++ Source:**

- **Module**: DataLayerEditor
- **File**: DataLayerEditorSubsystem.h

<a id="unreal.DataLayerEditorSubsystem.update_all_view_visibility"></a>

#### update_all_view_visibility

```python
def update_all_view_visibility(data_layer_that_changed: DataLayer) -> None
```

x.update_all_view_visibility(data_layer_that_changed) -> None
Update All View Visibility
deprecated: Per-view Data Layer visibility was removed.

Args:
    data_layer_that_changed (DataLayer):

<a id="unreal.DataLayerEditorSubsystem.update_all_actors_visibility"></a>

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

<a id="unreal.DataLayerEditorSubsystem.update_actor_visibility"></a>

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

<a id="unreal.DataLayerEditorSubsystem.update_actor_all_views_visibility"></a>

#### update_actor_all_views_visibility

```python
def update_actor_all_views_visibility(actor: Actor) -> None
```

x.update_actor_all_views_visibility(actor) -> None
Update Actor All Views Visibility
deprecated: Per-view Data Layer visibility was removed.

Args:
    actor (Actor):

<a id="unreal.DataLayerEditorSubsystem.toggle_data_layer_visibility"></a>

#### toggle_data_layer_visibility

```python
def toggle_data_layer_visibility(data_layer: DataLayerInstance) -> None
```

x.toggle_data_layer_visibility(data_layer) -> None
Toggles the DataLayer's visibility

Args:
    data_layer (DataLayerInstance): The DataLayer to affect

<a id="unreal.DataLayerEditorSubsystem.toggle_data_layers_visibility"></a>

#### toggle_data_layers_visibility

```python
def toggle_data_layers_visibility(
        data_layers: Array[DataLayerInstance]) -> None
```

x.toggle_data_layers_visibility(data_layers) -> None
Toggles the visibility of all of the DataLayers

Args:
    data_layers (Array[DataLayerInstance]): The DataLayers to affect

<a id="unreal.DataLayerEditorSubsystem.toggle_data_layers_is_loaded_in_editor"></a>

#### toggle_data_layers_is_loaded_in_editor

```python
def toggle_data_layers_is_loaded_in_editor(
        data_layers: Array[DataLayerInstance],
        is_from_user_change: bool) -> bool
```

x.toggle_data_layers_is_loaded_in_editor(data_layers, is_from_user_change) -> bool
Toggles the IsLoadedInEditor flag of all of the DataLayers

Args:
    data_layers (Array[DataLayerInstance]): The DataLayers to affect
    is_from_user_change (bool): If this change originates from a user change or not.

Returns:
    bool:

<a id="unreal.DataLayerEditorSubsystem.toggle_data_layers_is_dynamically_loaded_in_editor"></a>

#### toggle_data_layers_is_dynamically_loaded_in_editor

```python
def toggle_data_layers_is_dynamically_loaded_in_editor(
        data_layers: Array[DataLayer], is_from_user_change: bool) -> bool
```

x.toggle_data_layers_is_dynamically_loaded_in_editor(data_layers, is_from_user_change) -> bool
Toggle Data Layers Is Dynamically Loaded in Editor
deprecated: Use ToggleDataLayersIsLoadedInEditor instead

Args:
    data_layers (Array[DataLayer]): 
    is_from_user_change (bool): 

Returns:
    bool:

<a id="unreal.DataLayerEditorSubsystem.toggle_data_layer_is_loaded_in_editor"></a>

#### toggle_data_layer_is_loaded_in_editor

```python
def toggle_data_layer_is_loaded_in_editor(data_layer: DataLayerInstance,
                                          is_from_user_change: bool) -> bool
```

x.toggle_data_layer_is_loaded_in_editor(data_layer, is_from_user_change) -> bool
Toggles the DataLayer's IsLoadedInEditor flag

Args:
    data_layer (DataLayerInstance): The DataLayer to affect
    is_from_user_change (bool): If this change originates from a user change or not.

Returns:
    bool:

<a id="unreal.DataLayerEditorSubsystem.toggle_data_layer_is_dynamically_loaded_in_editor"></a>

#### toggle_data_layer_is_dynamically_loaded_in_editor

```python
def toggle_data_layer_is_dynamically_loaded_in_editor(
        data_layer: DataLayer, is_from_user_change: bool) -> bool
```

x.toggle_data_layer_is_dynamically_loaded_in_editor(data_layer, is_from_user_change) -> bool
Toggle Data Layer Is Dynamically Loaded in Editor
deprecated: Use ToggleDataLayerIsLoadedInEditor instead

Args:
    data_layer (DataLayer): 
    is_from_user_change (bool): 

Returns:
    bool:

<a id="unreal.DataLayerEditorSubsystem.set_parent_data_layer_for_data_layers"></a>

#### set_parent_data_layer_for_data_layers

```python
def set_parent_data_layer_for_data_layers(
        data_layers: Array[DataLayerInstance],
        parent_data_layer: DataLayerInstance) -> None
```

x.set_parent_data_layer_for_data_layers(data_layers, parent_data_layer) -> None
Sets a Parent DataLayer for a specified list of DataLayers

Args:
    data_layers (Array[DataLayerInstance]): The child DataLayers.
    parent_data_layer (DataLayerInstance): The parent DataLayer.

<a id="unreal.DataLayerEditorSubsystem.set_parent_data_layer"></a>

#### set_parent_data_layer

```python
def set_parent_data_layer(data_layer: DataLayerInstance,
                          parent_data_layer: DataLayerInstance) -> bool
```

x.set_parent_data_layer(data_layer, parent_data_layer) -> bool
Sets a Parent DataLayer for a specified DataLayer

Args:
    data_layer (DataLayerInstance): The child DataLayer.
    parent_data_layer (DataLayerInstance): The parent DataLayer.

Returns:
    bool: true if succeeded, false if failed.

<a id="unreal.DataLayerEditorSubsystem.set_data_layer_visibility"></a>

#### set_data_layer_visibility

```python
def set_data_layer_visibility(data_layer: DataLayerInstance,
                              is_visible: bool) -> None
```

x.set_data_layer_visibility(data_layer, is_visible) -> None
Changes the DataLayer's visibility to the provided state

Args:
    data_layer (DataLayerInstance): The DataLayer to affect.
    is_visible (bool): If true the DataLayer will be visible; if false, the DataLayer will not be visible.

<a id="unreal.DataLayerEditorSubsystem.set_data_layers_visibility"></a>

#### set_data_layers_visibility

```python
def set_data_layers_visibility(data_layers: Array[DataLayerInstance],
                               is_visible: bool) -> None
```

x.set_data_layers_visibility(data_layers, is_visible) -> None
Changes visibility of the DataLayers to the provided state

Args:
    data_layers (Array[DataLayerInstance]): The DataLayers to affect
    is_visible (bool): If true the DataLayers will be visible; if false, the DataLayers will not be visible

<a id="unreal.DataLayerEditorSubsystem.set_data_layers_is_loaded_in_editor"></a>

#### set_data_layers_is_loaded_in_editor

```python
def set_data_layers_is_loaded_in_editor(data_layers: Array[DataLayerInstance],
                                        is_loaded_in_editor: bool,
                                        is_from_user_change: bool) -> bool
```

x.set_data_layers_is_loaded_in_editor(data_layers, is_loaded_in_editor, is_from_user_change) -> bool
Changes the IsLoadedInEditor flag of the DataLayers to the provided state

Args:
    data_layers (Array[DataLayerInstance]): The DataLayers to affect
    is_loaded_in_editor (bool): The new value of the flag IsLoadedInEditor. If True, the Editor loading will consider this DataLayer to load or not an Actor part of this DataLayer. An Actor will not be loaded in the Editor if all its DataLayers are not LoadedInEditor.
    is_from_user_change (bool): If this change originates from a user change or not.

Returns:
    bool:

<a id="unreal.DataLayerEditorSubsystem.set_data_layers_is_dynamically_loaded_in_editor"></a>

#### set_data_layers_is_dynamically_loaded_in_editor

```python
def set_data_layers_is_dynamically_loaded_in_editor(
        data_layers: Array[DataLayer], is_loaded_in_editor: bool,
        is_from_user_change: bool) -> bool
```

x.set_data_layers_is_dynamically_loaded_in_editor(data_layers, is_loaded_in_editor, is_from_user_change) -> bool
Set Data Layers Is Dynamically Loaded in Editor
deprecated: Use SetDataLayersIsLoadedInEditor instead

Args:
    data_layers (Array[DataLayer]): 
    is_loaded_in_editor (bool): 
    is_from_user_change (bool): 

Returns:
    bool:

<a id="unreal.DataLayerEditorSubsystem.set_data_layer_is_loaded_in_editor"></a>

#### set_data_layer_is_loaded_in_editor

```python
def set_data_layer_is_loaded_in_editor(data_layer: DataLayerInstance,
                                       is_loaded_in_editor: bool,
                                       is_from_user_change: bool) -> bool
```

x.set_data_layer_is_loaded_in_editor(data_layer, is_loaded_in_editor, is_from_user_change) -> bool
Changes the DataLayer's IsLoadedInEditor flag to the provided state

Args:
    data_layer (DataLayerInstance): The DataLayer to affect.
    is_loaded_in_editor (bool): The new value of the flag IsLoadedInEditor. If True, the Editor loading will consider this DataLayer to load or not an Actor part of this DataLayer. An Actor will not be loaded in the Editor if all its DataLayers are not LoadedInEditor.
    is_from_user_change (bool): If this change originates from a user change or not.

Returns:
    bool:

<a id="unreal.DataLayerEditorSubsystem.set_data_layer_is_dynamically_loaded_in_editor"></a>

#### set_data_layer_is_dynamically_loaded_in_editor

```python
def set_data_layer_is_dynamically_loaded_in_editor(
        data_layer: DataLayer, is_loaded_in_editor: bool,
        is_from_user_change: bool) -> bool
```

x.set_data_layer_is_dynamically_loaded_in_editor(data_layer, is_loaded_in_editor, is_from_user_change) -> bool
Set Data Layer Is Dynamically Loaded in Editor
deprecated: Use SetDataLayerIsLoadedInEditor instead

Args:
    data_layer (DataLayer): 
    is_loaded_in_editor (bool): 
    is_from_user_change (bool): 

Returns:
    bool:

<a id="unreal.DataLayerEditorSubsystem.set_actor_editor_context_current_external_data_layer"></a>

#### set_actor_editor_context_current_external_data_layer

```python
def set_actor_editor_context_current_external_data_layer(
        external_data_layer_asset: ExternalDataLayerAsset) -> bool
```

x.set_actor_editor_context_current_external_data_layer(external_data_layer_asset) -> bool
Set Actor Editor Context Current External Data Layer

Args:
    external_data_layer_asset (ExternalDataLayerAsset): 

Returns:
    bool:

<a id="unreal.DataLayerEditorSubsystem.select_actors_in_data_layers"></a>

#### select_actors_in_data_layers

```python
def select_actors_in_data_layers(data_layers: Array[DataLayerInstance],
                                 select: bool,
                                 notify: bool,
                                 select_even_if_hidden: bool = False) -> bool
```

x.select_actors_in_data_layers(data_layers, select, notify, select_even_if_hidden=False) -> bool
Selects/de-selects actors belonging to the DataLayers.

Args:
    data_layers (Array[DataLayerInstance]): A valid list of DataLayers.
    select (bool): If true actors are selected; if false, actors are deselected.
    notify (bool): If true the Editor is notified of the selection change; if false, the Editor will not be notified
    select_even_if_hidden (bool): [optional]      If true even hidden actors will be selected; if false, hidden actors won't be selected.

Returns:
    bool: true if at least one actor was selected/deselected.

<a id="unreal.DataLayerEditorSubsystem.select_actors_in_data_layer"></a>

#### select_actors_in_data_layer

```python
def select_actors_in_data_layer(data_layer: DataLayerInstance,
                                select: bool,
                                notify: bool,
                                select_even_if_hidden: bool = False) -> bool
```

x.select_actors_in_data_layer(data_layer, select, notify, select_even_if_hidden=False) -> bool
Selects/de-selects actors belonging to the DataLayer.

Args:
    data_layer (DataLayerInstance): A valid DataLayer.
    select (bool): If true actors are selected; if false, actors are deselected.
    notify (bool): If true the Editor is notified of the selection change; if false, the Editor will not be notified.
    select_even_if_hidden (bool): [optional]      If true even hidden actors will be selected; if false, hidden actors won't be selected.

Returns:
    bool: true if at least one actor was selected/deselected.

<a id="unreal.DataLayerEditorSubsystem.rename_data_layer"></a>

#### rename_data_layer

```python
def rename_data_layer(data_layer: DataLayerInstance,
                      new_data_layer_label: Name) -> bool
```

x.rename_data_layer(data_layer, new_data_layer_label) -> bool
Rename Data Layer

Args:
    data_layer (DataLayerInstance): 
    new_data_layer_label (Name): 

Returns:
    bool:

<a id="unreal.DataLayerEditorSubsystem.remove_selected_actors_from_data_layers"></a>

#### remove_selected_actors_from_data_layers

```python
def remove_selected_actors_from_data_layers(
        data_layers: Array[DataLayerInstance]) -> bool
```

x.remove_selected_actors_from_data_layers(data_layers) -> bool
Removes selected actors from the DataLayers.

Args:
    data_layers (Array[DataLayerInstance]): A valid list of DataLayers.

Returns:
    bool: true if at least one actor was removed.

<a id="unreal.DataLayerEditorSubsystem.remove_selected_actors_from_data_layer"></a>

#### remove_selected_actors_from_data_layer

```python
def remove_selected_actors_from_data_layer(
        data_layer: DataLayerInstance) -> bool
```

x.remove_selected_actors_from_data_layer(data_layer) -> bool
Removes the selected actors from the DataLayer.

Args:
    data_layer (DataLayerInstance): A DataLayer.

Returns:
    bool: true if at least one actor was added.  false is returned if all selected actors already belong to the DataLayer.

<a id="unreal.DataLayerEditorSubsystem.remove_from_actor_editor_context"></a>

#### remove_from_actor_editor_context

```python
def remove_from_actor_editor_context(
        data_layer_instance: DataLayerInstance) -> None
```

x.remove_from_actor_editor_context(data_layer_instance) -> None
Remove from Actor Editor Context

Args:
    data_layer_instance (DataLayerInstance):

<a id="unreal.DataLayerEditorSubsystem.remove_actors_from_data_layers"></a>

#### remove_actors_from_data_layers

```python
def remove_actors_from_data_layers(
        actors: Array[Actor], data_layers: Array[DataLayerInstance]) -> bool
```

x.remove_actors_from_data_layers(actors, data_layers) -> bool
Remove the actors from the DataLayers

Args:
    actors (Array[Actor]): The actors to remove to the DataLayers
    data_layers (Array[DataLayerInstance]): A valid list of DataLayers.

Returns:
    bool: true if at least one actor was removed from at least one DataLayer.  false is returned if none of the actors belonged to any of the specified DataLayers.

<a id="unreal.DataLayerEditorSubsystem.remove_actors_from_data_layer"></a>

#### remove_actors_from_data_layer

```python
def remove_actors_from_data_layer(actors: Array[Actor],
                                  data_layer: DataLayerInstance) -> bool
```

x.remove_actors_from_data_layer(actors, data_layer) -> bool
Removes the actors from the specified DataLayer.

Args:
    actors (Array[Actor]): The actors to remove from the provided DataLayer
    data_layer (DataLayerInstance): 

Returns:
    bool: true if at least one actor was removed from the DataLayer.  false is returned if all the actors already belonged to the DataLayer.

<a id="unreal.DataLayerEditorSubsystem.remove_actors_from_all_data_layers"></a>

#### remove_actors_from_all_data_layers

```python
def remove_actors_from_all_data_layers(actors: Array[Actor]) -> bool
```

x.remove_actors_from_all_data_layers(actors) -> bool
Removes an actor from all DataLayers.

Args:
    actors (Array[Actor]): 

Returns:
    bool: true if any actor was changed.

<a id="unreal.DataLayerEditorSubsystem.remove_actor_from_data_layers"></a>

#### remove_actor_from_data_layers

```python
def remove_actor_from_data_layers(
        actor: Actor, data_layers: Array[DataLayerInstance]) -> bool
```

x.remove_actor_from_data_layers(actor, data_layers) -> bool
Removes the provided actor from the DataLayers.

Args:
    actor (Actor): The actor to remove from the provided DataLayers
    data_layers (Array[DataLayerInstance]): A valid list of DataLayers.

Returns:
    bool: true if the actor was removed from at least one of the provided DataLayers.

<a id="unreal.DataLayerEditorSubsystem.remove_actor_from_data_layer"></a>

#### remove_actor_from_data_layer

```python
def remove_actor_from_data_layer(
        actor: Actor, data_layer_to_remove: DataLayerInstance) -> bool
```

x.remove_actor_from_data_layer(actor, data_layer_to_remove) -> bool
Removes an actor from the specified DataLayer.

Args:
    actor (Actor): The actor to remove from the provided DataLayer
    data_layer_to_remove (DataLayerInstance): The DataLayer to remove the actor from

Returns:
    bool: true if the actor was removed from the DataLayer.  false is returned if the actor already belonged to the DataLayer.

<a id="unreal.DataLayerEditorSubsystem.remove_actor_from_all_data_layers"></a>

#### remove_actor_from_all_data_layers

```python
def remove_actor_from_all_data_layers(actor: Actor) -> bool
```

x.remove_actor_from_all_data_layers(actor) -> bool
Removes an actor from all DataLayers.

Args:
    actor (Actor): The actor to modify

Returns:
    bool: true if the actor was changed.

<a id="unreal.DataLayerEditorSubsystem.make_all_data_layers_visible"></a>

#### make_all_data_layers_visible

```python
def make_all_data_layers_visible() -> None
```

x.make_all_data_layers_visible() -> None
Set the visibility of all DataLayers to true

<a id="unreal.DataLayerEditorSubsystem.is_actor_valid_for_data_layer_instances"></a>

#### is_actor_valid_for_data_layer_instances

```python
def is_actor_valid_for_data_layer_instances(
        actor: Actor, data_layer_instances: Array[DataLayerInstance]) -> bool
```

x.is_actor_valid_for_data_layer_instances(actor, data_layer_instances) -> bool
Checks to see if the specified actor is in an appropriate state to interact with DataLayers

Args:
    actor (Actor): The actor to validate
    data_layer_instances (Array[DataLayerInstance]): The data layers used to do the validation

Returns:
    bool:

<a id="unreal.DataLayerEditorSubsystem.is_actor_valid_for_data_layer"></a>

#### is_actor_valid_for_data_layer

```python
def is_actor_valid_for_data_layer(actor: Actor) -> bool
```

x.is_actor_valid_for_data_layer(actor) -> bool
Is Actor Valid for Data Layer

Args:
    actor (Actor): 

Returns:
    bool:

<a id="unreal.DataLayerEditorSubsystem.get_data_layer_instances"></a>

#### get_data_layer_instances

```python
def get_data_layer_instances(
        data_layer_assets: Array[DataLayerAsset]) -> Array[DataLayerInstance]
```

x.get_data_layer_instances(data_layer_assets) -> Array[DataLayerInstance]
Gets the UDataLayerInstances associated to the each DataLayerAssets

Args:
    data_layer_assets (Array[DataLayerAsset]): The array of DataLayerAssets associated to UDataLayerInstances

Returns:
    Array[DataLayerInstance]: The array of UDataLayerInstances corresponding to a DataLayerAsset in the DataLayerAssets array

<a id="unreal.DataLayerEditorSubsystem.get_data_layer_instance"></a>

#### get_data_layer_instance

```python
def get_data_layer_instance(
        data_layer_asset: DataLayerAsset) -> DataLayerInstance
```

x.get_data_layer_instance(data_layer_asset) -> DataLayerInstance
Gets the UDataLayerInstance associated to the DataLayerAsset

Args:
    data_layer_asset (DataLayerAsset): The DataLayerAsset associated to the UDataLayerInstance

Returns:
    DataLayerInstance: The UDataLayerInstance of the provided DataLayerAsset

<a id="unreal.DataLayerEditorSubsystem.get_data_layer_from_label"></a>

#### get_data_layer_from_label

```python
def get_data_layer_from_label(data_layer_label: Name) -> DataLayerInstance
```

x.get_data_layer_from_label(data_layer_label) -> DataLayerInstance
Get Data Layer from Label

Args:
    data_layer_label (Name): 

Returns:
    DataLayerInstance:

<a id="unreal.DataLayerEditorSubsystem.get_data_layer"></a>

#### get_data_layer

```python
def get_data_layer(actor_data_layer: ActorDataLayer) -> DataLayerInstance
```

x.get_data_layer(actor_data_layer) -> DataLayerInstance
Get Data Layer

Args:
    actor_data_layer (ActorDataLayer): 

Returns:
    DataLayerInstance:

<a id="unreal.DataLayerEditorSubsystem.get_all_data_layers"></a>

#### get_all_data_layers

```python
def get_all_data_layers() -> Array[DataLayerInstance]
```

x.get_all_data_layers() -> Array[DataLayerInstance]
Returns all Data Layers

Returns:
    Array[DataLayerInstance]:

<a id="unreal.DataLayerEditorSubsystem.get_actors_from_data_layers"></a>

#### get_actors_from_data_layers

```python
def get_actors_from_data_layers(
        data_layers: Array[DataLayerInstance]) -> Array[Actor]
```

x.get_actors_from_data_layers(data_layers) -> Array[Actor]
Gets all the actors associated with ANY of the specified DataLayers. Analog to AppendActorsFromDataLayers but it returns rather than appends the actors.

Args:
    data_layers (Array[DataLayerInstance]): The DataLayers to find actors for.

Returns:
    Array[Actor]: The list to assign the found actors to.

<a id="unreal.DataLayerEditorSubsystem.get_actors_from_data_layer"></a>

#### get_actors_from_data_layer

```python
def get_actors_from_data_layer(data_layer: DataLayerInstance) -> Array[Actor]
```

x.get_actors_from_data_layer(data_layer) -> Array[Actor]
Gets all the actors associated with the specified DataLayer. Analog to AppendActorsFromDataLayer but it returns rather than appends the actors.

Args:
    data_layer (DataLayerInstance): The DataLayer to find actors for.

Returns:
    Array[Actor]: The list to assign the found actors to.

<a id="unreal.DataLayerEditorSubsystem.get_actor_editor_context_current_external_data_layer"></a>

#### get_actor_editor_context_current_external_data_layer

```python
def get_actor_editor_context_current_external_data_layer(
) -> ExternalDataLayerAsset
```

x.get_actor_editor_context_current_external_data_layer() -> ExternalDataLayerAsset
Get Actor Editor Context Current External Data Layer

Returns:
    ExternalDataLayerAsset:

<a id="unreal.DataLayerEditorSubsystem.delete_data_layers"></a>

#### delete_data_layers

```python
def delete_data_layers(
        data_layers_to_delete: Array[DataLayerInstance]) -> None
```

x.delete_data_layers(data_layers_to_delete) -> None
Deletes all of the provided DataLayers

Args:
    data_layers_to_delete (Array[DataLayerInstance]): A valid list of DataLayer.

<a id="unreal.DataLayerEditorSubsystem.delete_data_layer"></a>

#### delete_data_layer

```python
def delete_data_layer(data_layer_to_delete: DataLayerInstance) -> None
```

x.delete_data_layer(data_layer_to_delete) -> None
Deletes the provided DataLayer

Args:
    data_layer_to_delete (DataLayerInstance): A valid DataLayer

<a id="unreal.DataLayerEditorSubsystem.create_data_layer_instance"></a>

#### create_data_layer_instance

```python
def create_data_layer_instance(
        parameters: DataLayerCreationParameters) -> DataLayerInstance
```

x.create_data_layer_instance(parameters) -> DataLayerInstance
Creates a UDataLayerInstance Object

Args:
    parameters (DataLayerCreationParameters): The Data Layer Instance creation parameters

Returns:
    DataLayerInstance: The newly created UDataLayerInstance Object

<a id="unreal.DataLayerEditorSubsystem.create_data_layer"></a>

#### create_data_layer

```python
def create_data_layer(
        parent_data_layer: DataLayerInstance = None) -> DataLayerInstance
```

x.create_data_layer(parent_data_layer=None) -> DataLayerInstance
Create Data Layer

Args:
    parent_data_layer (DataLayerInstance): 

Returns:
    DataLayerInstance:

<a id="unreal.DataLayerEditorSubsystem.append_actors_from_data_layers"></a>

#### append_actors_from_data_layers

```python
def append_actors_from_data_layers(
        data_layers: Array[DataLayerInstance]) -> Array[Actor]
```

x.append_actors_from_data_layers(data_layers) -> Array[Actor]
Appends all the actors associated with ANY of the specified DataLayers.

Args:
    data_layers (Array[DataLayerInstance]): The DataLayers to find actors for.

Returns:
    Array[Actor]: 

    out_actors (Array[Actor]): The list to append the found actors to.

<a id="unreal.DataLayerEditorSubsystem.append_actors_from_data_layer"></a>

#### append_actors_from_data_layer

```python
def append_actors_from_data_layer(
        data_layer: DataLayerInstance) -> Array[Actor]
```

x.append_actors_from_data_layer(data_layer) -> Array[Actor]
Appends all the actors associated with the specified DataLayer.

Args:
    data_layer (DataLayerInstance): The DataLayer to find actors for.

Returns:
    Array[Actor]: 

    out_actors (Array[Actor]): The list to append the found actors to.

<a id="unreal.DataLayerEditorSubsystem.add_to_actor_editor_context"></a>

#### add_to_actor_editor_context

```python
def add_to_actor_editor_context(
        data_layer_instance: DataLayerInstance) -> None
```

x.add_to_actor_editor_context(data_layer_instance) -> None
Add to Actor Editor Context

Args:
    data_layer_instance (DataLayerInstance):

<a id="unreal.DataLayerEditorSubsystem.add_selected_actors_to_data_layers"></a>

#### add_selected_actors_to_data_layers

```python
def add_selected_actors_to_data_layers(
        data_layers: Array[DataLayerInstance]) -> bool
```

x.add_selected_actors_to_data_layers(data_layers) -> bool
Adds selected actors to the DataLayers.

Args:
    data_layers (Array[DataLayerInstance]): A valid list of DataLayers.

Returns:
    bool: true if at least one actor was added.  false is returned if all selected actors already belong to the DataLayers.

<a id="unreal.DataLayerEditorSubsystem.add_selected_actors_to_data_layer"></a>

#### add_selected_actors_to_data_layer

```python
def add_selected_actors_to_data_layer(data_layer: DataLayerInstance) -> bool
```

x.add_selected_actors_to_data_layer(data_layer) -> bool
Adds selected actors to the DataLayer.

Args:
    data_layer (DataLayerInstance): A DataLayer.

Returns:
    bool: true if at least one actor was added.  false is returned if all selected actors already belong to the DataLayer.

<a id="unreal.DataLayerEditorSubsystem.add_actor_to_data_layers"></a>

#### add_actor_to_data_layers

```python
def add_actor_to_data_layers(actor: Actor,
                             data_layers: Array[DataLayerInstance]) -> bool
```

x.add_actor_to_data_layers(actor, data_layers) -> bool
Adds the provided actor to the DataLayers.

Args:
    actor (Actor): The actor to add to the provided DataLayers
    data_layers (Array[DataLayerInstance]): A valid list of DataLayers.

Returns:
    bool: true if the actor was added to at least one of the provided DataLayers.

<a id="unreal.DataLayerEditorSubsystem.add_actor_to_data_layer"></a>

#### add_actor_to_data_layer

```python
def add_actor_to_data_layer(actor: Actor,
                            data_layer: DataLayerInstance) -> bool
```

x.add_actor_to_data_layer(actor, data_layer) -> bool
Adds the actor to the DataLayer.

Args:
    actor (Actor): The actor to add to the DataLayer
    data_layer (DataLayerInstance): The DataLayer to add the actor to

Returns:
    bool: true if the actor was added.  false is returned if the actor already belongs to the DataLayer.

<a id="unreal.DataLayerEditorSubsystem.add_actors_to_data_layers"></a>

#### add_actors_to_data_layers

```python
def add_actors_to_data_layers(actors: Array[Actor],
                              data_layers: Array[DataLayerInstance]) -> bool
```

x.add_actors_to_data_layers(actors, data_layers) -> bool
Add the actors to the DataLayers

Args:
    actors (Array[Actor]): The actors to add to the DataLayers
    data_layers (Array[DataLayerInstance]): A valid list of DataLayers.

Returns:
    bool: true if at least one actor was added to at least one DataLayer.  false is returned if all the actors already belonged to all specified DataLayers.

<a id="unreal.DataLayerEditorSubsystem.add_actors_to_data_layer"></a>

#### add_actors_to_data_layer

```python
def add_actors_to_data_layer(actors: Array[Actor],
                             data_layer: DataLayerInstance) -> bool
```

x.add_actors_to_data_layer(actors, data_layer) -> bool
Add the actors to the DataLayer

Args:
    actors (Array[Actor]): The actors to add to the DataLayer
    data_layer (DataLayerInstance): The DataLayer to add to

Returns:
    bool: true if at least one actor was added to the DataLayer.  false is returned if all the actors already belonged to the DataLayer.

<a id="unreal.DataLayerFactory"></a>