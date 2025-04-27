## ImportanceSamplingLibrary Objects

```python
class ImportanceSamplingLibrary(BlueprintFunctionLibrary)
```

Importance Sampling Library

**C++ Source:**

- **Module**: Engine
- **File**: ImportanceSamplingLibrary.h

<a id="unreal.ImportanceSamplingLibrary.random_sobol_float"></a>

#### random_sobol_float

```python
@classmethod
def random_sobol_float(cls, index: int, dimension: int, seed: float) -> float
```

X.random_sobol_float(index, dimension, seed) -> float


Args:
    index (int32): Which sequential point
    dimension (int32): Which Sobol dimension (0 to 15)
    seed (float): Random seed (in the range 0-1) to randomize across multiple sequences

Returns:
    float: Sobol-distributed random number between 0 and 1

<a id="unreal.ImportanceSamplingLibrary.random_sobol_cell3d"></a>

#### random_sobol_cell3d

```python
@classmethod
def random_sobol_cell3d(
        cls,
        index: int,
        num_cells: int = 1,
        cell: Vector = [0.000000, 0.000000, 0.000000],
        seed: Vector = [0.000000, 0.000000, 0.000000]) -> Vector
```

X.random_sobol_cell3d(index, num_cells=1, cell=[0.000000, 0.000000, 0.000000], seed=[0.000000, 0.000000, 0.000000]) -> Vector


Args:
    index (int32): Which sequential point in the cell (starting at 0)
    num_cells (int32): Size of cell grid, 1 to 1024. Rounded up to the next power of two
    cell (Vector): Give a point from this integer grid cell
    seed (Vector): Random 3D seed (components in the range 0-1) to randomize across multiple sequences

Returns:
    Vector: Sobol-distributed random 3D vector in the given grid cell

<a id="unreal.ImportanceSamplingLibrary.random_sobol_cell2d"></a>

#### random_sobol_cell2d

```python
@classmethod
def random_sobol_cell2d(cls,
                        index: int,
                        num_cells: int = 1,
                        cell: Vector2D = [0.000000, 0.000000],
                        seed: Vector2D = [0.000000, 0.000000]) -> Vector2D
```

X.random_sobol_cell2d(index, num_cells=1, cell=[0.000000, 0.000000], seed=[0.000000, 0.000000]) -> Vector2D


Args:
    index (int32): Which sequential point in the cell (starting at 0)
    num_cells (int32): Size of cell grid, 1 to 32768. Rounded up to the next power of two
    cell (Vector2D): Give a point from this integer grid cell
    seed (Vector2D): Random 2D seed (components in the range 0-1) to randomize across multiple sequences

Returns:
    Vector2D: Sobol-distributed random 2D position in the given grid cell

<a id="unreal.ImportanceSamplingLibrary.next_sobol_float"></a>

#### next_sobol_float

```python
@classmethod
def next_sobol_float(cls, index: int, dimension: int,
                     previous_value: float) -> float
```

X.next_sobol_float(index, dimension, previous_value) -> float


Args:
    index (int32): Which sequential point
    dimension (int32): Which Sobol dimension (0 to 15)
    previous_value (float): The Sobol value for Index-1

Returns:
    float: Sobol-distributed random number between 0 and 1

<a id="unreal.ImportanceSamplingLibrary.next_sobol_cell3d"></a>

#### next_sobol_cell3d

```python
@classmethod
def next_sobol_cell3d(
        cls,
        index: int,
        num_cells: int = 1,
        previous_value: Vector = [0.000000, 0.000000, 0.000000]) -> Vector
```

X.next_sobol_cell3d(index, num_cells=1, previous_value=[0.000000, 0.000000, 0.000000]) -> Vector


Args:
    index (int32): Which sequential point
    num_cells (int32): Size of cell grid, 1 to 1024. Rounded up to the next power of two
    previous_value (Vector): The Sobol value for Index-1

Returns:
    Vector: Sobol-distributed random 3D position in the same grid cell

<a id="unreal.ImportanceSamplingLibrary.next_sobol_cell2d"></a>

#### next_sobol_cell2d

```python
@classmethod
def next_sobol_cell2d(
        cls,
        index: int,
        num_cells: int = 1,
        previous_value: Vector2D = [0.000000, 0.000000]) -> Vector2D
```

X.next_sobol_cell2d(index, num_cells=1, previous_value=[0.000000, 0.000000]) -> Vector2D


Args:
    index (int32): Which sequential point
    num_cells (int32): Size of cell grid, 1 to 32768. Rounded up to the next power of two
    previous_value (Vector2D): The Sobol value for Index-1

Returns:
    Vector2D: Sobol-distributed random 2D position in the same grid cell

<a id="unreal.ImportanceSamplingLibrary.importance_sample"></a>

#### importance_sample

```python
@classmethod
def importance_sample(
        cls, texture: ImportanceTexture, rand: Vector2D, samples: int,
        intensity: float) -> Tuple[Vector2D, LinearColor, float, float]
```

X.importance_sample(texture, rand, samples, intensity) -> (sample_position=Vector2D, sample_color=LinearColor, sample_intensity=float, sample_size=float)
Distribute sample points proportional to Texture2D luminance.
outparam: SamplePosition - Importance sampled 2D output texture coordinate (0-1)
outparam: SampleColor - Representative color near Position from MIP level for SampleSize
outparam: SampleIntensity - Intensity of individual points, scaled by probability and number of samples
outparam: SampleSize - Local density of points near Position (scaled for 1x1 texture space)

Args:
    texture (ImportanceTexture): 
    rand (Vector2D): Random 2D point with components evenly distributed between 0 and 1
    samples (int32): Total number of samples that will be used
    intensity (float): Total intensity for light

Returns:
    tuple: 

    sample_position (Vector2D): 

    sample_color (LinearColor): 

    sample_intensity (float): 

    sample_size (float):

<a id="unreal.LevelBounds"></a>