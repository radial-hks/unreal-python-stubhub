## FontCacheType Objects

```python
class FontCacheType(EnumBase)
```

Enumerates supported font caching types.

**C++ Source:**

- **Module**: Engine
- **File**: Font.h

<a id="unreal.FontCacheType.OFFLINE"></a>

#### OFFLINE

0: The font is using offline caching (this is how UFont traditionally worked).

<a id="unreal.FontCacheType.RUNTIME"></a>

#### RUNTIME

1: The font is using runtime caching (this is how Slate fonts work).

<a id="unreal.FontHinting"></a>