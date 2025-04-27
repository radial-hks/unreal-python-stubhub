## SlateAccessibleBehavior Objects

```python
class SlateAccessibleBehavior(EnumBase)
```

Whether a widget should be included in accessibility, and if so, how its text should be retrieved.

**C++ Source:**

- **Module**: UMG
- **File**: SlateWrapperTypes.h

<a id="unreal.SlateAccessibleBehavior.NOT_ACCESSIBLE"></a>

#### NOT_ACCESSIBLE

0: Not accessible.

<a id="unreal.SlateAccessibleBehavior.AUTO"></a>

#### AUTO

1: Accessible, first checking to see if there's any custom default text assigned for widgets of this type.
If not, then it will attempt to use the alternate behavior (ie AccessibleSummaryBehavior instead of AccessibleBehavior)
and return that value instead. This acts as a reference so that you only need to set one value for both of them
to return the same thing.

<a id="unreal.SlateAccessibleBehavior.SUMMARY"></a>

#### SUMMARY

2: Accessible, and traverse all child widgets and concat their AccessibleSummaryText together.

<a id="unreal.SlateAccessibleBehavior.CUSTOM"></a>

#### CUSTOM

3: Accessible, and retrieve manually-assigned text from a TAttribute.

<a id="unreal.SlateAccessibleBehavior.TOOL_TIP"></a>

#### TOOL_TIP

4: Accessible, and use the tooltip's accessible text.

<a id="unreal.VirtualKeyboardType"></a>