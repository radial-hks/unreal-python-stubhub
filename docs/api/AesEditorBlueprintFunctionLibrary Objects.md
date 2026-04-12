## AesEditorBlueprintFunctionLibrary Objects

```python
class AesEditorBlueprintFunctionLibrary(BlueprintFunctionLibrary)
```

Aes Editor Blueprint Function Library

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesEditorMode
- **File**: AesEditorBlueprintFunctionLibrary.h

<a id="unreal.AesEditorBlueprintFunctionLibrary.undo"></a>

#### undo

```python
@classmethod
def undo(cls) -> None
```

X.undo() -> None
Undo

<a id="unreal.AesEditorBlueprintFunctionLibrary.switch_scheme"></a>

#### switch\_scheme

```python
@classmethod
def switch_scheme(cls, scheme_name: str) -> None
```

X.switch_scheme(scheme_name) -> None
Switch Scheme

Args:
    scheme_name (str):

<a id="unreal.AesEditorBlueprintFunctionLibrary.switch_layer"></a>

#### switch\_layer

```python
@classmethod
def switch_layer(cls, layer_name: Name) -> None
```

X.switch_layer(layer_name) -> None
Switch Layer

Args:
    layer_name (Name):

<a id="unreal.AesEditorBlueprintFunctionLibrary.set_road_level_filters"></a>

#### set\_road\_level\_filters

```python
@classmethod
def set_road_level_filters(cls, road_level_filters: Map[int, bool]) -> None
```

X.set_road_level_filters(road_level_filters) -> None
Set Road Level Filters

Args:
    road_level_filters (Map[int32, bool]):

<a id="unreal.AesEditorBlueprintFunctionLibrary.save_changes"></a>

#### save\_changes

```python
@classmethod
def save_changes(cls, need_backup: bool = True) -> None
```

X.save_changes(need_backup=True) -> None
Save Changes

Args:
    need_backup (bool):

<a id="unreal.AesEditorBlueprintFunctionLibrary.save_all"></a>

#### save\_all

```python
@classmethod
def save_all(cls, need_backup: bool = True) -> None
```

X.save_all(need_backup=True) -> None
Save All

Args:
    need_backup (bool):

<a id="unreal.AesEditorBlueprintFunctionLibrary.remove_selected"></a>

#### remove\_selected

```python
@classmethod
def remove_selected(cls) -> None
```

X.remove_selected() -> None
Remove Selected

<a id="unreal.AesEditorBlueprintFunctionLibrary.reimport_model"></a>

#### reimport\_model

```python
@classmethod
def reimport_model(cls, world_context_object: Object, guid: str) -> bool
```

X.reimport_model(world_context_object, guid) -> bool
Reimport Model

Args:
    world_context_object (Object): 
    guid (str): 

Returns:
    bool:

<a id="unreal.AesEditorBlueprintFunctionLibrary.redo"></a>

#### redo

```python
@classmethod
def redo(cls) -> None
```

X.redo() -> None
Redo

<a id="unreal.AesEditorBlueprintFunctionLibrary.load_schemes"></a>

#### load\_schemes

```python
@classmethod
def load_schemes(cls, scheme_folder_path: str) -> Array[str]
```

X.load_schemes(scheme_folder_path) -> Array[str]
Load Schemes

Args:
    scheme_folder_path (str): 

Returns:
    Array[str]:

<a id="unreal.AesEditorBlueprintFunctionLibrary.is_wdp"></a>

#### is\_wdp

```python
@classmethod
def is_wdp(cls) -> bool
```

X.is_wdp() -> bool
Is WDP

Returns:
    bool:

<a id="unreal.AesEditorBlueprintFunctionLibrary.is_valid_name"></a>

#### is\_valid\_name

```python
@classmethod
def is_valid_name(cls, name: str) -> bool
```

X.is_valid_name(name) -> bool
Is Valid Name

Args:
    name (str): 

Returns:
    bool:

<a id="unreal.AesEditorBlueprintFunctionLibrary.inject_embankment_select_action"></a>

#### inject\_embankment\_select\_action

```python
@classmethod
def inject_embankment_select_action(cls) -> None
```

X.inject_embankment_select_action() -> None
Inject Embankment Select Action

<a id="unreal.AesEditorBlueprintFunctionLibrary.inject_building_select_action"></a>

#### inject\_building\_select\_action

```python
@classmethod
def inject_building_select_action(cls) -> None
```

X.inject_building_select_action() -> None
Inject Building Select Action

<a id="unreal.AesEditorBlueprintFunctionLibrary.import_model_by_dialog"></a>

#### import\_model\_by\_dialog

```python
@classmethod
def import_model_by_dialog(cls, world_context_object: Object) -> None
```

X.import_model_by_dialog(world_context_object) -> None
Import Model by Dialog

Args:
    world_context_object (Object):

<a id="unreal.AesEditorBlueprintFunctionLibrary.has_change"></a>

#### has\_change

```python
@classmethod
def has_change(cls) -> bool
```

X.has_change() -> bool
Has Change

