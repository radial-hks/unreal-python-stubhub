## PropertyAnimatorClock Objects

```python
class PropertyAnimatorClock(PropertyAnimatorTextBase)
```

Animate supported string properties to display time

**C++ Source:**

- **Plugin**: PropertyAnimator
- **Module**: PropertyAnimator
- **File**: PropertyAnimatorClock.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``active_time_source`` (PropertyAnimatorCoreTimeSourceBase):  [Read-Only] Active time source with its options, determined by its name
- ``animator_display_name`` (Name):  [Read-Only] Display name as title property for component array, hide it but must be visible to editor for array title property
- ``animator_enabled`` (bool):  [Read-Write] Enable control of properties linked to this Animator
- ``display_format`` (str):  [Read-Write] Display date time format :
  %a - Weekday, eg) Sun
  %A - Weekday, eg) Sunday
  %w - Weekday, 0-6 (Sunday is 0)
  %y - Year, YY
  %Y - Year, YYYY
  %b - Month, eg) Jan
  %B - Month, eg) January
  %m - Month, 01-12
  %n - Month, 1-12
  %d - Day, 01-31
  %e - Day, 1-31
  %j - Day of the Year, 001-366
  %J - Day of the Year, 1-366
  %l - 12h Hour, 1-12
  %I - 12h Hour, 01-12
  %H - 24h Hour, 00-23
  %h - 24h Hour, 0-23
  %M - Minute, 00-59
  %N - Minute, 0-59
  %S - Second, 00-60
  %s - Second, 0-60
  %f - Millisecond, 000-999
  %F - Millisecond, 0-999
  %p - AM or PM
  %P - am or PM
  %t - Ticks since midnight, January 1, 0001
- ``linked_properties`` (Array[PropertyAnimatorCoreContext]):  [Read-Write] Context for properties linked to this Animator
- ``override_time_source`` (bool):  [Read-Write] Use the global time source or override it on this animator
- ``time_source_name`` (Name):  [Read-Write] The time source to use
- ``time_sources_instances`` (Map[Name, PropertyAnimatorCoreTimeSourceBase]):  [Read-Write]
  deprecated: Use TimeSources instead

<a id="unreal.PropertyAnimatorClock.display_format"></a>

#### display_format

```python
@property
def display_format() -> str
```

(str):  [Read-Write] Display date time format :
%a - Weekday, eg) Sun
%A - Weekday, eg) Sunday
%w - Weekday, 0-6 (Sunday is 0)
%y - Year, YY
%Y - Year, YYYY
%b - Month, eg) Jan
%B - Month, eg) January
%m - Month, 01-12
%n - Month, 1-12
%d - Day, 01-31
%e - Day, 1-31
%j - Day of the Year, 001-366
%J - Day of the Year, 1-366
%l - 12h Hour, 1-12
%I - 12h Hour, 01-12
%H - 24h Hour, 00-23
%h - 24h Hour, 0-23
%M - Minute, 00-59
%N - Minute, 0-59
%S - Second, 00-60
%s - Second, 0-60
%f - Millisecond, 000-999
%F - Millisecond, 0-999
%p - AM or PM
%P - am or PM
%t - Ticks since midnight, January 1, 0001

<a id="unreal.PropertyAnimatorClock.display_format"></a>

#### display_format

```python
@display_format.setter
def display_format(value: str) -> None
```

<a id="unreal.PropertyAnimatorEaseCurve"></a>