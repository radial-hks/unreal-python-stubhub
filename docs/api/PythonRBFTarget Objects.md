## PythonRBFTarget Objects

```python
class PythonRBFTarget(Object)
```

Python RBFTarget

**C++ Source:**

- **Plugin**: TAPython
- **Module**: TAPython
- **File**: PythonRBFLib.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_custom_curve`` (bool):  [Read-Write] Whether we want to apply an additional custom curve when activating this target.
                Ignored if the solver type is Interpolative.
- ``custom_curve`` (RichCurve):  [Read-Write] Custom curve to apply to activation of this target, if bApplyCustomCurve is true.
        Ignored if the solver type is Interpolative.
- ``distance_method`` (RBFDistanceMethod):  [Read-Write] Override the distance method used to calculate the distance from this target to
                the input. Ignored if the solver type is Interpolative.
- ``function_type`` (RBFFunctionType):  [Read-Write] Override the falloff function used to smooth the distance from this target to
                the input. Ignored if the solver type is Interpolative.
- ``scale_factor`` (float):  [Read-Write] How large the influence of this target.

<a id="unreal.PythonRBFTarget.set_values"></a>

#### set\_values

```python
def set_values(values: Array[float]) -> None
```

x.set_values(values) -> None
Set Values

Args:
    values (Array[float]):

<a id="unreal.PythonRBFTarget.get_values"></a>

#### get\_values

```python
def get_values() -> Array[float]
```

x.get_values() -> Array[float]
Get Values

Returns:
    Array[float]:

<a id="unreal.PythonRBFTarget.get_dimensions"></a>

#### get\_dimensions

```python
def get_dimensions() -> int
```

x.get_dimensions() -> int32
Get Dimensions

Returns:
    int32:

<a id="unreal.PythonRBFTarget.as_vector"></a>

#### as\_vector

```python
def as_vector(index: int) -> Vector
```

x.as_vector(index) -> Vector
As Vector

Args:
    index (int32): 

Returns:
    Vector:

<a id="unreal.PythonRBFTarget.as_rotator"></a>

#### as\_rotator

```python
def as_rotator(index: int) -> Rotator
```

x.as_rotator(index) -> Rotator
As Rotator

Args:
    index (int32): 

Returns:
    Rotator:

<a id="unreal.PythonRBFTarget.as_quat"></a>

#### as\_quat

```python
def as_quat(index: int) -> Quat
```

x.as_quat(index) -> Quat
As Quat

Args:
    index (int32): 

Returns:
    Quat:

<a id="unreal.PythonRBFTarget.add_from_vector"></a>

#### add\_from\_vector

```python
def add_from_vector(vector: Vector) -> None
```

x.add_from_vector(vector) -> None
Add from Vector

Args:
    vector (Vector):

<a id="unreal.PythonRBFTarget.add_from_rotator"></a>

#### add\_from\_rotator

```python
def add_from_rotator(rot: Rotator) -> None
```

x.add_from_rotator(rot) -> None
Add from Rotator

Args:
    rot (Rotator):

<a id="unreal.PythonRBFFunction"></a>