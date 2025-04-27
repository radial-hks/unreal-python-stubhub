## WrapBoxSlot Objects

```python
class WrapBoxSlot(PanelSlot)
```

The Slot for the UWrapBox, contains the widget that is flowed vertically

**C++ Source:**

- **Module**: UMG
- **File**: WrapBoxSlot.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``fill_empty_space`` (bool):  [Read-Write] Should this slot fill the remaining space on the line?
- ``fill_span_when_less_than`` (float):  [Read-Write] If the total available space in the wrap panel drops below this threshold, this slot will attempt to fill an entire line.
  NOTE: A value of 0, denotes no filling will occur.
- ``force_new_line`` (bool):  [Read-Write] Should this slot start on a new line?
- ``horizontal_alignment`` (HorizontalAlignment):  [Read-Write] The alignment of the object horizontally.
- ``padding`` (Margin):  [Read-Write] The padding area between the slot and the content it contains.
- ``vertical_alignment`` (VerticalAlignment):  [Read-Write] The alignment of the object vertically.

<a id="unreal.WrapBoxSlot.padding"></a>

#### padding

```python
@property
def padding() -> Margin
```

(Margin):  [Read-Write] The padding area between the slot and the content it contains.

<a id="unreal.WrapBoxSlot.padding"></a>

#### padding

```python
@padding.setter
def padding(value: Margin) -> None
```

<a id="unreal.WrapBoxSlot.fill_span_when_less_than"></a>

#### fill_span_when_less_than

```python
@property
def fill_span_when_less_than() -> float
```

(float):  [Read-Write] If the total available space in the wrap panel drops below this threshold, this slot will attempt to fill an entire line.
NOTE: A value of 0, denotes no filling will occur.

<a id="unreal.WrapBoxSlot.fill_span_when_less_than"></a>

#### fill_span_when_less_than

```python
@fill_span_when_less_than.setter
def fill_span_when_less_than(value: float) -> None
```

<a id="unreal.WrapBoxSlot.horizontal_alignment"></a>

#### horizontal_alignment

```python
@property
def horizontal_alignment() -> HorizontalAlignment
```

(HorizontalAlignment):  [Read-Write] The alignment of the object horizontally.

<a id="unreal.WrapBoxSlot.horizontal_alignment"></a>

#### horizontal_alignment

```python
@horizontal_alignment.setter
def horizontal_alignment(value: HorizontalAlignment) -> None
```

<a id="unreal.WrapBoxSlot.vertical_alignment"></a>

#### vertical_alignment

```python
@property
def vertical_alignment() -> VerticalAlignment
```

(VerticalAlignment):  [Read-Write] The alignment of the object vertically.

<a id="unreal.WrapBoxSlot.vertical_alignment"></a>

#### vertical_alignment

```python
@vertical_alignment.setter
def vertical_alignment(value: VerticalAlignment) -> None
```

<a id="unreal.WrapBoxSlot.fill_empty_space"></a>

#### fill_empty_space

```python
@property
def fill_empty_space() -> bool
```

(bool):  [Read-Write] Should this slot fill the remaining space on the line?

<a id="unreal.WrapBoxSlot.fill_empty_space"></a>

#### fill_empty_space

```python
@fill_empty_space.setter
def fill_empty_space(value: bool) -> None
```

<a id="unreal.WrapBoxSlot.force_new_line"></a>

#### force_new_line

```python
@property
def force_new_line() -> bool
```

(bool):  [Read-Write] Should this slot start on a new line?

<a id="unreal.WrapBoxSlot.force_new_line"></a>

#### force_new_line

```python
@force_new_line.setter
def force_new_line(value: bool) -> None
```

<a id="unreal.WrapBoxSlot.set_vertical_alignment"></a>

#### set_vertical_alignment

```python
def set_vertical_alignment(vertical_alignment: VerticalAlignment) -> None
```

x.set_vertical_alignment(vertical_alignment) -> None
Set Vertical Alignment

Args:
    vertical_alignment (VerticalAlignment):

<a id="unreal.WrapBoxSlot.set_padding"></a>

#### set_padding

```python
def set_padding(padding: Margin) -> None
```

x.set_padding(padding) -> None
Set Padding

Args:
    padding (Margin):

<a id="unreal.WrapBoxSlot.set_new_line"></a>

#### set_new_line

```python
def set_new_line(force_new_line: bool) -> None
```

x.set_new_line(force_new_line) -> None
Set New Line

Args:
    force_new_line (bool):

<a id="unreal.WrapBoxSlot.set_horizontal_alignment"></a>

#### set_horizontal_alignment

```python
def set_horizontal_alignment(
        horizontal_alignment: HorizontalAlignment) -> None
```

x.set_horizontal_alignment(horizontal_alignment) -> None
Set Horizontal Alignment

Args:
    horizontal_alignment (HorizontalAlignment):

<a id="unreal.WrapBoxSlot.set_fill_span_when_less_than"></a>

#### set_fill_span_when_less_than

```python
def set_fill_span_when_less_than(fill_span_when_less_than: float) -> None
```

x.set_fill_span_when_less_than(fill_span_when_less_than) -> None
Set Fill Span when Less Than

Args:
    fill_span_when_less_than (float):

<a id="unreal.WrapBoxSlot.set_fill_empty_space"></a>

#### set_fill_empty_space

```python
def set_fill_empty_space(inb_fill_empty_space: bool) -> None
```

x.set_fill_empty_space(inb_fill_empty_space) -> None
Set Fill Empty Space

Args:
    inb_fill_empty_space (bool):

<a id="unreal.DragDropOperation"></a>