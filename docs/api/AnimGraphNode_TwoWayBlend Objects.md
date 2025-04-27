## AnimGraphNode_TwoWayBlend Objects

```python
class AnimGraphNode_TwoWayBlend(AnimGraphNode_Base)
```

Anim Graph Node Two Way Blend

**C++ Source:**

- **Module**: AnimGraph
- **File**: AnimGraphNode_TwoWayBlend.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``become_relevant_function`` (MemberReference):  [Read-Write] Function called when the node becomes relevant, meaning it goes from having no weight to any weight.
- ``binding`` (AnimGraphNodeBinding):  [Read-Write] Bindings for pins that this node exposes
- ``blend_node`` (AnimNode_TwoWayBlend):  [Read-Write]
- ``initial_update_function`` (MemberReference):  [Read-Write] Function called before the node is updated for the first time
- ``show_pin_for_properties`` (Array[OptionalPinFromProperty]):  [Read-Write]
- ``tag`` (Name):  [Read-Write] Optional reference tag name. If this is set then this node can be referenced from elsewhere in this animation blueprint using an anim node reference
- ``update_function`` (MemberReference):  [Read-Write] Function called when the node is updated

<a id="unreal.AnimGraphNode_UseCachedPose"></a>