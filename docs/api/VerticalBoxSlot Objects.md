## VerticalBoxSlot Objects

```python
class VerticalBoxSlot(PanelSlot)
```

The Slot for the UVerticalBox, contains the widget that is flowed vertically

**C++ Source:**

- **Module**: UMG
- **File**: VerticalBoxSlot.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``horizontal_alignment`` (HorizontalAlignment):  [Read-Write] The alignment of the object horizontally.
- ``padding`` (Margin):  [Read-Write] The padding area between the slot and the content it contains.
- ``size`` (SlateChildSize):  [Read-Write] How much space this slot should occupy in the direction of the panel.
- ``vertical_alignment`` (VerticalAlignment):  [Read-Write] The alignment of the object vertically.

<a id="unreal.VerticalBoxSlot.size"></a>

#### size

```python
@property
def size() -> SlateChildSize
```

(SlateChildSize):  [Read-Write] How much space this slot should occupy in the direction of the panel.

<a id="unreal.VerticalBoxSlot.size"></a>

#### size

```python
@size.setter
def size(value: SlateChildSize) -> None
```

<a id="unreal.VerticalBoxSlot.padding"></a>

#### padding

```python
@property
def padding() -> Margin
```

(Margin):  [Read-Write] The padding area between the slot and the content it contains.

<a id="unreal.VerticalBoxSlot.padding"></a>

#### padding

```python
@padding.setter
def padding(value: Margin) -> None
```

<a id="unreal.VerticalBoxSlot.horizontal_alignment"></a>

#### horizontal_alignment

```python
@property
def horizontal_alignment() -> HorizontalAlignment
```

(HorizontalAlignment):  [Read-Write] The alignment of the object horizontally.

<a id="unreal.VerticalBoxSlot.horizontal_alignment"></a>

#### horizontal_alignment

```python
@horizontal_alignment.setter
def horizontal_alignment(value: HorizontalAlignment) -> None
```

<a id="unreal.VerticalBoxSlot.vertical_alignment"></a>

#### vertical_alignment

```python
@property
def vertical_alignment() -> VerticalAlignment
```

(VerticalAlignment):  [Read-Write] The alignment of the object vertically.

<a id="unreal.VerticalBoxSlot.vertical_alignment"></a>

#### vertical_alignment

```python
@vertical_alignment.setter
def vertical_alignment(value: VerticalAlignment) -> None
```

<a id="unreal.VerticalBoxSlot.set_vertical_alignment"></a>

#### set_vertical_alignment

```python
def set_vertical_alignment(vertical_alignment: VerticalAlignment) -> None
```

x.set_vertical_alignment(vertical_alignment) -> None
Set Vertical Alignment

Args:
    vertical_alignment (VerticalAlignment):

<a id="unreal.VerticalBoxSlot.set_size"></a>

#### set_size

```python
def set_size(size: SlateChildSize) -> None
```

x.set_size(size) -> None
Set Size

Args:
    size (SlateChildSize):

<a id="unreal.VerticalBoxSlot.set_padding"></a>

#### set_padding

```python
def set_padding(padding: Margin) -> None
```

x.set_padding(padding) -> None
Set Padding

Args:
    padding (Margin):

<a id="unreal.VerticalBoxSlot.set_horizontal_alignment"></a>

#### set_horizontal_alignment

```python
def set_horizontal_alignment(
        horizontal_alignment: HorizontalAlignment) -> None
```

x.set_horizontal_alignment(horizontal_alignment) -> None
Set Horizontal Alignment

Args:
    horizontal_alignment (HorizontalAlignment):

<a id="unreal.Viewport"></a>