## NiagaraDataInterfaceGrid2DCollectionReader Objects

```python
class NiagaraDataInterfaceGrid2DCollectionReader(
        NiagaraDataInterfaceGrid2DCollection)
```

Niagara Data Interface Grid 2DCollection Reader

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraDataInterfaceGrid2DCollectionReader.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``clear_before_non_iteration_stage`` (bool):  [Read-Write] Option to clear the buffer prior to a stage where the iteration count does not match the grid resolution.  Useful for stages where one wants to do sparse writes
  and accumulate values.
- ``di_name`` (str):  [Read-Write] Name of the Grid2DCollection Data Interface on the emitter
- ``emitter_name`` (str):  [Read-Write] Name of the emitter to read from
- ``num_attributes`` (int32):  [Read-Write] Number of Attributes
- ``num_cells_max_axis`` (int32):  [Read-Write] Number of cells on the longest axis
- ``num_cells_x`` (int32):  [Read-Write] Number of cells in X
- ``num_cells_y`` (int32):  [Read-Write] Number of cells in Y
- ``override_buffer_format`` (NiagaraGpuBufferFormat):  [Read-Write] When enabled overrides the format used to store data inside the grid, otherwise uses the project default setting.  Lower bit depth formats will save memory and performance at the cost of precision.
- ``override_format`` (bool):  [Read-Write]
- ``preview_attribute`` (Name):  [Read-Write] When enabled allows you to preview the grid in a debug display
- ``preview_grid`` (bool):  [Read-Write]
- ``render_target_user_parameter`` (NiagaraUserParameterBinding):  [Read-Write] Reference to a user parameter if we're reading one.
- ``set_grid_from_max_axis`` (bool):  [Read-Write] Set grid resolution according to longest axis
- ``world_b_box_size`` (Vector2D):  [Read-Write] World size of the grid

<a id="unreal.NiagaraDataInterfaceGrid3D"></a>