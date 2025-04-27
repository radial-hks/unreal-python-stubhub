## GeometryScriptSplineSamplingOptions Objects

```python
class GeometryScriptSplineSamplingOptions(StructBase)
```

Geometry Script Spline Sampling Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: PolyPathFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coordinate_space`` (SplineCoordinateSpace):  [Read-Write]
- ``error_tolerance`` (float):  [Read-Write]
- ``num_samples`` (int32):  [Read-Write]
- ``range_end`` (float):  [Read-Write] If not evaluating the full spline, where to stop sampling. Expressed in units based on the EvaluateRange value.
- ``range_method`` (GeometryScriptEvaluateSplineRange):  [Read-Write] How the RangeStart and RangeEnd parameters will be interpreted
- ``range_start`` (float):  [Read-Write] If not evaluating the full spline, where to start sampling. Expressed in units based on the EvaluateRange value.
- ``sample_spacing`` (GeometryScriptSampleSpacing):  [Read-Write]

<a id="unreal.GeometryScriptSplineSamplingOptions.__init__"></a>

#### __init__

```python
def __init__(
        num_samples: int = 0,
        error_tolerance: float = 0.000000,
        sample_spacing:
    GeometryScriptSampleSpacing = GeometryScriptSampleSpacing.UNIFORM_DISTANCE,
        coordinate_space: SplineCoordinateSpace = SplineCoordinateSpace.LOCAL,
        range_method:
    GeometryScriptEvaluateSplineRange = GeometryScriptEvaluateSplineRange.
    FULL_SPLINE,
        range_start: float = 0.000000,
        range_end: float = 0.000000) -> None
```

<a id="unreal.GeometryScriptSplineSamplingOptions.num_samples"></a>

#### num_samples

```python
@property
def num_samples() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeometryScriptSplineSamplingOptions.num_samples"></a>

#### num_samples

```python
@num_samples.setter
def num_samples(value: int) -> None
```

<a id="unreal.GeometryScriptSplineSamplingOptions.error_tolerance"></a>

#### error_tolerance

```python
@property
def error_tolerance() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptSplineSamplingOptions.error_tolerance"></a>

#### error_tolerance

```python
@error_tolerance.setter
def error_tolerance(value: float) -> None
```

<a id="unreal.GeometryScriptSplineSamplingOptions.sample_spacing"></a>

#### sample_spacing

```python
@property
def sample_spacing() -> GeometryScriptSampleSpacing
```

(GeometryScriptSampleSpacing):  [Read-Write]

<a id="unreal.GeometryScriptSplineSamplingOptions.sample_spacing"></a>

#### sample_spacing

```python
@sample_spacing.setter
def sample_spacing(value: GeometryScriptSampleSpacing) -> None
```

<a id="unreal.GeometryScriptSplineSamplingOptions.coordinate_space"></a>

#### coordinate_space

```python
@property
def coordinate_space() -> SplineCoordinateSpace
```

(SplineCoordinateSpace):  [Read-Write]

<a id="unreal.GeometryScriptSplineSamplingOptions.coordinate_space"></a>

#### coordinate_space

```python
@coordinate_space.setter
def coordinate_space(value: SplineCoordinateSpace) -> None
```

<a id="unreal.GeometryScriptSplineSamplingOptions.range_method"></a>

#### range_method

```python
@property
def range_method() -> GeometryScriptEvaluateSplineRange
```

(GeometryScriptEvaluateSplineRange):  [Read-Write] How the RangeStart and RangeEnd parameters will be interpreted

<a id="unreal.GeometryScriptSplineSamplingOptions.range_method"></a>

#### range_method

```python
@range_method.setter
def range_method(value: GeometryScriptEvaluateSplineRange) -> None
```

<a id="unreal.GeometryScriptSplineSamplingOptions.range_start"></a>

#### range_start

```python
@property
def range_start() -> float
```

(float):  [Read-Write] If not evaluating the full spline, where to start sampling. Expressed in units based on the EvaluateRange value.

<a id="unreal.GeometryScriptSplineSamplingOptions.range_start"></a>

#### range_start

```python
@range_start.setter
def range_start(value: float) -> None
```

<a id="unreal.GeometryScriptSplineSamplingOptions.range_end"></a>

#### range_end

```python
@property
def range_end() -> float
```

(float):  [Read-Write] If not evaluating the full spline, where to stop sampling. Expressed in units based on the EvaluateRange value.

<a id="unreal.GeometryScriptSplineSamplingOptions.range_end"></a>

#### range_end

```python
@range_end.setter
def range_end(value: float) -> None
```

<a id="unreal.GeometryScriptCopyMeshFromComponentOptions"></a>