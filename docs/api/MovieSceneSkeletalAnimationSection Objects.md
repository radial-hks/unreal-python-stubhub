## MovieSceneSkeletalAnimationSection Objects

```python
class MovieSceneSkeletalAnimationSection(MovieSceneSection)
```

Movie scene section that control skeletal animation

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieSceneSkeletalAnimationSection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color_tint`` (Color):  [Read-Write] The color tint for this section
- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this section evaluates at runtime.
- ``easing`` (MovieSceneEasingSettings):  [Read-Write]
- ``eval_options`` (MovieSceneSectionEvalOptions):  [Read-Write]
- ``is_active`` (bool):  [Read-Write] Toggle whether this section is active/inactive
- ``is_locked`` (bool):  [Read-Write] Toggle whether this section is locked/unlocked
- ``matched_location_offset`` (Vector):  [Read-Only] Location offset determined by matching
- ``matched_rotation_offset`` (Rotator):  [Read-Only] Rotation offset determined by matching
- ``params`` (MovieSceneSkeletalAnimationParams):  [Read-Write]
- ``post_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to continue 'postrolling' this section for after evaluation has ended.
- ``pre_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to prepare this section for evaluation before it actually starts.
- ``section_range`` (MovieSceneFrameRange):  [Read-Write] The range in which this section is active
- ``show_skeleton`` (bool):  [Read-Write] Whether to show the underlying skeleton for this section.
- ``start_location_offset`` (Vector):  [Read-Write] Location offset applied before the matched offset
- ``start_rotation_offset`` (Rotator):  [Read-Write] Location offset applied after the matched offset
- ``timecode_source`` (MovieSceneTimecodeSource):  [Read-Write] The timecode at which this movie scene section is based (ie. when it was recorded)

<a id="unreal.MovieSceneSkeletalAnimationSection.params"></a>

#### params

```python
@property
def params() -> MovieSceneSkeletalAnimationParams
```

(MovieSceneSkeletalAnimationParams):  [Read-Write]

<a id="unreal.MovieSceneSkeletalAnimationSection.params"></a>

#### params

```python
@params.setter
def params(value: MovieSceneSkeletalAnimationParams) -> None
```

<a id="unreal.MovieSceneSkeletalAnimationSection.start_location_offset"></a>

#### start_location_offset

```python
@property
def start_location_offset() -> Vector
```

(Vector):  [Read-Write] Location offset applied before the matched offset

<a id="unreal.MovieSceneSkeletalAnimationSection.start_location_offset"></a>

#### start_location_offset

```python
@start_location_offset.setter
def start_location_offset(value: Vector) -> None
```

<a id="unreal.MovieSceneSkeletalAnimationSection.start_rotation_offset"></a>

#### start_rotation_offset

```python
@property
def start_rotation_offset() -> Rotator
```

(Rotator):  [Read-Write] Location offset applied after the matched offset

<a id="unreal.MovieSceneSkeletalAnimationSection.start_rotation_offset"></a>

#### start_rotation_offset

```python
@start_rotation_offset.setter
def start_rotation_offset(value: Rotator) -> None
```

<a id="unreal.MovieSceneSkeletalAnimationSection.matched_location_offset"></a>

#### matched_location_offset

```python
@property
def matched_location_offset() -> Vector
```

(Vector):  [Read-Only] Location offset determined by matching

<a id="unreal.MovieSceneSkeletalAnimationSection.matched_rotation_offset"></a>

#### matched_rotation_offset

```python
@property
def matched_rotation_offset() -> Rotator
```

(Rotator):  [Read-Only] Rotation offset determined by matching

<a id="unreal.MovieSceneSkeletalAnimationSection.show_skeleton"></a>

#### show_skeleton

```python
@property
def show_skeleton() -> bool
```

(bool):  [Read-Write] Whether to show the underlying skeleton for this section.

<a id="unreal.MovieSceneSkeletalAnimationSection.show_skeleton"></a>

#### show_skeleton

```python
@show_skeleton.setter
def show_skeleton(value: bool) -> None
```

<a id="unreal.MovieSceneSlomoSection"></a>