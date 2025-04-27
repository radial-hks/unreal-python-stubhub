## ColorGradingSettings Objects

```python
class ColorGradingSettings(StructBase)
```

Color Grading Settings

**C++ Source:**

- **Module**: Engine
- **File**: Scene.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``global_`` (ColorGradePerRangeSettings):  [Read-Write]
- ``highlights`` (ColorGradePerRangeSettings):  [Read-Write]
- ``highlights_max`` (float):  [Read-Write]
- ``highlights_min`` (float):  [Read-Write]
- ``midtones`` (ColorGradePerRangeSettings):  [Read-Write]
- ``shadows`` (ColorGradePerRangeSettings):  [Read-Write]
- ``shadows_max`` (float):  [Read-Write]

<a id="unreal.ColorGradingSettings.__init__"></a>

#### __init__

```python
def __init__(global_: ColorGradePerRangeSettings = [
    [1.000000, 1.000000, 1.000000, 1.000000],
    [1.000000, 1.000000, 1.000000, 1.000000],
    [1.000000, 1.000000, 1.000000, 1.000000],
    [1.000000, 1.000000, 1.000000, 1.000000],
    [0.000000, 0.000000, 0.000000, 0.000000]
],
             shadows: ColorGradePerRangeSettings = [
                 [1.000000, 1.000000, 1.000000, 1.000000],
                 [1.000000, 1.000000, 1.000000, 1.000000],
                 [1.000000, 1.000000, 1.000000, 1.000000],
                 [1.000000, 1.000000, 1.000000, 1.000000],
                 [0.000000, 0.000000, 0.000000, 0.000000]
             ],
             midtones: ColorGradePerRangeSettings = [
                 [1.000000, 1.000000, 1.000000, 1.000000],
                 [1.000000, 1.000000, 1.000000, 1.000000],
                 [1.000000, 1.000000, 1.000000, 1.000000],
                 [1.000000, 1.000000, 1.000000, 1.000000],
                 [0.000000, 0.000000, 0.000000, 0.000000]
             ],
             highlights: ColorGradePerRangeSettings = [
                 [1.000000, 1.000000, 1.000000, 1.000000],
                 [1.000000, 1.000000, 1.000000, 1.000000],
                 [1.000000, 1.000000, 1.000000, 1.000000],
                 [1.000000, 1.000000, 1.000000, 1.000000],
                 [0.000000, 0.000000, 0.000000, 0.000000]
             ],
             shadows_max: float = 0.000000,
             highlights_min: float = 0.000000,
             highlights_max: float = 0.000000) -> None
```

<a id="unreal.ColorGradingSettings.global_"></a>

#### global_

```python
@property
def global_() -> ColorGradePerRangeSettings
```

(ColorGradePerRangeSettings):  [Read-Write]

<a id="unreal.ColorGradingSettings.global_"></a>

#### global_

```python
@global_.setter
def global_(value: ColorGradePerRangeSettings) -> None
```

<a id="unreal.ColorGradingSettings.shadows"></a>

#### shadows

```python
@property
def shadows() -> ColorGradePerRangeSettings
```

(ColorGradePerRangeSettings):  [Read-Write]

<a id="unreal.ColorGradingSettings.shadows"></a>

#### shadows

```python
@shadows.setter
def shadows(value: ColorGradePerRangeSettings) -> None
```

<a id="unreal.ColorGradingSettings.midtones"></a>

#### midtones

```python
@property
def midtones() -> ColorGradePerRangeSettings
```

(ColorGradePerRangeSettings):  [Read-Write]

<a id="unreal.ColorGradingSettings.midtones"></a>

#### midtones

```python
@midtones.setter
def midtones(value: ColorGradePerRangeSettings) -> None
```

<a id="unreal.ColorGradingSettings.highlights"></a>

#### highlights

```python
@property
def highlights() -> ColorGradePerRangeSettings
```

(ColorGradePerRangeSettings):  [Read-Write]

<a id="unreal.ColorGradingSettings.highlights"></a>

#### highlights

```python
@highlights.setter
def highlights(value: ColorGradePerRangeSettings) -> None
```

<a id="unreal.ColorGradingSettings.shadows_max"></a>

#### shadows_max

```python
@property
def shadows_max() -> float
```

(float):  [Read-Write]

<a id="unreal.ColorGradingSettings.shadows_max"></a>

#### shadows_max

```python
@shadows_max.setter
def shadows_max(value: float) -> None
```

<a id="unreal.ColorGradingSettings.highlights_min"></a>

#### highlights_min

```python
@property
def highlights_min() -> float
```

(float):  [Read-Write]

<a id="unreal.ColorGradingSettings.highlights_min"></a>

#### highlights_min

```python
@highlights_min.setter
def highlights_min(value: float) -> None
```

<a id="unreal.ColorGradingSettings.highlights_max"></a>

#### highlights_max

```python
@property
def highlights_max() -> float
```

(float):  [Read-Write]

<a id="unreal.ColorGradingSettings.highlights_max"></a>

#### highlights_max

```python
@highlights_max.setter
def highlights_max(value: float) -> None
```

<a id="unreal.FilmStockSettings"></a>