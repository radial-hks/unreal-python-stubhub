## HorizontalBoxSlot Objects

```python
class HorizontalBoxSlot(PanelSlot)
```

Horizontal Box Slot

**C++ Source:**

- **Module**: UMG
- **File**: HorizontalBoxSlot.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``horizontal_alignment`` (HorizontalAlignment):  [Read-Write]
- ``padding`` (Margin):  [Read-Write] The amount of padding between the slots parent and the content.
- ``size`` (SlateChildSize):  [Read-Write] How much space this slot should occupy in the direction of the panel.
- ``vertical_alignment`` (VerticalAlignment):  [Read-Write]

<a id="unreal.HorizontalBoxSlot.size"></a>

#### size

```python
@property
def size() -> SlateChildSize
```

(SlateChildSize):  [Read-Write] How much space this slot should occupy in the direction of the panel.

<a id="unreal.HorizontalBoxSlot.size"></a>

#### size

```python
@size.setter
def size(value: SlateChildSize) -> None
```

<a id="unreal.HorizontalBoxSlot.padding"></a>

#### padding

```python
@property
def padding() -> Margin
```

(Margin):  [Read-Write] The amount of padding between the slots parent and the content.

<a id="unreal.HorizontalBoxSlot.padding"></a>

#### padding

```python
@padding.setter
def padding(value: Margin) -> None
```

<a id="unreal.HorizontalBoxSlot.horizontal_alignment"></a>

#### horizontal_alignment

```python
@property
def horizontal_alignment() -> HorizontalAlignment
```

(HorizontalAlignment):  [Read-Write]

<a id="unreal.HorizontalBoxSlot.horizontal_alignment"></a>

#### horizontal_alignment

```python
@horizontal_alignment.setter
def horizontal_alignment(value: HorizontalAlignment) -> None
```

<a id="unreal.HorizontalBoxSlot.vertical_alignment"></a>

#### vertical_alignment

```python
@property
def vertical_alignment() -> VerticalAlignment
```

(VerticalAlignment):  [Read-Write]

<a id="unreal.HorizontalBoxSlot.vertical_alignment"></a>

#### vertical_alignment

```python
@vertical_alignment.setter
def vertical_alignment(value: VerticalAlignment) -> None
```

<a id="unreal.HorizontalBoxSlot.set_vertical_alignment"></a>

#### set_vertical_alignment

```python
def set_vertical_alignment(vertical_alignment: VerticalAlignment) -> None
```

x.set_vertical_alignment(vertical_alignment) -> None
Set Vertical Alignment

Args:
    vertical_alignment (VerticalAlignment):

<a id="unreal.HorizontalBoxSlot.set_size"></a>

#### set_size

```python
def set_size(size: SlateChildSize) -> None
```

x.set_size(size) -> None
Set Size

Args:
    size (SlateChildSize):

<a id="unreal.HorizontalBoxSlot.set_padding"></a>

#### set_padding

```python
def set_padding(padding: Margin) -> None
```

x.set_padding(padding) -> None
Set Padding

Args:
    padding (Margin):

<a id="unreal.HorizontalBoxSlot.set_horizontal_alignment"></a>

#### set_horizontal_alignment

```python
def set_horizontal_alignment(
        horizontal_alignment: HorizontalAlignment) -> None
```

x.set_horizontal_alignment(horizontal_alignment) -> None
Set Horizontal Alignment

Args:
    horizontal_alignment (HorizontalAlignment):

<a id="unreal.Image"></a>