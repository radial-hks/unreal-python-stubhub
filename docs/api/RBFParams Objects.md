## RBFParams Objects

```python
class RBFParams(StructBase)
```

Parameters used by RBF solver

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: RBFSolver.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``automatic_radius`` (bool):  [Read-Write] Automatically pick the radius based on the average distance between targets
- ``distance_method`` (RBFDistanceMethod):  [Read-Write]
- ``function`` (RBFFunctionType):  [Read-Write]
- ``median_max`` (float):  [Read-Write] Maximum distance used for median
- ``median_min`` (float):  [Read-Write] Minimum distance used for median
- ``median_reference`` (Vector):  [Read-Write] Rotation or position of median (used for normalization)
- ``normalize_method`` (RBFNormalizeMethod):  [Read-Write] Method to use for normalizing the weight
- ``radius`` (float):  [Read-Write] Default radius for each target.
- ``solver_type`` (RBFSolverType):  [Read-Write] Specifies the type of solver to use. The additive solver requires normalization, for the
                most part, whereas the Interpolative solver is not as reliant on it. The interpolative
                solver also has smoother blending, whereas the additive solver requires more targets but
                has a more precise control over the influence of each target.
- ``twist_axis`` (BoneAxis):  [Read-Write] Axis to use when DistanceMethod is SwingAngle
- ``weight_threshold`` (float):  [Read-Write] Weight below which we shouldn't bother returning a contribution from a target

<a id="unreal.RBFParams.__init__"></a>

#### __init__

```python
def __init__(solver_type: RBFSolverType = RBFSolverType.ADDITIVE,
             radius: float = 0.000000,
             automatic_radius: bool = False,
             function: RBFFunctionType = RBFFunctionType.GAUSSIAN,
             distance_method: RBFDistanceMethod = RBFDistanceMethod.EUCLIDEAN,
             twist_axis: BoneAxis = BoneAxis.BA_X,
             weight_threshold: float = 0.000000,
             normalize_method: RBFNormalizeMethod = RBFNormalizeMethod.
             ONLY_NORMALIZE_ABOVE_ONE,
             median_reference: Vector = [0.000000, 0.000000, 0.000000],
             median_min: float = 0.000000,
             median_max: float = 0.000000) -> None
```

<a id="unreal.RBFParams.solver_type"></a>

#### solver_type

```python
@property
def solver_type() -> RBFSolverType
```

(RBFSolverType):  [Read-Write] Specifies the type of solver to use. The additive solver requires normalization, for the
              most part, whereas the Interpolative solver is not as reliant on it. The interpolative
              solver also has smoother blending, whereas the additive solver requires more targets but
              has a more precise control over the influence of each target.

<a id="unreal.RBFParams.solver_type"></a>

#### solver_type

```python
@solver_type.setter
def solver_type(value: RBFSolverType) -> None
```

<a id="unreal.RBFParams.radius"></a>

#### radius

```python
@property
def radius() -> float
```

(float):  [Read-Write] Default radius for each target.

<a id="unreal.RBFParams.radius"></a>

#### radius

```python
@radius.setter
def radius(value: float) -> None
```

<a id="unreal.RBFParams.automatic_radius"></a>

#### automatic_radius

```python
@property
def automatic_radius() -> bool
```

(bool):  [Read-Write] Automatically pick the radius based on the average distance between targets

<a id="unreal.RBFParams.automatic_radius"></a>

#### automatic_radius

```python
@automatic_radius.setter
def automatic_radius(value: bool) -> None
```

<a id="unreal.RBFParams.function"></a>

#### function

```python
@property
def function() -> RBFFunctionType
```

(RBFFunctionType):  [Read-Write]

<a id="unreal.RBFParams.function"></a>

#### function

```python
@function.setter
def function(value: RBFFunctionType) -> None
```

<a id="unreal.RBFParams.distance_method"></a>

#### distance_method

```python
@property
def distance_method() -> RBFDistanceMethod
```

(RBFDistanceMethod):  [Read-Write]

<a id="unreal.RBFParams.distance_method"></a>

#### distance_method

```python
@distance_method.setter
def distance_method(value: RBFDistanceMethod) -> None
```

<a id="unreal.RBFParams.twist_axis"></a>

#### twist_axis

```python
@property
def twist_axis() -> BoneAxis
```

(BoneAxis):  [Read-Write] Axis to use when DistanceMethod is SwingAngle

<a id="unreal.RBFParams.twist_axis"></a>

#### twist_axis

```python
@twist_axis.setter
def twist_axis(value: BoneAxis) -> None
```

<a id="unreal.RBFParams.weight_threshold"></a>

#### weight_threshold

```python
@property
def weight_threshold() -> float
```

(float):  [Read-Write] Weight below which we shouldn't bother returning a contribution from a target

<a id="unreal.RBFParams.weight_threshold"></a>

#### weight_threshold

```python
@weight_threshold.setter
def weight_threshold(value: float) -> None
```

<a id="unreal.RBFParams.normalize_method"></a>

#### normalize_method

```python
@property
def normalize_method() -> RBFNormalizeMethod
```

(RBFNormalizeMethod):  [Read-Write] Method to use for normalizing the weight

<a id="unreal.RBFParams.normalize_method"></a>

#### normalize_method

```python
@normalize_method.setter
def normalize_method(value: RBFNormalizeMethod) -> None
```

<a id="unreal.RBFParams.median_reference"></a>

#### median_reference

```python
@property
def median_reference() -> Vector
```

(Vector):  [Read-Write] Rotation or position of median (used for normalization)

<a id="unreal.RBFParams.median_reference"></a>

#### median_reference

```python
@median_reference.setter
def median_reference(value: Vector) -> None
```

<a id="unreal.RBFParams.median_min"></a>

#### median_min

```python
@property
def median_min() -> float
```

(float):  [Read-Write] Minimum distance used for median

<a id="unreal.RBFParams.median_min"></a>

#### median_min

```python
@median_min.setter
def median_min(value: float) -> None
```

<a id="unreal.RBFParams.median_max"></a>

#### median_max

```python
@property
def median_max() -> float
```

(float):  [Read-Write] Maximum distance used for median

<a id="unreal.RBFParams.median_max"></a>

#### median_max

```python
@median_max.setter
def median_max(value: float) -> None
```

<a id="unreal.AnimNode_PoseSnapshot"></a>