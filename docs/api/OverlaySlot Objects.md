## OverlaySlot Objects

```python
class OverlaySlot(PanelSlot)
```

Slot for the UOverlay panel.  Allows content to be hover above other content.

**C++ Source:**

- **Module**: UMG
- **File**: OverlaySlot.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``horizontal_alignment`` (HorizontalAlignment):  [Read-Write] The alignment of the object horizontally.
- ``padding`` (Margin):  [Read-Write] The padding area between the slot and the content it contains.
- ``vertical_alignment`` (VerticalAlignment):  [Read-Write] The alignment of the object vertically.

<a id="unreal.OverlaySlot.padding"></a>

#### padding

```python
@property
def padding() -> Margin
```

(Margin):  [Read-Write] The padding area between the slot and the content it contains.

<a id="unreal.OverlaySlot.padding"></a>

#### padding

```python
@padding.setter
def padding(value: Margin) -> None
```

<a id="unreal.OverlaySlot.horizontal_alignment"></a>

#### horizontal_alignment

```python
@property
def horizontal_alignment() -> HorizontalAlignment
```

(HorizontalAlignment):  [Read-Write] The alignment of the object horizontally.

<a id="unreal.OverlaySlot.horizontal_alignment"></a>

#### horizontal_alignment

```python
@horizontal_alignment.setter
def horizontal_alignment(value: HorizontalAlignment) -> None
```

<a id="unreal.OverlaySlot.vertical_alignment"></a>

#### vertical_alignment

```python
@property
def vertical_alignment() -> VerticalAlignment
```

(VerticalAlignment):  [Read-Write] The alignment of the object vertically.

<a id="unreal.OverlaySlot.vertical_alignment"></a>

#### vertical_alignment

```python
@vertical_alignment.setter
def vertical_alignment(value: VerticalAlignment) -> None
```

<a id="unreal.OverlaySlot.set_vertical_alignment"></a>

#### set_vertical_alignment

```python
def set_vertical_alignment(vertical_alignment: VerticalAlignment) -> None
```

x.set_vertical_alignment(vertical_alignment) -> None
Set the alignment of the object vertically.

Args:
    vertical_alignment (VerticalAlignment):

<a id="unreal.OverlaySlot.set_padding"></a>

#### set_padding

```python
def set_padding(padding: Margin) -> None
```

x.set_padding(padding) -> None
Set padding area between the slot and the content it contains.

Args:
    padding (Margin):

<a id="unreal.OverlaySlot.set_horizontal_alignment"></a>

#### set_horizontal_alignment

```python
def set_horizontal_alignment(
        horizontal_alignment: HorizontalAlignment) -> None
```

x.set_horizontal_alignment(horizontal_alignment) -> None
Set the alignment of the object horizontally.

Args:
    horizontal_alignment (HorizontalAlignment):

<a id="unreal.SlatePostBufferProcessorUpdater"></a>