## GridSlot Objects

```python
class GridSlot(PanelSlot)
```

A slot for UGridPanel, these slots all share the same size as the largest slot
in the grid.

**C++ Source:**

- **Module**: UMG
- **File**: GridSlot.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``column`` (int32):  [Read-Write] The column index of the cell this slot is in
- ``column_span`` (int32):  [Read-Write]
- ``horizontal_alignment`` (HorizontalAlignment):  [Read-Write] The alignment of the object horizontally.
- ``layer`` (int32):  [Read-Write] Positive values offset this cell to be hit-tested and drawn on top of others. Default is 0; i.e. no offset.
- ``nudge`` (Vector2D):  [Read-Write] Offset this slot's content by some amount; positive values offset to lower right
- ``padding`` (Margin):  [Read-Write] The padding area between the slot and the content it contains.
- ``row`` (int32):  [Read-Write] The row index of the cell this slot is in
- ``row_span`` (int32):  [Read-Write]
- ``vertical_alignment`` (VerticalAlignment):  [Read-Write] The alignment of the object vertically.

<a id="unreal.GridSlot.padding"></a>

#### padding

```python
@property
def padding() -> Margin
```

(Margin):  [Read-Write] The padding area between the slot and the content it contains.

<a id="unreal.GridSlot.padding"></a>

#### padding

```python
@padding.setter
def padding(value: Margin) -> None
```

<a id="unreal.GridSlot.horizontal_alignment"></a>

#### horizontal\_alignment

```python
@property
def horizontal_alignment() -> HorizontalAlignment
```

(HorizontalAlignment):  [Read-Write] The alignment of the object horizontally.

<a id="unreal.GridSlot.horizontal_alignment"></a>

#### horizontal\_alignment

```python
@horizontal_alignment.setter
def horizontal_alignment(value: HorizontalAlignment) -> None
```

<a id="unreal.GridSlot.vertical_alignment"></a>

#### vertical\_alignment

```python
@property
def vertical_alignment() -> VerticalAlignment
```

(VerticalAlignment):  [Read-Write] The alignment of the object vertically.

<a id="unreal.GridSlot.vertical_alignment"></a>

#### vertical\_alignment

```python
@vertical_alignment.setter
def vertical_alignment(value: VerticalAlignment) -> None
```

<a id="unreal.GridSlot.row"></a>

#### row

```python
@property
def row() -> int
```

(int32):  [Read-Write] The row index of the cell this slot is in

<a id="unreal.GridSlot.row"></a>

#### row

```python
@row.setter
def row(value: int) -> None
```

<a id="unreal.GridSlot.row_span"></a>

#### row\_span

```python
@property
def row_span() -> int
```

(int32):  [Read-Write]

<a id="unreal.GridSlot.row_span"></a>

#### row\_span

```python
@row_span.setter
def row_span(value: int) -> None
```

<a id="unreal.GridSlot.column"></a>

#### column

```python
@property
def column() -> int
```

(int32):  [Read-Write] The column index of the cell this slot is in

<a id="unreal.GridSlot.column"></a>

#### column

```python
@column.setter
def column(value: int) -> None
```

<a id="unreal.GridSlot.column_span"></a>

#### column\_span

```python
@property
def column_span() -> int
```

(int32):  [Read-Write]

<a id="unreal.GridSlot.column_span"></a>

#### column\_span

```python
@column_span.setter
def column_span(value: int) -> None
```

<a id="unreal.GridSlot.layer"></a>

#### layer

```python
@property
def layer() -> int
```

(int32):  [Read-Write] Positive values offset this cell to be hit-tested and drawn on top of others. Default is 0; i.e. no offset.

<a id="unreal.GridSlot.layer"></a>

#### layer

```python
@layer.setter
def layer(value: int) -> None
```

<a id="unreal.GridSlot.nudge"></a>

#### nudge

```python
@property
def nudge() -> Vector2D
```

(Vector2D):  [Read-Write] Offset this slot's content by some amount; positive values offset to lower right

<a id="unreal.GridSlot.nudge"></a>

#### nudge

```python
@nudge.setter
def nudge(value: Vector2D) -> None
```

<a id="unreal.GridSlot.set_vertical_alignment"></a>

#### set\_vertical\_alignment

```python
def set_vertical_alignment(vertical_alignment: VerticalAlignment) -> None
```

x.set_vertical_alignment(vertical_alignment) -> None
Set Vertical Alignment

Args:
    vertical_alignment (VerticalAlignment):

<a id="unreal.GridSlot.set_row_span"></a>

#### set\_row\_span

```python
def set_row_span(row_span: int) -> None
```

x.set_row_span(row_span) -> None
How many rows this this slot spans over

Args:
    row_span (int32):

<a id="unreal.GridSlot.set_row"></a>

#### set\_row

```python
def set_row(row: int) -> None
```

x.set_row(row) -> None
Sets the row index of the slot, this determines what cell the slot is in the panel

Args:
    row (int32):

<a id="unreal.GridSlot.set_padding"></a>

#### set\_padding

```python
def set_padding(padding: Margin) -> None
```

x.set_padding(padding) -> None
Set Padding

Args:
    padding (Margin):

<a id="unreal.GridSlot.set_nudge"></a>

#### set\_nudge

```python
def set_nudge(nudge: Vector2D) -> None
```

x.set_nudge(nudge) -> None
Sets the offset for this slot's content by some amount; positive values offset to lower right

Args:
    nudge (Vector2D):

<a id="unreal.GridSlot.set_layer"></a>

#### set\_layer

```python
def set_layer(layer: int) -> None
```

x.set_layer(layer) -> None
Sets positive values offset this cell to be hit-tested and drawn on top of others.

Args:
    layer (int32):

<a id="unreal.GridSlot.set_horizontal_alignment"></a>

#### set\_horizontal\_alignment

```python
def set_horizontal_alignment(
        horizontal_alignment: HorizontalAlignment) -> None
```

x.set_horizontal_alignment(horizontal_alignment) -> None
Set Horizontal Alignment

Args:
    horizontal_alignment (HorizontalAlignment):

<a id="unreal.GridSlot.set_column_span"></a>

#### set\_column\_span

```python
def set_column_span(column_span: int) -> None
```

x.set_column_span(column_span) -> None
How many columns this slot spans over

Args:
    column_span (int32):

<a id="unreal.GridSlot.set_column"></a>

#### set\_column

```python
def set_column(column: int) -> None
```

x.set_column(column) -> None
Sets the column index of the slot, this determines what cell the slot is in the panel

Args:
    column (int32):

<a id="unreal.HorizontalBox"></a>