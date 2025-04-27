## OverlayItem Objects

```python
class OverlayItem(StructBase)
```

Overlay Item

**C++ Source:**

- **Module**: Overlay
- **File**: Overlays.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``end_time`` (Timespan):  [Read-Write] When the overlay should be cleared
- ``position`` (Vector2D):  [Read-Write] The position of the text on screen (Between 0.0 and 1.0)
- ``start_time`` (Timespan):  [Read-Write] When the overlay should be displayed
- ``text`` (str):  [Read-Write] Text that appears onscreen when the overlay is shown

<a id="unreal.OverlayItem.__init__"></a>

#### __init__

```python
def __init__(start_time: Timespan = [0, 0, 0, 0, 0],
             end_time: Timespan = [0, 0, 0, 0, 0],
             text: str = "",
             position: Vector2D = [0.000000, 0.000000]) -> None
```

<a id="unreal.OverlayItem.start_time"></a>

#### start_time

```python
@property
def start_time() -> Timespan
```

(Timespan):  [Read-Write] When the overlay should be displayed

<a id="unreal.OverlayItem.start_time"></a>

#### start_time

```python
@start_time.setter
def start_time(value: Timespan) -> None
```

<a id="unreal.OverlayItem.end_time"></a>

#### end_time

```python
@property
def end_time() -> Timespan
```

(Timespan):  [Read-Write] When the overlay should be cleared

<a id="unreal.OverlayItem.end_time"></a>

#### end_time

```python
@end_time.setter
def end_time(value: Timespan) -> None
```

<a id="unreal.OverlayItem.text"></a>

#### text

```python
@property
def text() -> str
```

(str):  [Read-Write] Text that appears onscreen when the overlay is shown

<a id="unreal.OverlayItem.text"></a>

#### text

```python
@text.setter
def text(value: str) -> None
```

<a id="unreal.OverlayItem.position"></a>

#### position

```python
@property
def position() -> Vector2D
```

(Vector2D):  [Read-Write] The position of the text on screen (Between 0.0 and 1.0)

<a id="unreal.OverlayItem.position"></a>

#### position

```python
@position.setter
def position(value: Vector2D) -> None
```

<a id="unreal.MassProcessingContext"></a>