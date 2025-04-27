## AnimNode_LayeredBoneBlend Objects

```python
class AnimNode_LayeredBoneBlend(AnimNode_Base)
```

Layered blend (per bone); has dynamic number of blendposes that can blend per different bone sets

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_LayeredBoneBlend.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_pose`` (PoseLink):  [Read-Write] The source pose
- ``blend_masks`` (Array[BlendProfile]):  [Read-Write] The blend masks to use for our layer inputs. Allows the use of per-bone alphas.
  Blend masks are used when BlendMode is BlendMask.
- ``blend_mode`` (LayeredBoneBlendMode):  [Read-Write] Whether to use branch filters or a blend mask to specify an input pose per-bone influence
- ``blend_poses`` (Array[PoseLink]):  [Read-Write] Each layer's blended pose
- ``blend_root_motion_based_on_root_bone`` (bool):  [Read-Write] Whether to incorporate the per-bone blend weight of the root bone when lending root motion
- ``blend_weights`` (Array[float]):  [Read-Write] The weights of each layer
- ``curve_blend_option`` (CurveBlendOption):  [Read-Write] How to blend the layers together
- ``layer_setup`` (Array[InputBlendPose]):  [Read-Write] Configuration for the parts of the skeleton to blend for each layer. Allows
  certain parts of the tree to be blended out or omitted from the pose.
  LayerSetup is used when BlendMode is BranchFilter.
- ``lod_threshold`` (int32):  [Read-Write] * Max LOD that this node is allowed to run
  * For example if you have LODThreshold to be 2, it will run until LOD 2 (based on 0 index)
  * when the component LOD becomes 3, it will stop update/evaluate
  * currently transition would be issue and that has to be re-visited
- ``mesh_space_rotation_blend`` (bool):  [Read-Write] Whether to blend bone rotations in mesh space or in local space
- ``mesh_space_scale_blend`` (bool):  [Read-Write] Whether to blend bone scales in mesh space or in local space

<a id="unreal.AnimNode_LayeredBoneBlend.__init__"></a>

#### __init__

```python
def __init__(
        base_pose: PoseLink = [],
        blend_poses: Array[PoseLink] = [],
        blend_weights: Array[float] = [],
        lod_threshold: int = 0,
        mesh_space_rotation_blend: bool = False,
        mesh_space_scale_blend: bool = False,
        curve_blend_option: CurveBlendOption = CurveBlendOption.OVERRIDE
) -> None
```

<a id="unreal.AnimNode_LayeredBoneBlend.base_pose"></a>

#### base_pose

```python
@property
def base_pose() -> PoseLink
```

(PoseLink):  [Read-Write] The source pose

<a id="unreal.AnimNode_LayeredBoneBlend.base_pose"></a>

#### base_pose

```python
@base_pose.setter
def base_pose(value: PoseLink) -> None
```

<a id="unreal.AnimNode_LayeredBoneBlend.blend_poses"></a>

#### blend_poses

```python
@property
def blend_poses() -> Array[PoseLink]
```

(Array[PoseLink]):  [Read-Write] Each layer's blended pose

<a id="unreal.AnimNode_LayeredBoneBlend.blend_poses"></a>

#### blend_poses

```python
@blend_poses.setter
def blend_poses(value: Array[PoseLink]) -> None
```

<a id="unreal.AnimNode_LayeredBoneBlend.blend_weights"></a>

#### blend_weights

```python
@property
def blend_weights() -> Array[float]
```

(Array[float]):  [Read-Write] The weights of each layer

<a id="unreal.AnimNode_LayeredBoneBlend.blend_weights"></a>

#### blend_weights

```python
@blend_weights.setter
def blend_weights(value: Array[float]) -> None
```

<a id="unreal.AnimNode_LayeredBoneBlend.lod_threshold"></a>

#### lod_threshold

```python
@property
def lod_threshold() -> int
```

(int32):  [Read-Write] * Max LOD that this node is allowed to run
* For example if you have LODThreshold to be 2, it will run until LOD 2 (based on 0 index)
* when the component LOD becomes 3, it will stop update/evaluate
* currently transition would be issue and that has to be re-visited

<a id="unreal.AnimNode_LayeredBoneBlend.lod_threshold"></a>

#### lod_threshold

```python
@lod_threshold.setter
def lod_threshold(value: int) -> None
```

<a id="unreal.AnimNode_LayeredBoneBlend.mesh_space_rotation_blend"></a>

#### mesh_space_rotation_blend

```python
@property
def mesh_space_rotation_blend() -> bool
```

(bool):  [Read-Write] Whether to blend bone rotations in mesh space or in local space

<a id="unreal.AnimNode_LayeredBoneBlend.mesh_space_rotation_blend"></a>

#### mesh_space_rotation_blend

```python
@mesh_space_rotation_blend.setter
def mesh_space_rotation_blend(value: bool) -> None
```

<a id="unreal.AnimNode_LayeredBoneBlend.mesh_space_scale_blend"></a>

#### mesh_space_scale_blend

```python
@property
def mesh_space_scale_blend() -> bool
```

(bool):  [Read-Write] Whether to blend bone scales in mesh space or in local space

<a id="unreal.AnimNode_LayeredBoneBlend.mesh_space_scale_blend"></a>

#### mesh_space_scale_blend

```python
@mesh_space_scale_blend.setter
def mesh_space_scale_blend(value: bool) -> None
```

<a id="unreal.AnimNode_LayeredBoneBlend.curve_blend_option"></a>

#### curve_blend_option

```python
@property
def curve_blend_option() -> CurveBlendOption
```

(CurveBlendOption):  [Read-Write] How to blend the layers together

<a id="unreal.AnimNode_LayeredBoneBlend.curve_blend_option"></a>

#### curve_blend_option

```python
@curve_blend_option.setter
def curve_blend_option(value: CurveBlendOption) -> None
```

<a id="unreal.PerBoneBlendWeight"></a>