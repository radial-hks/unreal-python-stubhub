## InterchangeAnimationTrackSetInstanceNode Objects

```python
class InterchangeAnimationTrackSetInstanceNode(
        InterchangeAnimationTrackBaseNode)
```

Class to represent an animation that instances another animation track set node.

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeNodes
- **File**: InterchangeAnimationTrackSetNode.h

<a id="unreal.InterchangeAnimationTrackSetInstanceNode.set_custom_track_set_dependency_uid"></a>

#### set_custom_track_set_dependency_uid

```python
def set_custom_track_set_dependency_uid(attribute_value: str) -> bool
```

x.set_custom_track_set_dependency_uid(attribute_value) -> bool
Set the unique id of the level sequence this instance references.

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeAnimationTrackSetInstanceNode.set_custom_time_scale"></a>

#### set_custom_time_scale

```python
def set_custom_time_scale(attribute_value: float) -> bool
```

x.set_custom_time_scale(attribute_value) -> bool
Set the time scale used for the level sequence instance.

Args:
    attribute_value (float): 

Returns:
    bool:

<a id="unreal.InterchangeAnimationTrackSetInstanceNode.set_custom_start_frame"></a>

#### set_custom_start_frame

```python
def set_custom_start_frame(attribute_value: int) -> bool
```

x.set_custom_start_frame(attribute_value) -> bool
Set the frame where the level sequence instance starts.

Args:
    attribute_value (int32): 

Returns:
    bool:

<a id="unreal.InterchangeAnimationTrackSetInstanceNode.set_custom_duration"></a>

#### set_custom_duration

```python
def set_custom_duration(attribute_value: int) -> bool
```

x.set_custom_duration(attribute_value) -> bool
Set the level sequence instance duration in number of frames.

Args:
    attribute_value (int32): 

Returns:
    bool:

<a id="unreal.InterchangeAnimationTrackSetInstanceNode.get_custom_track_set_dependency_uid"></a>

#### get_custom_track_set_dependency_uid

```python
def get_custom_track_set_dependency_uid() -> Optional[str]
```

x.get_custom_track_set_dependency_uid() -> str or None
Get the unique id of the level sequence this instance references.

Returns:
    str or None: 

    attribute_value (str):

<a id="unreal.InterchangeAnimationTrackSetInstanceNode.get_custom_time_scale"></a>

#### get_custom_time_scale

```python
def get_custom_time_scale() -> Optional[float]
```

x.get_custom_time_scale() -> float or None
Get the time scale used for the level sequence instance.

Returns:
    float or None: 

    attribute_value (float):

<a id="unreal.InterchangeAnimationTrackSetInstanceNode.get_custom_start_frame"></a>

#### get_custom_start_frame

```python
def get_custom_start_frame() -> Optional[int]
```

x.get_custom_start_frame() -> int32 or None
Get the frame where the level sequence instance starts.

Returns:
    int32 or None: 

    attribute_value (int32):

<a id="unreal.InterchangeAnimationTrackSetInstanceNode.get_custom_duration"></a>

#### get_custom_duration

```python
def get_custom_duration() -> Optional[int]
```

x.get_custom_duration() -> int32 or None
Get the level sequence instance duration in number of frames.

Returns:
    int32 or None: 

    attribute_value (int32):

<a id="unreal.InterchangeAnimationTrackNode"></a>