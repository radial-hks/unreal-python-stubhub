## NeuralProfileStruct Objects

```python
class NeuralProfileStruct(StructBase)
```

struct with all the settings we want in UNeuralProfile, separate to make it easer to pass this data around in the engine.

**C++ Source:**

- **Module**: Engine
- **File**: NeuralProfile.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``batch_size_override`` (int32):  [Read-Write] Used to override the batch size if the batch dimension is dynamic (-1)
- ``input_dimension`` (IntVector4):  [Read-Write] Input dimension of the NNEModelData model
- ``input_format`` (NeuralProfileFormat):  [Read-Write] Define the expected input format, if any output from material is not this format, a custom conversion
  will be applied for this conversion.
- ``nne_model_data`` (Object):  [Read-Write] Stores the NNEModelData imported from e.g., onnx model
- ``output_dimension`` (IntVector4):  [Read-Write] Output dimension of the NNEModelData model
- ``output_format`` (NeuralProfileFormat):  [Read-Write] Define the expected output format. A conversion between the output format and the actual format will
  be applied automatically.
- ``runtime_type`` (NeuralProfileRuntimeType):  [Read-Write] runtime type (support "NNERuntimeORTDml" only at this moment)
- ``tile_overlap`` (IntPoint):  [Read-Write] Tile border overlaps (Left|Right, Top|Bottom). The larger this value, the more tiles are required to cover the whole screen when TileSize is Auto.
- ``tile_overlap_resolve_type`` (TileOverlapResolveType):  [Read-Write]
- ``tile_size`` (NeuralModelTileType):  [Read-Write] Total tiles used. Each tile will be executed by 1 batch

<a id="unreal.NeuralProfileStruct.__init__"></a>

#### __init__

```python
def __init__(input_format: NeuralProfileFormat = NeuralProfileFormat.TYPE32,
             output_format: NeuralProfileFormat = NeuralProfileFormat.TYPE32,
             runtime_type: NeuralProfileRuntimeType = NeuralProfileRuntimeType.
             NNE_RUNTIME_ORT_DML,
             nne_model_data: Object = None,
             input_dimension: IntVector4 = [0, 0, 0, 0],
             output_dimension: IntVector4 = [0, 0, 0, 0],
             batch_size_override: int = 0) -> None
```

<a id="unreal.NeuralProfileStruct.input_format"></a>

#### input_format

```python
@property
def input_format() -> NeuralProfileFormat
```

(NeuralProfileFormat):  [Read-Only] Define the expected input format, if any output from material is not this format, a custom conversion
will be applied for this conversion.

<a id="unreal.NeuralProfileStruct.output_format"></a>

#### output_format

```python
@property
def output_format() -> NeuralProfileFormat
```

(NeuralProfileFormat):  [Read-Only] Define the expected output format. A conversion between the output format and the actual format will
be applied automatically.

<a id="unreal.NeuralProfileStruct.runtime_type"></a>

#### runtime_type

```python
@property
def runtime_type() -> NeuralProfileRuntimeType
```

(NeuralProfileRuntimeType):  [Read-Only] runtime type (support "NNERuntimeORTDml" only at this moment)

<a id="unreal.NeuralProfileStruct.nne_model_data"></a>

#### nne_model_data

```python
@property
def nne_model_data() -> Object
```

(Object):  [Read-Only] Stores the NNEModelData imported from e.g., onnx model

<a id="unreal.NeuralProfileStruct.input_dimension"></a>

#### input_dimension

```python
@property
def input_dimension() -> IntVector4
```

(IntVector4):  [Read-Only] Input dimension of the NNEModelData model

<a id="unreal.NeuralProfileStruct.output_dimension"></a>

#### output_dimension

```python
@property
def output_dimension() -> IntVector4
```

(IntVector4):  [Read-Only] Output dimension of the NNEModelData model

<a id="unreal.NeuralProfileStruct.batch_size_override"></a>

#### batch_size_override

```python
@property
def batch_size_override() -> int
```

(int32):  [Read-Only] Used to override the batch size if the batch dimension is dynamic (-1)

<a id="unreal.SpecularProfileStruct"></a>