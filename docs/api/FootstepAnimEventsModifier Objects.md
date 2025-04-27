## FootstepAnimEventsModifier Objects

```python
class FootstepAnimEventsModifier(AnimationModifier)
```

Generates animation notifies and/or sync markers for any specified bone(s)

**C++ Source:**

- **Plugin**: AnimationModifierLibrary
- **Module**: AnimationModifierLibrary
- **File**: FootstepAnimEventsModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``foot_definitions`` (Array[FootDefinition]):  [Read-Write] Foot bone(s) to be processed
- ``generated_notify_tracks`` (Set[Name]):  [Read-Only] Keep track of to be generated tracks during modifier application
- ``ground_threshold`` (float):  [Read-Write] Threshold for determining if a foot bone position can be considered to be on the ground level
- ``processed_notify_tracks`` (Set[Name]):  [Read-Only] Keep track of tracks modified during modifier application
- ``reapply_post_owner_change`` (bool):  [Read-Write] If this is set to true then the animation modifier will call it's reapply function after any change made to the owning asset.
- ``sample_rate`` (int32):  [Read-Write] Rate used to sample the animation
- ``should_remove_pre_existing_notifies_or_sync_markers`` (bool):  [Read-Write] If true, applying the anim modifier becomes a destructive action, meaning that any existing matched tracks will have their data overwritten by the modifier.
  Otherwise, no previous notifies or sync markers will removed when applying the anim modifier.
- ``speed_threshold`` (float):  [Read-Write] Threshold to start finding the smallest foot bone translation speed.

  Note that the foot bone translation speed is normalize therefore when a footstep occurs
  the speed will be very close to zero, thus for most cases this value won't need to be changed.

<a id="unreal.FootstepAnimEventsModifier.sample_rate"></a>

#### sample_rate

```python
@property
def sample_rate() -> int
```

(int32):  [Read-Only] Rate used to sample the animation

<a id="unreal.FootstepAnimEventsModifier.ground_threshold"></a>

#### ground_threshold

```python
@property
def ground_threshold() -> float
```

(float):  [Read-Only] Threshold for determining if a foot bone position can be considered to be on the ground level

<a id="unreal.FootstepAnimEventsModifier.speed_threshold"></a>

#### speed_threshold

```python
@property
def speed_threshold() -> float
```

(float):  [Read-Only] Threshold to start finding the smallest foot bone translation speed.

Note that the foot bone translation speed is normalize therefore when a footstep occurs
the speed will be very close to zero, thus for most cases this value won't need to be changed.

<a id="unreal.FootstepAnimEventsModifier.foot_definitions"></a>

#### foot_definitions

```python
@property
def foot_definitions() -> Array[FootDefinition]
```

(Array[FootDefinition]):  [Read-Only] Foot bone(s) to be processed

<a id="unreal.FootstepAnimEventsModifier.should_remove_pre_existing_notifies_or_sync_markers"></a>

#### should_remove_pre_existing_notifies_or_sync_markers

```python
@property
def should_remove_pre_existing_notifies_or_sync_markers() -> bool
```

(bool):  [Read-Only] If true, applying the anim modifier becomes a destructive action, meaning that any existing matched tracks will have their data overwritten by the modifier.
Otherwise, no previous notifies or sync markers will removed when applying the anim modifier.

<a id="unreal.MotionExtractorUtilityLibrary"></a>