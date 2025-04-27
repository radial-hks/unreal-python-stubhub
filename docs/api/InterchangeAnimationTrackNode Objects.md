## InterchangeAnimationTrackNode Objects

```python
class InterchangeAnimationTrackNode(InterchangeAnimationTrackBaseNode)
```

Class to represent an animation on the property of a camera, light, or scene node
The list of supported properties is enumerated in EInterchangeAnimatedProperty.

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeNodes
- **File**: InterchangeAnimationTrackSetNode.h

<a id="unreal.InterchangeAnimationTrackNode.set_custom_property_track"></a>

#### set_custom_property_track

```python
def set_custom_property_track(
        property_track: InterchangePropertyTracks) -> bool
```

x.set_custom_property_track(property_track) -> bool
Set the property animated by this track.

Args:
    property_track (InterchangePropertyTracks): 

Returns:
    bool:

<a id="unreal.InterchangeAnimationTrackNode.set_custom_frame_count"></a>

#### set_custom_frame_count

```python
def set_custom_frame_count(attribute_value: int) -> bool
```

x.set_custom_frame_count(attribute_value) -> bool
Set the number of frames for the animation of this track.

Args:
    attribute_value (int32): 

Returns:
    bool:

<a id="unreal.InterchangeAnimationTrackNode.set_custom_animation_payload_key"></a>

#### set_custom_animation_payload_key

```python
def set_custom_animation_payload_key(
        unique_id: str, type: InterchangeAnimationPayLoadType) -> bool
```

x.set_custom_animation_payload_key(unique_id, type) -> bool
Set the payload key needed to retrieve the animation for this track.

Args:
    unique_id (str): 
    type (InterchangeAnimationPayLoadType): 

Returns:
    bool:

<a id="unreal.InterchangeAnimationTrackNode.set_custom_actor_dependency_uid"></a>

#### set_custom_actor_dependency_uid

```python
def set_custom_actor_dependency_uid(dependency_uid: str) -> bool
```

x.set_custom_actor_dependency_uid(dependency_uid) -> bool
Set the actor dependency to this object.

Args:
    dependency_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeAnimationTrackNode.get_custom_property_track"></a>

#### get_custom_property_track

```python
def get_custom_property_track() -> Optional[InterchangePropertyTracks]
```

x.get_custom_property_track() -> InterchangePropertyTracks or None
Get the property animated by this track.

Returns:
    InterchangePropertyTracks or None: 

    property_track (InterchangePropertyTracks):

<a id="unreal.InterchangeAnimationTrackNode.get_custom_frame_count"></a>

#### get_custom_frame_count

```python
def get_custom_frame_count() -> Optional[int]
```

x.get_custom_frame_count() -> int32 or None
Get the number of frames for the animation of this track.

Returns:
    int32 or None: 

    attribute_value (int32):

<a id="unreal.InterchangeAnimationTrackNode.get_custom_animation_payload_key"></a>

#### get_custom_animation_payload_key

```python
def get_custom_animation_payload_key(
) -> Optional[InterchangeAnimationPayLoadKey]
```

x.get_custom_animation_payload_key() -> InterchangeAnimationPayLoadKey or None
Get the payload key needed to retrieve the animation for this track.

Returns:
    InterchangeAnimationPayLoadKey or None: 

    animation_pay_load_key (InterchangeAnimationPayLoadKey):

<a id="unreal.InterchangeAnimationTrackNode.get_custom_actor_dependency_uid"></a>

#### get_custom_actor_dependency_uid

```python
def get_custom_actor_dependency_uid() -> Optional[str]
```

x.get_custom_actor_dependency_uid() -> str or None
Get the actor dependency to this object.

Returns:
    str or None: 

    dependency_uid (str):

<a id="unreal.InterchangeTransformAnimationTrackNode"></a>