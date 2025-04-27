## NiagaraDataInterfaceGrid2D Objects

```python
class NiagaraDataInterfaceGrid2D(NiagaraDataInterfaceRWBase)
```

Niagara Data Interface Grid 2D

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraDataInterfaceRW.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``clear_before_non_iteration_stage`` (bool):  [Read-Write] Option to clear the buffer prior to a stage where the iteration count does not match the grid resolution.  Useful for stages where one wants to do sparse writes
  and accumulate values.
- ``num_attributes`` (int32):  [Read-Write] Number of Attributes
- ``num_cells_max_axis`` (int32):  [Read-Write] Number of cells on the longest axis
- ``num_cells_x`` (int32):  [Read-Write] Number of cells in X
- ``num_cells_y`` (int32):  [Read-Write] Number of cells in Y
- ``set_grid_from_max_axis`` (bool):  [Read-Write] Set grid resolution according to longest axis
- ``world_b_box_size`` (Vector2D):  [Read-Write] World size of the grid

<a id="unreal.NiagaraDataInterfaceGrid2DCollection"></a>