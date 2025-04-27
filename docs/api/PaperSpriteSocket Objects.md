## PaperSpriteSocket Objects

```python
class PaperSpriteSocket(StructBase)
```

TODO:: Should have some nice UI and enforce unique names, etc...

**C++ Source:**

- **Plugin**: Paper2D
- **Module**: Paper2D
- **File**: PaperSprite.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``local_transform`` (Transform):  [Read-Write] Transform in pivot space (*not* texture space)
- ``socket_name`` (Name):  [Read-Write] Name of the socket

<a id="unreal.PaperSpriteSocket.__init__"></a>

#### __init__

```python
def __init__(local_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                           [-0.000000, 0.000000, 0.000000],
                                           [1.000000, 1.000000, 1.000000]],
             socket_name: Name = "None") -> None
```

<a id="unreal.PaperSpriteSocket.local_transform"></a>

#### local_transform

```python
@property
def local_transform() -> Transform
```

(Transform):  [Read-Only] Transform in pivot space (*not* texture space)

<a id="unreal.PaperSpriteSocket.socket_name"></a>

#### socket_name

```python
@property
def socket_name() -> Name
```

(Name):  [Read-Only] Name of the socket

<a id="unreal.PaperTileInfo"></a>