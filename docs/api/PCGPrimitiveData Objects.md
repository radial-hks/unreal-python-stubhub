## PCGPrimitiveData Objects

```python
class PCGPrimitiveData(PCGSpatialDataWithPointCache)
```

PCGPrimitive Data

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGPrimitiveData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``keep_zero_density_points`` (bool):  [Read-Write]
- ``metadata`` (PCGMetadata):  [Read-Only] Not accessible through blueprint to make sure the constness is preserved
- ``primitive`` (PrimitiveComponent):  [Read-Only]
- ``target_actor`` (Actor):  [Read-Write] Recipient of any artifacts generated using this data.
- ``voxel_size`` (Vector):  [Read-Write]

<a id="unreal.PCGPrimitiveData.voxel_size"></a>

#### voxel_size

```python
@property
def voxel_size() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.PCGPrimitiveData.voxel_size"></a>

#### voxel_size

```python
@voxel_size.setter
def voxel_size(value: Vector) -> None
```

<a id="unreal.PCGPrimitiveData.primitive"></a>

#### primitive

```python
@property
def primitive() -> PrimitiveComponent
```

(PrimitiveComponent):  [Read-Only]

<a id="unreal.PCGProjectionData"></a>