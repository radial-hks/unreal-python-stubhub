## LinkedAnimGraphLibrary Objects

```python
class LinkedAnimGraphLibrary(BlueprintFunctionLibrary)
```

Exposes operations to be performed on anim node contexts

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: LinkedAnimGraphLibrary.h

<a id="unreal.LinkedAnimGraphLibrary.has_linked_anim_instance"></a>

#### has_linked_anim_instance

```python
@classmethod
def has_linked_anim_instance(cls, node: LinkedAnimGraphReference) -> bool
```

X.has_linked_anim_instance(node) -> bool
Returns whether the node hosts an instance (e.g. linked anim graph or layer)

Args:
    node (LinkedAnimGraphReference): 

Returns:
    bool:

<a id="unreal.LinkedAnimGraphLibrary.get_linked_anim_instance"></a>

#### get_linked_anim_instance

```python
@classmethod
def get_linked_anim_instance(cls,
                             node: LinkedAnimGraphReference) -> AnimInstance
```

X.get_linked_anim_instance(node) -> AnimInstance
Get the linked instance is hosted by this node. If the node does not host an instance then HasLinkedAnimInstance will return false

Args:
    node (LinkedAnimGraphReference): 

Returns:
    AnimInstance:

<a id="unreal.LinkedAnimGraphLibrary.convert_to_linked_anim_graph_pure"></a>

#### convert_to_linked_anim_graph_pure

```python
@classmethod
def convert_to_linked_anim_graph_pure(
        cls, node: AnimNodeReference) -> Tuple[LinkedAnimGraphReference, bool]
```

X.convert_to_linked_anim_graph_pure(node) -> (linked_anim_graph=LinkedAnimGraphReference, result=bool)
Get a linked anim graph reference from an anim node reference (pure)

Args:
    node (AnimNodeReference): 

Returns:
    tuple: 

    linked_anim_graph (LinkedAnimGraphReference): 

    result (bool):

<a id="unreal.LinkedAnimGraphLibrary.convert_to_linked_anim_graph"></a>

#### convert_to_linked_anim_graph

```python
@classmethod
def convert_to_linked_anim_graph(
    cls, node: AnimNodeReference
) -> Tuple[LinkedAnimGraphReference, AnimNodeReferenceConversionResult]
```

X.convert_to_linked_anim_graph(node) -> (LinkedAnimGraphReference, result=AnimNodeReferenceConversionResult)
Get a linked anim graph reference from an anim node reference

Args:
    node (AnimNodeReference): 

Returns:
    AnimNodeReferenceConversionResult: 

    result (AnimNodeReferenceConversionResult):

<a id="unreal.MirrorAnimLibrary"></a>