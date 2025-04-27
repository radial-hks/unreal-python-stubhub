## AnchorData Objects

```python
class AnchorData(StructBase)
```

Anchor Data

**C++ Source:**

- **Module**: UMG
- **File**: CanvasPanelSlot.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alignment`` (Vector2D):  [Read-Write] Alignment is the pivot point of the widget.  Starting in the upper left at (0,0),
  ending in the lower right at (1,1).  Moving the alignment point allows you to move
  the origin of the widget.
- ``anchors`` (Anchors):  [Read-Write] Anchors.
- ``offsets`` (Margin):  [Read-Write] Offset.

<a id="unreal.AnchorData.__init__"></a>

#### __init__

```python
def __init__(offsets: Margin = [0.000000, 0.000000, 0.000000, 0.000000],
             anchors: Anchors = [[0.000000, 0.000000], [0.000000, 0.000000]],
             alignment: Vector2D = [0.000000, 0.000000]) -> None
```

<a id="unreal.AnchorData.offsets"></a>

#### offsets

```python
@property
def offsets() -> Margin
```

(Margin):  [Read-Write] Offset.

<a id="unreal.AnchorData.offsets"></a>

#### offsets

```python
@offsets.setter
def offsets(value: Margin) -> None
```

<a id="unreal.AnchorData.anchors"></a>

#### anchors

```python
@property
def anchors() -> Anchors
```

(Anchors):  [Read-Write] Anchors.

<a id="unreal.AnchorData.anchors"></a>

#### anchors

```python
@anchors.setter
def anchors(value: Anchors) -> None
```

<a id="unreal.AnchorData.alignment"></a>

#### alignment

```python
@property
def alignment() -> Vector2D
```

(Vector2D):  [Read-Write] Alignment is the pivot point of the widget.  Starting in the upper left at (0,0),
ending in the lower right at (1,1).  Moving the alignment point allows you to move
the origin of the widget.

<a id="unreal.AnchorData.alignment"></a>

#### alignment

```python
@alignment.setter
def alignment(value: Vector2D) -> None
```

<a id="unreal.RichTextStyleRow"></a>