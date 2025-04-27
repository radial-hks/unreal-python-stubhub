## ConsumeMouseWheel Objects

```python
class ConsumeMouseWheel(EnumBase)
```

Used to determine how we should handle mouse wheel input events when someone scrolls.

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateTypes.h

<a id="unreal.ConsumeMouseWheel.WHEN_SCROLLING_POSSIBLE"></a>

#### WHEN_SCROLLING_POSSIBLE

0: Only consume the mouse wheel event when we actually scroll some amount.

<a id="unreal.ConsumeMouseWheel.ALWAYS"></a>

#### ALWAYS

1: Always consume mouse wheel event even if we don't scroll at all.

<a id="unreal.ConsumeMouseWheel.NEVER"></a>

#### NEVER

2: Never consume the mouse wheel

<a id="unreal.WindowTitleBarMode"></a>