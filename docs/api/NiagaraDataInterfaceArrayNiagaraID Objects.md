## NiagaraDataInterfaceArrayNiagaraID Objects

```python
class NiagaraDataInterfaceArrayNiagaraID(NiagaraDataInterfaceArray)
```

Niagara Data Interface Array Niagara ID

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraDataInterfaceArrayNiagaraID.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``gpu_sync_mode`` (NiagaraGpuSyncMode):  [Read-Write] How to do we want to synchronize modifications to the array data.
- ``int_data`` (Array[NiagaraID]):  [Read-Write]
- ``max_elements`` (int32):  [Read-Write] When greater than 0 sets the maximum number of elements the array can hold, only relevant when using operations that modify the array size.

<a id="unreal.NiagaraDataInterfaceArrayNiagaraID.int_data"></a>

#### int_data

```python
@property
def int_data() -> Array[NiagaraID]
```

(Array[NiagaraID]):  [Read-Write]

<a id="unreal.NiagaraDataInterfaceArrayNiagaraID.int_data"></a>

#### int_data

```python
@int_data.setter
def int_data(value: Array[NiagaraID]) -> None
```

<a id="unreal.NiagaraDataInterfaceAudioPlayerSettings"></a>