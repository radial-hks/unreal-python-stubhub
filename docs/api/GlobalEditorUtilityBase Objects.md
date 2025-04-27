## GlobalEditorUtilityBase Objects

```python
class GlobalEditorUtilityBase(Object)
```

Global Editor Utility Base

**C++ Source:**

- **Module**: Blutility
- **File**: GlobalEditorUtilityBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_run_default_action`` (bool):  [Read-Write] Should this blueprint automatically run OnDefaultActionClicked, or should it open up a details panel to edit properties and/or offer multiple buttons
- ``help_text`` (str):  [Read-Write]
- ``on_each_selected_actor`` (ForEachActorIteratorSignature):  [Read-Write] The method called for each selected actor when ForEachSelectedActor is called
- ``on_each_selected_asset`` (ForEachAssetIteratorSignature):  [Read-Write] The method called for each selected asset when ForEachSelectedAsset is called

<a id="unreal.GlobalEditorUtilityBase.help_text"></a>

#### help_text

```python
@property
def help_text() -> str
```

(str):  [Read-Write]

<a id="unreal.GlobalEditorUtilityBase.help_text"></a>

#### help_text

```python
@help_text.setter
def help_text(value: str) -> None
```

<a id="unreal.GlobalEditorUtilityBase.auto_run_default_action"></a>

#### auto_run_default_action

```python
@property
def auto_run_default_action() -> bool
```

(bool):  [Read-Only] Should this blueprint automatically run OnDefaultActionClicked, or should it open up a details panel to edit properties and/or offer multiple buttons

<a id="unreal.GlobalEditorUtilityBase.on_each_selected_actor"></a>

#### on_each_selected_actor

```python
@property
def on_each_selected_actor() -> ForEachActorIteratorSignature
```

(ForEachActorIteratorSignature):  [Read-Write] The method called for each selected actor when ForEachSelectedActor is called

<a id="unreal.GlobalEditorUtilityBase.on_each_selected_actor"></a>

#### on_each_selected_actor

```python
@on_each_selected_actor.setter
def on_each_selected_actor(value: ForEachActorIteratorSignature) -> None
```

<a id="unreal.GlobalEditorUtilityBase.on_each_selected_asset"></a>

#### on_each_selected_asset

```python
@property
def on_each_selected_asset() -> ForEachAssetIteratorSignature
```

(ForEachAssetIteratorSignature):  [Read-Write] The method called for each selected asset when ForEachSelectedAsset is called

<a id="unreal.GlobalEditorUtilityBase.on_each_selected_asset"></a>

#### on_each_selected_asset

```python
@on_each_selected_asset.setter
def on_each_selected_asset(value: ForEachAssetIteratorSignature) -> None
```

<a id="unreal.GlobalEditorUtilityBase.set_actor_selection_state"></a>

#### set_actor_selection_state

```python
def set_actor_selection_state(actor: Actor, should_be_selected: bool) -> None
```

x.set_actor_selection_state(actor, should_be_selected) -> None
Set the selection state for the selected actor

Args:
    actor (Actor): 
    should_be_selected (bool):

<a id="unreal.GlobalEditorUtilityBase.select_nothing"></a>

#### select_nothing

```python
def select_nothing() -> None
```

x.select_nothing() -> None
Selects nothing in the editor (another way to clear the selection)

<a id="unreal.GlobalEditorUtilityBase.rename_asset"></a>

#### rename_asset

```python
def rename_asset(asset: Object, new_name: str) -> None
```

x.rename_asset(asset, new_name) -> None
Renames an asset (cannot move folders)

Args:
    asset (Object): 
    new_name (str):

<a id="unreal.GlobalEditorUtilityBase.on_default_action_clicked"></a>

#### on_default_action_clicked

```python
def on_default_action_clicked() -> None
```

x.on_default_action_clicked() -> None
The default action called when the blutility is invoked if bAutoRunDefaultAction=true (it is never called otherwise)

<a id="unreal.GlobalEditorUtilityBase.get_selection_set"></a>

#### get_selection_set

```python
def get_selection_set() -> Array[Actor]
```

x.get_selection_set() -> Array[Actor]
Get Selection Set

Returns:
    Array[Actor]:

<a id="unreal.GlobalEditorUtilityBase.get_selection_bounds"></a>

#### get_selection_bounds

```python
def get_selection_bounds() -> Tuple[Vector, Vector, float]
```

x.get_selection_bounds() -> (origin=Vector, box_extent=Vector, sphere_radius=float)
Get Selection Bounds

Returns:
    tuple: 

    origin (Vector): 

    box_extent (Vector): 

    sphere_radius (float):

<a id="unreal.GlobalEditorUtilityBase.get_selected_assets"></a>

#### get_selected_assets

```python
def get_selected_assets() -> Array[Object]
```

x.get_selected_assets() -> Array[Object]
Gets the set of currently selected assets

Returns:
    Array[Object]:

<a id="unreal.GlobalEditorUtilityBase.get_editor_user_settings"></a>

#### get_editor_user_settings

```python
def get_editor_user_settings() -> EditorPerProjectUserSettings
```

x.get_editor_user_settings() -> EditorPerProjectUserSettings
Get Editor User Settings

Returns:
    EditorPerProjectUserSettings:

<a id="unreal.GlobalEditorUtilityBase.get_actor_reference"></a>

#### get_actor_reference

```python
def get_actor_reference(path_to_actor: str) -> Actor
```

x.get_actor_reference(path_to_actor) -> Actor
Attempts to find the actor specified by PathToActor in the current editor world

Args:
    path_to_actor (str): The path to the actor (e.g. PersistentLevel.PlayerStart)

Returns:
    Actor: A reference to the actor, or none if it wasn't found

<a id="unreal.GlobalEditorUtilityBase.for_each_selected_asset"></a>

#### for_each_selected_asset

```python
def for_each_selected_asset() -> None
```

x.for_each_selected_asset() -> None
Calls OnEachSelectedAsset for each selected asset

<a id="unreal.GlobalEditorUtilityBase.for_each_selected_actor"></a>

#### for_each_selected_actor

```python
def for_each_selected_actor() -> None
```

x.for_each_selected_actor() -> None
Calls OnEachSelectedActor for each selected actor

<a id="unreal.GlobalEditorUtilityBase.clear_actor_selection_set"></a>

#### clear_actor_selection_set

```python
def clear_actor_selection_set() -> None
```

x.clear_actor_selection_set() -> None
Remove all actors from the selection set

<a id="unreal.EditorUtilityExtension"></a>