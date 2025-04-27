## PoseSearchRoledSkeleton Objects

```python
class PoseSearchRoledSkeleton(StructBase)
```

Pose Search Roled Skeleton

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchSchema.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``mirror_data_table`` (MirrorDataTable):  [Read-Write] Setting up and assigning a mirror data table will allow all your assets in your database to access the mirrored version of the data. This is required for mirroring to work with Motion Matching.
- ``role`` (Name):  [Read-Write]
- ``skeleton`` (Skeleton):  [Read-Write] Skeleton Reference for Motion Matching Database assets. Must be set to a compatible skeleton to the animation data in the database.

<a id="unreal.PoseSearchRoledSkeleton.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.PerSkeletonAnimationSharingSetup"></a>