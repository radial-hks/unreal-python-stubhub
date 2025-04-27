## GeometryScriptNonUniformPointSamplingOptions Objects

```python
class GeometryScriptNonUniformPointSamplingOptions(StructBase)
```

Geometry Script Non Uniform Point Sampling Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshSamplingFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``invert_weights`` (bool):  [Read-Write] If true, weight values are inverted
- ``max_sampling_radius`` (float):  [Read-Write] If MaxSampleRadius > SampleRadius, then output sample radius will be in range [SampleRadius, MaxSampleRadius]
- ``size_distribution`` (GeometryScriptSamplingDistributionMode):  [Read-Write] SizeDistribution setting controls the distribution of sample radii
- ``size_distribution_power`` (double):  [Read-Write] SizeDistributionPower is used to control how extreme the Size Distribution shift is. Valid range is [1,10]
- ``weight_mode`` (GeometryScriptSamplingWeightMode):  [Read-Write] WeightMode controls how any active Weight scheme is used to affect sample radius

<a id="unreal.GeometryScriptNonUniformPointSamplingOptions.__init__"></a>

#### __init__

```python
def __init__(
        max_sampling_radius: float = 0.000000,
        size_distribution:
    GeometryScriptSamplingDistributionMode = GeometryScriptSamplingDistributionMode
    .UNIFORM,
        size_distribution_power: float = 0.000000,
        weight_mode:
    GeometryScriptSamplingWeightMode = GeometryScriptSamplingWeightMode.
    WEIGHT_TO_RADIUS,
        invert_weights: bool = False) -> None
```

<a id="unreal.GeometryScriptNonUniformPointSamplingOptions.max_sampling_radius"></a>

#### max_sampling_radius

```python
@property
def max_sampling_radius() -> float
```

(float):  [Read-Write] If MaxSampleRadius > SampleRadius, then output sample radius will be in range [SampleRadius, MaxSampleRadius]

<a id="unreal.GeometryScriptNonUniformPointSamplingOptions.max_sampling_radius"></a>

#### max_sampling_radius

```python
@max_sampling_radius.setter
def max_sampling_radius(value: float) -> None
```

<a id="unreal.GeometryScriptNonUniformPointSamplingOptions.size_distribution"></a>

#### size_distribution

```python
@property
def size_distribution() -> GeometryScriptSamplingDistributionMode
```

(GeometryScriptSamplingDistributionMode):  [Read-Write] SizeDistribution setting controls the distribution of sample radii

<a id="unreal.GeometryScriptNonUniformPointSamplingOptions.size_distribution"></a>

#### size_distribution

```python
@size_distribution.setter
def size_distribution(value: GeometryScriptSamplingDistributionMode) -> None
```

<a id="unreal.GeometryScriptNonUniformPointSamplingOptions.size_distribution_power"></a>

#### size_distribution_power

```python
@property
def size_distribution_power() -> float
```

(double):  [Read-Write] SizeDistributionPower is used to control how extreme the Size Distribution shift is. Valid range is [1,10]

<a id="unreal.GeometryScriptNonUniformPointSamplingOptions.size_distribution_power"></a>

#### size_distribution_power

```python
@size_distribution_power.setter
def size_distribution_power(value: float) -> None
```

<a id="unreal.GeometryScriptNonUniformPointSamplingOptions.weight_mode"></a>

#### weight_mode

```python
@property
def weight_mode() -> GeometryScriptSamplingWeightMode
```

(GeometryScriptSamplingWeightMode):  [Read-Write] WeightMode controls how any active Weight scheme is used to affect sample radius

<a id="unreal.GeometryScriptNonUniformPointSamplingOptions.weight_mode"></a>

#### weight_mode

```python
@weight_mode.setter
def weight_mode(value: GeometryScriptSamplingWeightMode) -> None
```

<a id="unreal.GeometryScriptNonUniformPointSamplingOptions.invert_weights"></a>

#### invert_weights

```python
@property
def invert_weights() -> bool
```

(bool):  [Read-Write] If true, weight values are inverted

<a id="unreal.GeometryScriptNonUniformPointSamplingOptions.invert_weights"></a>

#### invert_weights

```python
@invert_weights.setter
def invert_weights(value: bool) -> None
```

<a id="unreal.GeometryScriptPlanarSimplifyOptions"></a>