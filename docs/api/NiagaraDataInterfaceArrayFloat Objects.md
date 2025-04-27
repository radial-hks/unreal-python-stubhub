## NiagaraDataInterfaceArrayFloat Objects

```python
class NiagaraDataInterfaceArrayFloat(NiagaraDataInterfaceArray)
```

Niagara Data Interface Array Float

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraDataInterfaceArrayFloat.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``float_data`` (Array[float]):  [Read-Write]
- ``gpu_sync_mode`` (NiagaraGpuSyncMode):  [Read-Write] How to do we want to synchronize modifications to the array data.
- ``max_elements`` (int32):  [Read-Write] When greater than 0 sets the maximum number of elements the array can hold, only relevant when using operations that modify the array size.

<a id="unreal.NiagaraDataInterfaceArrayFloat.float_data"></a>

#### float_data

```python
@property
def float_data() -> Array[float]
```

(Array[float]):  [Read-Write]

<a id="unreal.NiagaraDataInterfaceArrayFloat.float_data"></a>

#### float_data

```python
@float_data.setter
def float_data(value: Array[float]) -> None
```

<a id="unreal.NiagaraDataInterfaceArrayFloat2"></a>