## InputModifierDeadZone Objects

```python
class InputModifierDeadZone(InputModifier)
```

Dead Zone
Input values within the range LowerThreshold -> UpperThreshold will be remapped from 0 -> 1.
Values outside this range will be clamped.

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: InputModifiers.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``lower_threshold`` (float):  [Read-Write] Threshold below which input is ignored
  This value should always be lower then the UpperThreshold.
- ``type`` (DeadZoneType):  [Read-Write]
- ``upper_threshold`` (float):  [Read-Write] Threshold above which input is clamped to 1

<a id="unreal.InputModifierDeadZone.lower_threshold"></a>

#### lower_threshold

```python
@property
def lower_threshold() -> float
```

(float):  [Read-Write] Threshold below which input is ignored
This value should always be lower then the UpperThreshold.

<a id="unreal.InputModifierDeadZone.lower_threshold"></a>

#### lower_threshold

```python
@lower_threshold.setter
def lower_threshold(value: float) -> None
```

<a id="unreal.InputModifierDeadZone.upper_threshold"></a>

#### upper_threshold

```python
@property
def upper_threshold() -> float
```

(float):  [Read-Write] Threshold above which input is clamped to 1

<a id="unreal.InputModifierDeadZone.upper_threshold"></a>

#### upper_threshold

```python
@upper_threshold.setter
def upper_threshold(value: float) -> None
```

<a id="unreal.InputModifierDeadZone.type"></a>

#### type

```python
@property
def type() -> DeadZoneType
```

(DeadZoneType):  [Read-Write]

<a id="unreal.InputModifierDeadZone.type"></a>

#### type

```python
@type.setter
def type(value: DeadZoneType) -> None
```

<a id="unreal.InputModifierScalar"></a>