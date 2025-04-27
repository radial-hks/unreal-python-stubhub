## DatasmithScene Objects

```python
class DatasmithScene(Object)
```

Datasmith Scene

**C++ Source:**

- **Plugin**: DatasmithContent
- **Module**: DatasmithContent
- **File**: DatasmithScene.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_import_data`` (DatasmithSceneImportData):  [Read-Write] Importing data and options used for this Datasmith scene
- ``clothes`` (Map[Name, Object]):  [Read-Only]
- ``level_sequences`` (Map[Name, LevelSequence]):  [Read-Only] Map of all the level sequences related to this Datasmith Scene
- ``level_variant_sets`` (Map[Name, LevelVariantSets]):  [Read-Only] Map of all the level variant sets related to this Datasmith Scene
- ``material_functions`` (Map[Name, MaterialFunction]):  [Read-Only] Map of all the material functions related to this Datasmith Scene
- ``materials`` (Map[Name, MaterialInterface]):  [Read-Only] Map of all the materials related to this Datasmith Scene
- ``static_meshes`` (Map[Name, StaticMesh]):  [Read-Only] Map of all the static meshes related to this Datasmith Scene
- ``textures`` (Map[Name, Texture]):  [Read-Only] Map of all the textures related to this Datasmith Scene

<a id="unreal.DatasmithScene.has_asset_user_data_of_class"></a>

#### has_asset_user_data_of_class

```python
def has_asset_user_data_of_class(user_data_class: Class) -> bool
```

x.has_asset_user_data_of_class(user_data_class) -> bool
Checks whether or not an instance of the provided AssetUserData class is contained.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to check for

Returns:
    bool: Whether or not an instance of InUserDataClass was found

<a id="unreal.DatasmithScene.get_asset_user_data_of_class"></a>

#### get_asset_user_data_of_class

```python
def get_asset_user_data_of_class(user_data_class: Class) -> AssetUserData
```

x.get_asset_user_data_of_class(user_data_class) -> AssetUserData
Returns an instance of the provided AssetUserData class if it's contained in the target asset.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to get

Returns:
    AssetUserData: The instance of the UAssetUserData class contained, or null if it doesn't exist

<a id="unreal.DatasmithScene.add_asset_user_data_of_class"></a>

#### add_asset_user_data_of_class

```python
def add_asset_user_data_of_class(user_data_class: Class) -> bool
```

x.add_asset_user_data_of_class(user_data_class) -> bool
Creates and adds an instance of the provided AssetUserData class to the target asset.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to create

Returns:
    bool: Whether or not an instance of InUserDataClass was succesfully added

<a id="unreal.GeometryCacheCodecBase"></a>