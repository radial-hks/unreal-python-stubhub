## BlendStackInputAnimNodeLibrary Objects

```python
class BlendStackInputAnimNodeLibrary(BlueprintFunctionLibrary)
```

Exposes operations that can be run on a Blend Stack node via Anim Node Functions such as "On Become Relevant" and "On Update".

**C++ Source:**

- **Plugin**: BlendStack
- **Module**: BlendStack
- **File**: BlendStackInputAnimNodeLibrary.h

<a id="unreal.BlendStackInputAnimNodeLibrary.get_properties"></a>

#### get_properties

```python
@classmethod
def get_properties(
    cls, blend_stack_input_node: BlendStackInputAnimNodeReference
) -> Tuple[AnimationAsset, float]
```

X.get_properties(blend_stack_input_node) -> (animation_asset=AnimationAsset, accumulated_time=float)
Get Properties

Args:
    blend_stack_input_node (BlendStackInputAnimNodeReference): 

Returns:
    tuple: 

    animation_asset (AnimationAsset): 

    accumulated_time (float):

<a id="unreal.BlendStackInputAnimNodeLibrary.convert_to_blend_stack_input_node_pure"></a>

#### convert_to_blend_stack_input_node_pure

```python
@classmethod
def convert_to_blend_stack_input_node_pure(
        cls, node: AnimNodeReference
) -> Tuple[BlendStackInputAnimNodeReference, bool]
```

X.convert_to_blend_stack_input_node_pure(node) -> (blend_stack_input_node=BlendStackInputAnimNodeReference, result=bool)
Get a blend stack input node context from an anim node context (pure)

Args:
    node (AnimNodeReference): 

Returns:
    tuple: 

    blend_stack_input_node (BlendStackInputAnimNodeReference): 

    result (bool):

<a id="unreal.BlendStackInputAnimNodeLibrary.convert_to_blend_stack_input_node"></a>

#### convert_to_blend_stack_input_node

```python
@classmethod
def convert_to_blend_stack_input_node(
    cls, node: AnimNodeReference
) -> Tuple[BlendStackInputAnimNodeReference,
           AnimNodeReferenceConversionResult]
```

X.convert_to_blend_stack_input_node(node) -> (BlendStackInputAnimNodeReference, result=AnimNodeReferenceConversionResult)
Get a blend stack input node context from an anim node context

Args:
    node (AnimNodeReference): 

Returns:
    AnimNodeReferenceConversionResult: 

    result (AnimNodeReferenceConversionResult):

<a id="unreal.AnimationBlendStackGraph"></a>