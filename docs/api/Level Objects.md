## Level Objects

```python
class Level(Object)
```

A Level is a collection of Actors (lights, volumes, mesh instances etc.).
Multiple Levels can be loaded and unloaded into the World to create a streaming experience.
see: https://docs.unrealengine.com/latest/INT/Engine/Levels
see: UActor

**C++ Source:**

- **Module**: Engine
- **File**: Level.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``lightmap_total_size`` (float):  [Read-Only] Total number of KB used for lightmap textures in the level.
- ``shadowmap_total_size`` (float):  [Read-Only] Total number of KB used for shadowmap textures in the level.
- ``use_actor_folders`` (bool):  [Read-Write] Use actor folder objects, actor folders of this level will be persistent in their own object.
- ``use_external_actors`` (bool):  [Read-Write] Use external actors, new actor spawned in this level will be external and existing external actors will be loaded on load.

<a id="unreal.Level.has_asset_user_data_of_class"></a>

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

<a id="unreal.Level.get_asset_user_data_of_class"></a>

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

<a id="unreal.Level.add_asset_user_data_of_class"></a>

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

<a id="unreal.TextureCollection"></a>