## MotionWarpingUtilities Objects

```python
class MotionWarpingUtilities(BlueprintFunctionLibrary)
```

Motion Warping Utilities

**C++ Source:**

- **Plugin**: MotionWarping
- **Module**: MotionWarping
- **File**: MotionWarpingComponent.h

<a id="unreal.MotionWarpingUtilities.get_motion_warping_windows_from_animation"></a>

#### get_motion_warping_windows_from_animation

```python
@classmethod
def get_motion_warping_windows_from_animation(
        cls, animation: AnimSequenceBase) -> Array[MotionWarpingWindowData]
```

X.get_motion_warping_windows_from_animation(animation) -> Array[MotionWarpingWindowData]


Args:
    animation (AnimSequenceBase): 

Returns:
    Array[MotionWarpingWindowData]: 

    out_windows (Array[MotionWarpingWindowData]):

<a id="unreal.MotionWarpingUtilities.get_motion_warping_windows_for_warp_target_from_animation"></a>

#### get_motion_warping_windows_for_warp_target_from_animation

```python
@classmethod
def get_motion_warping_windows_for_warp_target_from_animation(
        cls, animation: AnimSequenceBase,
        warp_target_name: Name) -> Array[MotionWarpingWindowData]
```

X.get_motion_warping_windows_for_warp_target_from_animation(animation, warp_target_name) -> Array[MotionWarpingWindowData]


Args:
    animation (AnimSequenceBase): 
    warp_target_name (Name): 

Returns:
    Array[MotionWarpingWindowData]: 

    out_windows (Array[MotionWarpingWindowData]):

<a id="unreal.MotionWarpingUtilities.extract_root_motion_from_animation"></a>

#### extract_root_motion_from_animation

```python
@classmethod
def extract_root_motion_from_animation(cls, animation: AnimSequenceBase,
                                       start_time: float,
                                       end_time: float) -> Transform
```

X.extract_root_motion_from_animation(animation, start_time, end_time) -> Transform
Extract Root Motion transform from a contiguous position range

Args:
    animation (AnimSequenceBase): 
    start_time (float): 
    end_time (float): 

Returns:
    Transform:

<a id="unreal.MotionWarpingComponent"></a>