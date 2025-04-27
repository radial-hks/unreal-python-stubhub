## AssetManagerSearchRules Objects

```python
class AssetManagerSearchRules(StructBase)
```

Rules for how to scan the asset registry for assets matching path and type descriptions

**C++ Source:**

- **Module**: Engine
- **File**: AssetManagerTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_base_class`` (type(Class)):  [Read-Write] Assets must inherit from this class, for blueprints this should be the instance base class
- ``asset_scan_paths`` (Array[str]):  [Read-Write] List of top-level directories and specific assets to search, must be paths starting with /, directories should not have a trailing /
- ``exclude_patterns`` (Array[str]):  [Read-Write] Optional list of exclude wildcard patterns that can use *, if any of these match it will be excluded
- ``force_synchronous_scan`` (bool):  [Read-Write] True if this should force a synchronous scan of the disk even if an async scan is in progress
- ``has_blueprint_classes`` (bool):  [Read-Write] True if scanning for blueprints, false for all other assets
- ``include_patterns`` (Array[str]):  [Read-Write] Optional list of include wildcard patterns using * that will get matched against full package path. If there are any at least one of these must match
- ``skip_manager_include_check`` (bool):  [Read-Write] True if this test should skip the ShouldIncludeInAssetSearch function on AssetManager
- ``skip_virtual_path_expansion`` (bool):  [Read-Write] True if AssetScanPaths are real paths that do not need expansion

<a id="unreal.AssetManagerSearchRules.__init__"></a>

#### __init__

```python
def __init__(asset_scan_paths: Array[str] = [],
             include_patterns: Array[str] = [],
             exclude_patterns: Array[str] = [],
             asset_base_class: Class = None,
             has_blueprint_classes: bool = False,
             force_synchronous_scan: bool = False,
             skip_virtual_path_expansion: bool = False,
             skip_manager_include_check: bool = False) -> None
```

<a id="unreal.AssetManagerSearchRules.asset_scan_paths"></a>

#### asset_scan_paths

```python
@property
def asset_scan_paths() -> Array[str]
```

(Array[str]):  [Read-Write] List of top-level directories and specific assets to search, must be paths starting with /, directories should not have a trailing /

<a id="unreal.AssetManagerSearchRules.asset_scan_paths"></a>

#### asset_scan_paths

```python
@asset_scan_paths.setter
def asset_scan_paths(value: Array[str]) -> None
```

<a id="unreal.AssetManagerSearchRules.include_patterns"></a>

#### include_patterns

```python
@property
def include_patterns() -> Array[str]
```

(Array[str]):  [Read-Write] Optional list of include wildcard patterns using * that will get matched against full package path. If there are any at least one of these must match

<a id="unreal.AssetManagerSearchRules.include_patterns"></a>

#### include_patterns

```python
@include_patterns.setter
def include_patterns(value: Array[str]) -> None
```

<a id="unreal.AssetManagerSearchRules.exclude_patterns"></a>

#### exclude_patterns

```python
@property
def exclude_patterns() -> Array[str]
```

(Array[str]):  [Read-Write] Optional list of exclude wildcard patterns that can use *, if any of these match it will be excluded

<a id="unreal.AssetManagerSearchRules.exclude_patterns"></a>

#### exclude_patterns

```python
@exclude_patterns.setter
def exclude_patterns(value: Array[str]) -> None
```

<a id="unreal.AssetManagerSearchRules.asset_base_class"></a>

#### asset_base_class

```python
@property
def asset_base_class() -> Class
```

(type(Class)):  [Read-Write] Assets must inherit from this class, for blueprints this should be the instance base class

<a id="unreal.AssetManagerSearchRules.asset_base_class"></a>

#### asset_base_class

```python
@asset_base_class.setter
def asset_base_class(value: Class) -> None
```

<a id="unreal.AssetManagerSearchRules.has_blueprint_classes"></a>

#### has_blueprint_classes

```python
@property
def has_blueprint_classes() -> bool
```

(bool):  [Read-Write] True if scanning for blueprints, false for all other assets

<a id="unreal.AssetManagerSearchRules.has_blueprint_classes"></a>

#### has_blueprint_classes

```python
@has_blueprint_classes.setter
def has_blueprint_classes(value: bool) -> None
```

<a id="unreal.AssetManagerSearchRules.force_synchronous_scan"></a>

#### force_synchronous_scan

```python
@property
def force_synchronous_scan() -> bool
```

(bool):  [Read-Write] True if this should force a synchronous scan of the disk even if an async scan is in progress

<a id="unreal.AssetManagerSearchRules.force_synchronous_scan"></a>

#### force_synchronous_scan

```python
@force_synchronous_scan.setter
def force_synchronous_scan(value: bool) -> None
```

<a id="unreal.AssetManagerSearchRules.skip_virtual_path_expansion"></a>

#### skip_virtual_path_expansion

```python
@property
def skip_virtual_path_expansion() -> bool
```

(bool):  [Read-Write] True if AssetScanPaths are real paths that do not need expansion

<a id="unreal.AssetManagerSearchRules.skip_virtual_path_expansion"></a>

#### skip_virtual_path_expansion

```python
@skip_virtual_path_expansion.setter
def skip_virtual_path_expansion(value: bool) -> None
```

<a id="unreal.AssetManagerSearchRules.skip_manager_include_check"></a>

#### skip_manager_include_check

```python
@property
def skip_manager_include_check() -> bool
```

(bool):  [Read-Write] True if this test should skip the ShouldIncludeInAssetSearch function on AssetManager

<a id="unreal.AssetManagerSearchRules.skip_manager_include_check"></a>

#### skip_manager_include_check

```python
@skip_manager_include_check.setter
def skip_manager_include_check(value: bool) -> None
```

<a id="unreal.AudioVolumeSubmixSendSettings"></a>