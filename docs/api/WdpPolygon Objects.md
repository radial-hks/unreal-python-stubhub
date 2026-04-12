## WdpPolygon Objects

```python
class WdpPolygon(StructBase)
```

Wdp Polygon

**C++ Source:**

- **Plugin**: WdpCommon
- **Module**: WdpGeometry
- **File**: WdpPolygon.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``inner_loops`` (Array[WdpLoop]):  [Read-Only]
- ``outer_loop`` (WdpLoop):  [Read-Only]

<a id="unreal.WdpPolygon.__init__"></a>

#### \_\_init\_\_

```python
def __init__(outer_loop: WdpLoop = [[]],
             inner_loops: Array[WdpLoop] = []) -> None
```

<a id="unreal.WdpPolygon.outer_loop"></a>

#### outer\_loop

```python
@property
def outer_loop() -> WdpLoop
```

(WdpLoop):  [Read-Only]

<a id="unreal.WdpPolygon.inner_loops"></a>

#### inner\_loops

```python
@property
def inner_loops() -> Array[WdpLoop]
```

(Array[WdpLoop]):  [Read-Only]

<a id="unreal.WdpPolygon2D"></a>