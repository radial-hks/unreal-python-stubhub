## PCGProjectionData Objects

```python
class PCGProjectionData(PCGSpatialDataWithPointCache)
```

Generic projection class (A projected onto B) that intercepts spatial queries

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGProjectionData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``keep_zero_density_points`` (bool):  [Read-Write]
- ``metadata`` (PCGMetadata):  [Read-Only] Not accessible through blueprint to make sure the constness is preserved
- ``projection_params`` (PCGProjectionParams):  [Read-Only]
- ``source`` (PCGSpatialData):  [Read-Only]
- ``target`` (PCGSpatialData):  [Read-Only]
- ``target_actor`` (Actor):  [Read-Write] Recipient of any artifacts generated using this data.

<a id="unreal.PCGProjectionData.source"></a>

#### source

```python
@property
def source() -> PCGSpatialData
```

(PCGSpatialData):  [Read-Only]

<a id="unreal.PCGProjectionData.target"></a>

#### target

```python
@property
def target() -> PCGSpatialData
```

(PCGSpatialData):  [Read-Only]

<a id="unreal.PCGProjectionData.projection_params"></a>

#### projection_params

```python
@property
def projection_params() -> PCGProjectionParams
```

(PCGProjectionParams):  [Read-Only]

<a id="unreal.PCGBaseTextureData"></a>