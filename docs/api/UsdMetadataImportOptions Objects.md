## UsdMetadataImportOptions Objects

```python
class UsdMetadataImportOptions(StructBase)
```

Usd Metadata Import Options

**C++ Source:**

- **Plugin**: USDCore
- **Module**: USDClasses
- **File**: USDMetadataImportOptions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blocked_prefix_filters`` (Array[str]):  [Read-Write] When collecting metadata, we will ignore all entries that start with these prefixes.
  Note that you can use the ":" separator for nested dictionaries, so for example using
  "customData:ign" to ignore anything within the "ignoredValues" dictionary inside the
  "customData" dictionary
- ``collect_from_entire_subtrees`` (bool):  [Read-Write] Whether to collect USD metadata from not only a particular prim, but its entire subtree,
  when apropriate. This is useful when used together with collapsing settings, for example.
- ``collect_metadata`` (bool):  [Read-Write] Whether to collect USD prim metadata into AssetUserData objects at all
- ``collect_on_components`` (bool):  [Read-Write] We will always add the collected metadata to AssetUserData objects assigned to all generated assets
  that support them. When this option is enabled, however, we will also separately collect USD prim
  metadata and add that to AssetUserData objects added to every spawned *component*.
  This can be useful for tracking metadata on prims that don't usually generate assets, like simple
  Xforms, cameras, lights, etc., or for collecting metadata for prims with alternative draw modes
  enabled, like bounds or cards: We won't generate the usual assets for those, but the metadata could
  still be collected on the components with this option.
- ``invert_filters`` (bool):  [Read-Write] When this is false (default), the "BlockedPrefixFilters" property describe prefixes to block, and
  metadata entries that match any of those prefixes are ignored and not collected.
  When this is true, the "BlockedPrefixFilters" property is inverted, and describes prefixes to *allow*.
  In that case, entries are only allowed and collected if they match at least one of the provided prefixes.

<a id="unreal.UsdMetadataImportOptions.__init__"></a>

#### __init__

```python
def __init__(collect_metadata: bool = False,
             collect_from_entire_subtrees: bool = False,
             collect_on_components: bool = False,
             blocked_prefix_filters: Array[str] = [],
             invert_filters: bool = False) -> None
```

<a id="unreal.UsdMetadataImportOptions.collect_metadata"></a>

#### collect_metadata

```python
@property
def collect_metadata() -> bool
```

(bool):  [Read-Write] Whether to collect USD prim metadata into AssetUserData objects at all

<a id="unreal.UsdMetadataImportOptions.collect_metadata"></a>

#### collect_metadata

```python
@collect_metadata.setter
def collect_metadata(value: bool) -> None
```

<a id="unreal.UsdMetadataImportOptions.collect_from_entire_subtrees"></a>

#### collect_from_entire_subtrees

```python
@property
def collect_from_entire_subtrees() -> bool
```

(bool):  [Read-Write] Whether to collect USD metadata from not only a particular prim, but its entire subtree,
when apropriate. This is useful when used together with collapsing settings, for example.

<a id="unreal.UsdMetadataImportOptions.collect_from_entire_subtrees"></a>

#### collect_from_entire_subtrees

```python
@collect_from_entire_subtrees.setter
def collect_from_entire_subtrees(value: bool) -> None
```

<a id="unreal.UsdMetadataImportOptions.collect_on_components"></a>

#### collect_on_components

```python
@property
def collect_on_components() -> bool
```

(bool):  [Read-Write] We will always add the collected metadata to AssetUserData objects assigned to all generated assets
that support them. When this option is enabled, however, we will also separately collect USD prim
metadata and add that to AssetUserData objects added to every spawned *component*.
This can be useful for tracking metadata on prims that don't usually generate assets, like simple
Xforms, cameras, lights, etc., or for collecting metadata for prims with alternative draw modes
enabled, like bounds or cards: We won't generate the usual assets for those, but the metadata could
still be collected on the components with this option.

<a id="unreal.UsdMetadataImportOptions.collect_on_components"></a>

#### collect_on_components

```python
@collect_on_components.setter
def collect_on_components(value: bool) -> None
```

<a id="unreal.UsdMetadataImportOptions.blocked_prefix_filters"></a>

#### blocked_prefix_filters

```python
@property
def blocked_prefix_filters() -> Array[str]
```

(Array[str]):  [Read-Write] When collecting metadata, we will ignore all entries that start with these prefixes.
Note that you can use the ":" separator for nested dictionaries, so for example using
"customData:ign" to ignore anything within the "ignoredValues" dictionary inside the
"customData" dictionary

<a id="unreal.UsdMetadataImportOptions.blocked_prefix_filters"></a>

#### blocked_prefix_filters

```python
@blocked_prefix_filters.setter
def blocked_prefix_filters(value: Array[str]) -> None
```

<a id="unreal.UsdMetadataImportOptions.invert_filters"></a>

#### invert_filters

```python
@property
def invert_filters() -> bool
```

(bool):  [Read-Write] When this is false (default), the "BlockedPrefixFilters" property describe prefixes to block, and
metadata entries that match any of those prefixes are ignored and not collected.
When this is true, the "BlockedPrefixFilters" property is inverted, and describes prefixes to *allow*.
In that case, entries are only allowed and collected if they match at least one of the provided prefixes.

<a id="unreal.UsdMetadataImportOptions.invert_filters"></a>

#### invert_filters

```python
@invert_filters.setter
def invert_filters(value: bool) -> None
```

<a id="unreal.UsdStageOptions"></a>