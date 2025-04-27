## AnimGraphNode_AnimDynamics Objects

```python
class AnimGraphNode_AnimDynamics(AnimGraphNode_SkeletalControlBase)
```

Anim Graph Node Anim Dynamics

**C++ Source:**

- **Module**: AnimGraph
- **File**: AnimGraphNode_AnimDynamics.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``become_relevant_function`` (MemberReference):  [Read-Write] Function called when the node becomes relevant, meaning it goes from having no weight to any weight.
- ``binding`` (AnimGraphNodeBinding):  [Read-Write] Bindings for pins that this node exposes
- ``initial_update_function`` (MemberReference):  [Read-Write] Function called before the node is updated for the first time
- ``node`` (AnimNode_AnimDynamics):  [Read-Write]
- ``preview_live`` (bool):  [Read-Write] Preview the live physics object on the mesh
- ``show_angular_limits`` (bool):  [Read-Write] Show angular limit ranges in the viewport
- ``show_collision_spheres`` (bool):  [Read-Write] If planar limits are enabled and the collision mode isn't CoM, draw sphere collision sizes
- ``show_linear_limits`` (bool):  [Read-Write] Show linear (prismatic) limits in the viewport
- ``show_pin_for_properties`` (Array[OptionalPinFromProperty]):  [Read-Write]
- ``show_planar_limit`` (bool):  [Read-Write] Show planar limit info (actual plane, plane normal) in the viewport
- ``show_spherical_limit`` (bool):  [Read-Write] Show spherical limits in the viewport (preview live only)
- ``tag`` (Name):  [Read-Write] Optional reference tag name. If this is set then this node can be referenced from elsewhere in this animation blueprint using an anim node reference
- ``update_function`` (MemberReference):  [Read-Write] Function called when the node is updated

<a id="unreal.AnimGraphNode_ApplyAdditive"></a>