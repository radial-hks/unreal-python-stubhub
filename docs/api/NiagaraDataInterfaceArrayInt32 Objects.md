## NiagaraDataInterfaceArrayInt32 Objects

```python
class NiagaraDataInterfaceArrayInt32(NiagaraDataInterfaceArray)
```

Niagara Data Interface Array Int 32

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraDataInterfaceArrayInt.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``gpu_sync_mode`` (NiagaraGpuSyncMode):  [Read-Write] How to do we want to synchronize modifications to the array data.
- ``int_data`` (Array[int32]):  [Read-Write]
- ``max_elements`` (int32):  [Read-Write] When greater than 0 sets the maximum number of elements the array can hold, only relevant when using operations that modify the array size.

<a id="unreal.NiagaraDataInterfaceArrayInt32.int_data"></a>

#### int_data

```python
@property
def int_data() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.NiagaraDataInterfaceArrayInt32.int_data"></a>

#### int_data

```python
@int_data.setter
def int_data(value: Array[int]) -> None
```

<a id="unreal.NiagaraDataInterfaceArrayUInt8"></a>