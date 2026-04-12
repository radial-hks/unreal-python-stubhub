## InputModifierFOVScaling Objects

```python
class InputModifierFOVScaling(InputModifier)
```

FOV Scaling
Apply FOV dependent scaling to input values, per axis

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: InputModifiers.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``fov_scale`` (float):  [Read-Write] Extra scalar applied on top of basic FOV scaling.
- ``fov_scaling_type`` (FOVScalingType):  [Read-Write]

<a id="unreal.InputModifierFOVScaling.fov_scale"></a>

#### fov\_scale

```python
@property
def fov_scale() -> float
```

(float):  [Read-Write] Extra scalar applied on top of basic FOV scaling.

<a id="unreal.InputModifierFOVScaling.fov_scale"></a>

#### fov\_scale

```python
@fov_scale.setter
def fov_scale(value: float) -> None
```

<a id="unreal.InputModifierFOVScaling.fov_scaling_type"></a>

#### fov\_scaling\_type

```python
@property
def fov_scaling_type() -> FOVScalingType
```

(FOVScalingType):  [Read-Write]

<a id="unreal.InputModifierFOVScaling.fov_scaling_type"></a>

#### fov\_scaling\_type

```python
@fov_scaling_type.setter
def fov_scaling_type(value: FOVScalingType) -> None
```

<a id="unreal.InputModifierToWorldSpace"></a>