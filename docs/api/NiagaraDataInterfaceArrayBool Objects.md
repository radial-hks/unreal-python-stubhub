## NiagaraDataInterfaceArrayBool Objects

```python
class NiagaraDataInterfaceArrayBool(NiagaraDataInterfaceArray)
```

Niagara Data Interface Array Bool

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraDataInterfaceArrayInt.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bool_data`` (Array[bool]):  [Read-Write]
- ``gpu_sync_mode`` (NiagaraGpuSyncMode):  [Read-Write] How to do we want to synchronize modifications to the array data.
- ``max_elements`` (int32):  [Read-Write] When greater than 0 sets the maximum number of elements the array can hold, only relevant when using operations that modify the array size.

<a id="unreal.NiagaraDataInterfaceArrayBool.bool_data"></a>

#### bool_data

```python
@property
def bool_data() -> Array[bool]
```

(Array[bool]):  [Read-Write]

<a id="unreal.NiagaraDataInterfaceArrayBool.bool_data"></a>

#### bool_data

```python
@bool_data.setter
def bool_data(value: Array[bool]) -> None
```

<a id="unreal.NiagaraDataInterfaceArrayNiagaraID"></a>