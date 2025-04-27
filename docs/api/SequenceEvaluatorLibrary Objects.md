## SequenceEvaluatorLibrary Objects

```python
class SequenceEvaluatorLibrary(BlueprintFunctionLibrary)
```

Exposes operations to be performed on a sequence evaluator anim node
Note: Experimental and subject to change!

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: SequenceEvaluatorLibrary.h

<a id="unreal.SequenceEvaluatorLibrary.set_sequence_with_inertial_blending"></a>

#### set_sequence_with_inertial_blending

```python
@classmethod
def set_sequence_with_inertial_blending(
        cls,
        update_context: AnimUpdateContext,
        sequence_evaluator: SequenceEvaluatorReference,
        sequence: AnimSequenceBase,
        blend_time: float = 0.200000) -> SequenceEvaluatorReference
```

X.set_sequence_with_inertial_blending(update_context, sequence_evaluator, sequence, blend_time=0.200000) -> SequenceEvaluatorReference
Set the current sequence of the sequence evaluator with an inertial blend time

Args:
    update_context (AnimUpdateContext): 
    sequence_evaluator (SequenceEvaluatorReference): 
    sequence (AnimSequenceBase): 
    blend_time (float): 

Returns:
    SequenceEvaluatorReference:

<a id="unreal.SequenceEvaluatorLibrary.set_sequence"></a>

#### set_sequence

```python
@classmethod
def set_sequence(cls, sequence_evaluator: SequenceEvaluatorReference,
                 sequence: AnimSequenceBase) -> SequenceEvaluatorReference
```

X.set_sequence(sequence_evaluator, sequence) -> SequenceEvaluatorReference
Set the current sequence of the sequence evaluator

Args:
    sequence_evaluator (SequenceEvaluatorReference): 
    sequence (AnimSequenceBase): 

Returns:
    SequenceEvaluatorReference:

<a id="unreal.SequenceEvaluatorLibrary.set_explicit_time"></a>

#### set_explicit_time

```python
@classmethod
def set_explicit_time(cls, sequence_evaluator: SequenceEvaluatorReference,
                      time: float) -> SequenceEvaluatorReference
```

X.set_explicit_time(sequence_evaluator, time) -> SequenceEvaluatorReference
Set the current accumulated time of the sequence evaluator

Args:
    sequence_evaluator (SequenceEvaluatorReference): 
    time (float): 

Returns:
    SequenceEvaluatorReference:

<a id="unreal.SequenceEvaluatorLibrary.set_explicit_frame"></a>

#### set_explicit_frame

```python
@classmethod
def set_explicit_frame(cls, sequence_evaluator: SequenceEvaluatorReference,
                       frame: int) -> SequenceEvaluatorReference
```

X.set_explicit_frame(sequence_evaluator, frame) -> SequenceEvaluatorReference
Set the current accumulated time, using a frame number, of the sequence evaluator

Args:
    sequence_evaluator (SequenceEvaluatorReference): 
    frame (int32): 

Returns:
    SequenceEvaluatorReference:

<a id="unreal.SequenceEvaluatorLibrary.get_sequence"></a>

#### get_sequence

```python
@classmethod
def get_sequence(
        cls,
        sequence_evaluator: SequenceEvaluatorReference) -> AnimSequenceBase
```

X.get_sequence(sequence_evaluator) -> AnimSequenceBase
Gets the current sequence of the sequence evaluator

Args:
    sequence_evaluator (SequenceEvaluatorReference): 

Returns:
    AnimSequenceBase:

<a id="unreal.SequenceEvaluatorLibrary.get_accumulated_time"></a>

#### get_accumulated_time

```python
@classmethod
def get_accumulated_time(
        cls, sequence_evaluator: SequenceEvaluatorReference) -> float
```

X.get_accumulated_time(sequence_evaluator) -> float
Gets the current accumulated time of the sequence evaluator

Args:
    sequence_evaluator (SequenceEvaluatorReference): 

Returns:
    float:

<a id="unreal.SequenceEvaluatorLibrary.convert_to_sequence_evaluator_pure"></a>

#### convert_to_sequence_evaluator_pure

```python
@classmethod
def convert_to_sequence_evaluator_pure(
        cls,
        node: AnimNodeReference) -> Tuple[SequenceEvaluatorReference, bool]
```

X.convert_to_sequence_evaluator_pure(node) -> (sequence_evaluator=SequenceEvaluatorReference, result=bool)
Get a sequence evaluator context from an anim node context (pure)

Args:
    node (AnimNodeReference): 

Returns:
    tuple: 

    sequence_evaluator (SequenceEvaluatorReference): 

    result (bool):

<a id="unreal.SequenceEvaluatorLibrary.convert_to_sequence_evaluator"></a>

#### convert_to_sequence_evaluator

```python
@classmethod
def convert_to_sequence_evaluator(
    cls, node: AnimNodeReference
) -> Tuple[SequenceEvaluatorReference, AnimNodeReferenceConversionResult]
```

X.convert_to_sequence_evaluator(node) -> (SequenceEvaluatorReference, result=AnimNodeReferenceConversionResult)
Get a sequence evaluator context from an anim node context

Args:
    node (AnimNodeReference): 

Returns:
    AnimNodeReferenceConversionResult: 

    result (AnimNodeReferenceConversionResult):

<a id="unreal.SequenceEvaluatorLibrary.advance_time"></a>

#### advance_time

```python
@classmethod
def advance_time(cls,
                 update_context: AnimUpdateContext,
                 sequence_evaluator: SequenceEvaluatorReference,
                 play_rate: float = 1.000000) -> SequenceEvaluatorReference
```

X.advance_time(update_context, sequence_evaluator, play_rate=1.000000) -> SequenceEvaluatorReference
Advance the current accumulated time of the sequence evaluator

Args:
    update_context (AnimUpdateContext): 
    sequence_evaluator (SequenceEvaluatorReference): 
    play_rate (float): 

Returns:
    SequenceEvaluatorReference:

<a id="unreal.SequencePlayerLibrary"></a>