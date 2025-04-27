## AnimGraphNode_TransitionPoseEvaluator Objects

```python
class AnimGraphNode_TransitionPoseEvaluator(AnimGraphNode_Base)
```

Anim Graph Node Transition Pose Evaluator

**C++ Source:**

- **Module**: AnimGraph
- **File**: AnimGraphNode_TransitionPoseEvaluator.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``become_relevant_function`` (MemberReference):  [Read-Write] Function called when the node becomes relevant, meaning it goes from having no weight to any weight.
- ``binding`` (AnimGraphNodeBinding):  [Read-Write] Bindings for pins that this node exposes
- ``initial_update_function`` (MemberReference):  [Read-Write] Function called before the node is updated for the first time
- ``node`` (AnimNode_TransitionPoseEvaluator):  [Read-Write]
- ``show_pin_for_properties`` (Array[OptionalPinFromProperty]):  [Read-Write]
- ``tag`` (Name):  [Read-Write] Optional reference tag name. If this is set then this node can be referenced from elsewhere in this animation blueprint using an anim node reference
- ``update_function`` (MemberReference):  [Read-Write] Function called when the node is updated

<a id="unreal.AnimGraphNode_TransitionPoseEvaluator.node"></a>

#### node

```python
@property
def node() -> AnimNode_TransitionPoseEvaluator
```

(AnimNode_TransitionPoseEvaluator):  [Read-Write]

<a id="unreal.AnimGraphNode_TransitionPoseEvaluator.node"></a>

#### node

```python
@node.setter
def node(value: AnimNode_TransitionPoseEvaluator) -> None
```

<a id="unreal.AnimGraphNode_TransitionResult"></a>