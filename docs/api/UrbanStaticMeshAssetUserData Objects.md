## UrbanStaticMeshAssetUserData Objects

```python
class UrbanStaticMeshAssetUserData(AssetUserData)
```

Asset user data that can be used with Urban Static Mesh Entity

**C++ Source:**

- **Plugin**: AesBuilder
- **Module**: UrbanEntityBuilder
- **File**: UrbanStaticMeshAssetUserData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``material_color`` (Map[SoftObjectPath, LinearColor]):  [Read-Only] Meta-data are available at runtime in game, i.e. used in blueprint to display build-boarded information
  typedef TMap<FSoftObjectPath, FColor> FMetaDataContainer;
- ``material_simplification`` (Map[SoftObjectPath, str]):  [Read-Only]

<a id="unreal.UrbanStaticMeshAssetUserData.material_color"></a>

#### material\_color

```python
@property
def material_color() -> Map[SoftObjectPath, LinearColor]
```

(Map[SoftObjectPath, LinearColor]):  [Read-Only] Meta-data are available at runtime in game, i.e. used in blueprint to display build-boarded information
typedef TMap<FSoftObjectPath, FColor> FMetaDataContainer;

<a id="unreal.UrbanStaticMeshAssetUserData.material_simplification"></a>

#### material\_simplification

```python
@property
def material_simplification() -> Map[SoftObjectPath, str]
```

(Map[SoftObjectPath, str]):  [Read-Only]

<a id="unreal.UrbanStaticMeshBlueprintLibrary"></a>