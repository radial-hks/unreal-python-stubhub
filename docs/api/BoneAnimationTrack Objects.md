## BoneAnimationTrack Objects

```python
class BoneAnimationTrack(StructBase)
```

Structure encapsulating a single bone animation track.

**C++ Source:**

- **Module**: Engine
- **File**: IAnimationDataModel.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone_tree_index`` (int32):  [Read-Only] Index corresponding to the bone this track corresponds to within the target USkeleton
- ``internal_track_data`` (RawAnimSequenceTrack):  [Read-Only] Internally stored data representing the animation bone data
- ``name`` (Name):  [Read-Only] Name of the bone this track corresponds to

<a id="unreal.BoneAnimationTrack.__init__"></a>

#### __init__

```python
def __init__(internal_track_data: RawAnimSequenceTrack = [],
             bone_tree_index: int = 0,
             name: Name = "None") -> None
```

<a id="unreal.BoneAnimationTrack.internal_track_data"></a>

#### internal_track_data

```python
@property
def internal_track_data() -> RawAnimSequenceTrack
```

(RawAnimSequenceTrack):  [Read-Only] Internally stored data representing the animation bone data

<a id="unreal.BoneAnimationTrack.bone_tree_index"></a>

#### bone_tree_index

```python
@property
def bone_tree_index() -> int
```

(int32):  [Read-Only] Index corresponding to the bone this track corresponds to within the target USkeleton

<a id="unreal.BoneAnimationTrack.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Only] Name of the bone this track corresponds to

<a id="unreal.AnimationCurveData"></a>