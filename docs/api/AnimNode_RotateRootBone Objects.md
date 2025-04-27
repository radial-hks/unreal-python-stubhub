## AnimNode_RotateRootBone Objects

```python
class AnimNode_RotateRootBone(AnimNode_Base)
```

TODO:: Comment

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_RotateRootBone.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_pose`` (PoseLink):  [Read-Write]
- ``mesh_to_component`` (Rotator):  [Read-Write]
- ``pitch`` (float):  [Read-Write]
- ``pitch_scale_bias_clamp`` (InputScaleBiasClamp):  [Read-Write]
- ``rotate_root_motion_attribute`` (bool):  [Read-Write] If enabled, rotating the root bone using this node will also rotate the direction of the root motion custom attribute
- ``yaw`` (float):  [Read-Write]
- ``yaw_scale_bias_clamp`` (InputScaleBiasClamp):  [Read-Write]

<a id="unreal.AnimNode_RotateRootBone.__init__"></a>

#### __init__

```python
def __init__(base_pose: PoseLink = [],
             pitch: float = 0.000000,
             yaw: float = 0.000000,
             pitch_scale_bias_clamp: InputScaleBiasClamp = [
                 False, False, False, [0.000000,
                                       1.000000], [0.000000, 1.000000],
                 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000
             ],
             yaw_scale_bias_clamp: InputScaleBiasClamp = [
                 False, False, False, [0.000000,
                                       1.000000], [0.000000, 1.000000],
                 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000
             ],
             mesh_to_component: Rotator = [0.000000, 0.000000, 0.000000],
             rotate_root_motion_attribute: bool = False) -> None
```

<a id="unreal.AnimNode_RotateRootBone.base_pose"></a>

#### base_pose

```python
@property
def base_pose() -> PoseLink
```

(PoseLink):  [Read-Write]

<a id="unreal.AnimNode_RotateRootBone.base_pose"></a>

#### base_pose

```python
@base_pose.setter
def base_pose(value: PoseLink) -> None
```

<a id="unreal.AnimNode_RotateRootBone.pitch"></a>

#### pitch

```python
@property
def pitch() -> float
```

(float):  [Read-Write]

<a id="unreal.AnimNode_RotateRootBone.pitch"></a>

#### pitch

```python
@pitch.setter
def pitch(value: float) -> None
```

<a id="unreal.AnimNode_RotateRootBone.yaw"></a>

#### yaw

```python
@property
def yaw() -> float
```

(float):  [Read-Write]

<a id="unreal.AnimNode_RotateRootBone.yaw"></a>

#### yaw

```python
@yaw.setter
def yaw(value: float) -> None
```

<a id="unreal.AnimNode_RotateRootBone.pitch_scale_bias_clamp"></a>

#### pitch_scale_bias_clamp

```python
@property
def pitch_scale_bias_clamp() -> InputScaleBiasClamp
```

(InputScaleBiasClamp):  [Read-Write]

<a id="unreal.AnimNode_RotateRootBone.pitch_scale_bias_clamp"></a>

#### pitch_scale_bias_clamp

```python
@pitch_scale_bias_clamp.setter
def pitch_scale_bias_clamp(value: InputScaleBiasClamp) -> None
```

<a id="unreal.AnimNode_RotateRootBone.yaw_scale_bias_clamp"></a>

#### yaw_scale_bias_clamp

```python
@property
def yaw_scale_bias_clamp() -> InputScaleBiasClamp
```

(InputScaleBiasClamp):  [Read-Write]

<a id="unreal.AnimNode_RotateRootBone.yaw_scale_bias_clamp"></a>

#### yaw_scale_bias_clamp

```python
@yaw_scale_bias_clamp.setter
def yaw_scale_bias_clamp(value: InputScaleBiasClamp) -> None
```

<a id="unreal.AnimNode_RotateRootBone.mesh_to_component"></a>

#### mesh_to_component

```python
@property
def mesh_to_component() -> Rotator
```

(Rotator):  [Read-Write]

<a id="unreal.AnimNode_RotateRootBone.mesh_to_component"></a>

#### mesh_to_component

```python
@mesh_to_component.setter
def mesh_to_component(value: Rotator) -> None
```

<a id="unreal.AnimNode_RotateRootBone.rotate_root_motion_attribute"></a>

#### rotate_root_motion_attribute

```python
@property
def rotate_root_motion_attribute() -> bool
```

(bool):  [Read-Write] If enabled, rotating the root bone using this node will also rotate the direction of the root motion custom attribute

<a id="unreal.AnimNode_RotateRootBone.rotate_root_motion_attribute"></a>

#### rotate_root_motion_attribute

```python
@rotate_root_motion_attribute.setter
def rotate_root_motion_attribute(value: bool) -> None
```

<a id="unreal.AnimNode_RotationOffsetBlendSpace"></a>