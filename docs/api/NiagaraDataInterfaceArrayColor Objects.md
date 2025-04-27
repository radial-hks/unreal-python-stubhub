## NiagaraDataInterfaceArrayColor Objects

```python
class NiagaraDataInterfaceArrayColor(NiagaraDataInterfaceArray)
```

Niagara Data Interface Array Color

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraDataInterfaceArrayFloat.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color_data`` (Array[LinearColor]):  [Read-Write]
- ``gpu_sync_mode`` (NiagaraGpuSyncMode):  [Read-Write] How to do we want to synchronize modifications to the array data.
- ``max_elements`` (int32):  [Read-Write] When greater than 0 sets the maximum number of elements the array can hold, only relevant when using operations that modify the array size.

<a id="unreal.NiagaraDataInterfaceArrayColor.color_data"></a>

#### color_data

```python
@property
def color_data() -> Array[LinearColor]
```

(Array[LinearColor]):  [Read-Write]

<a id="unreal.NiagaraDataInterfaceArrayColor.color_data"></a>

#### color_data

```python
@color_data.setter
def color_data(value: Array[LinearColor]) -> None
```

<a id="unreal.NiagaraDataInterfaceArrayQuat"></a>