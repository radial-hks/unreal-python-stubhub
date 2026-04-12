## BlendSpaceLibrary Objects

```python
class BlendSpaceLibrary(BlueprintFunctionLibrary)
```

Exposes operations to be performed on a blend space anim node.

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: BlendSpaceLibrary.h

<a id="unreal.BlendSpaceLibrary.snap_to_position"></a>

#### snap\_to\_position

```python
@classmethod
def snap_to_position(cls, blend_space: BlendSpaceReference,
                     new_position: Vector) -> None
```

X.snap_to_position(blend_space, new_position) -> None
Forces the Position to the specified value

Args:
    blend_space (BlendSpaceReference): 
    new_position (Vector):

<a id="unreal.BlendSpaceLibrary.get_position"></a>

#### get\_position

```python
@classmethod
def get_position(cls, blend_space: BlendSpaceReference) -> Vector
```

X.get_position(blend_space) -> Vector
Get the current position of the blend space.

Args:
    blend_space (BlendSpaceReference): 

Returns:
    Vector:

<a id="unreal.BlendSpaceLibrary.get_filtered_position"></a>

#### get\_filtered\_position

```python
@classmethod
def get_filtered_position(cls, blend_space: BlendSpaceReference) -> Vector
```

X.get_filtered_position(blend_space) -> Vector
Get the current sample coordinates after going through the filtering.

Args:
    blend_space (BlendSpaceReference): 

Returns:
    Vector:

<a id="unreal.BlendSpaceLibrary.convert_to_blend_space_pure"></a>

#### convert\_to\_blend\_space\_pure

```python
@classmethod
def convert_to_blend_space_pure(
        cls, node: AnimNodeReference) -> Tuple[BlendSpaceReference, bool]
```

X.convert_to_blend_space_pure(node) -> (blend_space=BlendSpaceReference, result=bool)
Get a blend space context from an anim node context (pure).

Args:
    node (AnimNodeReference): 

Returns:
    tuple: 

    blend_space (BlendSpaceReference): 

    result (bool):

<a id="unreal.BlendSpaceLibrary.convert_to_blend_space"></a>

#### convert\_to\_blend\_space

```python
@classmethod
def convert_to_blend_space(
    cls, node: AnimNodeReference
) -> Tuple[BlendSpaceReference, AnimNodeReferenceConversionResult]
```

X.convert_to_blend_space(node) -> (BlendSpaceReference, result=AnimNodeReferenceConversionResult)
Get a blend space context from an anim node context.

Args:
    node (AnimNodeReference): 

Returns:
    AnimNodeReferenceConversionResult: 

    result (AnimNodeReferenceConversionResult):

<a id="unreal.SequencerAnimationOverride"></a>