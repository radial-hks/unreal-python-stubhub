## MagicCesiumManageSystem Objects

```python
class MagicCesiumManageSystem(WorldSubsystem)
```

Magic Cesium Manage System

**C++ Source:**

- **Plugin**: GISCesium
- **Module**: MagicCesium
- **File**: MagicCesiumManageSystem.h

<a id="unreal.MagicCesiumManageSystem.transfrom_aes_geo_location_to_cesium_geo_location"></a>

#### transfrom\_aes\_geo\_location\_to\_cesium\_geo\_location

```python
def transfrom_aes_geo_location_to_cesium_geo_location(
        aes_center_geo_location: Vector,
        target_aes_geo_location: Vector) -> Vector
```

x.transfrom_aes_geo_location_to_cesium_geo_location(aes_center_geo_location, target_aes_geo_location) -> Vector
AES经纬度反算Cesium经纬度的工具

Args:
    aes_center_geo_location (Vector): 
    target_aes_geo_location (Vector): 

Returns:
    Vector: 

    out_cesium_geo_location (Vector):

<a id="unreal.MagicCesium3DTileset"></a>