## IKRigDefinition Objects

```python
class IKRigDefinition(Object)
```

IKRig Definition

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRig
- **File**: IKRigDefinition.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``draw_goals`` (bool):  [Read-Write] Draw bones in the viewport.
- ``goal_size`` (float):  [Read-Write] The size of the Goals in the editor viewport.
- ``goal_thickness`` (float):  [Read-Write] The thickness of the Goals in the editor viewport.
- ``preview_skeletal_mesh`` (SkeletalMesh):  [Read-Write] The skeletal mesh to run the IK solve on (loaded into viewport).
  NOTE: you can assign ANY Skeletal Mesh to apply the IK Rig to. Compatibility is determined when a new mesh is assigned
  by comparing it's hierarchy with the goals, solvers and bone settings required by the rig. See output log for details.

<a id="unreal.IKRig_BodyMoverEffector"></a>