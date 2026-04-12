## EarthSpatialDataInterface Objects

```python
class EarthSpatialDataInterface(Interface)
```

Earth Spatial Data Interface

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthSpatialDataInterface.h

<a id="unreal.EarthSpatialDataInterface.update_spatial_data"></a>

#### update\_spatial\_data

```python
def update_spatial_data() -> None
```

x.update_spatial_data() -> None
更新空间数据

<a id="unreal.EarthSpatialDataInterface.set_spatial_data_type"></a>

#### set\_spatial\_data\_type

```python
def set_spatial_data_type(spatial_data_type: EarthSpatialDataType) -> None
```

x.set_spatial_data_type(spatial_data_type) -> None
设置空间数据类型

Args:
    spatial_data_type (EarthSpatialDataType):

<a id="unreal.EarthSpatialDataInterface.set_spatial_data"></a>

#### set\_spatial\_data

```python
def set_spatial_data(spatial_data: InstancedStruct) -> None
```

x.set_spatial_data(spatial_data) -> None
获取空间数据

Args:
    spatial_data (InstancedStruct):

<a id="unreal.EarthSpatialDataInterface.get_spatial_data_type"></a>

#### get\_spatial\_data\_type

```python
def get_spatial_data_type() -> EarthSpatialDataType
```

x.get_spatial_data_type() -> EarthSpatialDataType
获取空间数据类型

Returns:
    EarthSpatialDataType:

<a id="unreal.EarthSpatialDataInterface.get_spatial_data"></a>

#### get\_spatial\_data

```python
def get_spatial_data() -> InstancedStruct
```

x.get_spatial_data() -> InstancedStruct
获取空间数据

Returns:
    InstancedStruct:

<a id="unreal.EarthSpatialDataLibrary"></a>