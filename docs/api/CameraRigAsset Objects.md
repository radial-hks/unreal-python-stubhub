## CameraRigAsset Objects

```python
class CameraRigAsset(Object)
```

A camera rig asset, which runs a hierarchy of camera nodes to drive
the behavior of a camera.

**C++ Source:**

- **Plugin**: GameplayCameras
- **Module**: GameplayCameras
- **File**: CameraRigAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``gameplay_tags`` (GameplayTagContainer):  [Read-Write] The gameplay tags on this camera rig.
- ``initial_orientation`` (CameraRigInitialOrientation):  [Read-Write] Default orientation initialization when this camera rig is activated.

<a id="unreal.CameraRigAsset.has_matching_gameplay_tag"></a>

#### has_matching_gameplay_tag

```python
def has_matching_gameplay_tag(tag_to_check: GameplayTag) -> bool
```

x.has_matching_gameplay_tag(tag_to_check) -> bool
Check if the asset has a gameplay tag that matches against the specified tag (expands to include parents of asset tags)

Args:
    tag_to_check (GameplayTag): Tag to check for a match

Returns:
    bool: True if the asset has a gameplay tag that matches, false if not

<a id="unreal.CameraRigAsset.has_any_matching_gameplay_tags"></a>

#### has_any_matching_gameplay_tags

```python
def has_any_matching_gameplay_tags(
        tag_container: GameplayTagContainer) -> bool
```

x.has_any_matching_gameplay_tags(tag_container) -> bool
Check if the asset has gameplay tags that matches against any of the specified tags (expands to include parents of asset tags)

Args:
    tag_container (GameplayTagContainer): Tag container to check for a match

Returns:
    bool: True if the asset has matches any of the gameplay tags, will be false if container is empty

<a id="unreal.CameraRigAsset.has_all_matching_gameplay_tags"></a>

#### has_all_matching_gameplay_tags

```python
def has_all_matching_gameplay_tags(
        tag_container: GameplayTagContainer) -> bool
```

x.has_all_matching_gameplay_tags(tag_container) -> bool
Check if the asset has gameplay tags that matches against all of the specified tags (expands to include parents of asset tags)

Args:
    tag_container (GameplayTagContainer): Tag container to check for a match

Returns:
    bool: True if the asset has matches all of the gameplay tags, will be true if container is empty

<a id="unreal.MVVMBlueprintViewConversionFunction"></a>