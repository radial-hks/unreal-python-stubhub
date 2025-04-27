## FontLoadingPolicy Objects

```python
class FontLoadingPolicy(EnumBase)
```

EFont Loading Policy

**C++ Source:**

- **Module**: SlateCore
- **File**: CompositeFont.h

<a id="unreal.FontLoadingPolicy.LAZY_LOAD"></a>

#### LAZY_LOAD

0: Lazy load the entire font into memory. This will consume more memory than Streaming, however there will be zero file-IO when rendering glyphs within the font, although the initial load may cause a hitch.

<a id="unreal.FontLoadingPolicy.STREAM"></a>

#### STREAM

1: Stream the font from disk. This will consume less memory than LazyLoad or Inline, however there will be file-IO when rendering glyphs, which may cause hitches under certain circumstances or on certain platforms.

<a id="unreal.FontLoadingPolicy.INLINE"></a>

#### INLINE

2: Embed the font data within the asset. This will consume more memory than Streaming, however it is guaranteed to be hitch free (only valid for font data within a Font Face asset).

<a id="unreal.FontLayoutMethod"></a>