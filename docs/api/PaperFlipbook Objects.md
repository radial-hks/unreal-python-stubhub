## PaperFlipbook Objects

```python
class PaperFlipbook(Object)
```

Contains an animation sequence of sprite frames

**C++ Source:**

- **Plugin**: Paper2D
- **Module**: Paper2D
- **File**: PaperFlipbook.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collision_source`` (FlipbookCollisionMode):  [Read-Write] Collision source
- ``default_material`` (MaterialInterface):  [Read-Write] The material to use on a flipbook player instance if not overridden
- ``frames_per_second`` (float):  [Read-Write] The nominal frame rate to play this flipbook animation back at
- ``key_frames`` (Array[PaperFlipbookKeyFrame]):  [Read-Write] The set of key frames for this flipbook animation (each one has a duration and a sprite to display)

<a id="unreal.PaperFlipbook.frames_per_second"></a>

#### frames_per_second

```python
@property
def frames_per_second() -> float
```

(float):  [Read-Only] The nominal frame rate to play this flipbook animation back at

<a id="unreal.PaperFlipbook.default_material"></a>

#### default_material

```python
@property
def default_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Only] The material to use on a flipbook player instance if not overridden

<a id="unreal.PaperFlipbook.collision_source"></a>

#### collision_source

```python
@property
def collision_source() -> FlipbookCollisionMode
```

(FlipbookCollisionMode):  [Read-Only] Collision source

<a id="unreal.PaperFlipbook.is_valid_key_frame_index"></a>

#### is_valid_key_frame_index

```python
def is_valid_key_frame_index(index: int) -> bool
```

x.is_valid_key_frame_index(index) -> bool
Is the specified Index within the valid range of key frames?

Args:
    index (int32): 

Returns:
    bool:

<a id="unreal.PaperFlipbook.get_total_duration"></a>

#### get_total_duration

```python
def get_total_duration() -> float
```

x.get_total_duration() -> float
Returns the total duration in seconds

Returns:
    float:

<a id="unreal.PaperFlipbook.get_sprite_at_time"></a>

#### get_sprite_at_time

```python
def get_sprite_at_time(time: float,
                       clamp_to_ends: bool = False) -> PaperSprite
```

x.get_sprite_at_time(time, clamp_to_ends=False) -> PaperSprite
Returns the sprite at the specified time (in seconds), or nullptr if none exists.
When bClampToEnds is true, it will choose the first or last sprite if the time is out of range.

Args:
    time (float): 
    clamp_to_ends (bool): 

Returns:
    PaperSprite:

<a id="unreal.PaperFlipbook.get_sprite_at_frame"></a>

#### get_sprite_at_frame

```python
def get_sprite_at_frame(frame_index: int) -> PaperSprite
```

x.get_sprite_at_frame(frame_index) -> PaperSprite
Returns the sprite at the specified keyframe index, or nullptr if none exists

Args:
    frame_index (int32): 

Returns:
    PaperSprite:

<a id="unreal.PaperFlipbook.get_num_key_frames"></a>

#### get_num_key_frames

```python
def get_num_key_frames() -> int
```

x.get_num_key_frames() -> int32
Returns the number of key frames

Returns:
    int32:

<a id="unreal.PaperFlipbook.get_num_frames"></a>

#### get_num_frames

```python
def get_num_frames() -> int
```

x.get_num_frames() -> int32
Returns the total number of frames

Returns:
    int32:

<a id="unreal.PaperFlipbook.get_key_frame_index_at_time"></a>

#### get_key_frame_index_at_time

```python
def get_key_frame_index_at_time(time: float,
                                clamp_to_ends: bool = False) -> int
```

x.get_key_frame_index_at_time(time, clamp_to_ends=False) -> int32
Returns the keyframe index that covers the specified time (in seconds), or INDEX_NONE if none exists.
When bClampToEnds is true, it will choose the first or last keyframe if the time is out of range.

Args:
    time (float): 
    clamp_to_ends (bool): 

Returns:
    int32:

<a id="unreal.PaperFlipbookActor"></a>