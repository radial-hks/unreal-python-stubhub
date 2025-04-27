## PCGWorldRayHitData Objects

```python
class PCGWorldRayHitData(PCGSurfaceData)
```

Executes collision queries against world collision.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGWorldData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``keep_zero_density_points`` (bool):  [Read-Write]
- ``local_bounds`` (Box):  [Read-Only]
- ``metadata`` (PCGMetadata):  [Read-Only] Not accessible through blueprint to make sure the constness is preserved
- ``query_params`` (PCGWorldRayHitQueryParams):  [Read-Write]
- ``target_actor`` (Actor):  [Read-Write] Recipient of any artifacts generated using this data.
- ``transform`` (Transform):  [Read-Only]

<a id="unreal.PCGWorldRayHitData.query_params"></a>

#### query_params

```python
@property
def query_params() -> PCGWorldRayHitQueryParams
```

(PCGWorldRayHitQueryParams):  [Read-Write]

<a id="unreal.PCGWorldRayHitData.query_params"></a>

#### query_params

```python
@query_params.setter
def query_params(value: PCGWorldRayHitQueryParams) -> None
```

<a id="unreal.PCGMetadataBitwiseSettings"></a>