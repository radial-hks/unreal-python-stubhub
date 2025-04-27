## TextOverflowPolicy Objects

```python
class TextOverflowPolicy(EnumBase)
```

The different methods that can be used to determine what happens to text when it is longer than its allowed length

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateTypes.h

<a id="unreal.TextOverflowPolicy.CLIP"></a>

#### CLIP

0: Overflowing text will be clipped

<a id="unreal.TextOverflowPolicy.ELLIPSIS"></a>

#### ELLIPSIS

1: Overflowing text will be replaced with an ellipsis

<a id="unreal.TextOverflowPolicy.MULTILINE_ELLIPSIS"></a>

#### MULTILINE_ELLIPSIS

2: Overflowing text will be replaced with an ellipsis. A partially clipped line on the vertical axis will be totally clipped, and ellipsis displayed on previous line

<a id="unreal.TextOverflowPolicy.MIDDLE_ELLIPSIS"></a>

#### MIDDLE_ELLIPSIS

3: Overflowing text will be replaced with an ellipsis starting from the center\n
Current Limits:
- Multiline is not supported
- RichText is not fully supported
- Highlight text is not supported
- Arabic mix with western character is not supported

<a id="unreal.TextTransformPolicy"></a>