## UsdStageOptions Objects

```python
class UsdStageOptions(StructBase)
```

Usd Stage Options

**C++ Source:**

- **Plugin**: USDCore
- **Module**: USDClasses
- **File**: USDStageOptions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``meters_per_unit`` (float):  [Read-Write] MetersPerUnit to use for the stage. Defaults to 0.01 (i.e. 1cm per unit, which equals UE units)
- ``up_axis`` (UsdUpAxis):  [Read-Write] UpAxis to use for the stage. Defaults to ZAxis, which equals the UE convention

<a id="unreal.UsdStageOptions.__init__"></a>

#### __init__

```python
def __init__(meters_per_unit: float = 0.000000,
             up_axis: UsdUpAxis = UsdUpAxis.Y_AXIS) -> None
```

<a id="unreal.UsdStageOptions.meters_per_unit"></a>

#### meters_per_unit

```python
@property
def meters_per_unit() -> float
```

(float):  [Read-Write] MetersPerUnit to use for the stage. Defaults to 0.01 (i.e. 1cm per unit, which equals UE units)

<a id="unreal.UsdStageOptions.meters_per_unit"></a>

#### meters_per_unit

```python
@meters_per_unit.setter
def meters_per_unit(value: float) -> None
```

<a id="unreal.UsdStageOptions.up_axis"></a>

#### up_axis

```python
@property
def up_axis() -> UsdUpAxis
```

(UsdUpAxis):  [Read-Write] UpAxis to use for the stage. Defaults to ZAxis, which equals the UE convention

<a id="unreal.UsdStageOptions.up_axis"></a>

#### up_axis

```python
@up_axis.setter
def up_axis(value: UsdUpAxis) -> None
```

<a id="unreal.UsdUnrealAssetInfo"></a>