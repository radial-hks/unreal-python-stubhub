## TextJustify Objects

```python
class TextJustify(EnumBase)
```

EText Justify

**C++ Source:**

- **Module**: Slate
- **File**: TextLayout.h

<a id="unreal.TextJustify.LEFT"></a>

#### LEFT

0: Justify the text logically to the left.
When text is flowing left-to-right, this will align text visually to the left.
When text is flowing right-to-left, this will align text visually to the right.

<a id="unreal.TextJustify.CENTER"></a>

#### CENTER

1: Justify the text in the center.
Text flow direction has no impact on this justification mode.

<a id="unreal.TextJustify.RIGHT"></a>

#### RIGHT

2: Justify the text logically to the right.
When text is flowing left-to-right, this will align text visually to the right.
When text is flowing right-to-left, this will align text visually to the left.

<a id="unreal.TextJustify.INVARIANT_LEFT"></a>

#### INVARIANT_LEFT

3: Always justify the text to the left, regardless of the flow direction of the current culture.

<a id="unreal.TextJustify.INVARIANT_RIGHT"></a>

#### INVARIANT_RIGHT

4: Always justify the text to the right, regardless of the flow direction of the current culture.

<a id="unreal.TextWrappingPolicy"></a>