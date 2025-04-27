## GeometryScriptMeshPointSamplingOptions Objects

```python
class GeometryScriptMeshPointSamplingOptions(StructBase)
```

Geometry Script Mesh Point Sampling Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshSamplingFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``max_num_samples`` (int32):  [Read-Write] Maximum number of samples requested. If 0 or default value, mesh will be maximally sampled
- ``random_seed`` (int32):  [Read-Write] Random Seed used to initialize sampling strategies
- ``sampling_radius`` (float):  [Read-Write] Desired "radius" of sample points. Spacing between samples is at least 2x this value.
- ``sub_sample_density`` (double):  [Read-Write] Density of subsampling used in Poisson strategy. Larger numbers mean "more accurate" (but slower) results.

<a id="unreal.GeometryScriptMeshPointSamplingOptions.__init__"></a>

#### __init__

```python
def __init__(sampling_radius: float = 0.000000,
             max_num_samples: int = 0,
             random_seed: int = 0,
             sub_sample_density: float = 0.000000) -> None
```

<a id="unreal.GeometryScriptMeshPointSamplingOptions.sampling_radius"></a>

#### sampling_radius

```python
@property
def sampling_radius() -> float
```

(float):  [Read-Write] Desired "radius" of sample points. Spacing between samples is at least 2x this value.

<a id="unreal.GeometryScriptMeshPointSamplingOptions.sampling_radius"></a>

#### sampling_radius

```python
@sampling_radius.setter
def sampling_radius(value: float) -> None
```

<a id="unreal.GeometryScriptMeshPointSamplingOptions.max_num_samples"></a>

#### max_num_samples

```python
@property
def max_num_samples() -> int
```

(int32):  [Read-Write] Maximum number of samples requested. If 0 or default value, mesh will be maximally sampled

<a id="unreal.GeometryScriptMeshPointSamplingOptions.max_num_samples"></a>

#### max_num_samples

```python
@max_num_samples.setter
def max_num_samples(value: int) -> None
```

<a id="unreal.GeometryScriptMeshPointSamplingOptions.random_seed"></a>

#### random_seed

```python
@property
def random_seed() -> int
```

(int32):  [Read-Write] Random Seed used to initialize sampling strategies

<a id="unreal.GeometryScriptMeshPointSamplingOptions.random_seed"></a>

#### random_seed

```python
@random_seed.setter
def random_seed(value: int) -> None
```

<a id="unreal.GeometryScriptMeshPointSamplingOptions.sub_sample_density"></a>

#### sub_sample_density

```python
@property
def sub_sample_density() -> float
```

(double):  [Read-Write] Density of subsampling used in Poisson strategy. Larger numbers mean "more accurate" (but slower) results.

<a id="unreal.GeometryScriptMeshPointSamplingOptions.sub_sample_density"></a>

#### sub_sample_density

```python
@sub_sample_density.setter
def sub_sample_density(value: float) -> None
```

<a id="unreal.GeometryScriptNonUniformPointSamplingOptions"></a>