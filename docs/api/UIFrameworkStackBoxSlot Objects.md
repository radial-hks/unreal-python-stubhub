## UIFrameworkStackBoxSlot Objects

```python
class UIFrameworkStackBoxSlot(UIFrameworkSlotBase)
```

UIFramework Stack Box Slot

**C++ Source:**

- **Plugin**: UIFramework
- **Module**: UIFramework
- **File**: UIFStackBox.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``horizontal_alignment`` (HorizontalAlignment):  [Read-Write] Horizontal alignment of the widget inside the slot.
- ``padding`` (Margin):  [Read-Write] Distance between that surrounds the widget inside the slot.
- ``size`` (SlateChildSize):  [Read-Write] How much space this slot should occupy in the direction of the panel.
- ``vertical_alignment`` (VerticalAlignment):  [Read-Write] Vertical alignment of the widget inside the slot.
- ``widget`` (UIFrameworkWidget):  [Read-Write]

<a id="unreal.UIFrameworkStackBoxSlot.__init__"></a>

#### __init__

```python
def __init__(
        widget: UIFrameworkWidget = None,
        horizontal_alignment: HorizontalAlignment = HorizontalAlignment.
    H_ALIGN_FILL,
        vertical_alignment: VerticalAlignment = VerticalAlignment.V_ALIGN_FILL,
        padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000],
        size: SlateChildSize = [1.000000, SlateSizeRule.FILL]) -> None
```

<a id="unreal.UIFrameworkStackBoxSlot.horizontal_alignment"></a>

#### horizontal_alignment

```python
@property
def horizontal_alignment() -> HorizontalAlignment
```

(HorizontalAlignment):  [Read-Write] Horizontal alignment of the widget inside the slot.

<a id="unreal.UIFrameworkStackBoxSlot.horizontal_alignment"></a>

#### horizontal_alignment

```python
@horizontal_alignment.setter
def horizontal_alignment(value: HorizontalAlignment) -> None
```

<a id="unreal.UIFrameworkStackBoxSlot.vertical_alignment"></a>

#### vertical_alignment

```python
@property
def vertical_alignment() -> VerticalAlignment
```

(VerticalAlignment):  [Read-Write] Vertical alignment of the widget inside the slot.

<a id="unreal.UIFrameworkStackBoxSlot.vertical_alignment"></a>

#### vertical_alignment

```python
@vertical_alignment.setter
def vertical_alignment(value: VerticalAlignment) -> None
```

<a id="unreal.UIFrameworkStackBoxSlot.padding"></a>

#### padding

```python
@property
def padding() -> Margin
```

(Margin):  [Read-Write] Distance between that surrounds the widget inside the slot.

<a id="unreal.UIFrameworkStackBoxSlot.padding"></a>

#### padding

```python
@padding.setter
def padding(value: Margin) -> None
```

<a id="unreal.UIFrameworkStackBoxSlot.size"></a>

#### size

```python
@property
def size() -> SlateChildSize
```

(SlateChildSize):  [Read-Write] How much space this slot should occupy in the direction of the panel.

<a id="unreal.UIFrameworkStackBoxSlot.size"></a>

#### size

```python
@size.setter
def size(value: SlateChildSize) -> None
```

<a id="unreal.UIFrameworkUserWidgetNamedSlot"></a>