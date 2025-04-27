## LidarPointCloudFileIO_ASCII Objects

```python
class LidarPointCloudFileIO_ASCII(BlueprintFunctionLibrary)
```

Inherits from UBlueprintFunctionLibrary to allow exposure to Blueprint Library in the same class.

**C++ Source:**

- **Plugin**: LidarPointCloud
- **Module**: LidarPointCloudRuntime
- **File**: LidarPointCloudFileIO_ASCII.h

<a id="unreal.LidarPointCloudFileIO_ASCII.create_point_cloud_from_file"></a>

#### create_point_cloud_from_file

```python
@classmethod
def create_point_cloud_from_file(
    cls, world_context_object: Object, filename: str, use_async: bool,
    rgb_range: Vector2D, columns: LidarPointCloudImportSettings_ASCII_Columns,
    latent_info: LatentActionInfo
) -> Tuple[LidarPointCloudAsyncMode, float, LidarPointCloud]
```

X.create_point_cloud_from_file(world_context_object, filename, use_async, rgb_range, columns, latent_info) -> (async_mode=LidarPointCloudAsyncMode, progress=float, point_cloud=LidarPointCloud)
Create Point Cloud from File

Args:
    world_context_object (Object): 
    filename (str): 
    use_async (bool): 
    rgb_range (Vector2D): 
    columns (LidarPointCloudImportSettings_ASCII_Columns): 
    latent_info (LatentActionInfo): 

Returns:
    tuple: 

    async_mode (LidarPointCloudAsyncMode): 

    progress (float): 

    point_cloud (LidarPointCloud):

<a id="unreal.GeometryCache"></a>