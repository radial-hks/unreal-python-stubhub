## TAPythonPrimitiveHitResult Objects

```python
class TAPythonPrimitiveHitResult(StructBase)
```

TAPython Primitive Hit Result

**C++ Source:**

- **Plugin**: TAPython
- **Module**: TAPython
- **File**: PythonBPLib.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component`` (PrimitiveComponent):  [Read-Write]
- ``hit_locations`` (Array[Vector]):  [Read-Write]
- ``hit_normals`` (Array[Vector]):  [Read-Write]
- ``is_this_triangles_vertex_all_visible`` (Array[bool]):  [Read-Write]
- ``screen_normals`` (Array[Vector]):  [Read-Write]
- ``screen_positions`` (Array[Vector2D]):  [Read-Write]
- ``transform`` (Transform):  [Read-Write]
- ``triangle_ids`` (Array[int32]):  [Read-Write] The index of output in the expression

<a id="unreal.TAPythonPrimitiveHitResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(component: PrimitiveComponent = None,
             triangle_ids: Array[int] = [],
             is_this_triangles_vertex_all_visible: Array[bool] = [],
             transform: Transform = [[0.000000, 0.000000, 0.000000],
                                     [-0.000000, 0.000000, 0.000000],
                                     [1.000000, 1.000000, 1.000000]],
             screen_positions: Array[Vector2D] = [],
             hit_locations: Array[Vector] = [],
             hit_normals: Array[Vector] = [],
             screen_normals: Array[Vector] = []) -> None
```

<a id="unreal.TAPythonPrimitiveHitResult.component"></a>

#### component

```python
@property
def component() -> PrimitiveComponent
```

(PrimitiveComponent):  [Read-Write]

<a id="unreal.TAPythonPrimitiveHitResult.component"></a>

#### component

```python
@component.setter
def component(value: PrimitiveComponent) -> None
```

<a id="unreal.TAPythonPrimitiveHitResult.triangle_ids"></a>

#### triangle\_ids

```python
@property
def triangle_ids() -> Array[int]
```

(Array[int32]):  [Read-Write] The index of output in the expression

<a id="unreal.TAPythonPrimitiveHitResult.triangle_ids"></a>

#### triangle\_ids

```python
@triangle_ids.setter
def triangle_ids(value: Array[int]) -> None
```

<a id="unreal.TAPythonPrimitiveHitResult.is_this_triangles_vertex_all_visible"></a>

#### is\_this\_triangles\_vertex\_all\_visible

```python
@property
def is_this_triangles_vertex_all_visible() -> Array[bool]
```

(Array[bool]):  [Read-Write]

<a id="unreal.TAPythonPrimitiveHitResult.is_this_triangles_vertex_all_visible"></a>

#### is\_this\_triangles\_vertex\_all\_visible

```python
@is_this_triangles_vertex_all_visible.setter
def is_this_triangles_vertex_all_visible(value: Array[bool]) -> None
```

<a id="unreal.TAPythonPrimitiveHitResult.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.TAPythonPrimitiveHitResult.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.TAPythonPrimitiveHitResult.screen_positions"></a>

#### screen\_positions

```python
@property
def screen_positions() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Write]

<a id="unreal.TAPythonPrimitiveHitResult.screen_positions"></a>

#### screen\_positions

```python
@screen_positions.setter
def screen_positions(value: Array[Vector2D]) -> None
```

<a id="unreal.TAPythonPrimitiveHitResult.hit_locations"></a>

#### hit\_locations

```python
@property
def hit_locations() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.TAPythonPrimitiveHitResult.hit_locations"></a>

#### hit\_locations

```python
@hit_locations.setter
def hit_locations(value: Array[Vector]) -> None
```

<a id="unreal.TAPythonPrimitiveHitResult.hit_normals"></a>

#### hit\_normals

```python
@property
def hit_normals() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.TAPythonPrimitiveHitResult.hit_normals"></a>

#### hit\_normals

```python
@hit_normals.setter
def hit_normals(value: Array[Vector]) -> None
```

<a id="unreal.TAPythonPrimitiveHitResult.screen_normals"></a>

#### screen\_normals

```python
@property
def screen_normals() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.TAPythonPrimitiveHitResult.screen_normals"></a>

#### screen\_normals

```python
@screen_normals.setter
def screen_normals(value: Array[Vector]) -> None
```

<a id="unreal.TAPythonMaterialConnection"></a>