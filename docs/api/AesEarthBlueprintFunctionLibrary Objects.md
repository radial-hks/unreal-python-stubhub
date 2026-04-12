## AesEarthBlueprintFunctionLibrary Objects

```python
class AesEarthBlueprintFunctionLibrary(BlueprintFunctionLibrary)
```

Aes Earth Blueprint Function Library

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesEarth
- **File**: AesEarthBlueprintFunctionLibrary.h

<a id="unreal.AesEarthBlueprintFunctionLibrary.refresh_scene"></a>

#### refresh\_scene

```python
@classmethod
def refresh_scene(cls) -> None
```

X.refresh_scene() -> None
Refresh Scene

<a id="unreal.AesEarthBlueprintFunctionLibrary.get_aes_georeference"></a>

#### get\_aes\_georeference

```python
@classmethod
def get_aes_georeference(cls, world_context_object: Object) -> AesGeoreference
```

X.get_aes_georeference(world_context_object) -> AesGeoreference
获取AesGeoreferencing 并自动从EarthActor获取坐标数据

Args:
    world_context_object (Object): 

Returns:
    AesGeoreference:

<a id="unreal.AesEarthBlueprintFunctionLibrary.building_extract"></a>

#### building\_extract

```python
@classmethod
def building_extract(cls, actor: AesEarth, target_quadkey: str) -> None
```

X.building_extract(actor, target_quadkey) -> None
Building Extract

Args:
    actor (AesEarth): 
    target_quadkey (str):

<a id="unreal.AesRoadActor"></a>