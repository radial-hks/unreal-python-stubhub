## NiagaraDataInterfaceGrid3DCollection Objects

```python
class NiagaraDataInterfaceGrid3DCollection(NiagaraDataInterfaceGrid3D)
```

Niagara Data Interface Grid 3DCollection

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraDataInterfaceGrid3DCollection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cell_size`` (float):  [Read-Write] World space size of a cell
- ``clear_before_non_iteration_stage`` (bool):  [Read-Write] Option to clear the buffer prior to a stage where the iteration count does not match the grid resolution.  Useful for stages where one wants to do sparse writes
  and accumulate values.
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

<a id="unreal.NiagaraDataInterfaceGrid3DCollection.get_texture_size"></a>

#### get_texture_size

```python
def get_texture_size(component: NiagaraComponent) -> Tuple[int, int, int]
```

x.get_texture_size(component) -> (size_x=int32, size_y=int32, size_z=int32)
Get Texture Size

Args:
    component (NiagaraComponent): 

Returns:
    tuple: 

    size_x (int32): 

    size_y (int32): 

    size_z (int32):

<a id="unreal.NiagaraDataInterfaceGrid3DCollection.get_raw_texture_size"></a>

#### get_raw_texture_size

```python
def get_raw_texture_size(component: NiagaraComponent) -> Tuple[int, int, int]
```

x.get_raw_texture_size(component) -> (size_x=int32, size_y=int32, size_z=int32)
Get Raw Texture Size

Args:
    component (NiagaraComponent): 

Returns:
    tuple: 

    size_x (int32): 

    size_y (int32): 

    size_z (int32):

<a id="unreal.NiagaraDataInterfaceGrid3DCollection.fill_volume_texture"></a>

#### fill_volume_texture

```python
def fill_volume_texture(component: NiagaraComponent, dest: VolumeTexture,
                        attribute_index: int) -> bool
```

x.fill_volume_texture(component, dest, attribute_index) -> bool
Fills a texture render target 2d with the current data from the simulation
#todo(dmp): this will eventually go away when we formalize how data makes it out of Niagara
#todo(dmp): reimplement for 3d
deprecated: This function has been replaced by object user variables on the emitter to specify render targets to fill with data.

Args:
    component (NiagaraComponent): 
    dest (VolumeTexture): 
    attribute_index (int32): 

Returns:
    bool:

<a id="unreal.NiagaraDataInterfaceGrid3DCollection.fill_raw_volume_texture"></a>

#### fill_raw_volume_texture

```python
def fill_raw_volume_texture(
        component: NiagaraComponent,
        dest: VolumeTexture) -> Optional[Tuple[int, int, int]]
```

x.fill_raw_volume_texture(component, dest) -> (tiles_x=int32, tiles_y=int32, tile_z=int32) or None
Fill Raw Volume Texture
deprecated: This function has been replaced by object user variables on the emitter to specify render targets to fill with data.

Args:
    component (NiagaraComponent): 
    dest (VolumeTexture): 

Returns:
    tuple or None: 

    tiles_x (int32): 

    tiles_y (int32): 

    tile_z (int32):

<a id="unreal.NiagaraDataInterfaceGrid3DCollectionReader"></a>