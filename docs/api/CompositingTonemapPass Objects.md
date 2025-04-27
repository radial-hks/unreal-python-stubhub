## CompositingTonemapPass Objects

```python
class CompositingTonemapPass(CompositingElementTransform)
```

Compositing Tonemap Pass

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: CompositingElementTransforms.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``chromatic_aberration`` (float):  [Read-Write] in percent, Scene chromatic aberration / color fringe (camera imperfection) to simulate an artifact that happens in real-world lens, mostly visible in the image corners.
- ``color_grading_settings`` (ColorGradingSettings):  [Read-Write] Color grading settings.
- ``enabled`` (bool):  [Read-Write]
- ``film_stock_settings`` (FilmStockSettings):  [Read-Write] Film stock settings.
- ``intermediate`` (bool):  [Read-Write] Marks this pass for 'internal use only' - prevents it from being exposed to parent elements.
  When set, render target resources used by this element will be reused. For transforms, all 'Intermediate'
  passes are available to the next transform pass, and released after that.
- ``pass_name`` (Name):  [Read-Write]

<a id="unreal.CompositingTonemapPass.color_grading_settings"></a>

#### color_grading_settings

```python
@property
def color_grading_settings() -> ColorGradingSettings
```

(ColorGradingSettings):  [Read-Write] Color grading settings.

<a id="unreal.CompositingTonemapPass.color_grading_settings"></a>

#### color_grading_settings

```python
@color_grading_settings.setter
def color_grading_settings(value: ColorGradingSettings) -> None
```

<a id="unreal.CompositingTonemapPass.film_stock_settings"></a>

#### film_stock_settings

```python
@property
def film_stock_settings() -> FilmStockSettings
```

(FilmStockSettings):  [Read-Write] Film stock settings.

<a id="unreal.CompositingTonemapPass.film_stock_settings"></a>

#### film_stock_settings

```python
@film_stock_settings.setter
def film_stock_settings(value: FilmStockSettings) -> None
```

<a id="unreal.CompositingTonemapPass.chromatic_aberration"></a>

#### chromatic_aberration

```python
@property
def chromatic_aberration() -> float
```

(float):  [Read-Write] in percent, Scene chromatic aberration / color fringe (camera imperfection) to simulate an artifact that happens in real-world lens, mostly visible in the image corners.

<a id="unreal.CompositingTonemapPass.chromatic_aberration"></a>

#### chromatic_aberration

```python
@chromatic_aberration.setter
def chromatic_aberration(value: float) -> None
```

<a id="unreal.MultiPassChromaKeyer"></a>