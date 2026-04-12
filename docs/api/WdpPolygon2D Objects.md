## WdpPolygon2D Objects

```python
class WdpPolygon2D(StructBase)
```

Wdp Polygon 2D

**C++ Source:**

- **Plugin**: WdpCommon
- **Module**: WdpGeometry
- **File**: WdpPolygon2D.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``inner_loops`` (Array[WdpLoop2D]):  [Read-Only]
- ``outer_loop`` (WdpLoop2D):  [Read-Only]

<a id="unreal.WdpPolygon2D.__init__"></a>

#### \_\_init\_\_

```python
def __init__(outer_loop: WdpLoop2D = [],
             inner_loops: Array[WdpLoop2D] = []) -> None
```

<a id="unreal.WdpPolygon2D.outer_loop"></a>

#### outer\_loop

```python
@property
def outer_loop() -> WdpLoop2D
```

(WdpLoop2D):  [Read-Only]

<a id="unreal.WdpPolygon2D.inner_loops"></a>

#### inner\_loops

```python
@property
def inner_loops() -> Array[WdpLoop2D]
```

(Array[WdpLoop2D]):  [Read-Only]

<a id="unreal.WdpPickFilter"></a>