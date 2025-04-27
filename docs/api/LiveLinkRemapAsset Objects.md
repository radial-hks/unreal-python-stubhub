## LiveLinkRemapAsset Objects

```python
class LiveLinkRemapAsset(LiveLinkRetargetAsset)
```

Remap asset for data coming from Live Link. Allows simple application of bone transforms into current pose based on name remapping only

**C++ Source:**

- **Module**: LiveLinkAnimationCore
- **File**: LiveLinkRemapAsset.h

<a id="unreal.LiveLinkRemapAsset.remap_curve_elements"></a>

#### remap_curve_elements

```python
def remap_curve_elements(curve_items: Map[Name, float]) -> Map[Name, float]
```

x.remap_curve_elements(curve_items) -> Map[Name, float]
Blueprint Implementable function for remapping, adding or otherwise modifying the curve element data from Live Link. This is run after GetRemappedCurveName

Args:
    curve_items (Map[Name, float]): 

Returns:
    Map[Name, float]: 

    curve_items (Map[Name, float]):

<a id="unreal.LiveLinkRemapAsset.get_remapped_curve_name"></a>

#### get_remapped_curve_name

```python
def get_remapped_curve_name(curve_name: Name) -> Name
```

x.get_remapped_curve_name(curve_name) -> Name
Blueprint Implementable function for getting a remapped curve name from the original

Args:
    curve_name (Name): 

Returns:
    Name:

<a id="unreal.LiveLinkRemapAsset.get_remapped_bone_name"></a>

#### get_remapped_bone_name

```python
def get_remapped_bone_name(bone_name: Name) -> Name
```

x.get_remapped_bone_name(bone_name) -> Name
Blueprint Implementable function for getting a remapped bone name from the original

Args:
    bone_name (Name): 

Returns:
    Name:

<a id="unreal.AnimGraphNode_LiveLinkPose"></a>