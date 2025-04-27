## BlendListBaseLibrary Objects

```python
class BlendListBaseLibrary(BlueprintFunctionLibrary)
```

Exposes operations to be performed on anim state machine node contexts

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: BlendListBaseLibrary.h

<a id="unreal.BlendListBaseLibrary.reset_node"></a>

#### reset_node

```python
@classmethod
def reset_node(cls, blend_list_base: BlendListBaseReference) -> None
```

X.reset_node(blend_list_base) -> None
Reset target blend list node to that the next blend is executed from a blank state

Args:
    blend_list_base (BlendListBaseReference):

<a id="unreal.BlendListBaseLibrary.convert_to_blend_list_base"></a>

#### convert_to_blend_list_base

```python
@classmethod
def convert_to_blend_list_base(
    cls, node: AnimNodeReference
) -> Tuple[BlendListBaseReference, AnimNodeReferenceConversionResult]
```

X.convert_to_blend_list_base(node) -> (BlendListBaseReference, result=AnimNodeReferenceConversionResult)
Get a blend list base context from an anim node context.

Args:
    node (AnimNodeReference): 

Returns:
    AnimNodeReferenceConversionResult: 

    result (AnimNodeReferenceConversionResult):

<a id="unreal.BlendSpacePlayerLibrary"></a>