## RandomPlayerSequenceEntry Objects

```python
class RandomPlayerSequenceEntry(StructBase)
```

The random player node holds a list of sequences and parameter ranges which will be played continuously
In a random order. If shuffle mode is enabled then each entry will be played once before repeating any

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_RandomPlayer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_in`` (AlphaBlend):  [Read-Write] Blending properties used when this entry is blending in ontop of another entry
- ``chance_to_play`` (float):  [Read-Write] When not in shuffle mode, this is the chance this entry will play (normalized against all other sample chances)
- ``max_loop_count`` (int32):  [Read-Write] Maximum number of times this entry will loop before ending
- ``max_play_rate`` (float):  [Read-Write] Maximum playrate for this entry
- ``min_loop_count`` (int32):  [Read-Write] Minimum number of times this entry will loop before ending
- ``min_play_rate`` (float):  [Read-Write] Minimum playrate for this entry
- ``sequence`` (AnimSequenceBase):  [Read-Write] Sequence to play when this entry is picked

<a id="unreal.RandomPlayerSequenceEntry.__init__"></a>

#### __init__

```python
def __init__(sequence: AnimSequenceBase = None,
             chance_to_play: float = 0.000000,
             min_loop_count: int = 0,
             max_loop_count: int = 0,
             min_play_rate: float = 0.000000,
             max_play_rate: float = 0.000000) -> None
```

<a id="unreal.RandomPlayerSequenceEntry.sequence"></a>

#### sequence

```python
@property
def sequence() -> AnimSequenceBase
```

(AnimSequenceBase):  [Read-Write] Sequence to play when this entry is picked

<a id="unreal.RandomPlayerSequenceEntry.sequence"></a>

#### sequence

```python
@sequence.setter
def sequence(value: AnimSequenceBase) -> None
```

<a id="unreal.RandomPlayerSequenceEntry.chance_to_play"></a>

#### chance_to_play

```python
@property
def chance_to_play() -> float
```

(float):  [Read-Write] When not in shuffle mode, this is the chance this entry will play (normalized against all other sample chances)

<a id="unreal.RandomPlayerSequenceEntry.chance_to_play"></a>

#### chance_to_play

```python
@chance_to_play.setter
def chance_to_play(value: float) -> None
```

<a id="unreal.RandomPlayerSequenceEntry.min_loop_count"></a>

#### min_loop_count

```python
@property
def min_loop_count() -> int
```

(int32):  [Read-Write] Minimum number of times this entry will loop before ending

<a id="unreal.RandomPlayerSequenceEntry.min_loop_count"></a>

#### min_loop_count

```python
@min_loop_count.setter
def min_loop_count(value: int) -> None
```

<a id="unreal.RandomPlayerSequenceEntry.max_loop_count"></a>

#### max_loop_count

```python
@property
def max_loop_count() -> int
```

(int32):  [Read-Write] Maximum number of times this entry will loop before ending

<a id="unreal.RandomPlayerSequenceEntry.max_loop_count"></a>

#### max_loop_count

```python
@max_loop_count.setter
def max_loop_count(value: int) -> None
```

<a id="unreal.RandomPlayerSequenceEntry.min_play_rate"></a>

#### min_play_rate

```python
@property
def min_play_rate() -> float
```

(float):  [Read-Write] Minimum playrate for this entry

<a id="unreal.RandomPlayerSequenceEntry.min_play_rate"></a>

#### min_play_rate

```python
@min_play_rate.setter
def min_play_rate(value: float) -> None
```

<a id="unreal.RandomPlayerSequenceEntry.max_play_rate"></a>

#### max_play_rate

```python
@property
def max_play_rate() -> float
```

(float):  [Read-Write] Maximum playrate for this entry

<a id="unreal.RandomPlayerSequenceEntry.max_play_rate"></a>

#### max_play_rate

```python
@max_play_rate.setter
def max_play_rate(value: float) -> None
```

<a id="unreal.AnimNode_RandomPlayer"></a>