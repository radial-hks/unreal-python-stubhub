## EditorLoadingAndSavingUtils Objects

```python
class EditorLoadingAndSavingUtils(Object)
```

This class is a wrapper for editor loading and saving functionality
It is meant to contain only functions that can be executed in script (but are also allowed in C++).
It is separated from FEditorFileUtils to ensure new easier to use methods can be created without breaking FEditorFileUtils backwards compatibility
However this should be used in place of FEditorFileUtils wherever possible as the goal is to deprecate FEditorFileUtils eventually

**C++ Source:**

- **Module**: UnrealEd
- **File**: FileHelpers.h

<a id="unreal.EditorLoadingAndSavingUtils.unload_packages"></a>

#### unload_packages

```python
@classmethod
def unload_packages(cls,
                    packages_to_unload: Array[Package]) -> Tuple[bool, Text]
```

X.unload_packages(packages_to_unload) -> (out_any_packages_unloaded=bool, out_error_message=Text)
Unloads a list of packages

Args:
    packages_to_unload (Array[Package]): Array of packages to unload.

Returns:
    tuple: 

    out_any_packages_unloaded (bool): 

    out_error_message (Text):

<a id="unreal.EditorLoadingAndSavingUtils.save_packages_with_dialog"></a>

#### save_packages_with_dialog

```python
@classmethod
def save_packages_with_dialog(cls, packages_to_save: Array[Package],
                              only_dirty: bool) -> bool
```

X.save_packages_with_dialog(packages_to_save, only_dirty) -> bool
Save all packages. Optionally prompting the user to select which packages to save.
Prompt the user to select which dirty packages to save and check them out from source control (if enabled).

Args:
    packages_to_save (Array[Package]): The list of packages to save.  Both map and content packages are supported
    only_dirty (bool): 

Returns:
    bool: true on success, false on fail.

<a id="unreal.EditorLoadingAndSavingUtils.save_packages"></a>

#### save_packages

```python
@classmethod
def save_packages(cls, packages_to_save: Array[Package],
                  only_dirty: bool) -> bool
```

X.save_packages(packages_to_save, only_dirty) -> bool
Save all packages.
Assume all dirty packages should be saved and check out from source control (if enabled).

Args:
    packages_to_save (Array[Package]): The list of packages to save.  Both map and content packages are supported
    only_dirty (bool): 

Returns:
    bool: true on success, false on fail.

<a id="unreal.EditorLoadingAndSavingUtils.save_map"></a>

#### save_map

```python
@classmethod
def save_map(cls, world: World, asset_path: str) -> bool
```

X.save_map(world, asset_path) -> bool
Saves the specified map, returning true on success.

Args:
    world (World): The world to save.
    asset_path (str): The valid content directory path and name for the asset.  E.g "/Game/MyMap"

Returns:
    bool: true if the map was saved successfully.

<a id="unreal.EditorLoadingAndSavingUtils.save_dirty_packages_with_dialog"></a>

#### save_dirty_packages_with_dialog

```python
@classmethod
def save_dirty_packages_with_dialog(cls, save_map_packages: bool,
                                    save_content_packages: bool) -> bool
```

X.save_dirty_packages_with_dialog(save_map_packages, save_content_packages) -> bool
Looks at all currently loaded packages and saves them if their "bDirty" flag is set.
Prompt the user to select which dirty packages to save and check them out from source control (if enabled).

Args:
    save_map_packages (bool): true if map packages should be saved
    save_content_packages (bool): true if we should save content packages.

Returns:
    bool: true on success, false on fail.

<a id="unreal.EditorLoadingAndSavingUtils.save_dirty_packages"></a>

#### save_dirty_packages

```python
@classmethod
def save_dirty_packages(cls, save_map_packages: bool,
                        save_content_packages: bool) -> bool
```

X.save_dirty_packages(save_map_packages, save_content_packages) -> bool
Looks at all currently loaded packages and saves them if their "bDirty" flag is set.
Assume all dirty packages should be saved and check out from source control (if enabled).

Args:
    save_map_packages (bool): true if map packages should be saved
    save_content_packages (bool): true if we should save content packages.

Returns:
    bool: true on success, false on fail.

<a id="unreal.EditorLoadingAndSavingUtils.save_current_level"></a>

