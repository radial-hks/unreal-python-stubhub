## LidarPointCloudScalingMethod Objects

```python
class LidarPointCloudScalingMethod(EnumBase)
```

ELidar Point Cloud Scaling Method

**C++ Source:**

- **Plugin**: LidarPointCloud
- **Module**: LidarPointCloudRuntime
- **File**: LidarPointCloudShared.h

<a id="unreal.LidarPointCloudScalingMethod.PER_NODE"></a>

#### PER_NODE

0: Points are scaled based on the estimated density of their containing node.
Recommended for assets with high variance of point densities, but may produce less fine detail overall.
Default method in 4.25 and 4.26

<a id="unreal.LidarPointCloudScalingMethod.PER_NODE_ADAPTIVE"></a>

#### PER_NODE_ADAPTIVE

1: Similar to PerNode, but the density is calculated adaptively based on the current view.
Produces good amount of fine detail while being generally resistant to density variance.

<a id="unreal.LidarPointCloudScalingMethod.PER_POINT"></a>

#### PER_POINT

2: Points are scaled based on their individual calculated depth.
Capable of resolving the highest amount of fine detail, but is the most susceptible to
density changes across the dataset, and may result in patches of varying point sizes.

<a id="unreal.LidarPointCloudScalingMethod.FIXED_SCREEN_SIZE"></a>

#### FIXED_SCREEN_SIZE

3: Sprites will be rendered using screen-space scaling method.
In that mode, Point Size property will work as Screen Percentage.

<a id="unreal.LidarClippingVolumeMode"></a>