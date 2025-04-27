## AudioMaterialEnvelopeStyle Objects

```python
class AudioMaterialEnvelopeStyle(AudioMaterialWidgetStyle)
```

Represents the appearance of an Audio Material Envelope

**C++ Source:**

- **Plugin**: AudioWidgets
- **Module**: AudioWidgets
- **File**: AudioMaterialSlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``background_color`` (LinearColor):  [Read-Write]
- ``curve_color`` (LinearColor):  [Read-Write]
- ``desired_size`` (Vector2f):  [Read-Write] Desired Draw size of the rendered material
- ``material`` (MaterialInterface):  [Read-Write] Material used to render the Slate
- ``outline_color`` (LinearColor):  [Read-Write]

<a id="unreal.AudioMaterialEnvelopeStyle.__init__"></a>

#### __init__

```python
def __init__(
    material: MaterialInterface = None,
    desired_size: Vector2f = [0.000000, 0.000000],
    curve_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
    background_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
    outline_color: LinearColor = [0.000000, 0.000000, 0.000000,
                                  0.000000]) -> None
```

<a id="unreal.AudioMaterialEnvelopeStyle.curve_color"></a>

#### curve_color

```python
@property
def curve_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.AudioMaterialEnvelopeStyle.curve_color"></a>

#### curve_color

```python
@curve_color.setter
def curve_color(value: LinearColor) -> None
```

<a id="unreal.AudioMaterialEnvelopeStyle.background_color"></a>

#### background_color

```python
@property
def background_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.AudioMaterialEnvelopeStyle.background_color"></a>

#### background_color

```python
@background_color.setter
def background_color(value: LinearColor) -> None
```

<a id="unreal.AudioMaterialEnvelopeStyle.outline_color"></a>

#### outline_color

```python
@property
def outline_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.AudioMaterialEnvelopeStyle.outline_color"></a>

#### outline_color

```python
@outline_color.setter
def outline_color(value: LinearColor) -> None
```

<a id="unreal.AudioMeterDefaultColorStyle"></a>