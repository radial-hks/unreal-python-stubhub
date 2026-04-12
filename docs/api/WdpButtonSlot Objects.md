## WdpButtonSlot Objects

```python
class WdpButtonSlot(PanelSlot)
```

The Slot for the UWdpButtonSlot, contains the widget displayed in a button's single slot

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: WdpButtonSlot.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``horizontal_alignment`` (HorizontalAlignment):  [Read-Write] The alignment of the object horizontally.
- ``padding`` (Margin):  [Read-Write] The padding area between the slot and the content it contains.
- ``vertical_alignment`` (VerticalAlignment):  [Read-Write] The alignment of the object vertically.

<a id="unreal.WdpButtonSlot.padding"></a>

#### padding

```python
@property
def padding() -> Margin
```

(Margin):  [Read-Write] The padding area between the slot and the content it contains.

<a id="unreal.WdpButtonSlot.padding"></a>

#### padding

```python
@padding.setter
def padding(value: Margin) -> None
```

<a id="unreal.WdpButtonSlot.horizontal_alignment"></a>

#### horizontal\_alignment

```python
@property
def horizontal_alignment() -> HorizontalAlignment
```

(HorizontalAlignment):  [Read-Write] The alignment of the object horizontally.

<a id="unreal.WdpButtonSlot.horizontal_alignment"></a>

#### horizontal\_alignment

```python
@horizontal_alignment.setter
def horizontal_alignment(value: HorizontalAlignment) -> None
```

<a id="unreal.WdpButtonSlot.vertical_alignment"></a>

#### vertical\_alignment

```python
@property
def vertical_alignment() -> VerticalAlignment
```

(VerticalAlignment):  [Read-Write] The alignment of the object vertically.

<a id="unreal.WdpButtonSlot.vertical_alignment"></a>

#### vertical\_alignment

```python
@vertical_alignment.setter
def vertical_alignment(value: VerticalAlignment) -> None
```

<a id="unreal.WdpButtonSlot.set_vertical_alignment"></a>

#### set\_vertical\_alignment

```python
def set_vertical_alignment(vertical_alignment: VerticalAlignment) -> None
```

x.set_vertical_alignment(vertical_alignment) -> None
Set Vertical Alignment

Args:
    vertical_alignment (VerticalAlignment):

<a id="unreal.WdpButtonSlot.set_padding"></a>

#### set\_padding

```python
def set_padding(padding: Margin) -> None
```

x.set_padding(padding) -> None
Set Padding

Args:
    padding (Margin):

<a id="unreal.WdpButtonSlot.set_horizontal_alignment"></a>

#### set\_horizontal\_alignment

```python
def set_horizontal_alignment(
        horizontal_alignment: HorizontalAlignment) -> None
```

x.set_horizontal_alignment(horizontal_alignment) -> None
Set Horizontal Alignment

Args:
    horizontal_alignment (HorizontalAlignment):

<a id="unreal.ChinaMapAPI"></a>