## PlayheadOverlayStyle Objects

```python
class PlayheadOverlayStyle(SlateWidgetStyle)
```

Represents the appearance of a Waveform Viewer Overlay style

**C++ Source:**

- **Plugin**: AudioWidgets
- **Module**: AudioWidgets
- **File**: AudioWidgetsSlateTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``desired_height`` (float):  [Read-Write]
- ``desired_width`` (float):  [Read-Write]
- ``playhead_color`` (SlateColor):  [Read-Write]
- ``playhead_width`` (float):  [Read-Write]

<a id="unreal.PlayheadOverlayStyle.__init__"></a>

#### __init__

```python
def __init__(playhead_color: SlateColor = [[
    1.000000, 0.000000, 1.000000, 1.000000
], SlateColorStylingMode.USE_COLOR_SPECIFIED],
             playhead_width: float = 0.000000,
             desired_width: float = 0.000000,
             desired_height: float = 0.000000) -> None
```

<a id="unreal.PlayheadOverlayStyle.playhead_color"></a>

#### playhead_color

```python
@property
def playhead_color() -> SlateColor
```

(SlateColor):  [Read-Write]

<a id="unreal.PlayheadOverlayStyle.playhead_color"></a>

#### playhead_color

```python
@playhead_color.setter
def playhead_color(value: SlateColor) -> None
```

<a id="unreal.PlayheadOverlayStyle.playhead_width"></a>

#### playhead_width

```python
@property
def playhead_width() -> float
```

(float):  [Read-Write]

<a id="unreal.PlayheadOverlayStyle.playhead_width"></a>

#### playhead_width

```python
@playhead_width.setter
def playhead_width(value: float) -> None
```

<a id="unreal.PlayheadOverlayStyle.desired_width"></a>

#### desired_width

```python
@property
def desired_width() -> float
```

(float):  [Read-Write]

<a id="unreal.PlayheadOverlayStyle.desired_width"></a>

#### desired_width

```python
@desired_width.setter
def desired_width(value: float) -> None
```

<a id="unreal.PlayheadOverlayStyle.desired_height"></a>

#### desired_height

```python
@property
def desired_height() -> float
```

(float):  [Read-Write]

<a id="unreal.PlayheadOverlayStyle.desired_height"></a>

#### desired_height

```python
@desired_height.setter
def desired_height(value: float) -> None
```

<a id="unreal.ResonanceAudioReverbPluginSettings"></a>