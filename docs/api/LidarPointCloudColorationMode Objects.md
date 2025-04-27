## LidarPointCloudColorationMode Objects

```python
class LidarPointCloudColorationMode(EnumBase)
```

ELidar Point Cloud Coloration Mode

**C++ Source:**

- **Plugin**: LidarPointCloud
- **Module**: LidarPointCloudRuntime
- **File**: LidarPointCloudShared.h

<a id="unreal.LidarPointCloudColorationMode.NONE"></a>

#### NONE

0: Uses color tint only

<a id="unreal.LidarPointCloudColorationMode.DATA"></a>

#### DATA

1: Uses imported RGB / Intensity data

<a id="unreal.LidarPointCloudColorationMode.DATA_WITH_CLASSIFICATION_ALPHA"></a>

#### DATA_WITH_CLASSIFICATION_ALPHA

2: Uses imported RGB / Intensity data combined with Alpha mask from Classification Colors

<a id="unreal.LidarPointCloudColorationMode.ELEVATION"></a>

#### ELEVATION

3: The cloud's color will be overridden with elevation-based color

<a id="unreal.LidarPointCloudColorationMode.POSITION"></a>

#### POSITION

4: The cloud's color will be overridden with relative position-based color

<a id="unreal.LidarPointCloudColorationMode.CLASSIFICATION"></a>

#### CLASSIFICATION

5: Uses Classification ID of the point along with the component's Classification Colors property to sample the color

<a id="unreal.LidarPointCloudSpriteShape"></a>