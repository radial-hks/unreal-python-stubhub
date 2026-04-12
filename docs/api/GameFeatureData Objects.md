## GameFeatureData Objects

```python
class GameFeatureData(PrimaryDataAsset)
```

Data related to a game feature, a collection of code and content that adds a separable discrete feature to the game

**C++ Source:**

- **Plugin**: GameFeatures
- **Module**: GameFeatures
- **File**: GameFeatureData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actions`` (Array[GameFeatureAction]):  [Read-Write] List of actions to perform as this game feature is loaded/activated/deactivated/unloaded
- ``primary_asset_types_to_scan`` (Array[PrimaryAssetTypeInfo]):  [Read-Write] List of asset types to scan at startup

<a id="unreal.GameFeatureData.get_plugin_name"></a>

#### get\_plugin\_name

```python
@classmethod
def get_plugin_name(cls, gfd: GameFeatureData) -> str
```

X.get_plugin_name(gfd) -> str
Get Plugin Name

Args:
    gfd (GameFeatureData): 

Returns:
    str: 

    plugin_name (str):

<a id="unreal.AbilitySystemDebugHUD"></a>