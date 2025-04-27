## SequencePlayerLibrary Objects

```python
class SequencePlayerLibrary(BlueprintFunctionLibrary)
```

Exposes operations to be performed on a sequence player anim node
Note: Experimental and subject to change!

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: SequencePlayerLibrary.h

<a id="unreal.SequencePlayerLibrary.set_start_position"></a>

#### set_start_position

```python
@classmethod
def set_start_position(cls, sequence_player: SequencePlayerReference,
                       start_position: float) -> SequencePlayerReference
```

X.set_start_position(sequence_player, start_position) -> SequencePlayerReference
Set the start position of the sequence player.
If this is called from On Become Relevant or On Initial Update then it should be accompanied by a call to
SetAccumulatedTime to achieve the desired effect of resetting the play time of a sequence player.

Args:
    sequence_player (SequencePlayerReference): 
    start_position (float): 

Returns:
    SequencePlayerReference:

<a id="unreal.SequencePlayerLibrary.set_sequence_with_inertial_blending"></a>

#### set_sequence_with_inertial_blending

```python
@classmethod
def set_sequence_with_inertial_blending(
        cls,
        update_context: AnimUpdateContext,
        sequence_player: SequencePlayerReference,
        sequence: AnimSequenceBase,
        blend_time: float = 0.200000) -> SequencePlayerReference
```

X.set_sequence_with_inertial_blending(update_context, sequence_player, sequence, blend_time=0.200000) -> SequencePlayerReference
Set the current sequence of the sequence player with an inertial blend time

Args:
    update_context (AnimUpdateContext): 
    sequence_player (SequencePlayerReference): 
    sequence (AnimSequenceBase): 
    blend_time (float): 

Returns:
    SequencePlayerReference:

<a id="unreal.SequencePlayerLibrary.set_sequence"></a>

#### set_sequence

```python
@classmethod
def set_sequence(cls, sequence_player: SequencePlayerReference,
                 sequence: AnimSequenceBase) -> SequencePlayerReference
```

X.set_sequence(sequence_player, sequence) -> SequencePlayerReference
Set the current sequence of the sequence player

Args:
    sequence_player (SequencePlayerReference): 
    sequence (AnimSequenceBase): 

Returns:
    SequencePlayerReference:

<a id="unreal.SequencePlayerLibrary.set_play_rate"></a>

#### set_play_rate

```python
@classmethod
def set_play_rate(cls, sequence_player: SequencePlayerReference,
                  play_rate: float) -> SequencePlayerReference
```

X.set_play_rate(sequence_player, play_rate) -> SequencePlayerReference
Set the play rate of the sequence player

Args:
    sequence_player (SequencePlayerReference): 
    play_rate (float): 

Returns:
    SequencePlayerReference:

<a id="unreal.SequencePlayerLibrary.set_accumulated_time"></a>

#### set_accumulated_time

```python
@classmethod
def set_accumulated_time(cls, sequence_player: SequencePlayerReference,
                         time: float) -> SequencePlayerReference
```

X.set_accumulated_time(sequence_player, time) -> SequencePlayerReference
Set the current accumulated time of the sequence player

Args:
    sequence_player (SequencePlayerReference): 
    time (float): 

Returns:
    SequencePlayerReference:

<a id="unreal.SequencePlayerLibrary.get_start_position"></a>

#### get_start_position

```python
@classmethod
def get_start_position(cls, sequence_player: SequencePlayerReference) -> float
```

X.get_start_position(sequence_player) -> float
Get the start position of the sequence player

Args:
    sequence_player (SequencePlayerReference): 

Returns:
    float:

<a id="unreal.SequencePlayerLibrary.get_sequence_pure"></a>

#### get_sequence_pure

```python
@classmethod
def get_sequence_pure(
        cls, sequence_player: SequencePlayerReference) -> AnimSequenceBase
```

X.get_sequence_pure(sequence_player) -> AnimSequenceBase
Get the current sequence of the sequence player

