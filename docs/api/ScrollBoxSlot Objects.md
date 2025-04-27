## ScrollBoxSlot Objects

```python
class ScrollBoxSlot(PanelSlot)
```

The Slot for the UScrollBox, contains the widget that are scrollable

**C++ Source:**

- **Module**: UMG
- **File**: ScrollBoxSlot.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``horizontal_alignment`` (HorizontalAlignment):  [Read-Write] The alignment of the object horizontally.
- ``padding`` (Margin):  [Read-Write] The padding area between the slot and the content it contains.
- ``size`` (SlateChildSize):  [Read-Write] How much space this slot should occupy in the direction of the panel.
- ``vertical_alignment`` (VerticalAlignment):  [Read-Write] The alignment of the object vertically.

<a id="unreal.ScrollBoxSlot.size"></a>

#### size

```python
@property
def size() -> SlateChildSize
```

(SlateChildSize):  [Read-Write] How much space this slot should occupy in the direction of the panel.

<a id="unreal.ScrollBoxSlot.size"></a>

#### size

```python
@size.setter
def size(value: SlateChildSize) -> None
```

<a id="unreal.ScrollBoxSlot.padding"></a>

#### padding

```python
@property
def padding() -> Margin
```

(Margin):  [Read-Only] The padding area between the slot and the content it contains.

<a id="unreal.ScrollBoxSlot.horizontal_alignment"></a>

#### horizontal_alignment

```python
@property
def horizontal_alignment() -> HorizontalAlignment
```

(HorizontalAlignment):  [Read-Only] The alignment of the object horizontally.

<a id="unreal.ScrollBoxSlot.vertical_alignment"></a>

#### vertical_alignment

```python
@property
def vertical_alignment() -> VerticalAlignment
```

(VerticalAlignment):  [Read-Only] The alignment of the object vertically.

<a id="unreal.ScrollBoxSlot.set_vertical_alignment"></a>

#### set_vertical_alignment

```python
def set_vertical_alignment(vertical_alignment: VerticalAlignment) -> None
```

x.set_vertical_alignment(vertical_alignment) -> None
Set Vertical Alignment

Args:
    vertical_alignment (VerticalAlignment):

<a id="unreal.ScrollBoxSlot.set_padding"></a>

#### set_padding

```python
def set_padding(padding: Margin) -> None
```

x.set_padding(padding) -> None
Set Padding

Args:
    padding (Margin):

<a id="unreal.ScrollBoxSlot.set_horizontal_alignment"></a>

#### set_horizontal_alignment

```python
def set_horizontal_alignment(
        horizontal_alignment: HorizontalAlignment) -> None
```

x.set_horizontal_alignment(horizontal_alignment) -> None
Set Horizontal Alignment

Args:
    horizontal_alignment (HorizontalAlignment):

<a id="unreal.SizeBox"></a>