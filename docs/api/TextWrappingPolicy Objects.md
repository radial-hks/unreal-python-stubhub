## TextWrappingPolicy Objects

```python
class TextWrappingPolicy(EnumBase)
```

The different methods that can be used if a word is too long to be broken by the default line-break iterator.

**C++ Source:**

- **Module**: Slate
- **File**: TextLayout.h

<a id="unreal.TextWrappingPolicy.DEFAULT_WRAPPING"></a>

#### DEFAULT_WRAPPING

0: No fallback, just use the given line-break iterator

<a id="unreal.TextWrappingPolicy.ALLOW_PER_CHARACTER_WRAPPING"></a>

#### ALLOW_PER_CHARACTER_WRAPPING

1: Fallback to per-character wrapping if a word is too long

<a id="unreal.TextFlowDirection"></a>