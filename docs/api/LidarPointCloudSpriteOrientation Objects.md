## LidarPointCloudSpriteOrientation Objects

```python
class LidarPointCloudSpriteOrientation(EnumBase)
```

ELidar Point Cloud Sprite Orientation

**C++ Source:**

- **Plugin**: LidarPointCloud
- **Module**: LidarPointCloudRuntime
- **File**: LidarPointCloudComponent.h

<a id="unreal.LidarPointCloudSpriteOrientation.PREFER_FACING_CAMERA"></a>

#### PREFER_FACING_CAMERA

0: The sprites will face camera, even if Normals are available.

<a id="unreal.LidarPointCloudSpriteOrientation.PREFER_FACING_NORMAL"></a>

#### PREFER_FACING_NORMAL

1: The sprites will attempt to face Normals, if available, or fall back to facing camera otherwise.

<a id="unreal.LidarPointCloudDuplicateHandling"></a>