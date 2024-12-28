# نمایش پروتکل‌های امنیتی سیستم ویندوز

## توضیحات:

### دستور `netsh advfirewall show allprofiles`:
این دستور وضعیت پیکربندی فایروال سیستم ویندوز را نمایش می‌دهد.
اطلاعاتی از جمله پروتکل‌های فعال، قوانین فایروال و وضعیت فایروال برای تمام پروفایل‌ها (Public, Private, Domain) را نشان می‌دهد.

### کتابخانه `subprocess`:
این کتابخانه برای اجرای دستورات سیستم استفاده می‌شود.

## خروجی نمونه:
در صورتی که فایروال ویندوز فعال باشد، خروجی مشابه زیر خواهد بود:

```mathematica
Firewall settings and security protocols:
    Profile                = Domain
    State                  = ON
    Default inbound action = Block
    Default outbound action= Allow
    ...
