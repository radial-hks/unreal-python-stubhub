## AbcGeometryCacheSettings Objects

```python
class AbcGeometryCacheSettings(StructBase)
```

Abc Geometry Cache Settings

**C++ Source:**

- **Plugin**: AlembicImporter
- **Module**: AlembicLibrary
- **File**: AbcImportSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_constant_topology_optimizations`` (bool):  [Read-Write] Force the preprocessor to only do optimization once instead of when the preprocessor decides. This may lead to some problems with certain meshes but makes sure motion
            blur always works if the topology is constant.
- ``compressed_position_precision`` (float):  [Read-Write] Precision used for compressing vertex positions (lower = better result but less compression, higher = more lossy compression but smaller size)
- ``compressed_texture_coordinates_number_of_bits`` (int32):  [Read-Write] Bit-precision used for compressing texture coordinates (hight = better result but less compression, lower = more lossy compression but smaller size)
- ``flatten_tracks`` (bool):  [Read-Write] Whether or not to merge all vertex animation into one track
- ``motion_vectors`` (AbcGeometryCacheMotionVectorsImport):  [Read-Write]
- ``optimize_index_buffers`` (bool):  [Read-Write] Optimizes index buffers for each unique frame, to allow better cache coherency on the GPU. Very costly and time-consuming process, recommended to OFF.
- ``store_imported_vertex_numbers`` (bool):  [Read-Write] Store the imported vertex numbers. This lets you know the vertex numbers inside the DCC.
  The values of each vertex number will range from 0 to 7 for a cube. Even if the number of positions might be 24.

<a id="unreal.AbcGeometryCacheSettings.__init__"></a>

#### __init__

```python
def __init__(
        flatten_tracks: bool = False,
        store_imported_vertex_numbers: bool = False,
        apply_constant_topology_optimizations: bool = False,
        motion_vectors:
    AbcGeometryCacheMotionVectorsImport = AbcGeometryCacheMotionVectorsImport.
    NO_MOTION_VECTORS,
        optimize_index_buffers: bool = False,
        compressed_position_precision: float = 0.000000,
        compressed_texture_coordinates_number_of_bits: int = 0) -> None
```

<a id="unreal.AbcGeometryCacheSettings.flatten_tracks"></a>

#### flatten_tracks

```python
@property
def flatten_tracks() -> bool
```

(bool):  [Read-Write] Whether or not to merge all vertex animation into one track

<a id="unreal.AbcGeometryCacheSettings.flatten_tracks"></a>

#### flatten_tracks

```python
@flatten_tracks.setter
def flatten_tracks(value: bool) -> None
```

<a id="unreal.AbcGeometryCacheSettings.store_imported_vertex_numbers"></a>

#### store_imported_vertex_numbers

```python
@property
def store_imported_vertex_numbers() -> bool
```

(bool):  [Read-Write] Store the imported vertex numbers. This lets you know the vertex numbers inside the DCC.
The values of each vertex number will range from 0 to 7 for a cube. Even if the number of positions might be 24.

<a id="unreal.AbcGeometryCacheSettings.store_imported_vertex_numbers"></a>

#### store_imported_vertex_numbers

```python
@store_imported_vertex_numbers.setter
def store_imported_vertex_numbers(value: bool) -> None
```

<a id="unreal.AbcGeometryCacheSettings.apply_constant_topology_optimizations"></a>

#### apply_constant_topology_optimizations

```python
@property
def apply_constant_topology_optimizations() -> bool
```

(bool):  [Read-Write] Force the preprocessor to only do optimization once instead of when the preprocessor decides. This may lead to some problems with certain meshes but makes sure motion
          blur always works if the topology is constant.

<a id="unreal.AbcGeometryCacheSettings.apply_constant_topology_optimizations"></a>

#### apply_constant_topology_optimizations

```python
@apply_constant_topology_optimizations.setter
def apply_constant_topology_optimizations(value: bool) -> None
```

<a id="unreal.AbcGeometryCacheSettings.motion_vectors"></a>

#### motion_vectors

```python
@property
def motion_vectors() -> AbcGeometryCacheMotionVectorsImport
```

(AbcGeometryCacheMotionVectorsImport):  [Read-Write]

<a id="unreal.AbcGeometryCacheSettings.motion_vectors"></a>

#### motion_vectors

```python
@motion_vectors.setter
def motion_vectors(value: AbcGeometryCacheMotionVectorsImport) -> None
```

<a id="unreal.AbcGeometryCacheSettings.optimize_index_buffers"></a>

#### optimize_index_buffers

```python
@property
def optimize_index_buffers() -> bool
```

(bool):  [Read-Write] Optimizes index buffers for each unique frame, to allow better cache coherency on the GPU. Very costly and time-consuming process, recommended to OFF.

<a id="unreal.AbcGeometryCacheSettings.optimize_index_buffers"></a>

#### optimize_index_buffers

```python
@optimize_index_buffers.setter
def optimize_index_buffers(value: bool) -> None
```

<a id="unreal.AbcGeometryCacheSettings.compressed_position_precision"></a>

#### compressed_position_precision

```python
@property
def compressed_position_precision() -> float
```

(float):  [Read-Write] Precision used for compressing vertex positions (lower = better result but less compression, higher = more lossy compression but smaller size)

<a id="unreal.AbcGeometryCacheSettings.compressed_position_precision"></a>

#### compressed_position_precision

```python
@compressed_position_precision.setter
def compressed_position_precision(value: float) -> None
```

<a id="unreal.AbcGeometryCacheSettings.compressed_texture_coordinates_number_of_bits"></a>

#### compressed_texture_coordinates_number_of_bits

```python
@property
def compressed_texture_coordinates_number_of_bits() -> int
```

(int32):  [Read-Write] Bit-precision used for compressing texture coordinates (hight = better result but less compression, lower = more lossy compression but smaller size)

<a id="unreal.AbcGeometryCacheSettings.compressed_texture_coordinates_number_of_bits"></a>

#### compressed_texture_coordinates_number_of_bits

```python
@compressed_texture_coordinates_number_of_bits.setter
def compressed_texture_coordinates_number_of_bits(value: int) -> None
```

<a id="unreal.BoneReferencePair"></a>