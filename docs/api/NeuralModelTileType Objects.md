## NeuralModelTileType Objects

```python
class NeuralModelTileType(EnumBase)
```

ENeural Model Tile Type

**C++ Source:**

- **Module**: Engine
- **File**: NeuralProfile.h

<a id="unreal.NeuralModelTileType.ONE_BY_ONE"></a>

#### ONE_BY_ONE

0: The NNE model is loaded and used as it is. No dimension augmentation. E.g.,
if the input texture has different dimensions, it will be scaled down before application

<a id="unreal.NeuralModelTileType.TWO_BY_TWO"></a>

#### TWO_BY_TWO

1

<a id="unreal.NeuralModelTileType.FOUR_BY_FOUR"></a>

#### FOUR_BY_FOUR

2

<a id="unreal.NeuralModelTileType.EIGHT_BY_EIGHT"></a>

#### EIGHT_BY_EIGHT

3

<a id="unreal.NeuralModelTileType.AUTO"></a>

#### AUTO

4: Create tiled buffers in batch dimension automatically, where each tile runs the neural model
      e.g., if the model input dimension is (1x3x200x200) and the used buffer size of the post processing
      is 1000x1000, then 5x5 tiles ((5x5)x3x200x200) will be run and recombined.

<a id="unreal.TileOverlapResolveType"></a>