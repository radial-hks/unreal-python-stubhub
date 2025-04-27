## SlateVisibility Objects

```python
class SlateVisibility(EnumBase)
```

Is an entity visible?

**C++ Source:**

- **Module**: UMG
- **File**: SlateWrapperTypes.h

<a id="unreal.SlateVisibility.VISIBLE"></a>

#### VISIBLE

0: Visible and hit-testable (can interact with cursor). Default value.

<a id="unreal.SlateVisibility.COLLAPSED"></a>

#### COLLAPSED

1: Not visible and takes up no space in the layout (obviously not hit-testable).

<a id="unreal.SlateVisibility.HIDDEN"></a>

#### HIDDEN

2: Not visible but occupies layout space (obviously not hit-testable).

<a id="unreal.SlateVisibility.HIT_TEST_INVISIBLE"></a>

#### HIT_TEST_INVISIBLE

3: Visible but not hit-testable (cannot interact with cursor) and children in the hierarchy (if any) are also not hit-testable.

<a id="unreal.SlateVisibility.SELF_HIT_TEST_INVISIBLE"></a>

#### SELF_HIT_TEST_INVISIBLE

4: Visible but not hit-testable (cannot interact with cursor) and doesn't affect hit-testing on children (if any).

<a id="unreal.SlateAccessibleBehavior"></a>