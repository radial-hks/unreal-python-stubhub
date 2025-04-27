## BlendSpacePlayerLibrary Objects

```python
class BlendSpacePlayerLibrary(BlueprintFunctionLibrary)
```

Exposes operations to be performed on a blend space player anim node.

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: BlendSpacePlayerLibrary.h

<a id="unreal.BlendSpacePlayerLibrary.snap_to_position"></a>

#### snap_to_position

```python
@classmethod
def snap_to_position(cls, blend_space_player: BlendSpacePlayerReference,
                     new_position: Vector) -> None
```

X.snap_to_position(blend_space_player, new_position) -> None
Forces the Position to the specified value

Args:
    blend_space_player (BlendSpacePlayerReference): 
    new_position (Vector):

<a id="unreal.BlendSpacePlayerLibrary.should_reset_play_time_when_blend_space_changes"></a>

#### should_reset_play_time_when_blend_space_changes

```python
@classmethod
def should_reset_play_time_when_blend_space_changes(
        cls, blend_space_player: BlendSpacePlayerReference) -> bool
```

X.should_reset_play_time_when_blend_space_changes(blend_space_player) -> bool
Get the current value of whether the current play time should reset when BlendSpace changes of the blend space player.

Args:
    blend_space_player (BlendSpacePlayerReference): 

Returns:
    bool:

<a id="unreal.BlendSpacePlayerLibrary.set_reset_play_time_when_blend_space_changes"></a>

#### set_reset_play_time_when_blend_space_changes

```python
@classmethod
def set_reset_play_time_when_blend_space_changes(
        cls, blend_space_player: BlendSpacePlayerReference,
        reset: bool) -> BlendSpacePlayerReference
```

X.set_reset_play_time_when_blend_space_changes(blend_space_player, reset) -> BlendSpacePlayerReference
Set whether the current play time should reset when BlendSpace changes of the blend space player.

Args:
    blend_space_player (BlendSpacePlayerReference): 
    reset (bool): 

Returns:
    BlendSpacePlayerReference:

<a id="unreal.BlendSpacePlayerLibrary.set_play_rate"></a>

#### set_play_rate

```python
@classmethod
def set_play_rate(cls, blend_space_player: BlendSpacePlayerReference,
                  play_rate: float) -> BlendSpacePlayerReference
```

X.set_play_rate(blend_space_player, play_rate) -> BlendSpacePlayerReference
Set the play rate of the blend space player.

Args:
    blend_space_player (BlendSpacePlayerReference): 
    play_rate (float): 

Returns:
    BlendSpacePlayerReference:

<a id="unreal.BlendSpacePlayerLibrary.set_loop"></a>

#### set_loop

```python
@classmethod
def set_loop(cls, blend_space_player: BlendSpacePlayerReference,
             loop: bool) -> BlendSpacePlayerReference
```

X.set_loop(blend_space_player, loop) -> BlendSpacePlayerReference
Set the loop of the blend space player.

Args:
    blend_space_player (BlendSpacePlayerReference): 
    loop (bool): 

Returns:
    BlendSpacePlayerReference:

<a id="unreal.BlendSpacePlayerLibrary.set_blend_space_with_inertial_blending"></a>

#### set_blend_space_with_inertial_blending

```python
@classmethod
def set_blend_space_with_inertial_blending(
        cls,
        update_context: AnimUpdateContext,
        blend_space_player: BlendSpacePlayerReference,
        blend_space: BlendSpace,
        blend_time: float = 0.200000) -> BlendSpacePlayerReference
```

X.set_blend_space_with_inertial_blending(update_context, blend_space_player, blend_space, blend_time=0.200000) -> BlendSpacePlayerReference
Set the current BlendSpace of the blend space player with an interial blend time.

Args:
    update_context (AnimUpdateContext): 
    blend_space_player (BlendSpacePlayerReference): 
    blend_space (BlendSpace): 
    blend_time (float): 

Returns:
    BlendSpacePlayerReference:

