# dahdi-firmware
NethServer RPM for dahdi-firmware
Based on Sangoma source RPM

## How to build
```
make-srpm dahdi-firmware.spec
srpm=$(basename "$(grep '^Wrote: ' build.log | tail -1 )")
mock -D "dist .ns7" --resultdir=. -r nethserver-7-x86_64 $srpm
```

