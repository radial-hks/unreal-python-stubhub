## BlendStackAnimNodeLibrary Objects

```python
class BlendStackAnimNodeLibrary(BlueprintFunctionLibrary)
```

Exposes operations that can be run on a Blend Stack node via Anim Node Functions such as "On Become Relevant" and "On Update".

**C++ Source:**

- **Plugin**: BlendStack
- **Module**: BlendStack
- **File**: BlendStackAnimNodeLibrary.h

<a id="unreal.BlendStackAnimNodeLibrary.is_current_asset_looping"></a>

#### is_current_asset_looping

```python
@classmethod
def is_current_asset_looping(
        cls, blend_stack_node: BlendStackAnimNodeReference) -> bool
```

X.is_current_asset_looping(blend_stack_node) -> bool
Is Current Asset Looping

Args:
    blend_stack_node (BlendStackAnimNodeReference): 

Returns:
    bool:

<a id="unreal.BlendStackAnimNodeLibrary.get_current_blend_stack_anim_asset_time"></a>

#### get_current_blend_stack_anim_asset_time

```python
@classmethod
def get_current_blend_stack_anim_asset_time(cls,
                                            node: AnimNodeReference) -> float
```

X.get_current_blend_stack_anim_asset_time(node) -> float
Get the current elapsed time of the animation that is playing from a Blend Stack Input node

Args:
    node (AnimNodeReference): 

Returns:
    float:

<a id="unreal.BlendStackAnimNodeLibrary.get_current_blend_stack_anim_asset"></a>

#### get_current_blend_stack_anim_asset

```python
@classmethod
def get_current_blend_stack_anim_asset(
        cls, node: AnimNodeReference) -> AnimationAsset
```

X.get_current_blend_stack_anim_asset(node) -> AnimationAsset
Get the current AnimationAsset that is playing from a Blend Stack Input node

Args:
    node (AnimNodeReference): 

Returns:
    AnimationAsset:

<a id="unreal.BlendStackAnimNodeLibrary.get_current_asset_time_remaining"></a>

#### get_current_asset_time_remaining

```python
@classmethod
def get_current_asset_time_remaining(
        cls, blend_stack_node: BlendStackAnimNodeReference) -> float
```

X.get_current_asset_time_remaining(blend_stack_node) -> float
Get Current Asset Time Remaining

Args:
    blend_stack_node (BlendStackAnimNodeReference): 

Returns:
    float:

<a id="unreal.BlendStackAnimNodeLibrary.get_current_asset_time"></a>

#### get_current_asset_time

```python
@classmethod
def get_current_asset_time(
        cls, blend_stack_node: BlendStackAnimNodeReference) -> float
```

X.get_current_asset_time(blend_stack_node) -> float
Get Current Asset Time

Args:
    blend_stack_node (BlendStackAnimNodeReference): 

Returns:
    float:

<a id="unreal.BlendStackAnimNodeLibrary.get_current_asset"></a>

#### get_current_asset

```python
@classmethod
def get_current_asset(
        cls, blend_stack_node: BlendStackAnimNodeReference) -> AnimationAsset
```

X.get_current_asset(blend_stack_node) -> AnimationAsset
Get Current Asset

Args:
    blend_stack_node (BlendStackAnimNodeReference): 

Returns:
    AnimationAsset:

<a id="unreal.BlendStackAnimNodeLibrary.force_blend_next_update"></a>

#### force_blend_next_update

```python
@classmethod
def force_blend_next_update(
        cls, blend_stack_node: BlendStackAnimNodeReference) -> None
```

X.force_blend_next_update(blend_stack_node) -> None
Force Blend Next Update

Args:
    blend_stack_node (BlendStackAnimNodeReference):

<a id="unreal.BlendStackAnimNodeLibrary.convert_to_blend_stack_node_pure"></a>

#### convert_to_blend_stack_node_pure

```python
@classmethod
def convert_to_blend_stack_node_pure(
        cls,
        node: AnimNodeReference) -> Tuple[BlendStackAnimNodeReference, bool]
```

