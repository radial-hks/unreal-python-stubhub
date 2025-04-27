## StackBoxSlot Objects

```python
class StackBoxSlot(PanelSlot)
```

The Slot for the UStackBox, contains the widget that is flowed vertically or horizontally.

**C++ Source:**

- **Module**: UMG
- **File**: StackBoxSlot.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``horizontal_alignment`` (HorizontalAlignment):  [Read-Write] The alignment of the object horizontally.
- ``padding`` (Margin):  [Read-Write] The padding area between the slot and the content it contains.
- ``size`` (SlateChildSize):  [Read-Write] How much space this slot should occupy in the direction of the panel.
- ``vertical_alignment`` (VerticalAlignment):  [Read-Write] The alignment of the object vertically.

<a id="unreal.StackBoxSlot.padding"></a>

#### padding

```python
@property
def padding() -> Margin
```

(Margin):  [Read-Write] The padding area between the slot and the content it contains.

<a id="unreal.StackBoxSlot.padding"></a>

#### padding

```python
@padding.setter
def padding(value: Margin) -> None
```

<a id="unreal.StackBoxSlot.size"></a>

#### size

```python
@property
def size() -> SlateChildSize
```

(SlateChildSize):  [Read-Write] How much space this slot should occupy in the direction of the panel.

<a id="unreal.StackBoxSlot.size"></a>

#### size

```python
@size.setter
def size(value: SlateChildSize) -> None
```

<a id="unreal.StackBoxSlot.horizontal_alignment"></a>

#### horizontal_alignment

```python
@property
def horizontal_alignment() -> HorizontalAlignment
```

(HorizontalAlignment):  [Read-Write] The alignment of the object horizontally.

<a id="unreal.StackBoxSlot.horizontal_alignment"></a>

#### horizontal_alignment

```python
@horizontal_alignment.setter
def horizontal_alignment(value: HorizontalAlignment) -> None
```

<a id="unreal.StackBoxSlot.vertical_alignment"></a>

#### vertical_alignment

```python
@property
def vertical_alignment() -> VerticalAlignment
```

(VerticalAlignment):  [Read-Write] The alignment of the object vertically.

<a id="unreal.StackBoxSlot.vertical_alignment"></a>

#### vertical_alignment

```python
@vertical_alignment.setter
def vertical_alignment(value: VerticalAlignment) -> None
```

<a id="unreal.TextBlock"></a>