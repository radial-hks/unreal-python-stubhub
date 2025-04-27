## SelectionMode Objects

```python
class SelectionMode(EnumBase)
```

ESelection Mode

**C++ Source:**

- **Module**: Slate
- **File**: ITypedTableView.h

<a id="unreal.SelectionMode.NONE"></a>

#### NONE

0: Nothing can be selected and there is no hover cue for selection.  You can still handle mouse button events though.

<a id="unreal.SelectionMode.SINGLE"></a>

#### SINGLE

1: A single item can be selected at once, or no item may be selected.

<a id="unreal.SelectionMode.SINGLE_TOGGLE"></a>

#### SINGLE_TOGGLE

2: A single item can be selected at once, or no item may be selected.  You can click the item to toggle selection on and off.

<a id="unreal.SelectionMode.MULTI"></a>

#### MULTI

3: Multiple items can be selected at the same time.

<a id="unreal.ConsumeMouseWheel"></a>