## AnimationStateMachineLibrary Objects

```python
class AnimationStateMachineLibrary(BlueprintFunctionLibrary)
```

Exposes operations to be performed on anim state machine node contexts

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimationStateMachineLibrary.h

<a id="unreal.AnimationStateMachineLibrary.set_state"></a>

#### set_state

```python
@classmethod
def set_state(cls, update_context: AnimUpdateContext,
              node: AnimationStateMachineReference, target_state: Name,
              duration: float, blend_type: TransitionLogicType,
              blend_profile: BlendProfile,
              alpha_blend_option: AlphaBlendOption,
              custom_blend_curve: CurveFloat) -> None
```

X.set_state(update_context, node, target_state, duration, blend_type, blend_profile, alpha_blend_option, custom_blend_curve) -> None
Manually set the current state of the state machine
              NOTE: Custom blend type is not supported

Args:
    update_context (AnimUpdateContext): 
    node (AnimationStateMachineReference): 
    target_state (Name): 
    duration (float): 
    blend_type (TransitionLogicType): 
    blend_profile (BlendProfile): 
    alpha_blend_option (AlphaBlendOption): 
    custom_blend_curve (CurveFloat):

<a id="unreal.AnimationStateMachineLibrary.is_state_blending_out"></a>

#### is_state_blending_out

```python
@classmethod
def is_state_blending_out(cls, update_context: AnimUpdateContext,
                          node: AnimationStateResultReference) -> bool
```

X.is_state_blending_out(update_context, node) -> bool
Returns whether the state the node belongs to is blending out

Args:
    update_context (AnimUpdateContext): 
    node (AnimationStateResultReference): 

Returns:
    bool:

<a id="unreal.AnimationStateMachineLibrary.is_state_blending_in"></a>

#### is_state_blending_in

```python
@classmethod
def is_state_blending_in(cls, update_context: AnimUpdateContext,
                         node: AnimationStateResultReference) -> bool
```

X.is_state_blending_in(update_context, node) -> bool
Returns whether the state the node belongs to is blending in

Args:
    update_context (AnimUpdateContext): 
    node (AnimationStateResultReference): 

Returns:
    bool:

<a id="unreal.AnimationStateMachineLibrary.get_state"></a>

#### get_state

```python
@classmethod
def get_state(cls, update_context: AnimUpdateContext,
              node: AnimationStateMachineReference) -> Name
```

X.get_state(update_context, node) -> Name
Returns the name of the current state of this state machine

Args:
    update_context (AnimUpdateContext): 
    node (AnimationStateMachineReference): 

Returns:
    Name:

<a id="unreal.AnimationStateMachineLibrary.get_relevant_anim_time_remaining_fraction"></a>

#### get_relevant_anim_time_remaining_fraction

```python
@classmethod
def get_relevant_anim_time_remaining_fraction(
        cls, update_context: AnimUpdateContext,
        node: AnimationStateResultReference) -> float
```

X.get_relevant_anim_time_remaining_fraction(update_context, node) -> float
Returns the remaining animation time as a fraction of the duration for the state's most relevant asset player

Args:
    update_context (AnimUpdateContext): 
    node (AnimationStateResultReference): 

Returns:
    float:

<a id="unreal.AnimationStateMachineLibrary.get_relevant_anim_time_remaining"></a>

#### get_relevant_anim_time_remaining

```python
@classmethod
def get_relevant_anim_time_remaining(
        cls, update_context: AnimUpdateContext,
        node: AnimationStateResultReference) -> float
```

X.get_relevant_anim_time_remaining(update_context, node) -> float
Returns the remaining animation time of the state's most relevant asset player

Args:
    update_context (AnimUpdateContext): 
    node (AnimationStateResultReference): 

Returns:
    float:

<a id="unreal.AnimationStateMachineLibrary.convert_to_animation_state_result_pure"></a>

#### convert_to_animation_state_result_pure

```python
@classmethod
def convert_to_animation_state_result_pure(
        cls,
        node: AnimNodeReference) -> Tuple[AnimationStateResultReference, bool]
```

X.convert_to_animation_state_result_pure(node) -> (animation_state=AnimationStateResultReference, result=bool)
Get an anim state reference from an anim node reference (pure)

Args:
    node (AnimNodeReference): 

Returns:
    tuple: 

    animation_state (AnimationStateResultReference): 

    result (bool):

<a id="unreal.AnimationStateMachineLibrary.convert_to_animation_state_result"></a>

#### convert_to_animation_state_result

```python
@classmethod
def convert_to_animation_state_result(
    cls, node: AnimNodeReference
) -> Tuple[AnimationStateResultReference, AnimNodeReferenceConversionResult]
```

X.convert_to_animation_state_result(node) -> (animation_state=AnimationStateResultReference, result=AnimNodeReferenceConversionResult)
Get an anim state reference from an anim node reference

Args:
    node (AnimNodeReference): 

Returns:
    tuple: 

    animation_state (AnimationStateResultReference): 

    result (AnimNodeReferenceConversionResult):

<a id="unreal.AnimationStateMachineLibrary.convert_to_animation_state_machine_pure"></a>

#### convert_to_animation_state_machine_pure

```python
@classmethod
def convert_to_animation_state_machine_pure(
        cls, node: AnimNodeReference
) -> Tuple[AnimationStateMachineReference, bool]
```

X.convert_to_animation_state_machine_pure(node) -> (animation_state=AnimationStateMachineReference, result=bool)
Get an anim state machine from an anim node reference (pure)

Args:
    node (AnimNodeReference): 

Returns:
    tuple: 

    animation_state (AnimationStateMachineReference): 

    result (bool):

<a id="unreal.AnimationStateMachineLibrary.convert_to_animation_state_machine"></a>

#### convert_to_animation_state_machine

```python
@classmethod
def convert_to_animation_state_machine(
    cls, node: AnimNodeReference
) -> Tuple[AnimationStateMachineReference, AnimNodeReferenceConversionResult]
```

X.convert_to_animation_state_machine(node) -> (animation_state=AnimationStateMachineReference, result=AnimNodeReferenceConversionResult)
Get an anim state machine from an anim node reference

Args:
    node (AnimNodeReference): 

Returns:
    tuple: 

    animation_state (AnimationStateMachineReference): 

    result (AnimNodeReferenceConversionResult):

<a id="unreal.AnimExecutionContextLibrary"></a>