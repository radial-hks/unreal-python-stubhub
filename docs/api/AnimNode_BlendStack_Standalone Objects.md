## AnimNode_BlendStack_Standalone Objects

```python
class AnimNode_BlendStack_Standalone(AnimNode_AssetPlayerBase)
```

namespace UE::BlendStack

**C++ Source:**

- **Plugin**: BlendStack
- **Module**: BlendStack
- **File**: AnimNode_BlendStack.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_weight`` (float):  [Read-Write] Last encountered blendweight for this node
- ``internal_time_accumulator`` (float):  [Read-Write] Accumulated time used to reference the asset in this node
- ``max_active_blends`` (int32):  [Read-Write] Number of max active blending animation in the blend stack. If MaxActiveBlends is zero then blend stack is disabled
- ``max_blend_in_time_to_override_animation`` (float):  [Read-Write] if the most relevant (recently added) animation is within MaxBlendInTimeToOverrideAnimation, the new requested blend will take its spot
  otherwise a new blended will be added to the stack
- ``notify_recency_time_out`` (float):  [Read-Write] Window of time after firing a notify that any instance of the same notify will be filtered out.
- ``player_depth_blend_in_time_multiplier`` (float):  [Read-Write] AnimPlayers blend in timer will be incremented PlayerDepthBlendInTimeMultiplier times faster on a deeper blend
- ``should_filter_notifies`` (bool):  [Read-Write] Flag that determines if any notifies from originating from an anim player samples should be filtered or not.
- ``stitch_blend_max_cost`` (float):  [Read-Write] if the cost from searching StitchDatabase is above StitchBlendMaxCost, blend stack will perform a regular blend,
  and not using the returned stitch animation as blend
- ``stitch_blend_time`` (float):  [Read-Write] blend time in seconds used to blend into and out from a stitch animation
- ``stitch_database`` (Object):  [Read-Write] database used to search for an animation stitch to use as blend
- ``store_blended_pose`` (bool):  [Read-Write] if the number of requested blends is higher than MaxActiveBlends, blend stack will blend and accumulate
  into a stored pose all the overflowing animations. if bStoreBlendedPose is false, the memory to store the pose will be saved,
  but once reached the MaxActiveBlends, blendstack will start discarding animations, potentially resulting in animation pops

<a id="unreal.AnimNode_BlendStack_Standalone.__init__"></a>

#### __init__

```python
def __init__(blend_weight: float = 0.000000,
             internal_time_accumulator: float = 0.000000,
             stitch_database: Object = None,
             stitch_blend_time: float = 0.000000,
             stitch_blend_max_cost: float = 0.000000,
             notify_recency_time_out: float = 0.000000) -> None
```

<a id="unreal.AnimNode_BlendStack_Standalone.stitch_database"></a>

#### stitch_database

```python
@property
def stitch_database() -> Object
```

(Object):  [Read-Write] database used to search for an animation stitch to use as blend

<a id="unreal.AnimNode_BlendStack_Standalone.stitch_database"></a>

#### stitch_database

```python
@stitch_database.setter
def stitch_database(value: Object) -> None
```

<a id="unreal.AnimNode_BlendStack_Standalone.stitch_blend_time"></a>

#### stitch_blend_time

```python
@property
def stitch_blend_time() -> float
```

(float):  [Read-Write] blend time in seconds used to blend into and out from a stitch animation

<a id="unreal.AnimNode_BlendStack_Standalone.stitch_blend_time"></a>

#### stitch_blend_time

```python
@stitch_blend_time.setter
def stitch_blend_time(value: float) -> None
```

<a id="unreal.AnimNode_BlendStack_Standalone.stitch_blend_max_cost"></a>

#### stitch_blend_max_cost

```python
@property
def stitch_blend_max_cost() -> float
```

(float):  [Read-Write] if the cost from searching StitchDatabase is above StitchBlendMaxCost, blend stack will perform a regular blend,
and not using the returned stitch animation as blend

<a id="unreal.AnimNode_BlendStack_Standalone.stitch_blend_max_cost"></a>

#### stitch_blend_max_cost

```python
@stitch_blend_max_cost.setter
def stitch_blend_max_cost(value: float) -> None
```

<a id="unreal.AnimNode_BlendStack_Standalone.notify_recency_time_out"></a>

#### notify_recency_time_out

```python
@property
def notify_recency_time_out() -> float
```

(float):  [Read-Write] Window of time after firing a notify that any instance of the same notify will be filtered out.

<a id="unreal.AnimNode_BlendStack_Standalone.notify_recency_time_out"></a>

#### notify_recency_time_out

```python
@notify_recency_time_out.setter
def notify_recency_time_out(value: float) -> None
```

<a id="unreal.AnimNode_BlendStack"></a>