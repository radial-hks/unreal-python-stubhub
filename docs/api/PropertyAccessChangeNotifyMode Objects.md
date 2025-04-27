## PropertyAccessChangeNotifyMode Objects

```python
class PropertyAccessChangeNotifyMode(EnumBase)
```

Enum controlling when to emit property change notifications when setting a property value.
note: Mirrored from PropertyAccessUtil.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

<a id="unreal.PropertyAccessChangeNotifyMode.DEFAULT"></a>

#### DEFAULT

0: Notify only when a value change has actually occurred

<a id="unreal.PropertyAccessChangeNotifyMode.NEVER"></a>

#### NEVER

1: Never notify that a value change has occurred

<a id="unreal.PropertyAccessChangeNotifyMode.ALWAYS"></a>

#### ALWAYS

2: Always notify that a value change has occurred, even if the value is unchanged

<a id="unreal.NetworkFailure"></a>