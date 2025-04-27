## UAnimNotifyLibrary Objects

```python
class UAnimNotifyLibrary(BlueprintFunctionLibrary)
```

A library of commonly used functionality for Notifies, exposed to blueprint.

**C++ Source:**

- **Module**: Engine
- **File**: AnimNotifyLibrary.h

<a id="unreal.UAnimNotifyLibrary.notify_state_reached_end"></a>

#### notify_state_reached_end

```python
@classmethod
def notify_state_reached_end(
        cls, event_reference: AnimNotifyEventReference) -> bool
```

X.notify_state_reached_end(event_reference) -> bool
Get whether the notify state reached the end (was not cancelled)

Args:
    event_reference (AnimNotifyEventReference): The event to inspect

Returns:
    bool:

<a id="unreal.UAnimNotifyLibrary.is_blending_out"></a>

#### is_blending_out

```python
@classmethod
def is_blending_out(cls, event_reference: AnimNotifyEventReference) -> bool
```

X.is_blending_out(event_reference) -> bool
Gets whether this notify comes from a source that is blending out.

Args:
    event_reference (AnimNotifyEventReference): The event to inspect

Returns:
    bool: Whether this notify comes from a source that is blending out.

<a id="unreal.UAnimNotifyLibrary.get_current_animation_time_ratio"></a>

#### get_current_animation_time_ratio

```python
@classmethod
def get_current_animation_time_ratio(
        cls, event_reference: AnimNotifyEventReference) -> float
```

X.get_current_animation_time_ratio(event_reference) -> float
Get the current anim notify time as a ratio (0 -> 1) through the animation for when this notify was fired

Args:
    event_reference (AnimNotifyEventReference): The event to inspect

Returns:
    float: the time as a ratio (0 -> 1) through the animation for when this notify was fired

<a id="unreal.UAnimNotifyLibrary.get_current_animation_time"></a>

#### get_current_animation_time

```python
@classmethod
def get_current_animation_time(
        cls, event_reference: AnimNotifyEventReference) -> float
```

X.get_current_animation_time(event_reference) -> float
Get the current anim notify time in seconds for when this notify was fired

Args:
    event_reference (AnimNotifyEventReference): The event to inspect

Returns:
    float: the time in seconds through the current animation for when this notify was fired

<a id="unreal.UAnimNotifyLibrary.get_current_animation_notify_state_time_ratio"></a>

#### get_current_animation_notify_state_time_ratio

```python
@classmethod
def get_current_animation_notify_state_time_ratio(
        cls, event_reference: AnimNotifyEventReference) -> float
```

X.get_current_animation_notify_state_time_ratio(event_reference) -> float
Gets the current time as a ratio (0 -> 1) relative to the start of the notify state

Args:
    event_reference (AnimNotifyEventReference): The event to inspect

Returns:
    float: the current time as a ratio (0 -> 1) relative to the start of the notify state

<a id="unreal.UAnimNotifyLibrary.get_current_animation_notify_state_time"></a>

#### get_current_animation_notify_state_time

```python
@classmethod
def get_current_animation_notify_state_time(
        cls, event_reference: AnimNotifyEventReference) -> float
```

X.get_current_animation_notify_state_time(event_reference) -> float
Gets the current time in seconds relative to the start of the notify state, clamped to the range of the notify
state

Args:
    event_reference (AnimNotifyEventReference): The event to inspect

Returns:
    float: the current time in seconds relative to the start of the notify state, clamped to the range of the notify state

<a id="unreal.UAnimNotifyMirrorInspectionLibrary"></a>