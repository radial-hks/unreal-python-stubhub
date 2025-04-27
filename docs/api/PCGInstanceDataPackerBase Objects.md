## PCGInstanceDataPackerBase Objects

```python
class PCGInstanceDataPackerBase(Object)
```

PCGInstance Data Packer Base

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGInstanceDataPackerBase.h

<a id="unreal.PCGInstanceDataPackerBase.pack_instances"></a>

#### pack_instances

```python
def pack_instances(
    spatial_data: PCGSpatialData, instance_list: PCGMeshInstanceList
) -> Tuple[PCGContext, PCGPackedCustomData]
```

x.pack_instances(spatial_data, instance_list) -> (context=PCGContext, out_packed_custom_data=PCGPackedCustomData)
Defines the strategy for (H)ISM custom float data packing

Args:
    spatial_data (PCGSpatialData): 
    instance_list (PCGMeshInstanceList): 

Returns:
    tuple: 

    context (PCGContext): 

    out_packed_custom_data (PCGPackedCustomData):

<a id="unreal.PCGInstanceDataPackerBase.pack_custom_data_from_attributes"></a>

#### pack_custom_data_from_attributes

```python
def pack_custom_data_from_attributes(
        instance_list: PCGMeshInstanceList, metadata: PCGMetadata,
        attribute_names: Array[Name]) -> PCGPackedCustomData
```

x.pack_custom_data_from_attributes(instance_list, metadata, attribute_names) -> PCGPackedCustomData
Build a PackedCustomData by processing each attribute in order for each point in the InstanceList

Args:
    instance_list (PCGMeshInstanceList): 
    metadata (PCGMetadata): 
    attribute_names (Array[Name]): 

Returns:
    PCGPackedCustomData: 

    out_packed_custom_data (PCGPackedCustomData):

<a id="unreal.PCGInstanceDataPackerBase.add_type_to_packing"></a>

#### add_type_to_packing

```python
def add_type_to_packing(type_id: int) -> Optional[PCGPackedCustomData]
```

x.add_type_to_packing(type_id) -> PCGPackedCustomData or None
Interprets Metadata TypeId and increments OutPackedCustomData.NumCustomDataFloats appropriately. Returns false if the type could not be interpreted.

Args:
    type_id (int32): 

Returns:
    PCGPackedCustomData or None: 

    out_packed_custom_data (PCGPackedCustomData):

<a id="unreal.PCGInstancePackerBase"></a>