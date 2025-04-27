## NiagaraDataInterfaceGrid2DCollection Objects

```python
class NiagaraDataInterfaceGrid2DCollection(NiagaraDataInterfaceGrid2D)
```

Niagara Data Interface Grid 2DCollection

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraDataInterfaceGrid2DCollection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``clear_before_non_iteration_stage`` (bool):  [Read-Write] Option to clear the buffer prior to a stage where the iteration count does not match the grid resolution.  Useful for stages where one wants to do sparse writes
  and accumulate values.
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

<a id="unreal.NiagaraDataInterfaceGrid2DCollection.get_texture_size"></a>

#### get_texture_size

```python
def get_texture_size(component: NiagaraComponent) -> Tuple[int, int]
```

x.get_texture_size(component) -> (size_x=int32, size_y=int32)
Get Texture Size

Args:
    component (NiagaraComponent): 

Returns:
    tuple: 

    size_x (int32): 

    size_y (int32):

<a id="unreal.NiagaraDataInterfaceGrid2DCollection.get_raw_texture_size"></a>

#### get_raw_texture_size

```python
def get_raw_texture_size(component: NiagaraComponent) -> Tuple[int, int]
```

x.get_raw_texture_size(component) -> (size_x=int32, size_y=int32)
Get Raw Texture Size
deprecated: This function has been replaced by object user variables on the emitter to specify render targets to fill with data.

Args:
    component (NiagaraComponent): 

Returns:
    tuple: 

    size_x (int32): 

    size_y (int32):

<a id="unreal.NiagaraDataInterfaceGrid2DCollection.fill_texture2d"></a>

#### fill_texture2d

```python
def fill_texture2d(component: NiagaraComponent, dest: TextureRenderTarget2D,
                   attribute_index: int) -> bool
```

x.fill_texture2d(component, dest, attribute_index) -> bool
Fills a texture render target 2d with the current data from the simulation
#todo(dmp): this will eventually go away when we formalize how data makes it out of Niagara
deprecated: This function has been replaced by object user variables on the emitter to specify render targets to fill with data.

Args:
    component (NiagaraComponent): 
    dest (TextureRenderTarget2D): 
    attribute_index (int32): 

Returns:
    bool:

<a id="unreal.NiagaraDataInterfaceGrid2DCollection.fill_raw_texture2d"></a>

#### fill_raw_texture2d

```python
def fill_raw_texture2d(
        component: NiagaraComponent,
        dest: TextureRenderTarget2D) -> Optional[Tuple[int, int]]
```

x.fill_raw_texture2d(component, dest) -> (tiles_x=int32, tiles_y=int32) or None
Fill Raw Texture 2D
deprecated: This function has been replaced by object user variables on the emitter to specify render targets to fill with data.

Args:
    component (NiagaraComponent): 
    dest (TextureRenderTarget2D): 

Returns:
    tuple or None: 

    tiles_x (int32): 

    tiles_y (int32):

<a id="unreal.NiagaraDataInterfaceGrid2DCollectionReader"></a>