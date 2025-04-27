## TextCommit Objects

```python
class TextCommit(EnumBase)
```

Additional information about a text committal

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateEnums.h

<a id="unreal.TextCommit.DEFAULT"></a>

#### DEFAULT

0: Losing focus or similar event caused implicit commit

<a id="unreal.TextCommit.ON_ENTER"></a>

#### ON_ENTER

1: User committed via the enter key

<a id="unreal.TextCommit.ON_USER_MOVED_FOCUS"></a>

#### ON_USER_MOVED_FOCUS

2: User committed via tabbing away or moving focus explicitly away

<a id="unreal.TextCommit.ON_CLEARED"></a>

#### ON_CLEARED

3: Keyboard focus was explicitly cleared via the escape key or other similar action

<a id="unreal.SelectInfo"></a>