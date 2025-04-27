## AnimNode_RandomPlayer Objects

```python
class AnimNode_RandomPlayer(AnimNode_AssetPlayerRelevancyBase)
```

Anim Node Random Player

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_RandomPlayer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_weight`` (float):  [Read-Write] Last encountered blend weight for this node
- ``entries`` (Array[RandomPlayerSequenceEntry]):  [Read-Write] List of sequences to randomly step through
- ``ignore_for_relevancy_test`` (bool):  [Read-Write] If true, "Relevant anim" nodes that look for the highest weighted animation in a state will ignore this node
- ``shuffle_mode`` (bool):  [Read-Write] When shuffle mode is active we will never loop a sequence beyond MaxLoopCount
  without visiting each sequence in turn (no repeats). Enabling this will ignore
  ChanceToPlay for each entry

<a id="unreal.AnimNode_RandomPlayer.__init__"></a>

#### __init__

```python
def __init__(entries: Array[RandomPlayerSequenceEntry] = [],
             blend_weight: float = 0.000000,
             shuffle_mode: bool = False) -> None
```

<a id="unreal.AnimNode_RandomPlayer.entries"></a>

#### entries

```python
@property
def entries() -> Array[RandomPlayerSequenceEntry]
```

(Array[RandomPlayerSequenceEntry]):  [Read-Write] List of sequences to randomly step through

<a id="unreal.AnimNode_RandomPlayer.entries"></a>

#### entries

```python
@entries.setter
def entries(value: Array[RandomPlayerSequenceEntry]) -> None
```

<a id="unreal.AnimNode_RandomPlayer.blend_weight"></a>

#### blend_weight

```python
@property
def blend_weight() -> float
```

(float):  [Read-Write] Last encountered blend weight for this node

<a id="unreal.AnimNode_RandomPlayer.blend_weight"></a>

#### blend_weight

```python
@blend_weight.setter
def blend_weight(value: float) -> None
```

<a id="unreal.AnimNode_RandomPlayer.shuffle_mode"></a>

#### shuffle_mode

```python
@property
def shuffle_mode() -> bool
```

(bool):  [Read-Write] When shuffle mode is active we will never loop a sequence beyond MaxLoopCount
without visiting each sequence in turn (no repeats). Enabling this will ignore
ChanceToPlay for each entry

<a id="unreal.AnimNode_RandomPlayer.shuffle_mode"></a>

#### shuffle_mode

```python
@shuffle_mode.setter
def shuffle_mode(value: bool) -> None
```

<a id="unreal.AnimNode_RotateRootBone"></a>