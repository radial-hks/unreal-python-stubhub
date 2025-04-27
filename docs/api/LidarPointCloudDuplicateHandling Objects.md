## LidarPointCloudDuplicateHandling Objects

```python
class LidarPointCloudDuplicateHandling(EnumBase)
```

ELidar Point Cloud Duplicate Handling

**C++ Source:**

- **Plugin**: LidarPointCloud
- **Module**: LidarPointCloudRuntime
- **File**: LidarPointCloudSettings.h

<a id="unreal.LidarPointCloudDuplicateHandling.IGNORE"></a>

#### IGNORE

0: Keeps any duplicates found

<a id="unreal.LidarPointCloudDuplicateHandling.SELECT_FIRST"></a>

#### SELECT_FIRST

1: Keeps the first point and skips any further duplicates

<a id="unreal.LidarPointCloudDuplicateHandling.SELECT_BRIGHTER"></a>

#### SELECT_BRIGHTER

2: Selects the brightest of the duplicates

<a id="unreal.LidarPointCloudAsyncMode"></a>