## AnimGraphNode_CopyPoseFromMesh Objects

```python
class AnimGraphNode_CopyPoseFromMesh(AnimGraphNode_Base)
```

Anim Graph Node Copy Pose from Mesh

**C++ Source:**

- **Module**: AnimGraph
- **File**: AnimGraphNode_CopyPoseFromMesh.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``become_relevant_function`` (MemberReference):  [Read-Write] Function called when the node becomes relevant, meaning it goes from having no weight to any weight.
- ``binding`` (AnimGraphNodeBinding):  [Read-Write] Bindings for pins that this node exposes
- ``initial_update_function`` (MemberReference):  [Read-Write] Function called before the node is updated for the first time
- ``node`` (AnimNode_CopyPoseFromMesh):  [Read-Write]
- ``show_pin_for_properties`` (Array[OptionalPinFromProperty]):  [Read-Write]
- ``tag`` (Name):  [Read-Write] Optional reference tag name. If this is set then this node can be referenced from elsewhere in this animation blueprint using an anim node reference
- ``update_function`` (MemberReference):  [Read-Write] Function called when the node is updated

<a id="unreal.AnimGraphNode_CurveSource"></a>