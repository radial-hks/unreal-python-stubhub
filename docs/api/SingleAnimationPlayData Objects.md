## SingleAnimationPlayData Objects

```python
class SingleAnimationPlayData(StructBase)
```

Single Animation Play Data

**C++ Source:**

- **Module**: Engine
- **File**: SingleAnimationPlayData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``anim_to_play`` (AnimationAsset):  [Read-Write]
  todo: in the future, we should make this one UObject and have detail customization to display different things The default sequence to play on this skeletal mesh
- ``saved_looping`` (bool):  [Read-Write] Default setting for looping for SequenceToPlay. This is not current state of looping.
- ``saved_play_rate`` (float):  [Read-Write] Default setting for play rate of SequenceToPlay to play.
- ``saved_playing`` (bool):  [Read-Write] Default setting for playing for SequenceToPlay. This is not current state of playing.
- ``saved_position`` (float):  [Read-Write] Default setting for position of SequenceToPlay to play.

<a id="unreal.SingleAnimationPlayData.__init__"></a>

#### __init__

```python
def __init__(anim_to_play: AnimationAsset = None,
             saved_looping: bool = False,
             saved_playing: bool = False,
             saved_position: float = 0.000000,
             saved_play_rate: float = 0.000000) -> None
```

<a id="unreal.SingleAnimationPlayData.anim_to_play"></a>

#### anim_to_play

```python
@property
def anim_to_play() -> AnimationAsset
```

(AnimationAsset):  [Read-Write]
todo: in the future, we should make this one UObject and have detail customization to display different things The default sequence to play on this skeletal mesh

<a id="unreal.SingleAnimationPlayData.anim_to_play"></a>

#### anim_to_play

```python
@anim_to_play.setter
def anim_to_play(value: AnimationAsset) -> None
```

<a id="unreal.SingleAnimationPlayData.saved_looping"></a>

#### saved_looping

```python
@property
def saved_looping() -> bool
```

(bool):  [Read-Write] Default setting for looping for SequenceToPlay. This is not current state of looping.

<a id="unreal.SingleAnimationPlayData.saved_looping"></a>

#### saved_looping

```python
@saved_looping.setter
def saved_looping(value: bool) -> None
```

<a id="unreal.SingleAnimationPlayData.saved_playing"></a>

#### saved_playing

```python
@property
def saved_playing() -> bool
```

(bool):  [Read-Write] Default setting for playing for SequenceToPlay. This is not current state of playing.

<a id="unreal.SingleAnimationPlayData.saved_playing"></a>

#### saved_playing

```python
@saved_playing.setter
def saved_playing(value: bool) -> None
```

<a id="unreal.SingleAnimationPlayData.saved_position"></a>

#### saved_position

```python
@property
def saved_position() -> float
```

(float):  [Read-Write] Default setting for position of SequenceToPlay to play.

<a id="unreal.SingleAnimationPlayData.saved_position"></a>

#### saved_position

```python
@saved_position.setter
def saved_position(value: float) -> None
```

<a id="unreal.SingleAnimationPlayData.saved_play_rate"></a>

#### saved_play_rate

```python
@property
def saved_play_rate() -> float
```

(float):  [Read-Write] Default setting for play rate of SequenceToPlay to play.

<a id="unreal.SingleAnimationPlayData.saved_play_rate"></a>

#### saved_play_rate

```python
@saved_play_rate.setter
def saved_play_rate(value: float) -> None
```

<a id="unreal.SkelMeshMergeSectionMapping"></a>