<a id="unreal.BlendSpacePlayerLibrary.set_blend_space"></a>

#### set_blend_space

```python
@classmethod
def set_blend_space(cls, blend_space_player: BlendSpacePlayerReference,
                    blend_space: BlendSpace) -> BlendSpacePlayerReference
```

X.set_blend_space(blend_space_player, blend_space) -> BlendSpacePlayerReference
Set the current BlendSpace of the blend space player.

Args:
    blend_space_player (BlendSpacePlayerReference): 
    blend_space (BlendSpace): 

Returns:
    BlendSpacePlayerReference:

<a id="unreal.BlendSpacePlayerLibrary.get_start_position"></a>

#### get_start_position

```python
@classmethod
def get_start_position(cls,
                       blend_space_player: BlendSpacePlayerReference) -> float
```

X.get_start_position(blend_space_player) -> float
Get the current start position of the blend space player.

Args:
    blend_space_player (BlendSpacePlayerReference): 

Returns:
    float:

<a id="unreal.BlendSpacePlayerLibrary.get_position"></a>

#### get_position

```python
@classmethod
def get_position(cls, blend_space_player: BlendSpacePlayerReference) -> Vector
```

X.get_position(blend_space_player) -> Vector
Get the current position of the blend space player.

Args:
    blend_space_player (BlendSpacePlayerReference): 

Returns:
    Vector:

<a id="unreal.BlendSpacePlayerLibrary.get_play_rate"></a>

#### get_play_rate

```python
@classmethod
def get_play_rate(cls, blend_space_player: BlendSpacePlayerReference) -> float
```

X.get_play_rate(blend_space_player) -> float
Get the current play rate of the blend space player.

Args:
    blend_space_player (BlendSpacePlayerReference): 

Returns:
    float:

<a id="unreal.BlendSpacePlayerLibrary.get_loop"></a>

#### get_loop

```python
@classmethod
def get_loop(cls, blend_space_player: BlendSpacePlayerReference) -> bool
```

X.get_loop(blend_space_player) -> bool
Get the current loop of the blend space player.

Args:
    blend_space_player (BlendSpacePlayerReference): 

Returns:
    bool:

<a id="unreal.BlendSpacePlayerLibrary.get_blend_space"></a>

#### get_blend_space

```python
@classmethod
def get_blend_space(
        cls, blend_space_player: BlendSpacePlayerReference) -> BlendSpace
```

X.get_blend_space(blend_space_player) -> BlendSpace
Get the current BlendSpace of the blend space player.

Args:
    blend_space_player (BlendSpacePlayerReference): 

Returns:
    BlendSpace:

<a id="unreal.BlendSpacePlayerLibrary.convert_to_blend_space_player_pure"></a>

#### convert_to_blend_space_player_pure

```python
@classmethod
def convert_to_blend_space_player_pure(
        cls,
        node: AnimNodeReference) -> Tuple[BlendSpacePlayerReference, bool]
```

X.convert_to_blend_space_player_pure(node) -> (blend_space_player=BlendSpacePlayerReference, result=bool)
Get a blend space player context from an anim node context (pure).

Args:
    node (AnimNodeReference): 

Returns:
    tuple: 

    blend_space_player (BlendSpacePlayerReference): 

    result (bool):

<a id="unreal.BlendSpacePlayerLibrary.convert_to_blend_space_player"></a>

#### convert_to_blend_space_player

```python
@classmethod
def convert_to_blend_space_player(
    cls, node: AnimNodeReference
) -> Tuple[BlendSpacePlayerReference, AnimNodeReferenceConversionResult]
```

X.convert_to_blend_space_player(node) -> (BlendSpacePlayerReference, result=AnimNodeReferenceConversionResult)
Get a blend space player context from an anim node context.

Args:
    node (AnimNodeReference): 

Returns:
    AnimNodeReferenceConversionResult: 

    result (AnimNodeReferenceConversionResult):

<a id="unreal.AnimGraphLibrary"></a>