## NiagaraDataInterfaceArrayPosition Objects

```python
class NiagaraDataInterfaceArrayPosition(NiagaraDataInterfaceArray)
```

Niagara Data Interface Array Position

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraDataInterfaceArrayFloat.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``gpu_sync_mode`` (NiagaraGpuSyncMode):  [Read-Write] How to do we want to synchronize modifications to the array data.
- ``max_elements`` (int32):  [Read-Write] When greater than 0 sets the maximum number of elements the array can hold, only relevant when using operations that modify the array size.
- ``position_data`` (Array[NiagaraPosition]):  [Read-Write]

<a id="unreal.NiagaraDataInterfaceArrayPosition.position_data"></a>

#### position_data

```python
@property
def position_data() -> Array[NiagaraPosition]
```

(Array[NiagaraPosition]):  [Read-Write]

<a id="unreal.NiagaraDataInterfaceArrayPosition.position_data"></a>

#### position_data

```python
@position_data.setter
def position_data(value: Array[NiagaraPosition]) -> None
```

<a id="unreal.NiagaraDataInterfaceArrayFloat4"></a>