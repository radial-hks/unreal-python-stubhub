## ScalableFloat Objects

```python
class ScalableFloat(StructBase)
```

Generic numerical value in the form Value * Curve[Level]

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: ScalableFloat.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``curve`` (CurveTableRowHandle):  [Read-Write] Curve that is evaluated at a specific level. If found, it is multipled by Value
- ``registry_type`` (DataRegistryType):  [Read-Write] Name of Data Registry containing curve to use. If set the RowName inside Curve is used as the item name
- ``value`` (float):  [Read-Write] Raw value, is multiplied by curve

<a id="unreal.ScalableFloat.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: float = 0.000000,
             curve: CurveTableRowHandle = [None, "None"],
             registry_type: DataRegistryType = ["None"]) -> None
```

<a id="unreal.ScalableFloat.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Write] Raw value, is multiplied by curve

<a id="unreal.ScalableFloat.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.ScalableFloat.curve"></a>

#### curve

```python
@property
def curve() -> CurveTableRowHandle
```

(CurveTableRowHandle):  [Read-Write] Curve that is evaluated at a specific level. If found, it is multipled by Value

<a id="unreal.ScalableFloat.curve"></a>

#### curve

```python
@curve.setter
def curve(value: CurveTableRowHandle) -> None
```

<a id="unreal.ScalableFloat.registry_type"></a>

#### registry\_type

```python
@property
def registry_type() -> DataRegistryType
```

(DataRegistryType):  [Read-Write] Name of Data Registry containing curve to use. If set the RowName inside Curve is used as the item name

<a id="unreal.ScalableFloat.registry_type"></a>

#### registry\_type

```python
@registry_type.setter
def registry_type(value: DataRegistryType) -> None
```

<a id="unreal.GameplayEffectAttributeCaptureDefinition"></a>