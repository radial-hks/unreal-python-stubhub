## RetargetGlobalSettings Objects

```python
class RetargetGlobalSettings(StructBase)
```

Retarget Global Settings

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRig
- **File**: IKRetargetSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``direction_chain`` (Name):  [Read-Write] When using the "Chain" option as a Direction Source, this defines the chain to use to determine the facing direction of the character.
  Typically this would be the chain that contains the Spine bones.
- ``direction_source`` (WarpingDirectionSource):  [Read-Write] Defines the source used to determine the forward direction as the character animates in world space. Default is "Goals".
  This method uses various positions on the character to create a "best fit" global rotation that approximates the facing direction of the character over time.
  This global rotation is used to define the forward and sideways directions used when warping goals along those axes.
  The options are:
  Goals: uses the positions of the IK goals to approximate the facing direction. This is best used on characters with a vertical spine, like bipeds.
  Chain: uses the positions of the bones in a retarget chain to approximate the facing direction. This is best when used with the spine chain for characters with a horizontal spine, like quadrupeds.
  Root Bone: uses the rotation of the root bone of the skeleton. This is most robust, but character must have correct root motion with yaw rotation in movement direction.
- ``enable_fk`` (bool):  [Read-Write] When false, limbs are not copied via FK. Useful for debugging limb issues suspected to be caused by FK chain settings.
  Note: the retargeting order is: Root > FK > IK > Post
- ``enable_ik`` (bool):  [Read-Write] When false, IK is not applied as part of retargeter. Useful for debugging limb issues suspected to be caused by IK.
  Note: the retargeting order is: Root > FK > IK > Post
- ``enable_post`` (bool):  [Read-Write] When false, Post operations are not applied as part of retargeter. Useful for debugging issues suspected to be caused by the post phase.
  Note: the retargeting order is: Root > FK > IK > Post
- ``enable_root`` (bool):  [Read-Write] When false, the motion of the Retarget Root bone is not copied from the source. Useful for debugging issues with the root settings.
  Note: the retargeting order is: Root > FK > IK > Post
- ``forward_direction`` (BasicAxis):  [Read-Write] The world space axis that represents the forward facing direction for your character. By default, in Unreal, this is +Y.
- ``sideways_offset`` (float):  [Read-Write] Range -+Inf. Default is 0. A static offset in world units to move the IK goals perpendicular to the forward direction.
  Values less than zero will move the goals towards the center-line of the character. Values greater than zero push the goals outwards.
- ``warp_forwards`` (float):  [Read-Write] Range 0 to Inf. Default 1. Warps IK goal positions in the forward direction. Useful for stride warping.
  Values below 1 will create smaller, squashed strides. Values greater than 1 will create stretched, longer strides.
- ``warp_splay`` (float):  [Read-Write] Range 0 to +Inf. Default is 1.0f.
  Values below 1 pull all the goals towards the average of all the goals (towards each other).
  Values greater than 1 push the goals apart.
- ``warping`` (bool):  [Read-Write] Enable IK Warping.
  These options allow for global modifications to all IK Goals that have "Affected by IK Warping" turned on (the default).
  "Affected by IK Warping" can be found in the IK settings of a retarget chain.

<a id="unreal.RetargetGlobalSettings.__init__"></a>

#### __init__

```python
def __init__(enable_root: bool = False,
             enable_fk: bool = False,
             enable_ik: bool = False,
             enable_post: bool = False,
             warping: bool = False,
             direction_source: WarpingDirectionSource = WarpingDirectionSource.
             GOALS,
             forward_direction: BasicAxis = BasicAxis.X,
             direction_chain: Name = "None",
             warp_forwards: float = 0.000000,
             sideways_offset: float = 0.000000,
             warp_splay: float = 0.000000) -> None
```

<a id="unreal.RetargetGlobalSettings.enable_root"></a>

#### enable_root

```python
@property
def enable_root() -> bool
```

(bool):  [Read-Write] When false, the motion of the Retarget Root bone is not copied from the source. Useful for debugging issues with the root settings.
Note: the retargeting order is: Root > FK > IK > Post

<a id="unreal.RetargetGlobalSettings.enable_root"></a>

#### enable_root

```python
@enable_root.setter
def enable_root(value: bool) -> None
```

<a id="unreal.RetargetGlobalSettings.enable_fk"></a>

#### enable_fk

```python
@property
def enable_fk() -> bool
```

(bool):  [Read-Write] When false, limbs are not copied via FK. Useful for debugging limb issues suspected to be caused by FK chain settings.
Note: the retargeting order is: Root > FK > IK > Post

<a id="unreal.RetargetGlobalSettings.enable_fk"></a>

#### enable_fk

```python
@enable_fk.setter
def enable_fk(value: bool) -> None
```

<a id="unreal.RetargetGlobalSettings.enable_ik"></a>

#### enable_ik

```python
@property
def enable_ik() -> bool
```

