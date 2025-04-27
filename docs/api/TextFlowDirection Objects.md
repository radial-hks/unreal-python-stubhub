## TextFlowDirection Objects

```python
class TextFlowDirection(EnumBase)
```

The different directions that text can flow within a paragraph of text.
note: If you change this enum, make sure and update CVarDefaultTextFlowDirection and GetDefaultTextFlowDirection.

**C++ Source:**

- **Module**: Slate
- **File**: TextLayout.h

<a id="unreal.TextFlowDirection.AUTO"></a>

#### AUTO

0: Automatically detect the flow direction for each paragraph from its text

<a id="unreal.TextFlowDirection.LEFT_TO_RIGHT"></a>

#### LEFT_TO_RIGHT

1: Force text to be flowed left-to-right

<a id="unreal.TextFlowDirection.RIGHT_TO_LEFT"></a>

#### RIGHT_TO_LEFT

2: Force text to be flowed right-to-left

<a id="unreal.TextFlowDirection.CULTURE"></a>

#### CULTURE

3: Uses the set culture to determine if text should flow left-to-right or right-to-left.  By comparison, Auto will use the text itself to determine it.

<a id="unreal.StretchDirection"></a>