## NDISkelMesh_GpuUniformSamplingFormat Objects

```python
class NDISkelMesh_GpuUniformSamplingFormat(EnumBase)
```

This enum must match the order in NiagaraDataInterfaceSkeletalMesh.ush

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraSettings.h

<a id="unreal.NDISkelMesh_GpuUniformSamplingFormat.FULL"></a>

#### FULL

0: 64 bits per entry. Allow for the full int32 range of triangles (2 billion).

<a id="unreal.NDISkelMesh_GpuUniformSamplingFormat.LIMITED_24_8"></a>

#### LIMITED_24_8

1: 32 bits per entry. Allow for ~16.7 million triangles and 8 bits of probability precision.

<a id="unreal.NDISkelMesh_GpuUniformSamplingFormat.LIMITED_23_9"></a>

#### LIMITED_23_9

2: 32 bits per entry. Allow for ~8.4 millions triangles and 9 bits of probability precision.

<a id="unreal.NDISkelMesh_AdjacencyTriangleIndexFormat"></a>