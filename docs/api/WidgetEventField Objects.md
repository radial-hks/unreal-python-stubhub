## WidgetEventField Objects

```python
class WidgetEventField(StructBase)
```

Generic structure to notify when an event occurs.

class UMyWidget : public UWidget
{
  UPROPERTY(FieldNotify)
  FWidgetEventField SomeEvent;

  void OnSomeEvent()
  {
    BroadcastFieldValueChanged(FFieldNotificationClassDescriptor::Text);
  }
};
};

**C++ Source:**

- **Module**: UMG
- **File**: WidgetEventField.h

<a id="unreal.WidgetEventField.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.WidgetNavigationData"></a>