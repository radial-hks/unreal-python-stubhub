## InterchangeSkeletalAnimationTrackNode Objects

```python
class InterchangeSkeletalAnimationTrackNode(InterchangeAnimationTrackBaseNode)
```

* Class to hold onto the relationships between a set of animation tracks and the bones, morph targets of a skeleton.

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeNodes
- **File**: InterchangeAnimationTrackSetNode.h

<a id="unreal.InterchangeSkeletalAnimationTrackNode.set_custom_skeleton_node_uid"></a>

#### set_custom_skeleton_node_uid

```python
def set_custom_skeleton_node_uid(attribute_value: str) -> bool
```

x.set_custom_skeleton_node_uid(attribute_value) -> bool
Set the unique ID of the skeleton factory node. Return false if the attribute could not be set.

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeSkeletalAnimationTrackNode.set_custom_animation_stop_time"></a>

#### set_custom_animation_stop_time

```python
def set_custom_animation_stop_time(stop_time: float) -> bool
```

x.set_custom_animation_stop_time(stop_time) -> bool
Set the animation stop time. Return false if the attribute could not be set.

Args:
    stop_time (double): 

Returns:
    bool:

<a id="unreal.InterchangeSkeletalAnimationTrackNode.set_custom_animation_start_time"></a>

#### set_custom_animation_start_time

```python
def set_custom_animation_start_time(start_time: float) -> bool
```

x.set_custom_animation_start_time(start_time) -> bool
Set the animation start time. Return false if the attribute could not be set.

Args:
    start_time (double): 

Returns:
    bool:

<a id="unreal.InterchangeSkeletalAnimationTrackNode.set_custom_animation_sample_rate"></a>

#### set_custom_animation_sample_rate

```python
def set_custom_animation_sample_rate(sample_rate: float) -> bool
```

x.set_custom_animation_sample_rate(sample_rate) -> bool
Set the animation sample rate. Return false if the attribute could not be set.

Args:
    sample_rate (double): 

Returns:
    bool:

<a id="unreal.InterchangeSkeletalAnimationTrackNode.set_animation_payload_key_for_scene_node_uid"></a>

#### set_animation_payload_key_for_scene_node_uid

```python
def set_animation_payload_key_for_scene_node_uid(
        scene_node_uid: str, unique_id: str,
        type: InterchangeAnimationPayLoadType) -> bool
```

x.set_animation_payload_key_for_scene_node_uid(scene_node_uid, unique_id, type) -> bool
Set Animation Payload Key for Scene Node Uid

Args:
    scene_node_uid (str): 
    unique_id (str): 
    type (InterchangeAnimationPayLoadType): 

Returns:
    bool:

<a id="unreal.InterchangeSkeletalAnimationTrackNode.set_animation_payload_key_for_morph_target_node_uid"></a>

#### set_animation_payload_key_for_morph_target_node_uid

```python
def set_animation_payload_key_for_morph_target_node_uid(
        morph_target_node_uid: str, unique_id: str,
        type: InterchangeAnimationPayLoadType) -> bool
```

x.set_animation_payload_key_for_morph_target_node_uid(morph_target_node_uid, unique_id, type) -> bool
Set Animation Payload Key for Morph Target Node Uid

Args:
    morph_target_node_uid (str): 
    unique_id (str): 
    type (InterchangeAnimationPayLoadType): 

Returns:
    bool:

<a id="unreal.InterchangeSkeletalAnimationTrackNode.is_node_animated_with_baked_curve"></a>

#### is_node_animated_with_baked_curve

```python
def is_node_animated_with_baked_curve(scene_node_uid: str) -> bool
```

x.is_node_animated_with_baked_curve(scene_node_uid) -> bool
Is Node Animated with Baked Curve

Args:
    scene_node_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeSkeletalAnimationTrackNode.get_scene_node_animation_payload_keys"></a>

#### get_scene_node_animation_payload_keys

```python
def get_scene_node_animation_payload_keys(
) -> Tuple[Map[str, str], Map[str, int]]
```

x.get_scene_node_animation_payload_keys() -> (out_scene_node_animation_payload_key_uids=Map[str, str], out_scene_node_animation_payload_key_types=Map[str, uint8])
Get Scene Node Animation Payload Keys

Returns:
    tuple: 

    out_scene_node_animation_payload_key_uids (Map[str, str]): 

    out_scene_node_animation_payload_key_types (Map[str, uint8]):

<a id="unreal.InterchangeSkeletalAnimationTrackNode.get_morph_target_node_animation_payload_keys"></a>

#### get_morph_target_node_animation_payload_keys

```python
def get_morph_target_node_animation_payload_keys(
) -> Tuple[Map[str, str], Map[str, int]]
```

x.get_morph_target_node_animation_payload_keys() -> (out_morph_target_node_animation_payload_key_uids=Map[str, str], out_morph_target_node_animation_payload_key_types=Map[str, uint8])
Get Morph Target Node Animation Payload Keys

Returns:
    tuple: 

    out_morph_target_node_animation_payload_key_uids (Map[str, str]): 

    out_morph_target_node_animation_payload_key_types (Map[str, uint8]):

<a id="unreal.InterchangeSkeletalAnimationTrackNode.get_custom_skeleton_node_uid"></a>

#### get_custom_skeleton_node_uid

```python
def get_custom_skeleton_node_uid() -> Optional[str]
```

x.get_custom_skeleton_node_uid() -> str or None
Get the unique ID of the skeleton factory node. Return false if the attribute is not set.

Returns:
    str or None: 

    attribute_value (str):

<a id="unreal.InterchangeSkeletalAnimationTrackNode.get_custom_animation_stop_time"></a>

#### get_custom_animation_stop_time

```python
def get_custom_animation_stop_time() -> Optional[float]
```

x.get_custom_animation_stop_time() -> double or None
Get the animation stop time. Return false if the attribute is not set.

Returns:
    double or None: 

    stop_time (double):

<a id="unreal.InterchangeSkeletalAnimationTrackNode.get_custom_animation_start_time"></a>

#### get_custom_animation_start_time

```python
def get_custom_animation_start_time() -> Optional[float]
```

x.get_custom_animation_start_time() -> double or None
Get the animation start time. Return false if the attribute is not set.

Returns:
    double or None: 

    start_time (double):

<a id="unreal.InterchangeSkeletalAnimationTrackNode.get_custom_animation_sample_rate"></a>

#### get_custom_animation_sample_rate

```python
def get_custom_animation_sample_rate() -> Optional[float]
```

x.get_custom_animation_sample_rate() -> double or None
Get the animation sample rate. Return false if the attribute is not set.

Returns:
    double or None: 

    sample_rate (double):

<a id="unreal.InterchangePhysicalCameraNode"></a>