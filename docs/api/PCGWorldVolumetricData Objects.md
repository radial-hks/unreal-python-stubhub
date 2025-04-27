## PCGWorldVolumetricData Objects

```python
class PCGWorldVolumetricData(PCGVolumeData)
```

Queries volume for presence of world collision or not. Can be used to voxelize environment.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGWorldData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``keep_zero_density_points`` (bool):  [Read-Write]
- ``metadata`` (PCGMetadata):  [Read-Only] Not accessible through blueprint to make sure the constness is preserved
- ``query_params`` (PCGWorldVolumetricQueryParams):  [Read-Write]
- ``target_actor`` (Actor):  [Read-Write] Recipient of any artifacts generated using this data.
- ``volume`` (Volume):  [Read-Write]
- ``voxel_size`` (Vector):  [Read-Write] ~End UPCGSpatialDataWithPointCache interface

<a id="unreal.PCGWorldVolumetricData.query_params"></a>

#### query_params

```python
@property
def query_params() -> PCGWorldVolumetricQueryParams
```

(PCGWorldVolumetricQueryParams):  [Read-Write]

<a id="unreal.PCGWorldVolumetricData.query_params"></a>

#### query_params

```python
@query_params.setter
def query_params(value: PCGWorldVolumetricQueryParams) -> None
```

<a id="unreal.PCGWorldRayHitData"></a>