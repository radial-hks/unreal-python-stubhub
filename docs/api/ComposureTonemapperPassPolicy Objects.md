## ComposureTonemapperPassPolicy Objects

```python
class ComposureTonemapperPassPolicy(ComposurePostProcessPassPolicy)
```

Tonemapper only rules used for configuring how UComposurePostProcessingPassProxy executes

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: ComposureTonemapperPass.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``chromatic_aberration`` (float):  [Read-Write] in percent, Scene chromatic aberration / color fringe (camera imperfection) to simulate an artifact that happens in real-world lens, mostly visible in the image corners.
- ``color_grading_settings`` (ColorGradingSettings):  [Read-Write] Color grading settings.
- ``film_stock_settings`` (FilmStockSettings):  [Read-Write] Film stock settings.

<a id="unreal.ComposureTonemapperPassPolicy.color_grading_settings"></a>

#### color_grading_settings

```python
@property
def color_grading_settings() -> ColorGradingSettings
```

(ColorGradingSettings):  [Read-Write] Color grading settings.

<a id="unreal.ComposureTonemapperPassPolicy.color_grading_settings"></a>

#### color_grading_settings

```python
@color_grading_settings.setter
def color_grading_settings(value: ColorGradingSettings) -> None
```

<a id="unreal.ComposureTonemapperPassPolicy.film_stock_settings"></a>

#### film_stock_settings

```python
@property
def film_stock_settings() -> FilmStockSettings
```

(FilmStockSettings):  [Read-Write] Film stock settings.

<a id="unreal.ComposureTonemapperPassPolicy.film_stock_settings"></a>

#### film_stock_settings

```python
@film_stock_settings.setter
def film_stock_settings(value: FilmStockSettings) -> None
```

<a id="unreal.ComposureTonemapperPassPolicy.chromatic_aberration"></a>

#### chromatic_aberration

```python
@property
def chromatic_aberration() -> float
```

(float):  [Read-Write] in percent, Scene chromatic aberration / color fringe (camera imperfection) to simulate an artifact that happens in real-world lens, mostly visible in the image corners.

<a id="unreal.ComposureTonemapperPassPolicy.chromatic_aberration"></a>

#### chromatic_aberration

```python
@chromatic_aberration.setter
def chromatic_aberration(value: float) -> None
```

<a id="unreal.CompositingTextureLookupTable"></a>