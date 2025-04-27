## CanvasPanelSlot Objects

```python
class CanvasPanelSlot(PanelSlot)
```

Canvas Panel Slot

**C++ Source:**

- **Module**: UMG
- **File**: CanvasPanelSlot.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_size`` (bool):  [Read-Write] When AutoSize is true we use the widget's desired size
- ``layout_data`` (AnchorData):  [Read-Write] The anchoring information for the slot
- ``z_order`` (int32):  [Read-Write] The order priority this widget is rendered in.  Higher values are rendered last (and so they will appear to be on top).

<a id="unreal.CanvasPanelSlot.layout_data"></a>

#### layout_data

```python
@property
def layout_data() -> AnchorData
```

(AnchorData):  [Read-Write] The anchoring information for the slot

<a id="unreal.CanvasPanelSlot.layout_data"></a>

#### layout_data

```python
@layout_data.setter
def layout_data(value: AnchorData) -> None
```

<a id="unreal.CanvasPanelSlot.auto_size"></a>

#### auto_size

```python
@property
def auto_size() -> bool
```

(bool):  [Read-Write] When AutoSize is true we use the widget's desired size

<a id="unreal.CanvasPanelSlot.auto_size"></a>

#### auto_size

```python
@auto_size.setter
def auto_size(value: bool) -> None
```

<a id="unreal.CanvasPanelSlot.z_order"></a>

#### z_order

```python
@property
def z_order() -> int
```

(int32):  [Read-Write] The order priority this widget is rendered in.  Higher values are rendered last (and so they will appear to be on top).

<a id="unreal.CanvasPanelSlot.z_order"></a>

#### z_order

```python
@z_order.setter
def z_order(value: int) -> None
```

<a id="unreal.CanvasPanelSlot.set_z_order"></a>

#### set_z_order

```python
def set_z_order(z_order: int) -> None
```

x.set_z_order(z_order) -> None
Sets the z-order on the slot

Args:
    z_order (int32):

<a id="unreal.CanvasPanelSlot.set_size"></a>

#### set_size

```python
def set_size(size: Vector2D) -> None
```

x.set_size(size) -> None
Sets the size of the slot

Args:
    size (Vector2D):

<a id="unreal.CanvasPanelSlot.set_position"></a>

#### set_position

```python
def set_position(position: Vector2D) -> None
```

x.set_position(position) -> None
Sets the position of the slot

Args:
    position (Vector2D):

<a id="unreal.CanvasPanelSlot.set_offsets"></a>

#### set_offsets

```python
def set_offsets(offset: Margin) -> None
```

x.set_offsets(offset) -> None
Sets the offset data of the slot, which could be position and size, or margins depending on the anchor points

Args:
    offset (Margin):

<a id="unreal.CanvasPanelSlot.set_layout"></a>

#### set_layout

```python
def set_layout(layout_data: AnchorData) -> None
```

x.set_layout(layout_data) -> None
Sets the layout data of the slot

Args:
    layout_data (AnchorData):

<a id="unreal.CanvasPanelSlot.set_auto_size"></a>

#### set_auto_size

```python
def set_auto_size(inb_auto_size: bool) -> None
```

x.set_auto_size(inb_auto_size) -> None
Sets if the slot to be auto-sized

Args:
    inb_auto_size (bool):

<a id="unreal.CanvasPanelSlot.set_anchors"></a>

#### set_anchors

```python
def set_anchors(anchors: Anchors) -> None
```

x.set_anchors(anchors) -> None
Sets the anchors on the slot

Args:
    anchors (Anchors):

<a id="unreal.CanvasPanelSlot.set_alignment"></a>

#### set_alignment

```python
def set_alignment(alignment: Vector2D) -> None
```

x.set_alignment(alignment) -> None
Sets the alignment on the slot

Args:
    alignment (Vector2D):

<a id="unreal.CanvasPanelSlot.get_z_order"></a>

#### get_z_order

```python
def get_z_order() -> int
```

x.get_z_order() -> int32
Gets the z-order on the slot

Returns:
    int32:

<a id="unreal.CanvasPanelSlot.get_size"></a>

#### get_size

```python
def get_size() -> Vector2D
```

x.get_size() -> Vector2D
Gets the size of the slot

Returns:
    Vector2D:

<a id="unreal.CanvasPanelSlot.get_position"></a>

#### get_position

```python
def get_position() -> Vector2D
```

x.get_position() -> Vector2D
Gets the position of the slot

Returns:
    Vector2D:

<a id="unreal.CanvasPanelSlot.get_offsets"></a>

#### get_offsets

```python
def get_offsets() -> Margin
```

x.get_offsets() -> Margin
Gets the offset data of the slot, which could be position and size, or margins depending on the anchor points

Returns:
    Margin:

<a id="unreal.CanvasPanelSlot.get_layout"></a>

#### get_layout

```python
def get_layout() -> AnchorData
```

x.get_layout() -> AnchorData
Gets the layout data of the slot

Returns:
    AnchorData:

<a id="unreal.CanvasPanelSlot.get_auto_size"></a>

#### get_auto_size

```python
def get_auto_size() -> bool
```

x.get_auto_size() -> bool
Gets if the slot to be auto-sized

Returns:
    bool:

<a id="unreal.CanvasPanelSlot.get_anchors"></a>

#### get_anchors

```python
def get_anchors() -> Anchors
```

x.get_anchors() -> Anchors
Gets the anchors on the slot

Returns:
    Anchors:

<a id="unreal.CanvasPanelSlot.get_alignment"></a>

#### get_alignment

```python
def get_alignment() -> Vector2D
```

x.get_alignment() -> Vector2D
Gets the alignment on the slot

Returns:
    Vector2D:

<a id="unreal.CheckBox"></a>