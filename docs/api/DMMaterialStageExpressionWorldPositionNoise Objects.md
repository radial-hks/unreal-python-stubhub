## DMMaterialStageExpressionWorldPositionNoise Objects

```python
class DMMaterialStageExpressionWorldPositionNoise(DMMaterialStageExpression)
```

DMMaterial Stage Expression World Position Noise

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMMSEWorldPositionNoise.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_nested_inputs`` (bool):  [Read-Only]
- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``input_connectors`` (Array[DMMaterialStageConnector]):  [Read-Only]
- ``input_required`` (bool):  [Read-Only]
- ``location_type`` (DMLocationType):  [Read-Write]
- ``material_expression_class`` (type(Class)):  [Read-Only]
- ``menus`` (Array[DMExpressionMenu]):  [Read-Only]
- ``name`` (Text):  [Read-Only]
- ``noise_function`` (VectorNoiseFunction):  [Read-Write]
- ``output_connectors`` (Array[DMMaterialStageConnector]):  [Read-Only]
- ``quality`` (int32):  [Read-Write]
- ``shader_offset`` (WorldPositionIncludedOffsets):  [Read-Write]
- ``tile_size`` (int32):  [Read-Write]
- ``tiling`` (bool):  [Read-Write]

<a id="unreal.DMMaterialStageExpressionWorldPositionNoise.location_type"></a>

#### location_type

```python
@property
def location_type() -> DMLocationType
```

(DMLocationType):  [Read-Write]

<a id="unreal.DMMaterialStageExpressionWorldPositionNoise.location_type"></a>

#### location_type

```python
@location_type.setter
def location_type(value: DMLocationType) -> None
```

<a id="unreal.DMMaterialStageExpressionWorldPositionNoise.shader_offset"></a>

#### shader_offset

```python
@property
def shader_offset() -> WorldPositionIncludedOffsets
```

(WorldPositionIncludedOffsets):  [Read-Write]

<a id="unreal.DMMaterialStageExpressionWorldPositionNoise.shader_offset"></a>

#### shader_offset

```python
@shader_offset.setter
def shader_offset(value: WorldPositionIncludedOffsets) -> None
```

<a id="unreal.DMMaterialStageExpressionWorldPositionNoise.noise_function"></a>

#### noise_function

```python
@property
def noise_function() -> VectorNoiseFunction
```

(VectorNoiseFunction):  [Read-Write]

<a id="unreal.DMMaterialStageExpressionWorldPositionNoise.noise_function"></a>

#### noise_function

```python
@noise_function.setter
def noise_function(value: VectorNoiseFunction) -> None
```

<a id="unreal.DMMaterialStageExpressionWorldPositionNoise.quality"></a>

#### quality

```python
@property
def quality() -> int
```

(int32):  [Read-Write]

<a id="unreal.DMMaterialStageExpressionWorldPositionNoise.quality"></a>

#### quality

```python
@quality.setter
def quality(value: int) -> None
```

<a id="unreal.DMMaterialStageExpressionWorldPositionNoise.tiling"></a>

#### tiling

```python
@property
def tiling() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DMMaterialStageExpressionWorldPositionNoise.tiling"></a>

#### tiling

```python
@tiling.setter
def tiling(value: bool) -> None
```

<a id="unreal.DMMaterialStageExpressionWorldPositionNoise.tile_size"></a>

#### tile_size

```python
@property
def tile_size() -> int
```

(int32):  [Read-Write]

<a id="unreal.DMMaterialStageExpressionWorldPositionNoise.tile_size"></a>

#### tile_size

```python
@tile_size.setter
def tile_size(value: int) -> None
```

<a id="unreal.DMMaterialStageExpressionWorldPositionNoise.set_tiling"></a>

#### set_tiling

```python
def set_tiling(tiling: bool) -> None
```

x.set_tiling(tiling) -> None
Set Tiling

Args:
    tiling (bool):

<a id="unreal.DMMaterialStageExpressionWorldPositionNoise.set_tile_size"></a>

#### set_tile_size

```python
def set_tile_size(tile_size: int) -> None
```

x.set_tile_size(tile_size) -> None
Set Tile Size

Args:
    tile_size (int32):

<a id="unreal.DMMaterialStageExpressionWorldPositionNoise.set_shader_offset"></a>

#### set_shader_offset

```python
def set_shader_offset(shader_offset: WorldPositionIncludedOffsets) -> None
```

x.set_shader_offset(shader_offset) -> None
Set Shader Offset

Args:
    shader_offset (WorldPositionIncludedOffsets):

<a id="unreal.DMMaterialStageExpressionWorldPositionNoise.set_quality"></a>

#### set_quality

```python
def set_quality(quality: int) -> None
```

x.set_quality(quality) -> None
Set Quality

Args:
    quality (int32):

<a id="unreal.DMMaterialStageExpressionWorldPositionNoise.set_noise_function"></a>

#### set_noise_function

```python
def set_noise_function(noise_function: VectorNoiseFunction) -> None
```

x.set_noise_function(noise_function) -> None
Set Noise Function

Args:
    noise_function (VectorNoiseFunction):

<a id="unreal.DMMaterialStageExpressionWorldPositionNoise.set_location_type"></a>

#### set_location_type

```python
def set_location_type(location_type: DMLocationType) -> None
```

x.set_location_type(location_type) -> None
Set Location Type

Args:
    location_type (DMLocationType):

<a id="unreal.DMMaterialStageExpressionWorldPositionNoise.get_tiling"></a>

#### get_tiling

```python
def get_tiling() -> bool
```

x.get_tiling() -> bool
Get Tiling

Returns:
    bool:

<a id="unreal.DMMaterialStageExpressionWorldPositionNoise.get_tile_size"></a>

#### get_tile_size

```python
def get_tile_size() -> int
```

x.get_tile_size() -> int32
Get Tile Size

Returns:
    int32:

<a id="unreal.DMMaterialStageExpressionWorldPositionNoise.get_shader_offset"></a>

#### get_shader_offset

```python
def get_shader_offset() -> WorldPositionIncludedOffsets
```

x.get_shader_offset() -> WorldPositionIncludedOffsets
Get Shader Offset

Returns:
    WorldPositionIncludedOffsets:

<a id="unreal.DMMaterialStageExpressionWorldPositionNoise.get_quality"></a>

#### get_quality

```python
def get_quality() -> int
```

x.get_quality() -> int32
Get Quality

Returns:
    int32:

<a id="unreal.DMMaterialStageExpressionWorldPositionNoise.get_noise_function"></a>

#### get_noise_function

```python
def get_noise_function() -> VectorNoiseFunction
```

x.get_noise_function() -> VectorNoiseFunction
Get Noise Function

Returns:
    VectorNoiseFunction:

<a id="unreal.DMMaterialStageExpressionWorldPositionNoise.get_location_type"></a>

#### get_location_type

```python
def get_location_type() -> DMLocationType
```

x.get_location_type() -> DMLocationType
Get Location Type

Returns:
    DMLocationType:

<a id="unreal.DMMaterialStageGradientLinear"></a>