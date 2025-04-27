## AnimGraphNode_Base Objects

```python
class AnimGraphNode_Base(K2Node)
```

This is the base class for any animation graph nodes that generate or consume an animation pose in
the animation blend graph.

Any concrete implementations will be paired with a runtime graph node derived from FAnimNode_Base

**C++ Source:**

- **Module**: AnimGraph
- **File**: AnimGraphNode_Base.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``become_relevant_function`` (MemberReference):  [Read-Write] Function called when the node becomes relevant, meaning it goes from having no weight to any weight.
- ``binding`` (AnimGraphNodeBinding):  [Read-Write] Bindings for pins that this node exposes
- ``initial_update_function`` (MemberReference):  [Read-Write] Function called before the node is updated for the first time
- ``show_pin_for_properties`` (Array[OptionalPinFromProperty]):  [Read-Write]
- ``tag`` (Name):  [Read-Write] Optional reference tag name. If this is set then this node can be referenced from elsewhere in this animation blueprint using an anim node reference
- ``update_function`` (MemberReference):  [Read-Write] Function called when the node is updated

<a id="unreal.AnimGraphNode_AssetPlayerBase"></a>