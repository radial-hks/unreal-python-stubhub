## NiagaraDataInterfaceArrayQuat Objects

```python
class NiagaraDataInterfaceArrayQuat(NiagaraDataInterfaceArray)
```

Niagara Data Interface Array Quat

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraDataInterfaceArrayFloat.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``gpu_sync_mode`` (NiagaraGpuSyncMode):  [Read-Write] How to do we want to synchronize modifications to the array data.
- ``max_elements`` (int32):  [Read-Write] When greater than 0 sets the maximum number of elements the array can hold, only relevant when using operations that modify the array size.
- ``quat_data`` (Array[Quat]):  [Read-Write]

<a id="unreal.NiagaraDataInterfaceArrayQuat.quat_data"></a>

#### quat_data

```python
@property
def quat_data() -> Array[Quat]
```

(Array[Quat]):  [Read-Write]

<a id="unreal.NiagaraDataInterfaceArrayQuat.quat_data"></a>

#### quat_data

```python
@quat_data.setter
def quat_data(value: Array[Quat]) -> None
```

<a id="unreal.NiagaraDataInterfaceArrayMatrix"></a>