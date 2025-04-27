## NiagaraDataInterfaceGrid3D Objects

```python
class NiagaraDataInterfaceGrid3D(NiagaraDataInterfaceRWBase)
```

Niagara Data Interface Grid 3D

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraDataInterfaceRW.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cell_size`` (float):  [Read-Write] World space size of a cell
- ``clear_before_non_iteration_stage`` (bool):  [Read-Write] Option to clear the buffer prior to a stage where the iteration count does not match the grid resolution.  Useful for stages where one wants to do sparse writes
  and accumulate values.
- ``num_cells`` (IntVector):  [Read-Write] Number of cells
- ``num_cells_max_axis`` (int32):  [Read-Write] Number of cells on the longest axis
- ``set_resolution_method`` (SetResolutionMethod):  [Read-Write] Method for setting the grid resolution
- ``world_b_box_size`` (Vector):  [Read-Write] World size of the grid

<a id="unreal.NiagaraDataInterfaceGrid3DCollection"></a>