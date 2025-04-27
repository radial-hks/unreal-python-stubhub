## LevelSequence Objects

```python
class LevelSequence(MovieSceneSequence)
```

Movie scene animation for Actors.

**C++ Source:**

- **Module**: LevelSequence
- **File**: LevelSequence.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset

<a id="unreal.LevelSequence.remove_meta_data_by_class"></a>

#### remove_meta_data_by_class

```python
def remove_meta_data_by_class(class_: Class) -> None
```

x.remove_meta_data_by_class(class_) -> None
Remove meta-data of a particular type for this level sequence instance, if it exists

Args:
    class_ (type(Class)): The class type that you wish to remove the metadata for

<a id="unreal.LevelSequence.find_or_add_meta_data_by_class"></a>

#### find_or_add_meta_data_by_class

```python
def find_or_add_meta_data_by_class(class_: Class) -> Object
```

x.find_or_add_meta_data_by_class(class_) -> Object
Find meta-data of a particular type for this level sequence instance, adding it if it doesn't already exist.

Args:
    class_ (type(Class)): Class that you wish to find or create the metadata object for.

Returns:
    Object: An instance of this class as metadata on this Level Sequence.

<a id="unreal.LevelSequence.find_meta_data_by_class"></a>

#### find_meta_data_by_class

```python
def find_meta_data_by_class(class_: Class) -> Object
```

x.find_meta_data_by_class(class_) -> Object
Find meta-data of a particular type for this level sequence instance.

Args:
    class_ (type(Class)): Class that you wish to find the metadata object for.

Returns:
    Object: An instance of this class if it already exists as metadata on this Level Sequence, otherwise null.

<a id="unreal.LevelSequence.copy_meta_data"></a>

#### copy_meta_data

```python
def copy_meta_data(meta_data: Object) -> Object
```

x.copy_meta_data(meta_data) -> Object
Copy the specified meta data into this level sequence, overwriting any existing meta-data of the same type
Meta-data may implement the ILevelSequenceMetaData interface in order to hook into default ULevelSequence functionality.

Args:
    meta_data (Object): Existing Metadata Object that you wish to copy into this Level Sequence.

Returns:
    Object: The newly copied instance of the Metadata that now exists on this sequence.

<a id="unreal.LevelSequence.has_asset_user_data_of_class"></a>

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

<a id="unreal.LevelSequence.get_asset_user_data_of_class"></a>

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

<a id="unreal.LevelSequence.add_asset_user_data_of_class"></a>

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

<a id="unreal.LevelSequenceBurnInInitSettings"></a>