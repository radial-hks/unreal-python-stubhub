## MaterialStatistics Objects

```python
class MaterialStatistics(StructBase)
```

Material Statistics

**C++ Source:**

- **Module**: MaterialEditor
- **File**: MaterialEditingLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``num_interpolator_scalars`` (int32):  [Read-Write] Number of interpolator scalars required for user-defined interpolators
- ``num_pixel_shader_instructions`` (int32):  [Read-Write] Number of instructions used by most expensive pixel shader in the material
- ``num_pixel_texture_samples`` (int32):  [Read-Write] Number of textures sampled by the pixel shader
- ``num_samplers`` (int32):  [Read-Write] Number of samplers required by the material
- ``num_uv_scalars`` (int32):  [Read-Write] Number of interpolator scalars required for UVs
- ``num_vertex_shader_instructions`` (int32):  [Read-Write] Number of instructions used by most expensive vertex shader in the material
- ``num_vertex_texture_samples`` (int32):  [Read-Write] Number of textures sampled by the vertex shader
- ``num_virtual_texture_samples`` (int32):  [Read-Write] Number of virtual textures sampled

<a id="unreal.MaterialStatistics.__init__"></a>

#### \_\_init\_\_

```python
def __init__(num_vertex_shader_instructions: int = 0,
             num_pixel_shader_instructions: int = 0,
             num_samplers: int = 0,
             num_vertex_texture_samples: int = 0,
             num_pixel_texture_samples: int = 0,
             num_virtual_texture_samples: int = 0,
             num_uv_scalars: int = 0,
             num_interpolator_scalars: int = 0) -> None
```

<a id="unreal.MaterialStatistics.num_vertex_shader_instructions"></a>

#### num\_vertex\_shader\_instructions

```python
@property
def num_vertex_shader_instructions() -> int
```

(int32):  [Read-Write] Number of instructions used by most expensive vertex shader in the material

<a id="unreal.MaterialStatistics.num_vertex_shader_instructions"></a>

#### num\_vertex\_shader\_instructions

```python
@num_vertex_shader_instructions.setter
def num_vertex_shader_instructions(value: int) -> None
```

<a id="unreal.MaterialStatistics.num_pixel_shader_instructions"></a>

#### num\_pixel\_shader\_instructions

```python
@property
def num_pixel_shader_instructions() -> int
```

(int32):  [Read-Write] Number of instructions used by most expensive pixel shader in the material

<a id="unreal.MaterialStatistics.num_pixel_shader_instructions"></a>

#### num\_pixel\_shader\_instructions

```python
@num_pixel_shader_instructions.setter
def num_pixel_shader_instructions(value: int) -> None
```

<a id="unreal.MaterialStatistics.num_samplers"></a>

#### num\_samplers

```python
@property
def num_samplers() -> int
```

(int32):  [Read-Write] Number of samplers required by the material

<a id="unreal.MaterialStatistics.num_samplers"></a>

#### num\_samplers

```python
@num_samplers.setter
def num_samplers(value: int) -> None
```

<a id="unreal.MaterialStatistics.num_vertex_texture_samples"></a>

#### num\_vertex\_texture\_samples

```python
@property
def num_vertex_texture_samples() -> int
```

(int32):  [Read-Write] Number of textures sampled by the vertex shader

<a id="unreal.MaterialStatistics.num_vertex_texture_samples"></a>

#### num\_vertex\_texture\_samples

```python
@num_vertex_texture_samples.setter
def num_vertex_texture_samples(value: int) -> None
```

<a id="unreal.MaterialStatistics.num_pixel_texture_samples"></a>

#### num\_pixel\_texture\_samples

```python
@property
def num_pixel_texture_samples() -> int
```

(int32):  [Read-Write] Number of textures sampled by the pixel shader

<a id="unreal.MaterialStatistics.num_pixel_texture_samples"></a>

#### num\_pixel\_texture\_samples

```python
@num_pixel_texture_samples.setter
def num_pixel_texture_samples(value: int) -> None
```

<a id="unreal.MaterialStatistics.num_virtual_texture_samples"></a>

#### num\_virtual\_texture\_samples

```python
@property
def num_virtual_texture_samples() -> int
```

(int32):  [Read-Write] Number of virtual textures sampled

<a id="unreal.MaterialStatistics.num_virtual_texture_samples"></a>

#### num\_virtual\_texture\_samples

```python
@num_virtual_texture_samples.setter
def num_virtual_texture_samples(value: int) -> None
```

<a id="unreal.MaterialStatistics.num_uv_scalars"></a>

#### num\_uv\_scalars

```python
@property
def num_uv_scalars() -> int
```

(int32):  [Read-Write] Number of interpolator scalars required for UVs

<a id="unreal.MaterialStatistics.num_uv_scalars"></a>

#### num\_uv\_scalars

```python
@num_uv_scalars.setter
def num_uv_scalars(value: int) -> None
```

<a id="unreal.MaterialStatistics.num_interpolator_scalars"></a>

#### num\_interpolator\_scalars

```python
@property
def num_interpolator_scalars() -> int
```

(int32):  [Read-Write] Number of interpolator scalars required for user-defined interpolators

<a id="unreal.MaterialStatistics.num_interpolator_scalars"></a>

#### num\_interpolator\_scalars

```python
@num_interpolator_scalars.setter
def num_interpolator_scalars(value: int) -> None
```

<a id="unreal.XRHMDData"></a>