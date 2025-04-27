## UIFrameworkCanvasBoxSlot Objects

```python
class UIFrameworkCanvasBoxSlot(UIFrameworkSlotBase)
```

UIFramework Canvas Box Slot

**C++ Source:**

- **Plugin**: UIFramework
- **Module**: UIFramework
- **File**: UIFCanvasBox.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alignment`` (Vector2D):  [Read-Write] Alignment is the pivot point of the widget.  Starting in the upper left at (0,0),
  ending in the lower right at (1,1).  Moving the alignment point allows you to move
  the origin of the widget.
- ``anchors`` (Anchors):  [Read-Write] Anchors.
- ``offsets`` (Margin):  [Read-Write] Offset.
- ``size_to_content`` (bool):  [Read-Write] When true we use the widget's desired size
- ``widget`` (UIFrameworkWidget):  [Read-Write]
- ``z_order`` (int32):  [Read-Write] The order priority this widget is rendered inside the layer. Higher values are rendered last (and so they will appear to be on top).

<a id="unreal.UIFrameworkCanvasBoxSlot.__init__"></a>

#### __init__

```python
def __init__(widget: UIFrameworkWidget = None,
             anchors: Anchors = [[0.000000, 0.000000], [0.000000, 0.000000]],
             offsets: Margin = [0.000000, 0.000000, 0.000000, 0.000000],
             alignment: Vector2D = [0.000000, 0.000000],
             z_order: int = 0,
             size_to_content: bool = False) -> None
```

<a id="unreal.UIFrameworkCanvasBoxSlot.anchors"></a>

#### anchors

```python
@property
def anchors() -> Anchors
```

(Anchors):  [Read-Write] Anchors.

<a id="unreal.UIFrameworkCanvasBoxSlot.anchors"></a>

#### anchors

```python
@anchors.setter
def anchors(value: Anchors) -> None
```

<a id="unreal.UIFrameworkCanvasBoxSlot.offsets"></a>

#### offsets

```python
@property
def offsets() -> Margin
```

(Margin):  [Read-Write] Offset.

<a id="unreal.UIFrameworkCanvasBoxSlot.offsets"></a>

#### offsets

```python
@offsets.setter
def offsets(value: Margin) -> None
```

<a id="unreal.UIFrameworkCanvasBoxSlot.alignment"></a>

#### alignment

```python
@property
def alignment() -> Vector2D
```

(Vector2D):  [Read-Write] Alignment is the pivot point of the widget.  Starting in the upper left at (0,0),
ending in the lower right at (1,1).  Moving the alignment point allows you to move
the origin of the widget.

<a id="unreal.UIFrameworkCanvasBoxSlot.alignment"></a>

#### alignment

```python
@alignment.setter
def alignment(value: Vector2D) -> None
```

<a id="unreal.UIFrameworkCanvasBoxSlot.z_order"></a>

#### z_order

```python
@property
def z_order() -> int
```

(int32):  [Read-Write] The order priority this widget is rendered inside the layer. Higher values are rendered last (and so they will appear to be on top).

<a id="unreal.UIFrameworkCanvasBoxSlot.z_order"></a>

#### z_order

```python
@z_order.setter
def z_order(value: int) -> None
```

<a id="unreal.UIFrameworkCanvasBoxSlot.size_to_content"></a>

#### size_to_content

```python
@property
def size_to_content() -> bool
```

(bool):  [Read-Write] When true we use the widget's desired size

<a id="unreal.UIFrameworkCanvasBoxSlot.size_to_content"></a>

#### size_to_content

```python
@size_to_content.setter
def size_to_content(value: bool) -> None
```

<a id="unreal.UIFrameworkOverlaySlot"></a>