## EarthGeoReferenceLibrary Objects

```python
class EarthGeoReferenceLibrary(BlueprintFunctionLibrary)
```

地球地理参考系函数库

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesGeoreference
- **File**: EarthGeoReferenceLibrary.h

<a id="unreal.EarthGeoReferenceLibrary.update_geo_referencing_system"></a>

#### update\_geo\_referencing\_system

```python
@classmethod
def update_geo_referencing_system(
    cls, geo_referencing_system: EarthGeoReferencingSystem
) -> EarthGeoReferencingSystem
```

X.update_geo_referencing_system(geo_referencing_system) -> EarthGeoReferencingSystem
更新坐标系系统信息

Args:
    geo_referencing_system (EarthGeoReferencingSystem): 

Returns:
    EarthGeoReferencingSystem: 

    geo_referencing_system (EarthGeoReferencingSystem):

<a id="unreal.EarthGeoReferenceLibrary.transform_world_transform"></a>

#### transform\_world\_transform

```python
@classmethod
def transform_world_transform(
        cls, world_transform: Transform,
        source_geo_reference: EarthGeoReferencingSystem,
        target_geo_reference: EarthGeoReferencingSystem) -> Transform
```

X.transform_world_transform(world_transform, source_geo_reference, target_geo_reference) -> Transform
在两个坐标系系统间转换世界坐标变换

Args:
    world_transform (Transform): 
    source_geo_reference (EarthGeoReferencingSystem): 
    target_geo_reference (EarthGeoReferencingSystem): 

Returns:
    Transform:

<a id="unreal.EarthGeoReferenceLibrary.transform_world_location"></a>

#### transform\_world\_location

```python
@classmethod
def transform_world_location(
        cls, world_location: Vector,
        source_geo_reference: EarthGeoReferencingSystem,
        target_geo_reference: EarthGeoReferencingSystem) -> Vector
```

X.transform_world_location(world_location, source_geo_reference, target_geo_reference) -> Vector
在两个坐标系系统间转换世界坐标

Args:
    world_location (Vector): 
    source_geo_reference (EarthGeoReferencingSystem): 
    target_geo_reference (EarthGeoReferencingSystem): 

Returns:
    Vector:

<a id="unreal.AesMarkerSystemProvider"></a>