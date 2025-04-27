## PrimaryAssetLabel Objects

```python
class PrimaryAssetLabel(PrimaryDataAsset)
```

A seed file that is created to mark referenced assets as part of this primary asset

**C++ Source:**

- **Module**: Engine
- **File**: PrimaryAssetLabel.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_collection`` (CollectionReference):  [Read-Write] Collection to load asset references out of
- ``explicit_assets`` (Array[Object]):  [Read-Write] List of manually specified assets to label
- ``explicit_blueprints`` (Array[Class]):  [Read-Write] List of manually specified blueprint assets to label
- ``include_redirectors`` (bool):  [Read-Write] If true, redirectors found by the AssetLabel's explicit assets or directory will be labeled. If false, redirectors will be skipped.
- ``is_runtime_label`` (bool):  [Read-Write] Set to true if the label asset itself should be cooked and available at runtime. This does not affect the assets that are labeled, they are set with cook rule
- ``label_assets_in_my_directory`` (bool):  [Read-Write] True to Label everything in this directory and sub directories
- ``rules`` (PrimaryAssetRules):  [Read-Write] Management rules for this specific asset, if set it will override the type rules

<a id="unreal.HealthSnapshotBlueprintLibrary"></a>