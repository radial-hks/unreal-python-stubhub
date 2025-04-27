## GeometryScript_VolumeBake Objects

```python
class GeometryScript_VolumeBake(BlueprintFunctionLibrary)
```

Geometry Script Library Volume Texture Bake Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: VolumeTextureBakeFunctions.h

<a id="unreal.GeometryScript_VolumeBake.bake_signed_distance_to_volume_texture"></a>

#### bake_signed_distance_to_volume_texture

```python
@classmethod
def bake_signed_distance_to_volume_texture(
        cls, target_mesh: DynamicMesh, volume_texture: VolumeTexture,
        distance_settings: ComputeDistanceFieldSettings,
        texture_settings: DistanceFieldToTextureSettings) -> bool
```

X.bake_signed_distance_to_volume_texture(target_mesh, volume_texture, distance_settings, texture_settings) -> bool
Write a distance field to the given existing volume texture

Args:
    target_mesh (DynamicMesh): 
    volume_texture (VolumeTexture): 
    distance_settings (ComputeDistanceFieldSettings): 
    texture_settings (DistanceFieldToTextureSettings): 

Returns:
    bool:

<a id="unreal.LocationServices"></a>