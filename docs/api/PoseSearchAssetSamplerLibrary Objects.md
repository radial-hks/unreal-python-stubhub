## PoseSearchAssetSamplerLibrary Objects

```python
class PoseSearchAssetSamplerLibrary(BlueprintFunctionLibrary)
```

Pose Search Asset Sampler Library

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchAssetSamplerLibrary.h

<a id="unreal.PoseSearchAssetSamplerLibrary.sample_pose"></a>

#### sample_pose

```python
@classmethod
def sample_pose(
        cls, anim_instance: AnimInstance,
        input: PoseSearchAssetSamplerInput) -> PoseSearchAssetSamplerPose
```

X.sample_pose(anim_instance, input) -> PoseSearchAssetSamplerPose
Sample Pose

Args:
    anim_instance (AnimInstance): 
    input (PoseSearchAssetSamplerInput): 

Returns:
    PoseSearchAssetSamplerPose:

<a id="unreal.PoseSearchAssetSamplerLibrary.get_transform_by_name"></a>

#### get_transform_by_name

```python
@classmethod
def get_transform_by_name(
    cls,
    asset_sampler_pose: PoseSearchAssetSamplerPose,
    bone_name: Name,
    space: PoseSearchAssetSamplerSpace = PoseSearchAssetSamplerSpace.WORLD
) -> Tuple[Transform, PoseSearchAssetSamplerPose]
```

X.get_transform_by_name(asset_sampler_pose, bone_name, space=PoseSearchAssetSamplerSpace.WORLD) -> (Transform, asset_sampler_pose=PoseSearchAssetSamplerPose)
Get Transform by Name

Args:
    asset_sampler_pose (PoseSearchAssetSamplerPose): 
    bone_name (Name): 
    space (PoseSearchAssetSamplerSpace): 

Returns:
    PoseSearchAssetSamplerPose: 

    asset_sampler_pose (PoseSearchAssetSamplerPose):

<a id="unreal.PoseSearchAssetSamplerLibrary.get_transform"></a>

#### get_transform

```python
@classmethod
def get_transform(
    cls,
    asset_sampler_pose: PoseSearchAssetSamplerPose,
    bone_index: int = -1,
    space: PoseSearchAssetSamplerSpace = PoseSearchAssetSamplerSpace.WORLD
) -> Tuple[Transform, PoseSearchAssetSamplerPose]
```

X.get_transform(asset_sampler_pose, bone_index=-1, space=PoseSearchAssetSamplerSpace.WORLD) -> (Transform, asset_sampler_pose=PoseSearchAssetSamplerPose)
Get Transform

Args:
    asset_sampler_pose (PoseSearchAssetSamplerPose): 
    bone_index (int32): 
    space (PoseSearchAssetSamplerSpace): 

Returns:
    PoseSearchAssetSamplerPose: 

    asset_sampler_pose (PoseSearchAssetSamplerPose):

<a id="unreal.PoseSearchAssetSamplerLibrary.draw"></a>

#### draw

```python
@classmethod
def draw(
    cls, anim_instance: AnimInstance,
    asset_sampler_pose: PoseSearchAssetSamplerPose
) -> PoseSearchAssetSamplerPose
```

X.draw(anim_instance, asset_sampler_pose) -> PoseSearchAssetSamplerPose

todo:: it'd be nice if it was threadsafe...

Args:
    anim_instance (AnimInstance): 
    asset_sampler_pose (PoseSearchAssetSamplerPose): 

Returns:
    PoseSearchAssetSamplerPose: 

    asset_sampler_pose (PoseSearchAssetSamplerPose):

<a id="unreal.PoseSearchDatabase"></a>