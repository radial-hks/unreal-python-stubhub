## NiagaraDataInterfaceArray Objects

```python
class NiagaraDataInterfaceArray(NiagaraDataInterfaceRWBase)
```

Niagara Data Interface Array

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraDataInterfaceArray.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``gpu_sync_mode`` (NiagaraGpuSyncMode):  [Read-Write] How to do we want to synchronize modifications to the array data.
- ``max_elements`` (int32):  [Read-Write] When greater than 0 sets the maximum number of elements the array can hold, only relevant when using operations that modify the array size.

<a id="unreal.NiagaraDataInterfaceArray.gpu_sync_mode"></a>

#### gpu_sync_mode

```python
@property
def gpu_sync_mode() -> NiagaraGpuSyncMode
```

(NiagaraGpuSyncMode):  [Read-Only] How to do we want to synchronize modifications to the array data.

<a id="unreal.NiagaraDataInterfaceArray.max_elements"></a>

#### max_elements

```python
@property
def max_elements() -> int
```

(int32):  [Read-Only] When greater than 0 sets the maximum number of elements the array can hold, only relevant when using operations that modify the array size.

<a id="unreal.NiagaraDataInterfaceArrayFloat"></a>