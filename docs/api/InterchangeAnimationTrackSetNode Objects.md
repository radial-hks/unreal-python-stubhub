## InterchangeAnimationTrackSetNode Objects

```python
class InterchangeAnimationTrackSetNode(InterchangeBaseNode)
```

Class to represent a set of animation track nodes that share the same frame rate.

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeNodes
- **File**: InterchangeAnimationTrackSetNode.h

<a id="unreal.InterchangeAnimationTrackSetNode.set_custom_frame_rate"></a>

#### set_custom_frame_rate

```python
def set_custom_frame_rate(attribute_value: float) -> bool
```

x.set_custom_frame_rate(attribute_value) -> bool
Set the frame rate for the animations in the level sequence.

Args:
    attribute_value (float): 

Returns:
    bool:

<a id="unreal.InterchangeAnimationTrackSetNode.remove_custom_animation_track_uid"></a>

#### remove_custom_animation_track_uid

```python
def remove_custom_animation_track_uid(animation_track_uid: str) -> bool
```

x.remove_custom_animation_track_uid(animation_track_uid) -> bool
Remove one track dependency from this object.

Args:
    animation_track_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeAnimationTrackSetNode.get_custom_frame_rate"></a>

#### get_custom_frame_rate

```python
def get_custom_frame_rate() -> Optional[float]
```

x.get_custom_frame_rate() -> float or None
Get the frame rate for the animations in the level sequence.

Returns:
    float or None: 

    attribute_value (float):

<a id="unreal.InterchangeAnimationTrackSetNode.get_custom_animation_track_uids"></a>

#### get_custom_animation_track_uids

```python
def get_custom_animation_track_uids() -> Array[str]
```

x.get_custom_animation_track_uids() -> Array[str]
Retrieve the track dependency for this object.

Returns:
    Array[str]: 

    out_animation_track_uids (Array[str]):

<a id="unreal.InterchangeAnimationTrackSetNode.get_custom_animation_track_uid_count"></a>

#### get_custom_animation_track_uid_count

```python
def get_custom_animation_track_uid_count() -> int
```

x.get_custom_animation_track_uid_count() -> int32
Retrieve the number of track dependencies for this object.

Returns:
    int32:

<a id="unreal.InterchangeAnimationTrackSetNode.get_custom_animation_track_uid"></a>

#### get_custom_animation_track_uid

```python
def get_custom_animation_track_uid(index: int) -> str
```

x.get_custom_animation_track_uid(index) -> str
Retrieve one track dependency for this object.

Args:
    index (int32): 

Returns:
    str: 

    out_animation_track_uid (str):

<a id="unreal.InterchangeAnimationTrackSetNode.add_custom_animation_track_uid"></a>

#### add_custom_animation_track_uid

```python
def add_custom_animation_track_uid(animation_track_uid: str) -> bool
```

x.add_custom_animation_track_uid(animation_track_uid) -> bool
Add one track dependency to this object.

Args:
    animation_track_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeAnimationTrackBaseNode"></a>