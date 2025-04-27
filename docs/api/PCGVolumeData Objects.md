## PCGVolumeData Objects

```python
class PCGVolumeData(PCGSpatialDataWithPointCache)
```

PCGVolume Data

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGVolumeData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``keep_zero_density_points`` (bool):  [Read-Write]
- ``metadata`` (PCGMetadata):  [Read-Only] Not accessible through blueprint to make sure the constness is preserved
- ``target_actor`` (Actor):  [Read-Write] Recipient of any artifacts generated using this data.
- ``volume`` (Volume):  [Read-Write]
- ``voxel_size`` (Vector):  [Read-Write] ~End UPCGSpatialDataWithPointCache interface

<a id="unreal.PCGVolumeData.voxel_size"></a>

#### voxel_size

```python
@property
def voxel_size() -> Vector
```

(Vector):  [Read-Write] ~End UPCGSpatialDataWithPointCache interface

<a id="unreal.PCGVolumeData.voxel_size"></a>

#### voxel_size

```python
@voxel_size.setter
def voxel_size(value: Vector) -> None
```

<a id="unreal.PCGVolumeData.volume"></a>

#### volume

```python
@property
def volume() -> Volume
```

(Volume):  [Read-Write]

<a id="unreal.PCGVolumeData.volume"></a>

#### volume

```python
@volume.setter
def volume(value: Volume) -> None
```

<a id="unreal.PCGWorldVolumetricData"></a>