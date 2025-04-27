## AnimNotifyState_MotionWarping Objects

```python
class AnimNotifyState_MotionWarping(AnimNotifyState)
```

AnimNotifyState used to define a motion warping window in the animation

**C++ Source:**

- **Plugin**: MotionWarping
- **Module**: MotionWarping
- **File**: AnimNotifyState_MotionWarping.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``notify_color`` (Color):  [Read-Write] Color of Notify in editor
- ``root_motion_modifier`` (RootMotionModifier):  [Read-Write]
  TODO:: Prevent notify callbacks and add comments explaining why we don't use those here.
- ``should_fire_in_editor`` (bool):  [Read-Write] Whether this notify state instance should fire in animation editors

<a id="unreal.AnimNotifyState_MotionWarping.root_motion_modifier"></a>

#### root_motion_modifier

```python
@property
def root_motion_modifier() -> RootMotionModifier
```

(RootMotionModifier):  [Read-Only]
TODO:: Prevent notify callbacks and add comments explaining why we don't use those here.

<a id="unreal.AnimNotifyState_MotionWarping.on_warp_update"></a>

#### on_warp_update

```python
def on_warp_update(motion_warping_comp: MotionWarpingComponent,
                   modifier: RootMotionModifier) -> None
```

x.on_warp_update(motion_warping_comp, modifier) -> None
On Warp Update

Args:
    motion_warping_comp (MotionWarpingComponent): 
    modifier (RootMotionModifier):

<a id="unreal.AnimNotifyState_MotionWarping.on_warp_end"></a>

#### on_warp_end

```python
def on_warp_end(motion_warping_comp: MotionWarpingComponent,
                modifier: RootMotionModifier) -> None
```

x.on_warp_end(motion_warping_comp, modifier) -> None
On Warp End

Args:
    motion_warping_comp (MotionWarpingComponent): 
    modifier (RootMotionModifier):

<a id="unreal.AnimNotifyState_MotionWarping.on_warp_begin"></a>

#### on_warp_begin

```python
def on_warp_begin(motion_warping_comp: MotionWarpingComponent,
                  modifier: RootMotionModifier) -> None
```

x.on_warp_begin(motion_warping_comp, modifier) -> None
On Warp Begin

Args:
    motion_warping_comp (MotionWarpingComponent): 
    modifier (RootMotionModifier):

<a id="unreal.AnimNotifyState_MotionWarping.add_root_motion_modifier"></a>

#### add_root_motion_modifier

```python
def add_root_motion_modifier(motion_warping_comp: MotionWarpingComponent,
                             animation: AnimSequenceBase, start_time: float,
                             end_time: float) -> RootMotionModifier
```

x.add_root_motion_modifier(motion_warping_comp, animation, start_time, end_time) -> RootMotionModifier
Creates a root motion modifier from the config class defined in the notify

Args:
    motion_warping_comp (MotionWarpingComponent): 
    animation (AnimSequenceBase): 
    start_time (float): 
    end_time (float): 

Returns:
    RootMotionModifier:

<a id="unreal.AttributeBasedRootMotionComponent"></a>