Args:
    sequence_player (SequencePlayerReference): 

Returns:
    AnimSequenceBase:

<a id="unreal.SequencePlayerLibrary.get_sequence"></a>

#### get_sequence

```python
@classmethod
def get_sequence(
    cls, sequence_player: SequencePlayerReference,
    sequence_base: AnimSequenceBase
) -> Tuple[SequencePlayerReference, AnimSequenceBase]
```

X.get_sequence(sequence_player, sequence_base) -> (SequencePlayerReference, sequence_base=AnimSequenceBase)
Get the current sequence of the sequence player - DEPRECATED, please use pure version
deprecated: Function 'GetSequence' is deprecated.

Args:
    sequence_player (SequencePlayerReference): 
    sequence_base (AnimSequenceBase): 

Returns:
    AnimSequenceBase: 

    sequence_base (AnimSequenceBase):

<a id="unreal.SequencePlayerLibrary.get_play_rate"></a>

#### get_play_rate

```python
@classmethod
def get_play_rate(cls, sequence_player: SequencePlayerReference) -> float
```

X.get_play_rate(sequence_player) -> float
Get the play rate of the sequence player

Args:
    sequence_player (SequencePlayerReference): 

Returns:
    float:

<a id="unreal.SequencePlayerLibrary.get_loop_animation"></a>

#### get_loop_animation

```python
@classmethod
def get_loop_animation(cls, sequence_player: SequencePlayerReference) -> bool
```

X.get_loop_animation(sequence_player) -> bool
Get the looping state of the sequence player

Args:
    sequence_player (SequencePlayerReference): 

Returns:
    bool:

<a id="unreal.SequencePlayerLibrary.get_accumulated_time"></a>

#### get_accumulated_time

```python
@classmethod
def get_accumulated_time(cls,
                         sequence_player: SequencePlayerReference) -> float
```

X.get_accumulated_time(sequence_player) -> float
Gets the current accumulated time of the sequence player

Args:
    sequence_player (SequencePlayerReference): 

Returns:
    float:

<a id="unreal.SequencePlayerLibrary.convert_to_sequence_player_pure"></a>

#### convert_to_sequence_player_pure

```python
@classmethod
def convert_to_sequence_player_pure(
        cls, node: AnimNodeReference) -> Tuple[SequencePlayerReference, bool]
```

X.convert_to_sequence_player_pure(node) -> (sequence_player=SequencePlayerReference, result=bool)
Get a sequence player context from an anim node context (pure)

Args:
    node (AnimNodeReference): 

Returns:
    tuple: 

    sequence_player (SequencePlayerReference): 

    result (bool):

<a id="unreal.SequencePlayerLibrary.convert_to_sequence_player"></a>

#### convert_to_sequence_player

```python
@classmethod
def convert_to_sequence_player(
    cls, node: AnimNodeReference
) -> Tuple[SequencePlayerReference, AnimNodeReferenceConversionResult]
```

X.convert_to_sequence_player(node) -> (SequencePlayerReference, result=AnimNodeReferenceConversionResult)
Get a sequence player context from an anim node context

Args:
    node (AnimNodeReference): 

Returns:
    AnimNodeReferenceConversionResult: 

    result (AnimNodeReferenceConversionResult):

<a id="unreal.SequencePlayerLibrary.compute_play_rate_from_duration"></a>

#### compute_play_rate_from_duration

```python
@classmethod
def compute_play_rate_from_duration(cls,
                                    sequence_player: SequencePlayerReference,
                                    duration: float = 1.000000) -> float
```

X.compute_play_rate_from_duration(sequence_player, duration=1.000000) -> float
Returns the Play Rate to provide when playing this animation if a specific animation duration is desired

Args:
    sequence_player (SequencePlayerReference): 
    duration (float): 

Returns:
    float:

<a id="unreal.SkeletalControlLibrary"></a>