#### save_current_level

```python
@classmethod
def save_current_level(cls) -> bool
```

X.save_current_level() -> bool
Saves the active level, prompting the use for checkout if necessary.

Returns:
    bool: true on success, False on fail

<a id="unreal.EditorLoadingAndSavingUtils.reload_packages"></a>

#### reload_packages

```python
@classmethod
def reload_packages(
    cls,
    packages_to_reload: Array[Package],
    interaction_mode:
    ReloadPackagesInteractionMode = ReloadPackagesInteractionMode.INTERACTIVE
) -> Tuple[bool, Text]
```

X.reload_packages(packages_to_reload, interaction_mode=ReloadPackagesInteractionMode.INTERACTIVE) -> (out_any_packages_reloaded=bool, out_error_message=Text)
Helper function that attempts to reload the specified top-level packages.

Args:
    packages_to_reload (Array[Package]): The list of packages that should be reloaded
    interaction_mode (ReloadPackagesInteractionMode): Whether the function is allowed to ask the user questions (such as whether to reload dirty packages)

Returns:
    tuple: 

    out_any_packages_reloaded (bool): True if the set of loaded packages was changed

    out_error_message (Text): An error message specifying any problems with reloading packages

<a id="unreal.EditorLoadingAndSavingUtils.new_map_from_template"></a>

#### new_map_from_template

```python
@classmethod
def new_map_from_template(cls, path_to_template_level: str,
                          save_existing_map: bool) -> World
```

X.new_map_from_template(path_to_template_level, save_existing_map) -> World
New Map from Template

Args:
    path_to_template_level (str): 
    save_existing_map (bool): 

Returns:
    World:

<a id="unreal.EditorLoadingAndSavingUtils.new_blank_map"></a>

#### new_blank_map

```python
@classmethod
def new_blank_map(cls, save_existing_map: bool) -> World
```

X.new_blank_map(save_existing_map) -> World
New Blank Map

Args:
    save_existing_map (bool): 

Returns:
    World:

<a id="unreal.EditorLoadingAndSavingUtils.load_map_with_dialog"></a>

#### load_map_with_dialog

```python
@classmethod
def load_map_with_dialog(cls) -> World
```

X.load_map_with_dialog() -> World
Prompts the user to save the current map if necessary, the presents a load dialog and
loads a new map if selected by the user.

Returns:
    World:

<a id="unreal.EditorLoadingAndSavingUtils.load_map"></a>

#### load_map

```python
@classmethod
def load_map(cls, filename: str) -> World
```

X.load_map(filename) -> World
Loads the specified map.  Does not prompt the user to save the current map.

Args:
    filename (str): Level package filename, including path.

Returns:
    World: true if the map was loaded successfully.

<a id="unreal.EditorLoadingAndSavingUtils.import_scene"></a>

#### import_scene

```python
@classmethod
def import_scene(cls, filename: str) -> None
```

X.import_scene(filename) -> None
Imports a file such as (FBX or obj) and spawns actors f into the current level

Args:
    filename (str):

<a id="unreal.EditorLoadingAndSavingUtils.get_dirty_map_packages"></a>

#### get_dirty_map_packages

```python
@classmethod
def get_dirty_map_packages(cls) -> Array[Package]
```

X.get_dirty_map_packages() -> Array[Package]
Appends array with all currently dirty map packages.

Returns:
    Array[Package]: 

    out_dirty_packages (Array[Package]): Array to append dirty packages to.

<a id="unreal.EditorLoadingAndSavingUtils.get_dirty_content_packages"></a>

#### get_dirty_content_packages

```python
@classmethod
def get_dirty_content_packages(cls) -> Array[Package]
```

X.get_dirty_content_packages() -> Array[Package]
Appends array with all currently dirty content packages.

Returns:
    Array[Package]: 

    out_dirty_packages (Array[Package]): Array to append dirty packages to.

<a id="unreal.EditorLoadingAndSavingUtils.export_scene"></a>

#### export_scene

```python
@classmethod
def export_scene(cls, export_selected_actors_only: bool) -> None
```

X.export_scene(export_selected_actors_only) -> None
Exports the current scene

Args:
    export_selected_actors_only (bool):

<a id="unreal.FontFactory"></a>