## AnimNode_PoseSnapshot Objects

```python
class AnimNode_PoseSnapshot(AnimNode_Base)
```

Provide a snapshot pose, either from the internal named pose cache or via a supplied snapshot

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_PoseSnapshot.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``mode`` (SnapshotSourceMode):  [Read-Write] How to access the snapshot
- ``snapshot`` (PoseSnapshot):  [Read-Write] Snapshot to use. This should be populated at first by calling SnapshotPose
- ``snapshot_name`` (Name):  [Read-Write] The name of the snapshot previously stored with SavePoseSnapshot

<a id="unreal.AnimNode_PoseSnapshot.__init__"></a>

#### __init__

```python
def __init__(
        snapshot_name: Name = "None",
        snapshot: PoseSnapshot = [[], [], "None", "None", False],
        mode: SnapshotSourceMode = SnapshotSourceMode.NAMED_SNAPSHOT) -> None
```

<a id="unreal.AnimNode_PoseSnapshot.snapshot_name"></a>

#### snapshot_name

```python
@property
def snapshot_name() -> Name
```

(Name):  [Read-Write] The name of the snapshot previously stored with SavePoseSnapshot

<a id="unreal.AnimNode_PoseSnapshot.snapshot_name"></a>

#### snapshot_name

```python
@snapshot_name.setter
def snapshot_name(value: Name) -> None
```

<a id="unreal.AnimNode_PoseSnapshot.snapshot"></a>

#### snapshot

```python
@property
def snapshot() -> PoseSnapshot
```

(PoseSnapshot):  [Read-Write] Snapshot to use. This should be populated at first by calling SnapshotPose

<a id="unreal.AnimNode_PoseSnapshot.snapshot"></a>

#### snapshot

```python
@snapshot.setter
def snapshot(value: PoseSnapshot) -> None
```

<a id="unreal.AnimNode_PoseSnapshot.mode"></a>

#### mode

```python
@property
def mode() -> SnapshotSourceMode
```

(SnapshotSourceMode):  [Read-Write] How to access the snapshot

<a id="unreal.AnimNode_PoseSnapshot.mode"></a>

#### mode

```python
@mode.setter
def mode(value: SnapshotSourceMode) -> None
```

<a id="unreal.PoseSnapshot"></a>