## NiagaraDataInterfaceArrayFloat4 Objects

```python
class NiagaraDataInterfaceArrayFloat4(NiagaraDataInterfaceArray)
```

Niagara Data Interface Array Float 4

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraDataInterfaceArrayFloat.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``float_data`` (Array[Vector4]):  [Read-Write]
- ``gpu_sync_mode`` (NiagaraGpuSyncMode):  [Read-Write] How to do we want to synchronize modifications to the array data.
- ``max_elements`` (int32):  [Read-Write] When greater than 0 sets the maximum number of elements the array can hold, only relevant when using operations that modify the array size.

<a id="unreal.NiagaraDataInterfaceArrayFloat4.float_data"></a>

#### float_data

```python
@property
def float_data() -> Array[Vector4]
```

(Array[Vector4]):  [Read-Write]

<a id="unreal.NiagaraDataInterfaceArrayFloat4.float_data"></a>

#### float_data

```python
@float_data.setter
def float_data(value: Array[Vector4]) -> None
```

<a id="unreal.NiagaraDataInterfaceArrayColor"></a>