## RootMotionModifier_Scale Objects

```python
class RootMotionModifier_Scale(RootMotionModifier)
```

URootMotionModifier_Scale

**C++ Source:**

- **Plugin**: MotionWarping
- **Module**: MotionWarping
- **File**: RootMotionModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actual_start_time`` (float):  [Read-Write] Actual playback time when the modifier becomes active
- ``animation`` (AnimSequenceBase):  [Read-Write] Source of the root motion we are warping
- ``current_position`` (float):  [Read-Write] Current playback time of the animation
- ``end_time`` (float):  [Read-Write] End time of the warping window
- ``previous_position`` (float):  [Read-Write] Previous playback time of the animation
- ``scale`` (Vector):  [Read-Write] Vector used to scale each component of the translation
- ``start_time`` (float):  [Read-Write] Start time of the warping window
- ``start_transform`` (Transform):  [Read-Write] Character owner transform at the time this modifier becomes active
- ``total_root_motion_within_window`` (Transform):  [Read-Write] Total root motion within the warping window
- ``weight`` (float):  [Read-Write] Current blend weight of the animation

<a id="unreal.RootMotionModifier_Scale.scale"></a>

#### scale

```python
@property
def scale() -> Vector
```

(Vector):  [Read-Write] Vector used to scale each component of the translation

<a id="unreal.RootMotionModifier_Scale.scale"></a>

#### scale

```python
@scale.setter
def scale(value: Vector) -> None
```

<a id="unreal.RootMotionModifier_Scale.add_root_motion_modifier_scale"></a>

#### add_root_motion_modifier_scale

```python
@classmethod
def add_root_motion_modifier_scale(
    cls,
    motion_warping_comp: MotionWarpingComponent,
    animation: AnimSequenceBase,
    start_time: float,
    end_time: float,
    scale: Vector = [1.000000, 1.000000,
                     1.000000]) -> RootMotionModifier_Scale
```

X.add_root_motion_modifier_scale(motion_warping_comp, animation, start_time, end_time, scale=[1.000000, 1.000000, 1.000000]) -> RootMotionModifier_Scale
Add Root Motion Modifier Scale

Args:
    motion_warping_comp (MotionWarpingComponent): 
    animation (AnimSequenceBase): 
    start_time (float): 
    end_time (float): 
    scale (Vector): 

Returns:
    RootMotionModifier_Scale:

<a id="unreal.RootMotionModifier_AdjustmentBlendWarp"></a>