## PCGMeshInstanceList Objects

```python
class PCGMeshInstanceList(StructBase)
```

PCGMesh Instance List

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGMeshSelectorBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``descriptor`` (PCGSoftISMComponentDescriptor):  [Read-Write]
- ``instances`` (Array[Transform]):  [Read-Write]
- ``instances_indices`` (Array[int32]):  [Read-Write]
- ``instances_metadata_entry`` (Array[int64]):  [Read-Write]
  deprecated: Property 'InstancesMetadataEntry' is deprecated.
- ``point_data`` (PCGPointData):  [Read-Write]

<a id="unreal.PCGMeshInstanceList.__init__"></a>

#### __init__

```python
def __init__(instances: Array[Transform] = [],
             point_data: PCGPointData = None,
             instances_indices: Array[int] = []) -> None
```

<a id="unreal.PCGMeshInstanceList.instances"></a>

#### instances

```python
@property
def instances() -> Array[Transform]
```

(Array[Transform]):  [Read-Write]

<a id="unreal.PCGMeshInstanceList.instances"></a>

#### instances

```python
@instances.setter
def instances(value: Array[Transform]) -> None
```

<a id="unreal.PCGMeshInstanceList.point_data"></a>

#### point_data

```python
@property
def point_data() -> PCGPointData
```

(PCGPointData):  [Read-Write]

<a id="unreal.PCGMeshInstanceList.point_data"></a>

#### point_data

```python
@point_data.setter
def point_data(value: PCGPointData) -> None
```

<a id="unreal.PCGMeshInstanceList.instances_indices"></a>

#### instances_indices

```python
@property
def instances_indices() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.PCGMeshInstanceList.instances_indices"></a>

#### instances_indices

```python
@instances_indices.setter
def instances_indices(value: Array[int]) -> None
```

<a id="unreal.PCGMeshInstanceList.instances_metadata_entry"></a>

#### instances_metadata_entry

```python
@property
def instances_metadata_entry() -> Array[int]
```

(Array[int64]):  [Read-Write]
deprecated: Property 'InstancesMetadataEntry' is deprecated.

<a id="unreal.PCGMeshInstanceList.instances_metadata_entry"></a>

#### instances_metadata_entry

```python
@instances_metadata_entry.setter
def instances_metadata_entry(value: Array[int]) -> None
```

<a id="unreal.PCGMeshSelectorWeightedEntry"></a>