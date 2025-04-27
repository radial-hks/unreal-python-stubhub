## StateTreeNodeFormatting Objects

```python
class StateTreeNodeFormatting(EnumBase)
```

Enum describing in what format a text is expected to be returned.

- Normal text should be used for values
- Bold text should generally be used for actions, like name a of a task "<b>Play Animation</> {AnimName}".
- Subdued should be generally used for secondary/structural information, like "{Left} <s>equals</> {Right}".

**C++ Source:**

- **Plugin**: StateTree
- **Module**: StateTreeModule
- **File**: StateTreeNodeBase.h

<a id="unreal.StateTreeNodeFormatting.RICH_TEXT"></a>

#### RICH_TEXT

0: The returned text can contain following right text formatting (no nesting)
     - <b>Bold</> (bolder font is used)
     - <s>Subdued</> (normal font with lighter color)

<a id="unreal.StateTreeNodeFormatting.TEXT"></a>

#### TEXT

1: The text should be unformatted

<a id="unreal.StateTreeTransitionPriority"></a>