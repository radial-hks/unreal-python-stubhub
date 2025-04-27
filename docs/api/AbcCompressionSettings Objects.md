## AbcCompressionSettings Objects

```python
class AbcCompressionSettings(StructBase)
```

Abc Compression Settings

**C++ Source:**

- **Plugin**: AlembicImporter
- **Module**: AlembicLibrary
- **File**: AbcImportSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bake_matrix_animation`` (bool):  [Read-Write] Whether or not Matrix-only animation should be baked out as vertex animation (or skipped?)
- ``base_calculation_type`` (BaseCalculationType):  [Read-Write] Determines how the final number of bases that are stored as morph targets are calculated
- ``max_number_of_bases`` (int32):  [Read-Write] Will generate given fixed number of bases as morph targets
- ``merge_meshes`` (bool):  [Read-Write] Whether or not the individual meshes should be merged for compression purposes
- ``minimum_number_of_vertex_influence_percentage`` (float):  [Read-Write] Minimum percentage of influenced vertices required for a morph target to be valid
- ``percentage_of_total_bases`` (float):  [Read-Write] Will generate given percentage of the given bases as morph targets

<a id="unreal.AbcCompressionSettings.__init__"></a>

#### __init__

```python
def __init__(
        merge_meshes: bool = False,
        bake_matrix_animation: bool = False,
        base_calculation_type: BaseCalculationType = 0,
        percentage_of_total_bases: float = 0.000000,
        max_number_of_bases: int = 0,
        minimum_number_of_vertex_influence_percentage: float = 0.000000
) -> None
```

<a id="unreal.AbcCompressionSettings.merge_meshes"></a>

#### merge_meshes

```python
@property
def merge_meshes() -> bool
```

(bool):  [Read-Write] Whether or not the individual meshes should be merged for compression purposes

<a id="unreal.AbcCompressionSettings.merge_meshes"></a>

#### merge_meshes

```python
@merge_meshes.setter
def merge_meshes(value: bool) -> None
```

<a id="unreal.AbcCompressionSettings.bake_matrix_animation"></a>

#### bake_matrix_animation

```python
@property
def bake_matrix_animation() -> bool
```

(bool):  [Read-Write] Whether or not Matrix-only animation should be baked out as vertex animation (or skipped?)

<a id="unreal.AbcCompressionSettings.bake_matrix_animation"></a>

#### bake_matrix_animation

```python
@bake_matrix_animation.setter
def bake_matrix_animation(value: bool) -> None
```

<a id="unreal.AbcCompressionSettings.base_calculation_type"></a>

#### base_calculation_type

```python
@property
def base_calculation_type() -> BaseCalculationType
```

(BaseCalculationType):  [Read-Write] Determines how the final number of bases that are stored as morph targets are calculated

<a id="unreal.AbcCompressionSettings.base_calculation_type"></a>

#### base_calculation_type

```python
@base_calculation_type.setter
def base_calculation_type(value: BaseCalculationType) -> None
```

<a id="unreal.AbcCompressionSettings.percentage_of_total_bases"></a>

#### percentage_of_total_bases

```python
@property
def percentage_of_total_bases() -> float
```

(float):  [Read-Write] Will generate given percentage of the given bases as morph targets

<a id="unreal.AbcCompressionSettings.percentage_of_total_bases"></a>

#### percentage_of_total_bases

```python
@percentage_of_total_bases.setter
def percentage_of_total_bases(value: float) -> None
```

<a id="unreal.AbcCompressionSettings.max_number_of_bases"></a>

#### max_number_of_bases

```python
@property
def max_number_of_bases() -> int
```

(int32):  [Read-Write] Will generate given fixed number of bases as morph targets

<a id="unreal.AbcCompressionSettings.max_number_of_bases"></a>

#### max_number_of_bases

```python
@max_number_of_bases.setter
def max_number_of_bases(value: int) -> None
```

<a id="unreal.AbcCompressionSettings.minimum_number_of_vertex_influence_percentage"></a>

#### minimum_number_of_vertex_influence_percentage

```python
@property
def minimum_number_of_vertex_influence_percentage() -> float
```

(float):  [Read-Write] Minimum percentage of influenced vertices required for a morph target to be valid

<a id="unreal.AbcCompressionSettings.minimum_number_of_vertex_influence_percentage"></a>

#### minimum_number_of_vertex_influence_percentage

```python
@minimum_number_of_vertex_influence_percentage.setter
def minimum_number_of_vertex_influence_percentage(value: float) -> None
```

<a id="unreal.AbcSamplingSettings"></a>