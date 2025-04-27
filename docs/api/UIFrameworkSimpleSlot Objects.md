## UIFrameworkSimpleSlot Objects

```python
class UIFrameworkSimpleSlot(UIFrameworkSlotBase)
```

UIFramework Simple Slot

**C++ Source:**

- **Plugin**: UIFramework
- **Module**: UIFramework
- **File**: UIFSlotBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``horizontal_alignment`` (HorizontalAlignment):  [Read-Write]
- ``padding`` (Margin):  [Read-Write]
- ``vertical_alignment`` (VerticalAlignment):  [Read-Write]
- ``widget`` (UIFrameworkWidget):  [Read-Write]

<a id="unreal.UIFrameworkSimpleSlot.__init__"></a>

#### __init__

```python
def __init__(
    widget: UIFrameworkWidget = None,
    padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000],
    horizontal_alignment: HorizontalAlignment = HorizontalAlignment.
    H_ALIGN_FILL,
    vertical_alignment: VerticalAlignment = VerticalAlignment.V_ALIGN_FILL
) -> None
```

<a id="unreal.UIFrameworkSimpleSlot.padding"></a>

#### padding

```python
@property
def padding() -> Margin
```

(Margin):  [Read-Write]

<a id="unreal.UIFrameworkSimpleSlot.padding"></a>

#### padding

```python
@padding.setter
def padding(value: Margin) -> None
```

<a id="unreal.UIFrameworkSimpleSlot.horizontal_alignment"></a>

#### horizontal_alignment

```python
@property
def horizontal_alignment() -> HorizontalAlignment
```

(HorizontalAlignment):  [Read-Write]

<a id="unreal.UIFrameworkSimpleSlot.horizontal_alignment"></a>

#### horizontal_alignment

```python
@horizontal_alignment.setter
def horizontal_alignment(value: HorizontalAlignment) -> None
```

<a id="unreal.UIFrameworkSimpleSlot.vertical_alignment"></a>

#### vertical_alignment

```python
@property
def vertical_alignment() -> VerticalAlignment
```

(VerticalAlignment):  [Read-Write]

<a id="unreal.UIFrameworkSimpleSlot.vertical_alignment"></a>

#### vertical_alignment

```python
@vertical_alignment.setter
def vertical_alignment(value: VerticalAlignment) -> None
```

<a id="unreal.UIFrameworkGameLayerSlot"></a>