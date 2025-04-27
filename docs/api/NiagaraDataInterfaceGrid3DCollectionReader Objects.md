## NiagaraDataInterfaceGrid3DCollectionReader Objects

```python
class NiagaraDataInterfaceGrid3DCollectionReader(
        NiagaraDataInterfaceGrid3DCollection)
```

Niagara Data Interface Grid 3DCollection Reader

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraDataInterfaceGrid3DCollectionReader.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cell_size`` (float):  [Read-Write] World space size of a cell
- ``clear_before_non_iteration_stage`` (bool):  [Read-Write] Option to clear the buffer prior to a stage where the iteration count does not match the grid resolution.  Useful for stages where one wants to do sparse writes
  and accumulate values.
- ``di_name`` (str):  [Read-Write] Name of the Grid2DCollection Data Interface on the emitter
- ``emitter_name`` (str):  [Read-Write] Name of the emitter to read from
- ``num_attributes`` (int32):  [Read-Write] Number of attributes stored on the grid
- ``num_cells`` (IntVector):  [Read-Write] Number of cells
- ``num_cells_max_axis`` (int32):  [Read-Write] Number of cells on the longest axis
- ``override_buffer_format`` (NiagaraGpuBufferFormat):  [Read-Write] When enabled overrides the format used to store data inside the grid, otherwise uses the project default setting.  Lower bit depth formats will save memory and performance at the cost of precision.
- ``override_format`` (bool):  [Read-Write]
- ``preview_attribute`` (Name):  [Read-Write] When enabled allows you to preview the grid in a debug display
- ``preview_grid`` (bool):  [Read-Write]
- ``render_target_user_parameter`` (NiagaraUserParameterBinding):  [Read-Write] Reference to a user parameter if we're reading one.
- ``set_resolution_method`` (SetResolutionMethod):  [Read-Write] Method for setting the grid resolution
- ``world_b_box_size`` (Vector):  [Read-Write] World size of the grid

<a id="unreal.NiagaraDataInterfaceIntRenderTarget2D"></a>