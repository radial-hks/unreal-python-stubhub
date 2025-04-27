## DragDropOperation Objects

```python
class DragDropOperation(Object)
```

This class is the base drag drop operation for UMG, extend it to add additional data and add new functionality.

**C++ Source:**

- **Module**: UMG
- **File**: DragDropOperation.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``default_drag_visual`` (Widget):  [Read-Write] The Drag Visual is the widget to display when dragging the item.  Normally people create a new widget to represent the
  temporary drag.
- ``offset`` (Vector2D):  [Read-Write] A percentage offset (-1..+1) from the Pivot location, the percentage is of the desired size of the dragged visual.
- ``on_drag_cancelled`` (OnDragDropMulticast):  [Read-Write]
- ``on_dragged`` (OnDragDropMulticast):  [Read-Write]
- ``on_drop`` (OnDragDropMulticast):  [Read-Write]
- ``payload`` (Object):  [Read-Write] The payload of the drag operation.  This can be any UObject that you want to pass along as dragged data.  If you
  were building an inventory screen this would be the UObject representing the item being moved to another slot.
- ``pivot`` (DragPivot):  [Read-Write] Controls where the drag widget visual will appear when dragged relative to the pointer performing
  the drag operation.
- ``tag`` (str):  [Read-Write] A simple string tag you can optionally use to provide extra metadata about the operation.

<a id="unreal.DragDropOperation.tag"></a>

#### tag

```python
@property
def tag() -> str
```

(str):  [Read-Write] A simple string tag you can optionally use to provide extra metadata about the operation.

<a id="unreal.DragDropOperation.tag"></a>

#### tag

```python
@tag.setter
def tag(value: str) -> None
```

<a id="unreal.DragDropOperation.payload"></a>

#### payload

```python
@property
def payload() -> Object
```

(Object):  [Read-Write] The payload of the drag operation.  This can be any UObject that you want to pass along as dragged data.  If you
were building an inventory screen this would be the UObject representing the item being moved to another slot.

<a id="unreal.DragDropOperation.payload"></a>

#### payload

```python
@payload.setter
def payload(value: Object) -> None
```

<a id="unreal.DragDropOperation.default_drag_visual"></a>

#### default_drag_visual

```python
@property
def default_drag_visual() -> Widget
```

(Widget):  [Read-Only] The Drag Visual is the widget to display when dragging the item.  Normally people create a new widget to represent the
temporary drag.

<a id="unreal.DragDropOperation.pivot"></a>

#### pivot

```python
@property
def pivot() -> DragPivot
```

(DragPivot):  [Read-Write] Controls where the drag widget visual will appear when dragged relative to the pointer performing
the drag operation.

<a id="unreal.DragDropOperation.pivot"></a>

#### pivot

```python
@pivot.setter
def pivot(value: DragPivot) -> None
```

<a id="unreal.DragDropOperation.offset"></a>

#### offset

```python
@property
def offset() -> Vector2D
```

(Vector2D):  [Read-Write] A percentage offset (-1..+1) from the Pivot location, the percentage is of the desired size of the dragged visual.

<a id="unreal.DragDropOperation.offset"></a>

#### offset

```python
@offset.setter
def offset(value: Vector2D) -> None
```

<a id="unreal.DragDropOperation.on_drop"></a>

#### on_drop

```python
@property
def on_drop() -> OnDragDropMulticast
```

(OnDragDropMulticast):  [Read-Write]

<a id="unreal.DragDropOperation.on_drop"></a>

#### on_drop

```python
@on_drop.setter
def on_drop(value: OnDragDropMulticast) -> None
```

<a id="unreal.DragDropOperation.on_drag_cancelled"></a>

#### on_drag_cancelled

```python
@property
def on_drag_cancelled() -> OnDragDropMulticast
```

(OnDragDropMulticast):  [Read-Write]

<a id="unreal.DragDropOperation.on_drag_cancelled"></a>

#### on_drag_cancelled

```python
@on_drag_cancelled.setter
def on_drag_cancelled(value: OnDragDropMulticast) -> None
```

<a id="unreal.DragDropOperation.on_dragged"></a>

#### on_dragged

```python
@property
def on_dragged() -> OnDragDropMulticast
```

(OnDragDropMulticast):  [Read-Write]

<a id="unreal.DragDropOperation.on_dragged"></a>

#### on_dragged

```python
@on_dragged.setter
def on_dragged(value: OnDragDropMulticast) -> None
```

<a id="unreal.DragDropOperation.drop"></a>

#### drop

```python
def drop(pointer_event: PointerEvent) -> None
```

x.drop(pointer_event) -> None
Drop

Args:
    pointer_event (PointerEvent):

<a id="unreal.DragDropOperation.dragged"></a>

#### dragged

```python
def dragged(pointer_event: PointerEvent) -> None
```

x.dragged(pointer_event) -> None
Dragged

Args:
    pointer_event (PointerEvent):

<a id="unreal.DragDropOperation.drag_cancelled"></a>

#### drag_cancelled

```python
def drag_cancelled(pointer_event: PointerEvent) -> None
```

x.drag_cancelled(pointer_event) -> None
Drag Cancelled

Args:
    pointer_event (PointerEvent):

<a id="unreal.SlateLibrary"></a>