(bool):  [Read-Write] When false, IK is not applied as part of retargeter. Useful for debugging limb issues suspected to be caused by IK.
Note: the retargeting order is: Root > FK > IK > Post

<a id="unreal.RetargetGlobalSettings.enable_ik"></a>

#### enable_ik

```python
@enable_ik.setter
def enable_ik(value: bool) -> None
```

<a id="unreal.RetargetGlobalSettings.enable_post"></a>

#### enable_post

```python
@property
def enable_post() -> bool
```

(bool):  [Read-Write] When false, Post operations are not applied as part of retargeter. Useful for debugging issues suspected to be caused by the post phase.
Note: the retargeting order is: Root > FK > IK > Post

<a id="unreal.RetargetGlobalSettings.enable_post"></a>

#### enable_post

```python
@enable_post.setter
def enable_post(value: bool) -> None
```

<a id="unreal.RetargetGlobalSettings.warping"></a>

#### warping

```python
@property
def warping() -> bool
```

(bool):  [Read-Write] Enable IK Warping.
These options allow for global modifications to all IK Goals that have "Affected by IK Warping" turned on (the default).
"Affected by IK Warping" can be found in the IK settings of a retarget chain.

<a id="unreal.RetargetGlobalSettings.warping"></a>

#### warping

```python
@warping.setter
def warping(value: bool) -> None
```

<a id="unreal.RetargetGlobalSettings.direction_source"></a>

#### direction_source

```python
@property
def direction_source() -> WarpingDirectionSource
```

(WarpingDirectionSource):  [Read-Write] Defines the source used to determine the forward direction as the character animates in world space. Default is "Goals".
This method uses various positions on the character to create a "best fit" global rotation that approximates the facing direction of the character over time.
This global rotation is used to define the forward and sideways directions used when warping goals along those axes.
The options are:
Goals: uses the positions of the IK goals to approximate the facing direction. This is best used on characters with a vertical spine, like bipeds.
Chain: uses the positions of the bones in a retarget chain to approximate the facing direction. This is best when used with the spine chain for characters with a horizontal spine, like quadrupeds.
Root Bone: uses the rotation of the root bone of the skeleton. This is most robust, but character must have correct root motion with yaw rotation in movement direction.

<a id="unreal.RetargetGlobalSettings.direction_source"></a>

#### direction_source

```python
@direction_source.setter
def direction_source(value: WarpingDirectionSource) -> None
```

<a id="unreal.RetargetGlobalSettings.forward_direction"></a>

#### forward_direction

```python
@property
def forward_direction() -> BasicAxis
```

(BasicAxis):  [Read-Write] The world space axis that represents the forward facing direction for your character. By default, in Unreal, this is +Y.

<a id="unreal.RetargetGlobalSettings.forward_direction"></a>

#### forward_direction

```python
@forward_direction.setter
def forward_direction(value: BasicAxis) -> None
```

<a id="unreal.RetargetGlobalSettings.direction_chain"></a>

#### direction_chain

```python
@property
def direction_chain() -> Name
```

(Name):  [Read-Write] When using the "Chain" option as a Direction Source, this defines the chain to use to determine the facing direction of the character.
Typically this would be the chain that contains the Spine bones.

<a id="unreal.RetargetGlobalSettings.direction_chain"></a>

#### direction_chain

```python
@direction_chain.setter
def direction_chain(value: Name) -> None
```

<a id="unreal.RetargetGlobalSettings.warp_forwards"></a>

#### warp_forwards

```python
@property
def warp_forwards() -> float
```

(float):  [Read-Write] Range 0 to Inf. Default 1. Warps IK goal positions in the forward direction. Useful for stride warping.
Values below 1 will create smaller, squashed strides. Values greater than 1 will create stretched, longer strides.

<a id="unreal.RetargetGlobalSettings.warp_forwards"></a>

#### warp_forwards

```python
@warp_forwards.setter
def warp_forwards(value: float) -> None
```

<a id="unreal.RetargetGlobalSettings.sideways_offset"></a>

#### sideways_offset

```python
@property
def sideways_offset() -> float
```

(float):  [Read-Write] Range -+Inf. Default is 0. A static offset in world units to move the IK goals perpendicular to the forward direction.
Values less than zero will move the goals towards the center-line of the character. Values greater than zero push the goals outwards.

<a id="unreal.RetargetGlobalSettings.sideways_offset"></a>

#### sideways_offset

```python
@sideways_offset.setter
def sideways_offset(value: float) -> None
```

<a id="unreal.RetargetGlobalSettings.warp_splay"></a>

#### warp_splay

```python
@property
def warp_splay() -> float
```

(float):  [Read-Write] Range 0 to +Inf. Default is 1.0f.
Values below 1 pull all the goals towards the average of all the goals (towards each other).
Values greater than 1 push the goals apart.

<a id="unreal.RetargetGlobalSettings.warp_splay"></a>

#### warp_splay

```python
@warp_splay.setter
def warp_splay(value: float) -> None
```

<a id="unreal.TargetRootSettings"></a>