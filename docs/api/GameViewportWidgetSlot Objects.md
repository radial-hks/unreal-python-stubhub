## GameViewportWidgetSlot Objects

```python
class GameViewportWidgetSlot(StructBase)
```

The default value fills the entire screen / player region.

**C++ Source:**

- **Module**: UMG
- **File**: GameViewportSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alignment`` (Vector2D):  [Read-Write]
- ``anchors`` (Anchors):  [Read-Write]
- ``auto_remove_on_world_removed`` (bool):  [Read-Write] Remove the widget when the Widget's World is removed.
  note: The Widget is added to the GameViewportClient of the Widget's World. The GameViewportClient can migrate from World to World. The widget can stay visible if the owner of the widget also migrate.
- ``offsets`` (Margin):  [Read-Write]
- ``z_order`` (int32):  [Read-Write] The higher the number, the more on top this widget will be.

<a id="unreal.GameViewportWidgetSlot.__init__"></a>

#### __init__

```python
def __init__(anchors: Anchors = [[0.000000, 0.000000], [0.000000, 0.000000]],
             offsets: Margin = [0.000000, 0.000000, 0.000000, 0.000000],
             alignment: Vector2D = [0.000000, 0.000000],
             z_order: int = 0,
             auto_remove_on_world_removed: bool = False) -> None
```

<a id="unreal.GameViewportWidgetSlot.anchors"></a>

#### anchors

```python
@property
def anchors() -> Anchors
```

(Anchors):  [Read-Write]

<a id="unreal.GameViewportWidgetSlot.anchors"></a>

#### anchors

```python
@anchors.setter
def anchors(value: Anchors) -> None
```

<a id="unreal.GameViewportWidgetSlot.offsets"></a>

#### offsets

```python
@property
def offsets() -> Margin
```

(Margin):  [Read-Write]

<a id="unreal.GameViewportWidgetSlot.offsets"></a>

#### offsets

```python
@offsets.setter
def offsets(value: Margin) -> None
```

<a id="unreal.GameViewportWidgetSlot.alignment"></a>

#### alignment

```python
@property
def alignment() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.GameViewportWidgetSlot.alignment"></a>

#### alignment

```python
@alignment.setter
def alignment(value: Vector2D) -> None
```

<a id="unreal.GameViewportWidgetSlot.z_order"></a>

#### z_order

```python
@property
def z_order() -> int
```

(int32):  [Read-Write] The higher the number, the more on top this widget will be.

<a id="unreal.GameViewportWidgetSlot.z_order"></a>

#### z_order

```python
@z_order.setter
def z_order(value: int) -> None
```

<a id="unreal.GameViewportWidgetSlot.auto_remove_on_world_removed"></a>

#### auto_remove_on_world_removed

```python
@property
def auto_remove_on_world_removed() -> bool
```

(bool):  [Read-Write] Remove the widget when the Widget's World is removed.
note: The Widget is added to the GameViewportClient of the Widget's World. The GameViewportClient can migrate from World to World. The widget can stay visible if the owner of the widget also migrate.

<a id="unreal.GameViewportWidgetSlot.auto_remove_on_world_removed"></a>

#### auto_remove_on_world_removed

```python
@auto_remove_on_world_removed.setter
def auto_remove_on_world_removed(value: bool) -> None
```

<a id="unreal.AnchorData"></a>