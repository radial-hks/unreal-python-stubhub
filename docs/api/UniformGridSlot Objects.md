## UniformGridSlot Objects

```python
class UniformGridSlot(PanelSlot)
```

A slot for UUniformGridPanel, these slots all share the same size as the largest slot
in the grid.

**C++ Source:**

- **Module**: UMG
- **File**: UniformGridSlot.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``column`` (int32):  [Read-Write] The column index of the cell this slot is in
- ``horizontal_alignment`` (HorizontalAlignment):  [Read-Write] The alignment of the object horizontally.
- ``row`` (int32):  [Read-Write] The row index of the cell this slot is in
- ``vertical_alignment`` (VerticalAlignment):  [Read-Write] The alignment of the object vertically.

<a id="unreal.UniformGridSlot.horizontal_alignment"></a>

#### horizontal_alignment

```python
@property
def horizontal_alignment() -> HorizontalAlignment
```

(HorizontalAlignment):  [Read-Write] The alignment of the object horizontally.

<a id="unreal.UniformGridSlot.horizontal_alignment"></a>

#### horizontal_alignment

```python
@horizontal_alignment.setter
def horizontal_alignment(value: HorizontalAlignment) -> None
```

<a id="unreal.UniformGridSlot.vertical_alignment"></a>

#### vertical_alignment

```python
@property
def vertical_alignment() -> VerticalAlignment
```

(VerticalAlignment):  [Read-Write] The alignment of the object vertically.

<a id="unreal.UniformGridSlot.vertical_alignment"></a>

#### vertical_alignment

```python
@vertical_alignment.setter
def vertical_alignment(value: VerticalAlignment) -> None
```

<a id="unreal.UniformGridSlot.row"></a>

#### row

```python
@property
def row() -> int
```

(int32):  [Read-Write] The row index of the cell this slot is in

<a id="unreal.UniformGridSlot.row"></a>

#### row

```python
@row.setter
def row(value: int) -> None
```

<a id="unreal.UniformGridSlot.column"></a>

#### column

```python
@property
def column() -> int
```

(int32):  [Read-Write] The column index of the cell this slot is in

<a id="unreal.UniformGridSlot.column"></a>

#### column

```python
@column.setter
def column(value: int) -> None
```

<a id="unreal.UniformGridSlot.set_vertical_alignment"></a>

#### set_vertical_alignment

```python
def set_vertical_alignment(vertical_alignment: VerticalAlignment) -> None
```

x.set_vertical_alignment(vertical_alignment) -> None
Set Vertical Alignment

Args:
    vertical_alignment (VerticalAlignment):

<a id="unreal.UniformGridSlot.set_row"></a>

#### set_row

```python
def set_row(row: int) -> None
```

x.set_row(row) -> None
Sets the row index of the slot, this determines what cell the slot is in the panel

Args:
    row (int32):

<a id="unreal.UniformGridSlot.set_horizontal_alignment"></a>

#### set_horizontal_alignment

```python
def set_horizontal_alignment(
        horizontal_alignment: HorizontalAlignment) -> None
```

x.set_horizontal_alignment(horizontal_alignment) -> None
Set Horizontal Alignment

Args:
    horizontal_alignment (HorizontalAlignment):

<a id="unreal.UniformGridSlot.set_column"></a>

#### set_column

```python
def set_column(column: int) -> None
```

x.set_column(column) -> None
Sets the column index of the slot, this determines what cell the slot is in the panel

Args:
    column (int32):

<a id="unreal.VerticalBox"></a>