X.convert_to_blend_stack_node_pure(node) -> (blend_stack_node=BlendStackAnimNodeReference, result=bool)
Get a blend stack node context from an anim node context (pure)

Args:
    node (AnimNodeReference): 

Returns:
    tuple: 

    blend_stack_node (BlendStackAnimNodeReference): 

    result (bool):

<a id="unreal.BlendStackAnimNodeLibrary.convert_to_blend_stack_node"></a>

#### convert_to_blend_stack_node

```python
@classmethod
def convert_to_blend_stack_node(
    cls, node: AnimNodeReference
) -> Tuple[BlendStackAnimNodeReference, AnimNodeReferenceConversionResult]
```

X.convert_to_blend_stack_node(node) -> (BlendStackAnimNodeReference, result=AnimNodeReferenceConversionResult)
Get a blend stack node context from an anim node context

Args:
    node (AnimNodeReference): 

Returns:
    AnimNodeReferenceConversionResult: 

    result (AnimNodeReferenceConversionResult):

<a id="unreal.BlendStackAnimNodeLibrary.blend_to_with_settings"></a>

#### blend_to_with_settings

```python
@classmethod
def blend_to_with_settings(
        cls,
        context: AnimUpdateContext,
        blend_stack_node: BlendStackAnimNodeReference,
        animation_asset: AnimationAsset = None,
        animation_time: float = 0.000000,
        loop: bool = False,
        mirrored: bool = False,
        blend_time: float = 0.200000,
        blend_profile: BlendProfile = None,
        blend_option: AlphaBlendOption = AlphaBlendOption.HERMITE_CUBIC,
        inertial_blend: bool = False,
        blend_parameters: Vector = [0.000000, 0.000000, 0.000000],
        wanted_play_rate: float = 1.000000,
        activation_delay: float = 0.000000) -> None
```

X.blend_to_with_settings(context, blend_stack_node, animation_asset=None, animation_time=0.000000, loop=False, mirrored=False, blend_time=0.200000, blend_profile=None, blend_option=AlphaBlendOption.HERMITE_CUBIC, inertial_blend=False, blend_parameters=[0.000000, 0.000000, 0.000000], wanted_play_rate=1.000000, activation_delay=0.000000) -> None
Note: Experimental and subject to change!

Args:
    context (AnimUpdateContext): 
    blend_stack_node (BlendStackAnimNodeReference): 
    animation_asset (AnimationAsset): 
    animation_time (float): 
    loop (bool): 
    mirrored (bool): 
    blend_time (float): 
    blend_profile (BlendProfile): 
    blend_option (AlphaBlendOption): 
    inertial_blend (bool): 
    blend_parameters (Vector): 
    wanted_play_rate (float): 
    activation_delay (float):

<a id="unreal.BlendStackAnimNodeLibrary.blend_to"></a>

#### blend_to

```python
@classmethod
def blend_to(cls,
             context: AnimUpdateContext,
             blend_stack_node: BlendStackAnimNodeReference,
             animation_asset: AnimationAsset = None,
             animation_time: float = 0.000000,
             loop: bool = False,
             mirrored: bool = False,
             blend_time: float = 0.200000,
             blend_parameters: Vector = [0.000000, 0.000000, 0.000000],
             wanted_play_rate: float = 1.000000,
             activation_delay: float = 0.000000) -> None
```

X.blend_to(context, blend_stack_node, animation_asset=None, animation_time=0.000000, loop=False, mirrored=False, blend_time=0.200000, blend_parameters=[0.000000, 0.000000, 0.000000], wanted_play_rate=1.000000, activation_delay=0.000000) -> None
Blend To

Args:
    context (AnimUpdateContext): 
    blend_stack_node (BlendStackAnimNodeReference): 
    animation_asset (AnimationAsset): 
    animation_time (float): 
    loop (bool): 
    mirrored (bool): 
    blend_time (float): 
    blend_parameters (Vector): 
    wanted_play_rate (float): 
    activation_delay (float):

<a id="unreal.BlendStackInputAnimNodeLibrary"></a>