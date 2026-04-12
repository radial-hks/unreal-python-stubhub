## PrimaryAssetTypeInfo Objects

```python
class PrimaryAssetTypeInfo(StructBase)
```

Structure with publicly exposed information about an asset type. These can be loaded out of a config file or constructed at runtime

**C++ Source:**

- **Module**: Engine
- **File**: AssetManagerTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_base_class`` (Class):  [Read-Write] Base Class of all assets of this type
- ``directories`` (Array[DirectoryPath]):  [Read-Write] Directories to search for this asset type
- ``has_blueprint_classes`` (bool):  [Read-Write] True if the assets loaded are blueprints classes, false if they are normal UObjects
- ``is_editor_only`` (bool):  [Read-Write] If true this type will not cause anything to be cooked; the AssetManager will use instances of this type to
  define chunk assignments and NeverCook rules, but will ignore AlwaysCook rules. Assets labeled by instances
  of this type will need to be reference by another PrimaryAsset, or by something outside the AssetManager,
  to be cooked.
- ``primary_asset_type`` (Name):  [Read-Write] The logical name for this type of Primary Asset
- ``rules`` (PrimaryAssetRules):  [Read-Write] Default management rules for this type, individual assets can be overridden
- ``specific_assets`` (Array[SoftObjectPath]):  [Read-Write] Individual assets to scan

<a id="unreal.PrimaryAssetTypeInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.AbilityTriggerData"></a>