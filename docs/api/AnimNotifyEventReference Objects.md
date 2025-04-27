## AnimNotifyEventReference Objects

```python
class AnimNotifyEventReference(StructBase)
```

Anim Notify Event Reference

**C++ Source:**

- **Module**: Engine
- **File**: AnimNotifyQueue.h

<a id="unreal.AnimNotifyEventReference.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AnimNotifyEventReference.notify_state_reached_end"></a>

#### notify_state_reached_end

```python
def notify_state_reached_end() -> bool
```

x.notify_state_reached_end() -> bool
Get whether the notify state reached the end (was not cancelled)

Returns:
    bool:

<a id="unreal.AnimNotifyEventReference.is_blending_out"></a>

#### is_blending_out

```python
def is_blending_out() -> bool
```

x.is_blending_out() -> bool
Gets whether this notify comes from a source that is blending out.

Returns:
    bool: Whether this notify comes from a source that is blending out.

<a id="unreal.AnimNotifyEventReference.get_current_animation_time_ratio"></a>

#### get_current_animation_time_ratio

```python
def get_current_animation_time_ratio() -> float
```

x.get_current_animation_time_ratio() -> float
Get the current anim notify time as a ratio (0 -> 1) through the animation for when this notify was fired

Returns:
    float: the time as a ratio (0 -> 1) through the animation for when this notify was fired

<a id="unreal.AnimNotifyEventReference.get_current_animation_time"></a>

#### get_current_animation_time

```python
def get_current_animation_time() -> float
```

x.get_current_animation_time() -> float
Get the current anim notify time in seconds for when this notify was fired

Returns:
    float: the time in seconds through the current animation for when this notify was fired

<a id="unreal.AnimNotifyEventReference.get_current_animation_notify_state_time_ratio"></a>

#### get_current_animation_notify_state_time_ratio

```python
def get_current_animation_notify_state_time_ratio() -> float
```

x.get_current_animation_notify_state_time_ratio() -> float
Gets the current time as a ratio (0 -> 1) relative to the start of the notify state

Returns:
    float: the current time as a ratio (0 -> 1) relative to the start of the notify state

<a id="unreal.AnimNotifyEventReference.get_current_animation_notify_state_time"></a>

#### get_current_animation_notify_state_time

```python
def get_current_animation_notify_state_time() -> float
```

x.get_current_animation_notify_state_time() -> float
Gets the current time in seconds relative to the start of the notify state, clamped to the range of the notify
state

Returns:
    float: the current time in seconds relative to the start of the notify state, clamped to the range of the notify state

<a id="unreal.AnimNode_SingleNode"></a>