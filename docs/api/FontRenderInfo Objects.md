## FontRenderInfo Objects

```python
class FontRenderInfo(StructBase)
```

Information used in font rendering

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``clip_text`` (bool):  [Read-Write] Whether to clip text
- ``enable_shadow`` (bool):  [Read-Write] Whether to turn on shadowing
- ``glow_info`` (DepthFieldGlowInfo):  [Read-Write] Depth field glow parameters (only usable if font was imported with a depth field)

<a id="unreal.FontRenderInfo.__init__"></a>

#### __init__

```python
def __init__(
    clip_text: bool = False,
    enable_shadow: bool = False,
    glow_info: DepthFieldGlowInfo = [
        False, [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000],
        [0.000000, 0.000000]
    ]
) -> None
```

<a id="unreal.FontRenderInfo.clip_text"></a>

#### clip_text

```python
@property
def clip_text() -> bool
```

(bool):  [Read-Write] Whether to clip text

<a id="unreal.FontRenderInfo.clip_text"></a>

#### clip_text

```python
@clip_text.setter
def clip_text(value: bool) -> None
```

<a id="unreal.FontRenderInfo.enable_shadow"></a>

#### enable_shadow

```python
@property
def enable_shadow() -> bool
```

(bool):  [Read-Write] Whether to turn on shadowing

<a id="unreal.FontRenderInfo.enable_shadow"></a>

#### enable_shadow

```python
@enable_shadow.setter
def enable_shadow(value: bool) -> None
```

<a id="unreal.FontRenderInfo.glow_info"></a>

#### glow_info

```python
@property
def glow_info() -> DepthFieldGlowInfo
```

(DepthFieldGlowInfo):  [Read-Write] Depth field glow parameters (only usable if font was imported with a depth field)

<a id="unreal.FontRenderInfo.glow_info"></a>

#### glow_info

```python
@glow_info.setter
def glow_info(value: DepthFieldGlowInfo) -> None
```

<a id="unreal.CanvasUVTri"></a>