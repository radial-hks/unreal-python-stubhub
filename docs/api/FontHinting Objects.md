## FontHinting Objects

```python
class FontHinting(EnumBase)
```

EFont Hinting

**C++ Source:**

- **Module**: SlateCore
- **File**: CompositeFont.h

<a id="unreal.FontHinting.DEFAULT"></a>

#### DEFAULT

0: Use the default hinting specified in the font.

<a id="unreal.FontHinting.AUTO"></a>

#### AUTO

1: Force the use of an automatic hinting algorithm.

<a id="unreal.FontHinting.AUTO_LIGHT"></a>

#### AUTO_LIGHT

2: Force the use of an automatic light hinting algorithm, optimized for non-monochrome displays.

<a id="unreal.FontHinting.MONOCHROME"></a>

#### MONOCHROME

3: Force the use of an automatic hinting algorithm optimized for monochrome displays.

<a id="unreal.FontHinting.NONE"></a>

#### NONE

4: Do not use hinting.

<a id="unreal.FontLoadingPolicy"></a>