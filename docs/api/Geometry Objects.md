## Geometry Objects

```python
class Geometry(StructBase)
```

Represents the position, size, and absolute position of a Widget in Slate.
The absolute location of a geometry is usually screen space or
window space depending on where the geometry originated.
Geometries are usually paired with a SWidget pointer in order
to provide information about a specific widget (see FArrangedWidget).
A Geometry's parent is generally thought to be the Geometry of the
the corresponding parent widget.

**C++ Source:**

- **Module**: SlateCore
- **File**: Geometry.h

<a id="unreal.Geometry.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.SlateBrush"></a>