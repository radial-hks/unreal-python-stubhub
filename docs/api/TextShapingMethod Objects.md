## TextShapingMethod Objects

```python
class TextShapingMethod(EnumBase)
```

Methods that can be used to shape text.
note: If you change this enum, make sure and update CVarDefaultTextShapingMethod and GetDefaultTextShapingMethod.

**C++ Source:**

- **Module**: SlateCore
- **File**: FontCache.h

<a id="unreal.TextShapingMethod.AUTO"></a>

#### AUTO

0: Automatically picks the fastest possible shaping method (either KerningOnly or FullShaping) based on the reading direction of the text.
Left-to-right text uses the KerningOnly method, and right-to-left text uses the FullShaping method.

<a id="unreal.TextShapingMethod.KERNING_ONLY"></a>

#### KERNING_ONLY

1: Provides fake shaping using only kerning data.
This can be faster than full shaping, but won't render complex right-to-left or bi-directional glyphs (such as Arabic) correctly.
This can be useful as an optimization when you know your text block will only show simple glyphs (such as numbers).

<a id="unreal.TextShapingMethod.FULL_SHAPING"></a>

#### FULL_SHAPING

2: Provides full text shaping, allowing accurate rendering of complex right-to-left or bi-directional glyphs (such as Arabic).
This mode will perform ligature replacement for all languages (such as the combined "fi" glyph in English).

<a id="unreal.WidgetClipping"></a>