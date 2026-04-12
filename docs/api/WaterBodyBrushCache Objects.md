## WaterBodyBrushCache Objects

```python
class WaterBodyBrushCache(StructBase)
```

TODO [jonathan.bard] : rename : this is not a WaterBodyBrushCache, this a simple RenderTarget with a boolean to force an update on it
 This is also used for caching curves...

**C++ Source:**

- **Plugin**: Water
- **Module**: WaterEditor
- **File**: WaterBrushCacheContainer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cache_is_valid`` (bool):  [Read-Write]
- ``cache_render_target`` (TextureRenderTarget2D):  [Read-Write]

<a id="unreal.WaterBodyBrushCache.__init__"></a>

#### \_\_init\_\_

```python
def __init__(cache_render_target: TextureRenderTarget2D = None,
             cache_is_valid: bool = False) -> None
```

<a id="unreal.WaterBodyBrushCache.cache_render_target"></a>

#### cache\_render\_target

```python
@property
def cache_render_target() -> TextureRenderTarget2D
```

(TextureRenderTarget2D):  [Read-Write]

<a id="unreal.WaterBodyBrushCache.cache_render_target"></a>

#### cache\_render\_target

```python
@cache_render_target.setter
def cache_render_target(value: TextureRenderTarget2D) -> None
```

<a id="unreal.WaterBodyBrushCache.cache_is_valid"></a>

#### cache\_is\_valid

```python
@property
def cache_is_valid() -> bool
```

(bool):  [Read-Write]

<a id="unreal.WaterBodyBrushCache.cache_is_valid"></a>

#### cache\_is\_valid

```python
@cache_is_valid.setter
def cache_is_valid(value: bool) -> None
```

<a id="unreal.AesBakeBoardLayer"></a>