Returns:
    bool:

<a id="unreal.AesEditorBlueprintFunctionLibrary.get_texture_size_y"></a>

#### get\_texture\_size\_y

```python
@classmethod
def get_texture_size_y(cls, texture: Texture) -> int
```

X.get_texture_size_y(texture) -> int32
Get Texture Size Y

Args:
    texture (Texture): 

Returns:
    int32:

<a id="unreal.AesEditorBlueprintFunctionLibrary.get_texture_size_x"></a>

#### get\_texture\_size\_x

```python
@classmethod
def get_texture_size_x(cls, texture: Texture) -> int
```

X.get_texture_size_x(texture) -> int32
Get Texture Size X

Args:
    texture (Texture): 

Returns:
    int32:

<a id="unreal.AesEditorBlueprintFunctionLibrary.get_target_srs"></a>

#### get\_target\_srs

```python
@classmethod
def get_target_srs(cls, earth: AesEarth) -> str
```

X.get_target_srs(earth) -> str
Get Target SRS

Args:
    earth (AesEarth): 

Returns:
    str:

<a id="unreal.AesEditorBlueprintFunctionLibrary.get_source_srs"></a>

#### get\_source\_srs

```python
@classmethod
def get_source_srs(cls, earth: AesEarth) -> str
```

X.get_source_srs(earth) -> str
Get Source SRS

Args:
    earth (AesEarth): 

Returns:
    str:

<a id="unreal.AesEditorBlueprintFunctionLibrary.get_road_level_filters"></a>

#### get\_road\_level\_filters

```python
@classmethod
def get_road_level_filters(cls) -> Map[int, bool]
```

X.get_road_level_filters() -> Map[int32, bool]
Get Road Level Filters

Returns:
    Map[int32, bool]:

<a id="unreal.AesEditorBlueprintFunctionLibrary.focus_to_selected"></a>

#### focus\_to\_selected

```python
@classmethod
def focus_to_selected(cls) -> None
```

X.focus_to_selected() -> None
Focus to Selected

<a id="unreal.AesEditorBlueprintFunctionLibrary.focus_to_point"></a>

#### focus\_to\_point

```python
@classmethod
def focus_to_point(cls, world_context: Object, point: Vector) -> None
```

X.focus_to_point(world_context, point) -> None
Focus to Point

Args:
    world_context (Object): 
    point (Vector):

<a id="unreal.AesEditorBlueprintFunctionLibrary.focus_to_actor"></a>

#### focus\_to\_actor

```python
@classmethod
def focus_to_actor(cls, actor: Actor) -> None
```

X.focus_to_actor(actor) -> None
Focus to Actor

Args:
    actor (Actor):

<a id="unreal.AesEditorBlueprintFunctionLibrary.finish_vector_edit_mode"></a>

#### finish\_vector\_edit\_mode

```python
@classmethod
def finish_vector_edit_mode(cls) -> None
```

X.finish_vector_edit_mode() -> None
Finish Vector Edit Mode

<a id="unreal.AesEditorBlueprintFunctionLibrary.enter_vector_edit_mode"></a>

#### enter\_vector\_edit\_mode

```python
@classmethod
def enter_vector_edit_mode(cls) -> None
```

X.enter_vector_edit_mode() -> None
Enter Vector Edit Mode

<a id="unreal.AesEditorBlueprintFunctionLibrary.copy_to_clipboard"></a>

#### copy\_to\_clipboard

```python
@classmethod
def copy_to_clipboard(cls) -> None
```

X.copy_to_clipboard() -> None
Copy to Clipboard

<a id="unreal.AesEditorBlueprintFunctionLibrary.change_model_source"></a>

#### change\_model\_source

```python
@classmethod
def change_model_source(cls, world_context_object: Object, guid: str) -> bool
```

X.change_model_source(world_context_object, guid) -> bool
Change Model Source

Args:
    world_context_object (Object): 
    guid (str): 

Returns:
    bool:

<a id="unreal.AesEditorBlueprintFunctionLibrary.can_undo"></a>

#### can\_undo

```python
@classmethod
def can_undo(cls) -> bool
```

X.can_undo() -> bool
Can Undo

Returns:
    bool:

<a id="unreal.AesEditorBlueprintFunctionLibrary.can_redo"></a>

#### can\_redo

```python
@classmethod
def can_redo(cls) -> bool
```

X.can_redo() -> bool
Can Redo

Returns:
    bool:

<a id="unreal.AesEditorBlueprintFunctionLibrary.cancel_vector_edit_mode"></a>

#### cancel\_vector\_edit\_mode

```python
@classmethod
def cancel_vector_edit_mode(cls) -> None
```

X.cancel_vector_edit_mode() -> None
Cancel Vector Edit Mode

<a id="unreal.AesEditorBlueprintFunctionLibrary.cancel_current_action"></a>

#### cancel\_current\_action

```python
@classmethod
def cancel_current_action(cls) -> None
```

X.cancel_current_action() -> None
Cancel Current Action

<a id="unreal.AesEditorContextMenuItemWidget"></a>