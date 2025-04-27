## AvaTransitionLibrary Objects

```python
class AvaTransitionLibrary(BlueprintFunctionLibrary)
```

Ava Transition Library

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheTransition
- **File**: AvaTransitionLibrary.h

<a id="unreal.AvaTransitionLibrary.is_transition_active_in_layer"></a>

#### is_transition_active_in_layer

```python
@classmethod
def is_transition_active_in_layer(
        cls, transition_node: Object,
        scene_comparison_type: AvaTransitionComparisonResult,
        layer_comparison_type: AvaTransitionLayerCompareType,
        specific_layers: AvaTagHandleContainer) -> bool
```

X.is_transition_active_in_layer(transition_node, scene_comparison_type, layer_comparison_type, specific_layers) -> bool
Is Transition Active in Layer

Args:
    transition_node (Object): 
    scene_comparison_type (AvaTransitionComparisonResult): 
    layer_comparison_type (AvaTransitionLayerCompareType): 
    specific_layers (AvaTagHandleContainer): 

Returns:
    bool:

<a id="unreal.AvaTransitionLibrary.get_transition_type"></a>

#### get_transition_type

```python
@classmethod
def get_transition_type(cls, transition_node: Object) -> AvaTransitionType
```

X.get_transition_type(transition_node) -> AvaTransitionType
Get Transition Type

Args:
    transition_node (Object): 

Returns:
    AvaTransitionType:

<a id="unreal.AvaTransitionLibrary.get_transition_tree"></a>

#### get_transition_tree

```python
@classmethod
def get_transition_tree(cls, transition_node: Object) -> AvaTransitionTree
```

X.get_transition_tree(transition_node) -> AvaTransitionTree
Get Transition Tree

Args:
    transition_node (Object): 

Returns:
    AvaTransitionTree:

<a id="unreal.AvaTransitionLibrary.are_scenes_transitioning"></a>

#### are_scenes_transitioning

```python
@classmethod
def are_scenes_transitioning(cls, transition_node: Object,
                             layers: AvaTagHandleContainer,
                             scenes_to_ignore: Array[World]) -> bool
```

X.are_scenes_transitioning(transition_node, layers, scenes_to_ignore) -> bool
Are Scenes Transitioning

Args:
    transition_node (Object): 
    layers (AvaTagHandleContainer): 
    scenes_to_ignore (Array[World]): 

Returns:
    bool:

<a id="unreal.AvaTransitionPreviewManager"></a>