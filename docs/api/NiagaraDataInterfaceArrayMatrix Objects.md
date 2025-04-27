## NiagaraDataInterfaceArrayMatrix Objects

```python
class NiagaraDataInterfaceArrayMatrix(NiagaraDataInterfaceArray)
```

Niagara Data Interface Array Matrix

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraDataInterfaceArrayFloat.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``gpu_sync_mode`` (NiagaraGpuSyncMode):  [Read-Write] How to do we want to synchronize modifications to the array data.
- ``matrix_data`` (Array[Matrix]):  [Read-Write]
- ``max_elements`` (int32):  [Read-Write] When greater than 0 sets the maximum number of elements the array can hold, only relevant when using operations that modify the array size.

<a id="unreal.NiagaraDataInterfaceArrayMatrix.matrix_data"></a>

#### matrix_data

```python
@property
def matrix_data() -> Array[Matrix]
```

(Array[Matrix]):  [Read-Write]

<a id="unreal.NiagaraDataInterfaceArrayMatrix.matrix_data"></a>

#### matrix_data

```python
@matrix_data.setter
def matrix_data(value: Array[Matrix]) -> None
```

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary"></a>