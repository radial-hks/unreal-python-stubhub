## PluginBlueprintLibrary Objects

```python
class PluginBlueprintLibrary(BlueprintFunctionLibrary)
```

A function library of utilities for querying information about plugins.

**C++ Source:**

- **Module**: Engine
- **File**: PluginBlueprintLibrary.h

<a id="unreal.PluginBlueprintLibrary.is_plugin_mounted"></a>

#### is_plugin_mounted

```python
@classmethod
def is_plugin_mounted(cls, plugin_name: str) -> bool
```

X.is_plugin_mounted(plugin_name) -> bool
Determine whether a plugin is mounted.

Args:
    plugin_name (str): Name of the plugin

Returns:
    bool: true if the named plugin is mounted, or false otherwise

<a id="unreal.PluginBlueprintLibrary.get_plugin_version_name"></a>

#### get_plugin_version_name

```python
@classmethod
def get_plugin_version_name(cls, plugin_name: str) -> Optional[str]
```

X.get_plugin_version_name(plugin_name) -> str or None
Get the version name of a plugin.

Args:
    plugin_name (str): Name of the plugin

Returns:
    str or None: true if the named plugin was found and the plugin's version name was stored in OutVersionName, or false otherwise

    out_version_name (str): Version name of the plugin, if found

<a id="unreal.PluginBlueprintLibrary.get_plugin_version"></a>

#### get_plugin_version

```python
@classmethod
def get_plugin_version(cls, plugin_name: str) -> Optional[int]
```

X.get_plugin_version(plugin_name) -> int32 or None
Get the version number of a plugin.

Args:
    plugin_name (str): Name of the plugin

Returns:
    int32 or None: true if the named plugin was found and the plugin's version number was stored in OutVersion, or false otherwise

    out_version (int32): Version number of the plugin, if found

<a id="unreal.PluginBlueprintLibrary.get_plugin_name_for_object_path"></a>

#### get_plugin_name_for_object_path

```python
@classmethod
def get_plugin_name_for_object_path(
        cls, object_path: SoftObjectPath) -> Optional[str]
```

X.get_plugin_name_for_object_path(object_path) -> str or None
Get the name of the plugin containing an object.

Args:
    object_path (SoftObjectPath): Path to the object

Returns:
    str or None: true if the object is contained within a plugin and the plugin name was stored in OutPluginName, or false otherwise

    out_plugin_name (str): Name of the plugin containing the object, if found

<a id="unreal.PluginBlueprintLibrary.get_plugin_mounted_asset_path"></a>

#### get_plugin_mounted_asset_path

```python
@classmethod
def get_plugin_mounted_asset_path(cls, plugin_name: str) -> Optional[str]
```

X.get_plugin_mounted_asset_path(plugin_name) -> str or None
Get the virtual root path for assets in a plugin.

Args:
    plugin_name (str): Name of the plugin

Returns:
    str or None: true if the named plugin was found and the plugin's virtual root path was stored in OutAssetPath, or false otherwise

    out_asset_path (str): Virtual root path for the plugin's assets, if found

<a id="unreal.PluginBlueprintLibrary.get_plugin_editor_custom_virtual_path"></a>

#### get_plugin_editor_custom_virtual_path

```python
@classmethod
def get_plugin_editor_custom_virtual_path(cls,
                                          plugin_name: str) -> Optional[str]
```

X.get_plugin_editor_custom_virtual_path(plugin_name) -> str or None
Get the editor custom virtual path of a plugin.

Args:
    plugin_name (str): Name of the plugin

Returns:
    str or None: true if the named plugin was found and the plugin's editor custom virtual path was stored in OutVirtualPath, or false otherwise

    out_virtual_path (str): Editor custom virtual path of the plugin, if found

<a id="unreal.PluginBlueprintLibrary.get_plugin_descriptor_file_path"></a>

#### get_plugin_descriptor_file_path

```python
@classmethod
def get_plugin_descriptor_file_path(cls, plugin_name: str) -> Optional[str]
```

X.get_plugin_descriptor_file_path(plugin_name) -> str or None
Get the filesystem path to a plugin's descriptor.

Args:
    plugin_name (str): Name of the plugin

Returns:
    str or None: true if the named plugin was found and the plugin descriptor filesystem path was stored in OutFilePath, or false otherwise

    out_file_path (str): Filesystem path to the plugin's descriptor, if found

<a id="unreal.PluginBlueprintLibrary.get_plugin_description"></a>

#### get_plugin_description

```python
@classmethod
def get_plugin_description(cls, plugin_name: str) -> Optional[str]
```

X.get_plugin_description(plugin_name) -> str or None
Get the description of a plugin.

Args:
    plugin_name (str): Name of the plugin

Returns:
    str or None: true if the named plugin was found and the plugin's description was stored in OutDescription, or false otherwise

    out_description (str): Description of the plugin, if found

<a id="unreal.PluginBlueprintLibrary.get_plugin_content_dir"></a>

#### get_plugin_content_dir

```python
@classmethod
def get_plugin_content_dir(cls, plugin_name: str) -> Optional[str]
```

X.get_plugin_content_dir(plugin_name) -> str or None
Get the filesystem path to a plugin's content directory.

Args:
    plugin_name (str): Name of the plugin

Returns:
    str or None: true if the named plugin was found and the plugin content directory filesystem path was stored in OutContentDir, or false otherwise

    out_content_dir (str): Filesystem path to the plugin's content directory, if found

<a id="unreal.PluginBlueprintLibrary.get_plugin_base_dir"></a>

#### get_plugin_base_dir

```python
@classmethod
def get_plugin_base_dir(cls, plugin_name: str) -> Optional[str]
```

X.get_plugin_base_dir(plugin_name) -> str or None
Get the filesystem path to a plugin's base directory.

Args:
    plugin_name (str): Name of the plugin

Returns:
    str or None: true if the named plugin was found and the plugin base directory filesystem path was stored in OutBaseDir, or false otherwise

    out_base_dir (str): Filesystem path to the plugin's base directory, if found

<a id="unreal.PluginBlueprintLibrary.get_enabled_plugin_names"></a>

#### get_enabled_plugin_names

```python
@classmethod
def get_enabled_plugin_names(cls) -> Array[str]
```

X.get_enabled_plugin_names() -> Array[str]
Get the names of all enabled plugins.

Returns:
    Array[str]: The names of all enabled plugins.

<a id="unreal.PluginBlueprintLibrary.get_additional_project_plugin_search_paths"></a>

#### get_additional_project_plugin_search_paths

```python
@classmethod
def get_additional_project_plugin_search_paths(cls) -> Array[str]
```

X.get_additional_project_plugin_search_paths() -> Array[str]
Get the list of extra directories added by the project that are
recursively searched for plugins.

Returns:
    Array[str]: The additional project filesystem plugin search paths.

<a id="unreal.PluginBlueprintLibrary.get_additional_plugin_search_paths"></a>

#### get_additional_plugin_search_paths

```python
@classmethod
def get_additional_plugin_search_paths(cls) -> Array[str]
```

X.get_additional_plugin_search_paths() -> Array[str]
Get the list of extra directories that are recursively searched for
plugins (aside from the engine and project plugin directories).

Returns:
    Array[str]: The additional filesystem plugin search paths.

<a id="unreal.PointLight"></a>