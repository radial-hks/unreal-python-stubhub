## EditorUtilityLibrary Objects

```python
class EditorUtilityLibrary(BlueprintFunctionLibrary)
```

Expose editor utility functions to Blutilities

**C++ Source:**

- **Module**: Blutility
- **File**: EditorUtilityLibrary.h

<a id="unreal.EditorUtilityLibrary.sync_browser_to_folders"></a>

#### sync_browser_to_folders

```python
@classmethod
def sync_browser_to_folders(cls, folder_list: Array[str]) -> None
```

X.sync_browser_to_folders(folder_list) -> None
Sync the Content Browser to the given folder(s)

Args:
    folder_list (Array[str]): The list of folders to sync to in the Content Browser

<a id="unreal.EditorUtilityLibrary.rename_asset"></a>

#### rename_asset

```python
@classmethod
def rename_asset(cls, asset: Object, new_name: str) -> None
```

X.rename_asset(asset, new_name) -> None
Renames an asset (cannot move folders)

Args:
    asset (Object): 
    new_name (str):

<a id="unreal.EditorUtilityLibrary.get_selection_set"></a>

#### get_selection_set

```python
@classmethod
def get_selection_set(cls) -> Array[Actor]
```

X.get_selection_set() -> Array[Actor]
Get Selection Set

Returns:
    Array[Actor]:

<a id="unreal.EditorUtilityLibrary.get_selection_bounds"></a>

#### get_selection_bounds

```python
@classmethod
def get_selection_bounds(cls) -> Tuple[Vector, Vector, float]
```

X.get_selection_bounds() -> (origin=Vector, box_extent=Vector, sphere_radius=float)
Get Selection Bounds

Returns:
    tuple: 

    origin (Vector): 

    box_extent (Vector): 

    sphere_radius (float):

<a id="unreal.EditorUtilityLibrary.get_selected_path_view_folder_paths"></a>

#### get_selected_path_view_folder_paths

```python
@classmethod
def get_selected_path_view_folder_paths(cls) -> Array[str]
```

X.get_selected_path_view_folder_paths() -> Array[str]
Returns the folders that are selected in the path view for the content browser

Returns:
    Array[str]:

<a id="unreal.EditorUtilityLibrary.get_selected_folder_paths"></a>

#### get_selected_folder_paths

```python
@classmethod
def get_selected_folder_paths(cls) -> Array[str]
```

X.get_selected_folder_paths() -> Array[str]
Gets the path to the currently selected folder in the content browser

Returns:
    Array[str]:

<a id="unreal.EditorUtilityLibrary.get_selected_blueprint_classes"></a>

#### get_selected_blueprint_classes

```python
@classmethod
def get_selected_blueprint_classes(cls) -> Array[Class]
```

X.get_selected_blueprint_classes() -> Array[type(Class)]
Gets the set of currently selected classes

Returns:
    Array[type(Class)]:

<a id="unreal.EditorUtilityLibrary.get_selected_assets_of_class"></a>

#### get_selected_assets_of_class

```python
@classmethod
def get_selected_assets_of_class(cls, asset_class: Class) -> Array[Object]
```

X.get_selected_assets_of_class(asset_class) -> Array[Object]
Get Selected Assets Of Class

Args:
    asset_class (type(Class)): 

Returns:
    Array[Object]:

<a id="unreal.EditorUtilityLibrary.get_selected_assets"></a>

#### get_selected_assets

```python
@classmethod
def get_selected_assets(cls) -> Array[Object]
```

X.get_selected_assets() -> Array[Object]
Gets the set of currently selected assets

Returns:
    Array[Object]:

<a id="unreal.EditorUtilityLibrary.get_selected_asset_data"></a>

#### get_selected_asset_data

```python
@classmethod
def get_selected_asset_data(cls) -> Array[AssetData]
```

X.get_selected_asset_data() -> Array[AssetData]
Gets the set of currently selected asset data

Returns:
    Array[AssetData]:

<a id="unreal.EditorUtilityLibrary.get_current_content_browser_path"></a>

#### get_current_content_browser_path

```python
@classmethod
def get_current_content_browser_path(cls) -> Optional[str]
```

X.get_current_content_browser_path() -> str or None
Attempts to get the path for the active content browser, returns false if there is no active content browser
or if it was a virtual path

Returns:
    str or None: Whether a path was successfully returned

    out_path (str): The returned path if successfully found

<a id="unreal.EditorUtilityLibrary.get_current_content_browser_item_path"></a>

#### get_current_content_browser_item_path

```python
@classmethod
def get_current_content_browser_item_path(cls) -> ContentBrowserItemPath
```

X.get_current_content_browser_item_path() -> ContentBrowserItemPath
Gets the current content browser path if one is open, whether it is internal or virtual.

Returns:
    ContentBrowserItemPath:

<a id="unreal.EditorUtilityLibrary.get_actor_reference"></a>

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

<a id="unreal.EditorUtilityLibrary.convert_to_editor_utility_widget"></a>

#### convert_to_editor_utility_widget

```python
@classmethod
def convert_to_editor_utility_widget(cls, widget_bp: WidgetBlueprint) -> None
```

X.convert_to_editor_utility_widget(widget_bp) -> None
Convert to Editor Utility Widget

Args:
    widget_bp (WidgetBlueprint):

<a id="unreal.EditorUtilitySubsystem"></a>