## MirrorAnimLibrary Objects

```python
class MirrorAnimLibrary(BlueprintFunctionLibrary)
```

Exposes operations that can be run on a Mirror node via Anim Node Functions such as "On Become Relevant" and "On Update".

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: MirrorAnimLibrary.h

<a id="unreal.MirrorAnimLibrary.set_mirror_transition_blend_time"></a>

#### set_mirror_transition_blend_time

```python
@classmethod
def set_mirror_transition_blend_time(
        cls, mirror_node: MirrorAnimNodeReference,
        blend_time: float) -> MirrorAnimNodeReference
```

X.set_mirror_transition_blend_time(mirror_node, blend_time) -> MirrorAnimNodeReference
Set how long to blend using inertialization when switching mirrored state

Args:
    mirror_node (MirrorAnimNodeReference): 
    blend_time (float): 

Returns:
    MirrorAnimNodeReference:

<a id="unreal.MirrorAnimLibrary.set_mirror"></a>

#### set_mirror

```python
@classmethod
def set_mirror(cls, mirror_node: MirrorAnimNodeReference,
               mirror: bool) -> MirrorAnimNodeReference
```

X.set_mirror(mirror_node, mirror) -> MirrorAnimNodeReference
Set the mirror state

Args:
    mirror_node (MirrorAnimNodeReference): 
    mirror (bool): 

Returns:
    MirrorAnimNodeReference:

<a id="unreal.MirrorAnimLibrary.get_mirror_transition_blend_time"></a>

#### get_mirror_transition_blend_time

```python
@classmethod
def get_mirror_transition_blend_time(
        cls, mirror_node: MirrorAnimNodeReference) -> float
```

X.get_mirror_transition_blend_time(mirror_node) -> float
Get how long to blend using inertialization when switching mirrored state

Args:
    mirror_node (MirrorAnimNodeReference): 

Returns:
    float:

<a id="unreal.MirrorAnimLibrary.get_mirror_data_table"></a>

#### get_mirror_data_table

```python
@classmethod
def get_mirror_data_table(
        cls, mirror_node: MirrorAnimNodeReference) -> MirrorDataTable
```

X.get_mirror_data_table(mirror_node) -> MirrorDataTable
Get MirrorDataTable used to perform mirroring

Args:
    mirror_node (MirrorAnimNodeReference): 

Returns:
    MirrorDataTable:

<a id="unreal.MirrorAnimLibrary.get_mirror"></a>

#### get_mirror

```python
@classmethod
def get_mirror(cls, mirror_node: MirrorAnimNodeReference) -> bool
```

X.get_mirror(mirror_node) -> bool
Get the mirror state

Args:
    mirror_node (MirrorAnimNodeReference): 

Returns:
    bool:

<a id="unreal.MirrorAnimLibrary.convert_to_mirror_node_pure"></a>

#### convert_to_mirror_node_pure

```python
@classmethod
def convert_to_mirror_node_pure(
        cls, node: AnimNodeReference) -> Tuple[MirrorAnimNodeReference, bool]
```

X.convert_to_mirror_node_pure(node) -> (mirror_node=MirrorAnimNodeReference, result=bool)
Get a mirror context from an anim node context (pure)

Args:
    node (AnimNodeReference): 

Returns:
    tuple: 

    mirror_node (MirrorAnimNodeReference): 

    result (bool):

<a id="unreal.MirrorAnimLibrary.convert_to_mirror_node"></a>

#### convert_to_mirror_node

```python
@classmethod
def convert_to_mirror_node(
    cls, node: AnimNodeReference
) -> Tuple[MirrorAnimNodeReference, AnimNodeReferenceConversionResult]
```

X.convert_to_mirror_node(node) -> (MirrorAnimNodeReference, result=AnimNodeReferenceConversionResult)
Get a mirror node context from an anim node context

Args:
    node (AnimNodeReference): 

Returns:
    AnimNodeReferenceConversionResult: 

    result (AnimNodeReferenceConversionResult):

<a id="unreal.ModifyCurveAnimLibrary"></a>