## SnapshotSourceMode Objects

```python
class SnapshotSourceMode(EnumBase)
```

How to access the snapshot

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_PoseSnapshot.h

<a id="unreal.SnapshotSourceMode.NAMED_SNAPSHOT"></a>

#### NAMED_SNAPSHOT

0: Refer to an internal snapshot by name (previously stored with SavePoseSnapshot).
This can be more efficient than access via pin.

<a id="unreal.SnapshotSourceMode.SNAPSHOT_PIN"></a>

#### SNAPSHOT_PIN

1: Use a snapshot variable (previously populated using SnapshotPose).
This is more flexible and allows poses to be modified and managed externally to the animation blueprint.

<a id="unreal.DrivenDestinationMode"></a>