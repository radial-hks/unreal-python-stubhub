## MultiAnimAsset Objects

```python
class MultiAnimAsset(Object)
```

UObject defining tuples of UAnimationAsset(s) with associated Role(s) and relative transforms from a shared reference system via GetOrigin

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: MultiAnimAsset.h

<a id="unreal.MultiAnimAsset.bp_get_origin"></a>

#### bp_get_origin

```python
def bp_get_origin(role: Name) -> Transform
```

x.bp_get_origin(role) -> Transform
BP Get Origin

Args:
    role (Name): 

Returns:
    Transform:

<a id="unreal.MultiAnimAsset.bp_get_animation_asset"></a>

#### bp_get_animation_asset

```python
def bp_get_animation_asset(role: Name) -> AnimationAsset
```

x.bp_get_animation_asset(role) -> AnimationAsset
BP Get Animation Asset

Args:
    role (Name): 

Returns:
    AnimationAsset:

<a id="unreal.PoseSearchAssetSamplerLibrary"></a>